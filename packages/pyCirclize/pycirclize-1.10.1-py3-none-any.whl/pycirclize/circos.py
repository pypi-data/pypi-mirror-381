from __future__ import annotations

import itertools
import math
import textwrap
import warnings
from collections import defaultdict
from collections.abc import Callable, Sequence
from copy import deepcopy
from pathlib import Path
from typing import TYPE_CHECKING, Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.collections import PatchCollection
from matplotlib.colorbar import Colorbar
from matplotlib.colors import Colormap, Normalize
from matplotlib.projections.polar import PolarAxes

from pycirclize import config, utils
from pycirclize.annotation import adjust_annotation
from pycirclize.parser import Bed, Matrix, RadarTable
from pycirclize.patches import (
    ArcLine,
    ArcRectangle,
    BezierCurveLine,
    BezierCurveLink,
    Line,
)
from pycirclize.sector import Sector
from pycirclize.tooltip import (
    gen_gid,
    set_patch_tooltip,
    to_cytoband_tooltip,
    to_link_tooltip,
)
from pycirclize.tree import TreeViz

if TYPE_CHECKING:
    from collections.abc import Mapping

    from Bio.Phylo.BaseTree import Tree
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure
    from matplotlib.patches import Patch

    from pycirclize.track import Track
    from pycirclize.typing import Numeric


class Circos:
    """Circos Visualization Class"""

    def __init__(
        self,
        sectors: Mapping[str, Numeric | tuple[Numeric, Numeric]],
        start: float = 0,
        end: float = 360,
        *,
        space: Numeric | Sequence[Numeric] = 0,
        endspace: bool = True,
        sector2clockwise: dict[str, bool] | None = None,
        show_axis_for_debug: bool = False,
    ) -> None:
        """
        Parameters
        ----------
        sectors : Mapping[str, Numeric | tuple[Numeric, Numeric]]
            Sector name & size (or range) dict
        start : float, optional
            Plot start degree (`-360 <= start < end <= 360`)
        end : float, optional
            Plot end degree (`-360 <= start < end <= 360`)
        space : Numeric | Sequence[Numeric], optional
            Space degree(s) between sector
        endspace : bool, optional
            If True, insert space after the end sector
        sector2clockwise : dict[str, bool] | None, optional
            Sector name & clockwise bool dict. By default, `clockwise=True`.
        show_axis_for_debug : bool, optional
            Show axis for position check debugging (Developer option)
        """
        sector2clockwise = {} if sector2clockwise is None else sector2clockwise

        # Check start-end degree range
        self._check_degree_range(start, end)

        # Calculate sector region & add sector
        whole_deg_size = end - start
        space_num = len(sectors) if endspace else len(sectors) - 1
        if isinstance(space, Sequence):
            if len(space) != space_num:
                raise ValueError(f"{space=} is invalid.\nLength of space list must be {space_num}.")  # fmt: skip  # noqa: E501
            space_list = [*list(space), 0]
            space_deg_size = sum(space)
        else:
            space_list = [space] * space_num + [0]
            space_deg_size = space * space_num
        whole_deg_size_without_space = whole_deg_size - space_deg_size
        if whole_deg_size_without_space < 0:
            err_msg = textwrap.dedent(
                f"""
                Too large sector space size is set!!
                Circos Degree Size = {whole_deg_size} ({start} - {end})
                Total Sector Space Size = {space_deg_size}
                List of Sector Space Size = {space_list}
                """
            )[1:-1]
            raise ValueError(err_msg)

        sector2range = self._to_sector2range(sectors)
        sector_total_size = sum([max(r) - min(r) for r in sector2range.values()])

        rad_pos = math.radians(start)
        self._sectors: list[Sector] = []
        for idx, (sector_name, sector_range) in enumerate(sector2range.items()):
            sector_size = max(sector_range) - min(sector_range)
            sector_size_ratio = sector_size / sector_total_size
            deg_size = whole_deg_size_without_space * sector_size_ratio
            rad_size = math.radians(deg_size)
            rad_lim = (rad_pos, rad_pos + rad_size)
            rad_pos += rad_size + math.radians(space_list[idx])
            clockwise = sector2clockwise.get(sector_name, True)
            sector = Sector(sector_name, sector_range, rad_lim, clockwise)
            self._sectors.append(sector)

        self._deg_lim = (start, end)
        self._rad_lim = (math.radians(start), math.radians(end))
        self._patches: list[Patch] = []
        self._plot_funcs: list[Callable[[PolarAxes], None]] = []
        self._gid2tooltip: dict[str, str] = {}
        self._ax: PolarAxes | None = None
        self._show_axis_for_debug = show_axis_for_debug

    ############################################################
    # Property
    ############################################################

    @property
    def rad_size(self) -> float:
        """Circos radian size"""
        return max(self.rad_lim) - min(self.rad_lim)

    @property
    def rad_lim(self) -> tuple[float, float]:
        """Circos radian limit"""
        return self._rad_lim

    @property
    def deg_size(self) -> float:
        """Circos degree size"""
        return max(self.deg_lim) - min(self.deg_lim)

    @property
    def deg_lim(self) -> tuple[float, float]:
        """Circos degree limit"""
        return self._deg_lim

    @property
    def sectors(self) -> list[Sector]:
        """Sectors"""
        return self._sectors

    @property
    def tracks(self) -> list[Track]:
        """Tracks (from sectors)"""
        tracks = []
        for sector in self.sectors:
            for track in sector.tracks:
                tracks.append(track)
        return tracks

    @property
    def ax(self) -> PolarAxes:
        """Plot polar axes

        Can't access `ax` property before calling `circos.plotfig()` method
        """
        if self._ax is None:
            raise ValueError("Can't access ax property before calling `circos.plotfig() method")  # fmt:skip  # noqa: E501
        return self._ax

    ############################################################
    # Public Method
    ############################################################

    @classmethod
    def set_tooltip_enabled(cls, enabled: bool = True) -> None:
        """Enable/disable tooltip annotation using ipympl"""
        if enabled:
            try:
                import ipympl  # noqa: F401, PLC0415
                from IPython import get_ipython  # noqa: PLC0415

                get_ipython().run_line_magic("matplotlib", "widget")
                config.tooltip.enabled = True
            except Exception:
                warnings.warn("Failed to enable tooltip. To enable tooltip, an interactive python environment such as jupyter and ipympl installation are required.", stacklevel=2)  # fmt: skip  # noqa: E501
        else:
            config.tooltip.enabled = False

    @staticmethod
    def radar_chart(  # noqa: PLR0912, PLR0915
        table: str | Path | pd.DataFrame | RadarTable,
        *,
        r_lim: tuple[float, float] = (0, 100),
        vmin: float = 0,
        vmax: float = 100,
        fill: bool = True,
        marker_size: int = 0,
        bg_color: str | None = "#eeeeee80",
        circular: bool = False,
        cmap: str | dict[str, str] = "Set2",
        show_grid_label: bool = True,
        grid_interval_ratio: float | None = 0.2,
        grid_line_kws: dict[str, Any] | None = None,
        grid_label_kws: dict[str, Any] | None = None,
        grid_label_formatter: Callable[[float], str] | None = None,
        label_kws_handler: Callable[[str], dict[str, Any]] | None = None,
        line_kws_handler: Callable[[str], dict[str, Any]] | None = None,
        marker_kws_handler: Callable[[str], dict[str, Any]] | None = None,
    ) -> Circos:
        """Plot radar chart

        Parameters
        ----------
        table : str | Path | pd.DataFrame | RadarTable
            Table file or Table dataframe or RadarTable instance
        r_lim : tuple[float, float], optional
            Radar chart radius limit region (0 - 100)
        vmin : float, optional
            Min value
        vmax : float, optional
            Max value
        fill : bool, optional
            If True, fill color of radar chart.
        marker_size : int, optional
            Marker size
        bg_color : str | None, optional
            Background color
        circular : bool, optional
            If True, plot with circular style.
        cmap : str | dict[str, str], optional
            Colormap assigned to each target row(index) in table.
            User can set matplotlib's colormap (e.g. `tab10`, `Set2`) or
            target_name -> color dict (e.g. `dict(A="red", B="blue", C="green", ...)`)
        show_grid_label : bool, optional
            If True, show grid label.
        grid_interval_ratio : float | None, optional
            Grid interval ratio (0.0 - 1.0)
        grid_line_kws : dict[str, Any] | None, optional
            Keyword arguments passed to `track.line()` method
            (e.g. `dict(color="black", ls="dotted", lw=1.0, ...)`)
        grid_label_kws : dict[str, Any] | None, optional
            Keyword arguments passed to `track.text()` method
            (e.g. `dict(size=12, color="red", ...)`)
        grid_label_formatter : Callable[[float], str] | None, optional
            User-defined function to format grid label (e.g. `lambda v: f"{v:.1f}%"`).
        label_kws_handler : Callable[[str], dict[str, Any]] | None, optional
            Handler function for keyword arguments passed to `track.text()` method.
            Handler function takes each column name of table as an argument.
        line_kws_handler : Callable[[str], dict[str, Any]] | None, optional
            Handler function for keyword arguments passed to `track.line()` method.
            Handler function takes each row(index) name of table as an argument.
        marker_kws_handler : Callable[[str], dict[str, Any]] | None, optional
            Handler function for keyword arguments passed to `track.scatter()` method.
            Handler function takes each row(index) name of table as an argument.

        Returns
        -------
        circos : Circos
            Circos instance initialized for radar chart
        """
        # TODO: Refactor complex codes
        if not vmin < vmax:
            raise ValueError(f"vmax must be larger than vmin ({vmin=}, {vmax=})")
        size = vmax - vmin

        # Setup default properties
        grid_line_kws = {} if grid_line_kws is None else deepcopy(grid_line_kws)
        for k, v in dict(color="grey", ls="dashed", lw=0.5).items():
            grid_line_kws.setdefault(k, v)

        grid_label_kws = {} if grid_label_kws is None else deepcopy(grid_label_kws)
        for k, v in dict(color="dimgrey", size=10, ha="left", va="top").items():
            grid_label_kws.setdefault(k, v)

        # Initialize circos for radar chart
        radar_table = table if isinstance(table, RadarTable) else RadarTable(table)
        circos = Circos(dict(radar=radar_table.col_num))
        sector = circos.sectors[0]
        track = sector.add_track(r_lim)
        x = np.arange(radar_table.col_num + 1)

        # Plot background color
        if bg_color:
            track.fill_between(x, [vmax] * len(x), arc=circular, color=bg_color)

        # Plot grid line
        if grid_interval_ratio:
            if not 0 < grid_interval_ratio <= 1.0:
                raise ValueError(f"{grid_interval_ratio=} is invalid.")
            # Plot horizontal grid line & label
            stop, step = vmax + (size / 1000), size * grid_interval_ratio
            for v in np.arange(vmin, stop, step, dtype=np.float64):
                y = [v] * len(x)
                track.line(x, y, vmin=vmin, vmax=vmax, arc=circular, **grid_line_kws)
                if show_grid_label:
                    r = track._y_to_r(v, vmin, vmax)
                    # Format grid label
                    if grid_label_formatter:
                        text = grid_label_formatter(v)
                    else:
                        v2 = float(f"{v:.9f}")  # Correct rounding error
                        text = f"{v2:.0f}" if math.isclose(int(v2), v2) else str(v2)
                    track.text(text, 0, r, **grid_label_kws)
            # Plot vertical grid line
            for p in x[:-1]:
                track.line([p, p], [vmin, vmax], vmin=vmin, vmax=vmax, **grid_line_kws)

        # Plot radar charts
        if isinstance(cmap, str):
            row_name2color = radar_table.get_row_name2color(cmap)
        else:
            row_name2color = cmap
        for row_name, values in radar_table.row_name2values.items():
            y = [*values, values[0]]
            color = row_name2color[row_name]
            line_kws = line_kws_handler(row_name) if line_kws_handler else {}
            line_kws.setdefault("lw", 1.0)
            line_kws.setdefault("label", row_name)
            track.line(x, y, vmin=vmin, vmax=vmax, arc=False, color=color, **line_kws)
            if marker_size > 0:
                marker_kws = marker_kws_handler(row_name) if marker_kws_handler else {}
                marker_kws.setdefault("marker", "o")
                marker_kws.setdefault("zorder", 2)
                marker_kws.update(s=marker_size**2)
                marker_kws.update(tooltip=radar_table.get_row_tooltip(row_name))
                track.scatter(x, y, vmin=vmin, vmax=vmax, color=color, **marker_kws)
            if fill:
                fill_kws = dict(arc=False, color=color, alpha=0.5)
                track.fill_between(x, y, y2=vmin, vmin=vmin, vmax=vmax, **fill_kws)  # type:ignore

        # Plot column names
        for idx, col_name in enumerate(radar_table.col_names):
            deg = 360 * (idx / sector.size)
            label_kws = label_kws_handler(col_name) if label_kws_handler else {}
            label_kws.setdefault("size", 12)
            if math.isclose(deg, 0):
                label_kws.update(va="bottom")
            elif math.isclose(deg, 180):
                label_kws.update(va="top")
            elif 0 < deg < 180:
                label_kws.update(ha="left")
            elif 180 < deg < 360:
                label_kws.update(ha="right")
            track.text(col_name, idx, r=105, adjust_rotation=False, **label_kws)

        return circos

    @staticmethod
    def chord_diagram(
        matrix: str | Path | pd.DataFrame | Matrix,
        *,
        start: float = 0,
        end: float = 360,
        space: Numeric | Sequence[Numeric] = 0,
        endspace: bool = True,
        r_lim: tuple[float, float] = (97, 100),
        cmap: str | dict[str, str] = "viridis",
        link_cmap: list[tuple[str, str, str]] | None = None,
        ticks_interval: int | None = None,
        order: str | list[str] | None = None,
        label_kws: dict[str, Any] | None = None,
        ticks_kws: dict[str, Any] | None = None,
        link_kws: dict[str, Any] | None = None,
        link_kws_handler: Callable[[str, str], dict[str, Any] | None] | None = None,
    ) -> Circos:
        """Plot chord diagram

        Circos tracks and links are auto-defined from Matrix

        Parameters
        ----------
        matrix : str | Path | pd.DataFrame | Matrix
            Matrix file or Matrix dataframe or Matrix instance
        start : float, optional
            Plot start degree (-360 <= start < end <= 360)
        end : float, optional
            Plot end degree (-360 <= start < end <= 360)
        space : Numeric | NumericSequence, optional
            Space degree(s) between sector
        endspace : bool, optional
            If True, insert space after the end sector
        r_lim : tuple[float, float], optional
            Outer track radius limit region (0 - 100)
        cmap : str | dict[str, str], optional
            Colormap assigned to each outer track and link.
            User can set matplotlib's colormap (e.g. `viridis`, `jet`, `tab10`) or
            label_name -> color dict (e.g. `dict(A="red", B="blue", C="green", ...)`)
        link_cmap : list[tuple[str, str, str]] | None, optional
            Link colormap to overwrite link colors automatically set by cmap.
            User can set list of `from_label`, `to_label`, `color` tuple
            (e.g. `[("A", "B", "red"), ("A", "C", "#ffff00"), ...]`)
        ticks_interval : int | None, optional
            Ticks interval. If None, ticks are not plotted.
        order : str | list[str] | None, optional
            Sort order of matrix for plotting Chord Diagram. If `None`, no sorting.
            If `asc`|`desc`, sort in ascending(or descending) order by node size.
            If node name list is set, sort in user specified node order.
        label_kws : dict[str, Any] | None, optional
            Keyword arguments passed to `sector.text()` method
            (e.g. `dict(r=110, orientation="vertical", size=15, ...)`)
        ticks_kws : dict[str, Any] | None, optional
            Keyword arguments passed to `track.xticks_by_interval()` method
            (e.g. `dict(label_size=10, label_orientation="vertical", ...)`)
        link_kws : dict[str, Any] | None, optional
            Keyword arguments passed to `circos.link()` method
            (e.g. `dict(direction=1, ec="black", lw=0.5, alpha=0.8, ...)`)
        link_kws_handler : Callable[[str, str], dict[str, Any] | None] | None, optional
            User-defined function to handle keyword arguments for each link.
            This option allows user to set or override properties such as
            `fc`, `alpha`, `zorder`, etc... on each link.
            Handler function arguments `[str, str]` means `[from_label, to_label]`.

        Returns
        -------
        circos : Circos
            Circos instance initialized from Matrix
        """
        link_cmap = [] if link_cmap is None else deepcopy(link_cmap)
        label_kws = {} if label_kws is None else deepcopy(label_kws)
        ticks_kws = {} if ticks_kws is None else deepcopy(ticks_kws)
        link_kws = {} if link_kws is None else deepcopy(link_kws)

        # If input matrix is file path, convert to Matrix instance
        if isinstance(matrix, (str, Path, pd.DataFrame)):
            matrix = Matrix(matrix)

        # Sort matrix if order is set
        if order is not None:
            matrix = matrix.sort(order)

        # Get name2color dict from user-specified colormap
        names = matrix.all_names
        if isinstance(cmap, str):
            utils.ColorCycler.set_cmap(cmap)
            colors = utils.ColorCycler.get_color_list(len(names))
            name2color = dict(zip(names, colors, strict=True))
        elif isinstance(cmap, defaultdict):
            name2color = cmap
        else:
            name2color: dict[str, str] = defaultdict(lambda: "grey")
            name2color.update(cmap)

        # Initialize circos sectors
        circos = Circos(matrix.to_sectors(), start, end, space=space, endspace=endspace)
        for sector in circos.sectors:
            # Plot label, outer track axis & xticks
            sector.text(sector.name, **label_kws)
            outer_track = sector.add_track(r_lim)
            color = name2color[sector.name]
            outer_track.axis(fc=color)
            if ticks_interval is not None:
                outer_track.xticks_by_interval(ticks_interval, **ticks_kws)

        # Plot links
        fromto_label2color = {f"{t[0]}-->{t[1]}": t[2] for t in link_cmap}
        for link in matrix.to_links():
            from_label, to_label = link[0][0], link[1][0]
            fromto_label = f"{from_label}-->{to_label}"
            # Set link color
            if fromto_label in fromto_label2color:
                color = fromto_label2color[fromto_label]
            else:
                color = name2color[from_label]
            # Update link properties by user-defined handler function
            _link_kws = deepcopy(link_kws)
            _link_kws.update(fc=color)
            if link_kws_handler is not None:
                handle_link_kws = link_kws_handler(from_label, to_label)
                if handle_link_kws is not None:
                    _link_kws.update(handle_link_kws)
            circos.link(*link, **_link_kws)

        return circos

    initialize_from_matrix = chord_diagram  # For backward compatibility

    @staticmethod
    def initialize_from_tree(
        tree_data: str | Path | Tree,
        *,
        start: float = 0,
        end: float = 360,
        r_lim: tuple[float, float] = (50, 100),
        format: str = "newick",
        outer: bool = True,
        align_leaf_label: bool = True,
        ignore_branch_length: bool = False,
        leaf_label_size: float = 12,
        leaf_label_rmargin: float = 2.0,
        reverse: bool = False,
        ladderize: bool = False,
        line_kws: dict[str, Any] | None = None,
        label_formatter: Callable[[str], str] | None = None,
        align_line_kws: dict[str, Any] | None = None,
    ) -> tuple[Circos, TreeViz]:
        """Initialize Circos instance from phylogenetic tree

        Circos sector and track are auto-defined by phylogenetic tree

        Parameters
        ----------
        tree_data : str | Path | Tree
            Tree data (`File`|`File URL`|`Tree Object`|`Tree String`)
        start : float, optional
            Plot start degree (-360 <= start < end <= 360)
        end : float, optional
            Plot end degree (-360 <= start < end <= 360)
        r_lim : tuple[float, float], optional
            Tree track radius limit region (0 - 100)
        format : str, optional
            Tree format (`newick`|`phyloxml`|`nexus`|`nexml`|`cdao`)
        outer : bool, optional
            If True, plot tree on outer side. If False, plot tree on inner side.
        align_leaf_label: bool, optional
            If True, align leaf label.
        ignore_branch_length : bool, optional
            If True, ignore branch length for plotting tree.
        leaf_label_size : float, optional
            Leaf label size
        leaf_label_rmargin : float, optional
            Leaf label radius margin
        reverse : bool, optional
            If True, reverse tree
        ladderize : bool, optional
            If True, ladderize tree
        line_kws : dict[str, Any] | None, optional
            Patch properties (e.g. `dict(color="red", lw=1, ls="dashed", ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        align_line_kws : dict[str, Any] | None, optional
            Patch properties (e.g. `dict(lw=1, ls="dotted", alpha=1.0, ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        label_formatter : Callable[[str], str] | None, optional
            User-defined label text format function to change plot label text content.
            For example, if you want to change underscore of the label to space,
            set `lambda t: t.replace("_", " ")`.

        Returns
        -------
        circos : Circos
            Circos instance
        tv : TreeViz
            TreeViz instance
        """
        # Initialize circos sector with tree size
        tree = TreeViz.load_tree(tree_data, format=format)
        leaf_num = tree.count_terminals()
        circos = Circos(dict(tree=leaf_num), start=start, end=end)
        sector = circos.sectors[0]

        # Plot tree on track
        track = sector.add_track(r_lim)
        tv = track.tree(
            tree,
            format=format,
            outer=outer,
            align_leaf_label=align_leaf_label,
            ignore_branch_length=ignore_branch_length,
            leaf_label_size=leaf_label_size,
            leaf_label_rmargin=leaf_label_rmargin,
            reverse=reverse,
            ladderize=ladderize,
            line_kws=line_kws,
            label_formatter=label_formatter,
            align_line_kws=align_line_kws,
        )
        return circos, tv

    @staticmethod
    def initialize_from_bed(
        bed_file: str | Path,
        start: float = 0,
        end: float = 360,
        *,
        space: Numeric | Sequence[Numeric] = 0,
        endspace: bool = True,
        sector2clockwise: dict[str, bool] | None = None,
    ) -> Circos:
        """Initialize Circos instance from BED file

        Circos sectors are auto-defined by BED chromosomes

        Parameters
        ----------
        bed_file : str | Path
            Chromosome BED format file (zero-based coordinate)
        start : float, optional
            Plot start degree (-360 <= start < end <= 360)
        end : float, optional
            Plot end degree (-360 <= start < end <= 360)
        space : float | Sequence[float], optional
            Space degree(s) between sector
        endspace : bool, optional
            If True, insert space after the end sector
        sector2clockwise : dict[str, bool] | None, optional
            Sector name & clockwise bool dict. By default, `clockwise=True`.

        Returns
        -------
        circos : Circos
            Circos instance initialized from BED file
        """
        records = Bed(bed_file).records
        sectors = {rec.chr: (rec.start, rec.end) for rec in records}
        return Circos(
            sectors,
            start,
            end,
            space=space,
            endspace=endspace,
            sector2clockwise=sector2clockwise,
        )

    def add_cytoband_tracks(
        self,
        r_lim: tuple[float, float],
        cytoband_file: str | Path,
        *,
        track_name: str = "cytoband",
        cytoband_cmap: dict[str, str] | None = None,
    ) -> None:
        """Add track & plot chromosome cytoband on each sector

        Parameters
        ----------
        r_lim : tuple[float, float]
            Radius limit region (0 - 100)
        cytoband_file : str | Path
            Cytoband tsv file (UCSC format)
        track_name : str, optional
            Cytoband track name. By default, `cytoband`.
        cytoband_cmap : dict[str, str] | None, optional
            User-defined cytoband colormap. If None, use Circos style colormap.
            (e.g. `{"gpos100": "#000000", "gneg": "#FFFFFF", ...}`)
        """
        if cytoband_cmap is None:
            cytoband_cmap = config.CYTOBAND_COLORMAP
        cytoband_records = Bed(cytoband_file).records
        for sector in self.sectors:
            track = sector.add_track(r_lim, name=track_name)
            track.axis()
            for rec in cytoband_records:
                if sector.name == rec.chr:
                    color = cytoband_cmap.get(str(rec.score), "white")
                    tooltip = to_cytoband_tooltip(rec)
                    track.rect(rec.start, rec.end, tooltip=tooltip, fc=color)

    def get_sector(self, name: str) -> Sector:
        """Get sector by name

        Parameters
        ----------
        name : str
            Sector name

        Returns
        -------
        sector : Sector
            Sector
        """
        name2sector = {s.name: s for s in self.sectors}
        if name not in name2sector:
            raise ValueError(f"{name=} sector not found.")
        return name2sector[name]

    def get_group_sectors_deg_lim(
        self,
        group_sector_names: list[str],
    ) -> tuple[float, float]:
        """Get degree min-max limit in target group sectors

        Parameters
        ----------
        group_sector_names : list[str]
            Group sector names

        Returns
        -------
        group_sectors_deg_lim : tuple[float, float]
            Degree limit in group sectors
        """
        group_sectors = [self.get_sector(name) for name in group_sector_names]
        min_deg = min([min(s.deg_lim) for s in group_sectors])
        max_deg = max([max(s.deg_lim) for s in group_sectors])
        return min_deg, max_deg

    def axis(self, **kwargs) -> None:
        """Plot axis

        By default, simple black axis params(`fc="none", ec="black", lw=0.5`) are set.

        Parameters
        ----------
        **kwargs : dict, optional
            Patch properties (e.g. `fc="red", ec="blue", lw=0.5, ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        """
        # Set default params
        kwargs = utils.plot.set_axis_default_kwargs(**kwargs)

        # Axis facecolor placed behind other patches (zorder=0.99)
        fc_behind_kwargs = {**kwargs, **config.AXIS_FACE_PARAM}
        self.rect(**fc_behind_kwargs)

        # Axis edgecolor placed in front of other patches (zorder=1.01)
        ec_front_kwargs = {**kwargs, **config.AXIS_EDGE_PARAM}
        self.rect(**ec_front_kwargs)

    def text(
        self,
        text: str,
        *,
        r: float = 0,
        deg: float = 0,
        adjust_rotation: bool = False,
        orientation: str = "horizontal",
        **kwargs,
    ) -> None:
        """Plot text

        Parameters
        ----------
        text : str
            Text content
        r : float
            Radius position
        deg : float
            Degree position (0 - 360)
        adjust_rotation : bool, optional
            If True, text rotation is auto set based on `deg` param.
        orientation : str, optional
            Text orientation (`horizontal` or `vertical`)
            If adjust_rotation=True, orientation is used for rotation calculation.
        **kwargs : dict, optional
            Text properties (e.g. `size=12, color="red", rotation=90, ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html>
        """
        if "va" not in kwargs and "verticalalignment" not in kwargs:
            kwargs.update(dict(va="center"))
        if "ha" not in kwargs and "horizontalalignment" not in kwargs:
            kwargs.update(dict(ha="center"))
        if adjust_rotation:
            rad = math.radians(deg)
            params = utils.plot.get_label_params_by_rad(rad, orientation)
            kwargs.update(**params)

        def plot_text(ax: PolarAxes) -> None:
            ax.text(math.radians(deg), r, text, **kwargs)

        self._plot_funcs.append(plot_text)

    def line(
        self,
        *,
        r: float | tuple[float, float],
        deg_lim: tuple[float, float] | None = None,
        arc: bool = True,
        **kwargs,
    ) -> None:
        """Plot line

        Parameters
        ----------
        r : float | tuple[float, float]
            Line radius position (0 - 100). If r is float, (r, r) is set.
        deg_lim : tuple[float, float] | None, optional
            Degree limit region (-360 - 360). If None, `circos.deg_lim` is set.
        arc : bool, optional
            If True, plot arc style line for polar projection.
            If False, simply plot linear style line.
        **kwargs : dict, optional
            Patch properties (e.g. `color="red", lw=3, ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        """
        deg_lim = self.deg_lim if deg_lim is None else deg_lim
        rad_lim = (math.radians(min(deg_lim)), math.radians(max(deg_lim)))
        r_lim = r if isinstance(r, Sequence) else (r, r)
        LinePatch = ArcLine if arc else Line
        self._patches.append(LinePatch(rad_lim, r_lim, **kwargs))

    def rect(
        self,
        r_lim: tuple[float, float] = (0, 100),
        deg_lim: tuple[float, float] | None = None,
        **kwargs,
    ) -> None:
        """Plot rectangle

        Parameters
        ----------
        r_lim : tuple[float, float]
            Radius limit region (0 - 100)
        deg_lim : tuple[float, float]
            Degree limit region (-360 - 360). If None, `circos.deg_lim` is set.
        **kwargs : dict, optional
            Patch properties (e.g. `fc="red", ec="black", lw=1, hatch="//", ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        """
        deg_lim = self.deg_lim if deg_lim is None else deg_lim
        rad_lim = (math.radians(min(deg_lim)), math.radians(max(deg_lim)))

        radr = (min(rad_lim), min(r_lim))
        width = max(rad_lim) - min(rad_lim)
        height = max(r_lim) - min(r_lim)
        self._patches.append(ArcRectangle(radr, width, height, **kwargs))

    def link(
        self,
        sector_region1: tuple[str, float, float],
        sector_region2: tuple[str, float, float],
        r1: float | None = None,
        r2: float | None = None,
        *,
        color: str = "grey",
        alpha: float = 0.5,
        height_ratio: float = 0.5,
        direction: int = 0,
        arrow_length_ratio: float = 0.05,
        allow_twist: bool = True,
        **kwargs,
    ) -> None:
        """Plot link to specified region within or between sectors

        Parameters
        ----------
        sector_region1 : tuple[str, float, float]
            Link sector region1 (name, start, end)
        sector_region2 : tuple[str, float, float]
            Link sector region2 (name, start, end)
        r1 : float | None, optional
            Link radius end position for sector_region1.
            If None, lowest radius position of track in target sector is set.
        r2 : float | None, optional
            Link radius end position for sector_region2.
            If None, lowest radius position of track in target sector is set.
        color : str, optional
            Link color
        alpha : float, optional
            Link color alpha (transparency) value
        height_ratio : float, optional
            Bezier curve height ratio
        direction : int, optional
            `0`: No direction edge shape (Default)
            `1`: Forward direction arrow edge shape (region1 -> region2)
            `-1`: Reverse direction arrow edge shape (region1 <- region2)
            `2`: Bidirectional arrow edge shape (region1 <-> region2)
        arrow_length_ratio : float, optional
            Direction arrow length ratio
        allow_twist : bool, optional
            If False, twisted link is automatically resolved.
            <http://circos.ca/documentation/tutorials/links/twists/images>
        **kwargs : dict, optional
            Patch properties (e.g. `ec="red", lw=1.0, hatch="//", ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        """
        # Set data for plot link
        name1, start1, end1 = sector_region1
        name2, start2, end2 = sector_region2
        sector1, sector2 = self.get_sector(name1), self.get_sector(name2)
        r1 = sector1.get_lowest_r() if r1 is None else r1
        r2 = sector2.get_lowest_r() if r2 is None else r2
        rad_start1, rad_end1 = sector1.x_to_rad(start1), sector1.x_to_rad(end1)
        rad_start2, rad_end2 = sector2.x_to_rad(start2), sector2.x_to_rad(end2)

        # Set patch kwargs & default linewidth as 0.1
        # If linewidth=0 is set, twisted part is almost invisible
        kwargs.update(dict(color=color, alpha=alpha))
        if "lw" not in kwargs and "linewidth" not in kwargs:
            kwargs.update(dict(lw=0.1))

        if not allow_twist and (rad_end1 - rad_start1) * (rad_end2 - rad_start2) > 0:
            rad_start2, rad_end2 = rad_end2, rad_start2

        # Set tooltip content
        gid = gen_gid("link")
        kwargs["gid"] = gid
        tooltip = to_link_tooltip(sector_region1, sector_region2, direction)
        self._gid2tooltip[gid] = tooltip

        # Create bezier curve path patch
        bezier_curve_link = BezierCurveLink(
            rad_start1,
            rad_end1,
            r1,
            rad_start2,
            rad_end2,
            r2,
            height_ratio,
            direction,
            arrow_length_ratio,
            **kwargs,
        )
        self._patches.append(bezier_curve_link)

    def link_line(
        self,
        sector_pos1: tuple[str, float],
        sector_pos2: tuple[str, float],
        r1: float | None = None,
        r2: float | None = None,
        *,
        color: str = "black",
        height_ratio: float = 0.5,
        direction: int = 0,
        arrow_height: float = 3.0,
        arrow_width: float = 2.0,
        **kwargs,
    ) -> None:
        """Plot link line to specified position within or between sectors

        Parameters
        ----------
        sector_pos1 : tuple[str, float]
            Link line sector position1 (name, position)
        sector_pos2 : tuple[str, float]
            Link line sector position2 (name, position)
        r1 : float | None, optional
            Link line radius end position for sector_pos1.
            If None, lowest radius position of track in target sector is set.
        r2 : float | None, optional
            Link line radius end position for sector_pos2.
            If None, lowest radius position of track in target sector is set.
        color : str, optional
            Link line color
        height_ratio : float, optional
            Bezier curve height ratio
        direction : int, optional
            `0`: No direction edge shape (Default)
            `1`: Forward direction arrow edge shape (pos1 -> pos2)
            `-1`: Reverse direction arrow edge shape (pos1 <- pos2)
            `2`: Bidirectional arrow edge shape (pos1 <-> pos2)
        arrow_height : float, optional
            Arrow height size (Radius unit)
        arrow_width : float, optional
            Arrow width size (Degree unit)
        **kwargs : dict, optional
            Patch properties (e.g. `lw=1.0, ls="dashed", ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        """
        # Set data for plot link
        name1, pos1 = sector_pos1
        name2, pos2 = sector_pos2
        sector1, sector2 = self.get_sector(name1), self.get_sector(name2)
        r1 = sector1.get_lowest_r() if r1 is None else r1
        r2 = sector2.get_lowest_r() if r2 is None else r2
        rad_pos1, rad_pos2 = sector1.x_to_rad(pos1), sector2.x_to_rad(pos2)

        kwargs.update(color=color)

        bezier_curve_line = BezierCurveLine(
            rad_pos1,
            r1,
            rad_pos2,
            r2,
            height_ratio,
            direction,
            arrow_height,
            arrow_width,
            **kwargs,
        )
        self._patches.append(bezier_curve_line)

    def colorbar(
        self,
        bounds: tuple[float, float, float, float] = (1.02, 0.3, 0.02, 0.4),
        *,
        vmin: float = 0,
        vmax: float = 1,
        cmap: str | Colormap = "bwr",
        orientation: str = "vertical",
        label: str | None = None,
        colorbar_kws: dict[str, Any] | None = None,
        label_kws: dict[str, Any] | None = None,
        tick_kws: dict[str, Any] | None = None,
    ) -> None:
        """Plot colorbar

        Parameters
        ----------
        bounds : tuple[float, float, float, float], optional
            Colorbar bounds tuple (`x`, `y`, `width`, `height`)
        vmin : float, optional
            Colorbar min value
        vmax : float, optional
            Colorbar max value
        cmap : str | Colormap, optional
            Colormap (e.g. `viridis`, `Spectral`, `Reds`, `Greys`)
            <https://matplotlib.org/stable/tutorials/colors/colormaps.html>
        orientation : str, optional
            Colorbar orientation (`vertical`|`horizontal`)
        label : str | None, optional
            Colorbar label. If None, no label shown.
        colorbar_kws : dict[str, Any] | None, optional
            Colorbar properties (e.g. `dict(format="%.1f", ...)`)
            <https://matplotlib.org/stable/api/colorbar_api.html>
        label_kws : dict[str, Any] | None, optional
            Text properties (e.g. `dict(size=15, color="red", ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html>
        tick_kws : dict[str, Any] | None, optional
            Axes.tick_params properties (e.g. `dict(labelsize=12, colors="red", ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html>
        """
        colorbar_kws = {} if colorbar_kws is None else deepcopy(colorbar_kws)
        label_kws = {} if label_kws is None else deepcopy(label_kws)
        tick_kws = {} if tick_kws is None else deepcopy(tick_kws)

        def plot_colorbar(ax: PolarAxes) -> None:
            axin: Axes = ax.inset_axes(bounds)
            norm = Normalize(vmin=vmin, vmax=vmax)
            cb = Colorbar(
                axin,
                cmap=cmap,  # type: ignore
                norm=norm,
                orientation=orientation,  # type: ignore
                **colorbar_kws,
            )
            axin.tick_params(**tick_kws)
            if label:
                cb.set_label(label, **label_kws)

        self._plot_funcs.append(plot_colorbar)

    def plotfig(
        self,
        dpi: int = 100,
        *,
        ax: PolarAxes | None = None,
        figsize: tuple[float, float] = (8, 8),
        tooltip: bool = False,
    ) -> Figure:
        """Plot figure

        Parameters
        ----------
        dpi : int, optional
            Figure DPI
        ax : PolarAxes | None
            If None, figure and axes are newly created.
        figsize : tuple[float, float], optional
            Figure size
        tooltip : bool, optional
            If True, display tooltip on jupyter using `ipympl`.
            In the case of plotting on user-defined axes(figure),
            `Circos.set_tooltip_enabled()` must be called before
            creating figure to display tooltip.

        Returns
        -------
        figure : Figure
            Circos matplotlib figure
        """
        self.set_tooltip_enabled(tooltip)

        if ax is None:
            # Initialize Figure & PolarAxes
            fig, ax = self._initialize_figure(figsize=figsize, dpi=dpi)
        else:
            # Check PolarAxes or not
            if not isinstance(ax, PolarAxes):
                ax_class_name = type(ax).__name__
                raise ValueError(f"Input ax is not PolarAxes (={ax_class_name}).")
            fig = ax.get_figure()
        self._initialize_polar_axes(ax)

        # Plot trees (add 'patches' & 'plot functions')
        for tv in self._get_all_treeviz_list():
            tv._plot_tree_line()
            tv._plot_tree_label()

        # Plot all patches
        patches = []
        for patch in self._get_all_patches():
            # Set clip_on=False to enable Patch to be displayed outside of Axes
            patch.set_clip_on(False)
            # Collection cannot handle `zorder`, `hatch`
            # Separate default or user-defined `zorder`, `hatch` property patch
            zorder, hatch = patch.get_zorder(), patch.get_hatch()
            if not config.tooltip.enabled and zorder == 1 and hatch is None:
                patches.append(patch)
            else:
                ax.add_patch(patch)
        ax.add_collection(PatchCollection(patches, match_original=True, clip_on=False))  # type: ignore

        # Execute all plot functions
        for plot_func in self._get_all_plot_funcs():
            plot_func(ax)

        # Adjust annotation text position
        if config.ann_adjust.enable:
            adjust_annotation(ax)

        # Display patch tooltip
        if config.tooltip.enabled:
            set_patch_tooltip(ax, ax.patches, self._get_all_gid2tooltip())

        return fig  # type: ignore

    def savefig(
        self,
        savefile: str | Path,
        *,
        dpi: int = 100,
        figsize: tuple[float, float] = (8, 8),
        pad_inches: float = 0.5,
    ) -> None:
        """Save figure to file

        Parameters
        ----------
        savefile : str | Path
            Save file (`*.png`|`*.jpg`|`*.svg`|`*.pdf`)
        dpi : int, optional
            DPI
        figsize : tuple[float, float], optional
            Figure size
        pad_inches : float, optional
            Padding inches

        Warnings
        --------
        To plot a figure that settings a user-defined legend, subtracks, or annotations,
        call `fig.savefig()` instead of `gv.savefig()`.
        """
        fig = self.plotfig(dpi=dpi, figsize=figsize)
        fig.savefig(
            fname=savefile,  # type: ignore
            dpi=dpi,
            pad_inches=pad_inches,
            bbox_inches="tight",
        )
        # Clear & close figure to suppress memory leak
        if config.clear_savefig:
            fig.clear()
            plt.close(fig)

    ############################################################
    # Private Method
    ############################################################

    def _check_degree_range(self, start: float, end: float) -> None:
        """Check start-end degree range (`-360 <= start < end <= 360`)

        Parameters
        ----------
        start : float
            Start degree range
        end : float
            End degree range
        """
        min_deg, max_deg = -360, 360
        if not min_deg <= start < end <= max_deg:
            raise ValueError(f"start-end must be '{min_deg} <= start < end <= {max_deg}' ({start=}, {end=})")  # fmt: skip  # noqa: E501
        if end - start > max_deg:
            raise ValueError(f"'end - start' must be less than {max_deg} ({start=}, {end=})")  # fmt: skip  # noqa: E501

    def _to_sector2range(
        self,
        sectors: Mapping[str, Numeric | tuple[Numeric, Numeric]],
    ) -> dict[str, tuple[float, float]]:
        """Convert sectors to sector2range"""
        sector2range: dict[str, tuple[float, float]] = {}
        for name, value in sectors.items():
            if isinstance(value, Sequence):
                sector_start, sector_end = value
                if not sector_start < sector_end:
                    raise ValueError(f"{sector_end=} must be larger than {sector_start=}.")  # fmt: skip  # noqa: E501
                sector2range[name] = (sector_start, sector_end)
            else:
                sector2range[name] = (0, value)
        return sector2range

    def _initialize_figure(
        self,
        figsize: tuple[float, float] = (8, 8),
        dpi: int = 100,
    ) -> tuple[Figure, PolarAxes]:
        """Initialize figure

        Parameters
        ----------
        figsize : tuple[float, float], optional
            Figure size
        dpi : int, optional
            Figure DPI

        Returns
        -------
        fig : Figure
            Figure
        ax : PolarAxes
            PolarAxes
        """
        fig = plt.figure(figsize=figsize, dpi=dpi, tight_layout=True)
        ax = fig.add_subplot(projection="polar")
        return fig, ax  # type: ignore

    def _initialize_polar_axes(self, ax: PolarAxes) -> None:
        """Initialize polar axes params

        Parameters
        ----------
        ax : PolarAxes
            PolarAxes
        """
        ax.set_theta_zero_location("N")
        ax.set_theta_direction(-1)
        # Reason for setting the max radius limit at MAX_R(100) + R_PLOT_MARGIN
        # Because a portion of the patch at the upper boundary of 100 may be missed.
        ax.set_rlim(bottom=config.MIN_R, top=config.MAX_R + config.R_PLOT_MARGIN)

        show_axis = "on" if self._show_axis_for_debug else "off"
        ax.axis(show_axis)
        self._ax = ax

    def _get_all_patches(self) -> list[Patch]:
        """Get all patches from `circos, sector, track`

        Returns
        -------
        all_patches : list[Patch]
            All patches
        """
        circos_patches = self._patches
        sector_patches = list(itertools.chain(*[s.patches for s in self.sectors]))
        track_patches = list(itertools.chain(*[t.patches for t in self.tracks]))
        all_patches = circos_patches + sector_patches + track_patches
        # deepcopy to avoid putting original patch to figure
        return deepcopy(all_patches)

    def _get_all_plot_funcs(self) -> list[Callable[[PolarAxes], None]]:
        """Get all plot functions from `circos, sector, track`

        Returns
        -------
        all_plot_funcs : list[Callable[[PolarAxes], None]]
            All plot functions
        """
        circos_plot_funcs = self._plot_funcs
        sector_plot_funcs = list(itertools.chain(*[s.plot_funcs for s in self.sectors]))
        track_plot_funcs = list(itertools.chain(*[t.plot_funcs for t in self.tracks]))
        all_plot_funcs = circos_plot_funcs + sector_plot_funcs + track_plot_funcs
        return all_plot_funcs

    def _get_all_treeviz_list(self) -> list[TreeViz]:
        """Get all tree visualization instance list from tracks

        Returns
        -------
        all_treeviz_list : list[TreeViz]
            All tree visualization instance list
        """
        return list(itertools.chain(*[t._trees for t in self.tracks]))

    def _get_all_gid2tooltip(self) -> dict[str, str]:
        """Get all gid & tooltip dict

        Returns
        -------
        gid2tooltip : dict[str, str]
            Group ID & tooltip dict
        """
        all_gid2tooltip: dict[str, str] = {}
        all_gid2tooltip |= self._gid2tooltip
        for sector in self.sectors:
            all_gid2tooltip |= sector._gid2tooltip
        for track in self.tracks:
            all_gid2tooltip |= track._gid2tooltip
        return all_gid2tooltip
