from __future__ import annotations

import math
import textwrap
from collections.abc import Callable, Sequence
from copy import deepcopy
from typing import TYPE_CHECKING, Any

import matplotlib as mpl
import numpy as np
from Bio.SeqFeature import SeqFeature
from matplotlib.colors import Colormap, Normalize

from pycirclize import config, utils
from pycirclize.parser import StackedBarTable
from pycirclize.patches import ArcArrow, ArcLine, ArcRectangle
from pycirclize.tooltip import gen_gid, set_collection_tooltip, to_feature_tooltip
from pycirclize.tree import TreeViz
from pycirclize.utils.plot import select_textcolor

if TYPE_CHECKING:
    from pathlib import Path

    import pandas as pd
    from Bio.Phylo.BaseTree import Tree
    from matplotlib.patches import Patch
    from matplotlib.projections.polar import PolarAxes
    from PIL import Image

    from pycirclize.sector import Sector
    from pycirclize.typing import Numeric, NumericArrayLike


class Track:
    """Circos Track Class"""

    def __init__(
        self,
        name: str,
        r_lim: tuple[float, float],
        r_pad_ratio: float,
        parent_sector: Sector,
    ) -> None:
        """
        Parameters
        ----------
        name : str
            Track name
        r_lim : tuple[float, float]
            Track radius limit region
        r_pad_ratio : float
            Track padding ratio for plot data
        parent_sector : Sector
            Parent sector of track
        """
        # Track params
        self._name = name
        self._r_lim = r_lim
        self._r_pad_ratio = r_pad_ratio
        # Inherited from parent sector
        self._parent_sector = parent_sector
        self._rad_lim = parent_sector.rad_lim
        self._start = parent_sector.start
        self._end = parent_sector.end

        # Plot data and functions
        self._patches: list[Patch] = []
        self._gid2tooltip: dict[str, str] = {}
        self._plot_funcs: list[Callable[[PolarAxes], None]] = []
        self._trees: list[TreeViz] = []

    ############################################################
    # Property
    ############################################################

    @property
    def name(self) -> str:
        """Track name"""
        return self._name

    @property
    def size(self) -> float:
        """Track size (x coordinate)"""
        return self.end - self.start

    @property
    def start(self) -> float:
        """Track start position (x coordinate)"""
        return self._start

    @property
    def end(self) -> float:
        """Track end position (x coordinate)"""
        return self._end

    @property
    def center(self) -> float:
        """Track center position (x coordinate)"""
        return (self.start + self.end) / 2

    @property
    def r_size(self) -> float:
        """Track radius size"""
        return max(self.r_lim) - min(self.r_lim)

    @property
    def r_lim(self) -> tuple[float, float]:
        """Track radius limit"""
        return self._r_lim

    @property
    def r_center(self) -> float:
        """Track center radius"""
        return sum(self.r_lim) / 2

    @property
    def r_plot_size(self) -> float:
        """Track radius size for plot data (`r_size` with padding)"""
        return max(self.r_plot_lim) - min(self.r_plot_lim)

    @property
    def r_plot_lim(self) -> tuple[float, float]:
        """Track radius limit for plot data (`r_lim` with padding)"""
        edge_pad_size = (self.r_size * self._r_pad_ratio) / 2
        min_plot_r = min(self.r_lim) + edge_pad_size
        max_plot_r = max(self.r_lim) - edge_pad_size
        return (min_plot_r, max_plot_r)

    @property
    def rad_size(self) -> float:
        """Track radian size"""
        return max(self.rad_lim) - min(self.rad_lim)

    @property
    def rad_lim(self) -> tuple[float, float]:
        """Track radian limit"""
        return self._rad_lim

    @property
    def deg_size(self) -> float:
        """Track degree size"""
        return max(self.deg_lim) - min(self.deg_lim)

    @property
    def deg_lim(self) -> tuple[float, float]:
        """Track degree limit"""
        return (math.degrees(min(self.rad_lim)), math.degrees(max(self.rad_lim)))

    @property
    def parent_sector(self) -> Sector:
        """Parent sector"""
        return self._parent_sector

    @property
    def clockwise(self) -> bool:
        """Track coordinate direction"""
        return self.parent_sector.clockwise

    @property
    def patches(self) -> list[Patch]:
        """Plot patches"""
        return self._patches

    @property
    def plot_funcs(self) -> list[Callable[[PolarAxes], None]]:
        """Plot functions"""
        return self._plot_funcs

    ############################################################
    # Public Method
    ############################################################

    def x_to_rad(self, x: float, ignore_range_error: bool = False) -> float:
        """Convert x coordinate to radian in track start-end range

        Parameters
        ----------
        x : float
            X coordinate
        ignore_range_error : bool
            Ignore x coordinate range error

        Returns
        -------
        rad : float
            Radian coordinate
        """
        return self.parent_sector.x_to_rad(x, ignore_range_error)

    def axis(self, **kwargs) -> None:
        """Plot axis

        By default, simple black axis params(`fc="none", ec="black", lw=0.5`) are set.

        Parameters
        ----------
        **kwargs : dict, optional
            Patch properties (e.g. `fc="tomato", ec="blue", hatch="//"`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        """
        # Set default params
        kwargs = utils.plot.set_axis_default_kwargs(**kwargs)

        # Axis facecolor placed behind other patches (zorder=0.99)
        fc_behind_kwargs = {**kwargs, **config.AXIS_FACE_PARAM}
        self.rect(self.start, self.end, ignore_pad=True, **fc_behind_kwargs)

        # Axis edgecolor placed in front of other patches (zorder=1.01)
        ec_front_kwargs = {**kwargs, **config.AXIS_EDGE_PARAM}
        self.rect(self.start, self.end, ignore_pad=True, **ec_front_kwargs)

    def text(
        self,
        text: str,
        x: float | None = None,
        r: float | None = None,
        *,
        adjust_rotation: bool = True,
        orientation: str = "horizontal",
        ignore_range_error: bool = False,
        **kwargs,
    ) -> None:
        """Plot text

        Parameters
        ----------
        text : str
            Text content
        x : float | None, optional
            X position. If None, track center x position is set.
        r : float | None, optional
            Radius position. If None, track center radius position is set.
        adjust_rotation : bool, optional
            If True, text rotation is auto set based on `x` and `orientation` params.
        orientation : str, optional
            Text orientation (`horizontal` or `vertical`)
            If adjust_rotation=True, orientation is used for rotation calculation.
        ignore_range_error : bool, optional
            If True, ignore x position range error
            (ErrorCase: `not track.start <= x <= track.end`)
        **kwargs : dict, optional
            Text properties (e.g. `size=12, color="red", va="center", ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html>
        """
        # If value is None, center position is set.
        x = self.center if x is None else x
        r = self.r_center if r is None else r

        rad = self.x_to_rad(x, ignore_range_error)
        if adjust_rotation:
            params = utils.plot.get_label_params_by_rad(
                rad, orientation, only_rotation=True
            )
            kwargs.update(params)

        if "ha" not in kwargs and "horizontalalignment" not in kwargs:
            kwargs.update(dict(ha="center"))
        if "va" not in kwargs and "verticalalignment" not in kwargs:
            kwargs.update(dict(va="center"))

        def plot_text(ax: PolarAxes) -> None:
            ax.text(rad, r, text, **kwargs)

        self._plot_funcs.append(plot_text)

    def rect(
        self,
        start: float,
        end: float,
        *,
        r_lim: tuple[float, float] | None = None,
        ignore_pad: bool = False,
        tooltip: str | None = None,
        **kwargs,
    ) -> None:
        """Plot rectangle

        Parameters
        ----------
        start : float
            Start position (x coordinate)
        end : float
            End position (x coordinate)
        r_lim : tuple[float, float] | None, optional
            Radius limit range.
            If None, `track.r_lim` (ignore_pad=False) or
            `track.r_plot_lim` (ignore_pad=True) is set.
        ignore_pad : bool, optional
            If True, ignore track padding setting.
            If `r_lim` param is set by user, this option not works.
        tooltip : str | None, optional
            Tooltip label
        **kwargs : dict, optional
            Patch properties (e.g. `fc="red", ec="blue", lw=1.0, ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        """
        rad_rect_start = self.x_to_rad(start)
        rad_rect_end = self.x_to_rad(end)
        rad = min(rad_rect_start, rad_rect_end)
        width = abs(rad_rect_end - rad_rect_start)
        if r_lim is not None:
            min_range = min(self.r_lim) - config.EPSILON
            max_range = max(self.r_lim) + config.EPSILON
            if not min_range <= min(r_lim) < max(r_lim) <= max_range:
                raise ValueError(f"{r_lim=} is invalid track range.\n{self}")
            radr, height = (rad, min(r_lim)), max(r_lim) - min(r_lim)
        elif ignore_pad:
            radr, height = (rad, min(self.r_lim)), self.r_size
        else:
            radr, height = (rad, min(self.r_plot_lim)), self.r_plot_size
        if tooltip:
            gid = gen_gid("rect")
            self._gid2tooltip[gid] = tooltip
            kwargs["gid"] = gid
        arc_rect = ArcRectangle(radr, width, height, **kwargs)
        self._patches.append(arc_rect)

    def arrow(
        self,
        start: float,
        end: float,
        *,
        r_lim: tuple[float, float] | None = None,
        head_length: float = 2,
        shaft_ratio: float = 0.5,
        tooltip: str | None = None,
        **kwargs,
    ) -> None:
        """Plot arrow

        Parameters
        ----------
        start : float
            Start position (x coordinate)
        end : float
            End position (x coordinate)
        r_lim : tuple[float, float] | None, optional
            Radius limit range. If None, `track.r_lim` is set.
        head_length : float, optional
            Arrow head length (Degree unit)
        shaft_ratio : float, optional
            Arrow shaft ratio (0 - 1.0)
        tooltip : str | None, optional
            Tooltip label
        **kwargs : dict, optional
            Patch properties (e.g. `fc="red", ec="blue", lw=1.0, ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        """
        rad_arrow_start = self.x_to_rad(start)
        rad_arrow_end = self.x_to_rad(end)
        if r_lim is None:
            r, dr = min(self.r_plot_lim), self.r_plot_size
        else:
            min_range = min(self.r_lim) - config.EPSILON
            max_range = max(self.r_lim) + config.EPSILON
            if not min_range <= min(r_lim) < max(r_lim) <= max_range:
                raise ValueError(f"{r_lim=} is invalid track range.\n{self}")
            r, dr = min(r_lim), max(r_lim) - min(r_lim)
        if tooltip:
            gid = gen_gid("arrow")
            self._gid2tooltip[gid] = tooltip
            kwargs["gid"] = gid
        arc_arrow = ArcArrow(
            rad=rad_arrow_start,
            r=r,
            drad=rad_arrow_end - rad_arrow_start,
            dr=dr,
            head_length=math.radians(head_length),
            shaft_ratio=shaft_ratio,
            **kwargs,
        )
        self._patches.append(arc_arrow)

    def annotate(
        self,
        x: float,
        label: str,
        *,
        min_r: float | None = None,
        max_r: float | None = None,
        label_size: float = 8,
        shorten: int | None = 20,
        line_kws: dict[str, Any] | None = None,
        text_kws: dict[str, Any] | None = None,
    ) -> None:
        """Plot annotation label

        The position of annotation labels is automatically adjusted so that there is
        no overlap between them. The current algorithm for automatic adjustment of
        overlap label positions is experimental and may be changed in the future.

        Parameters
        ----------
        x : float
            X coordinate
        label : str
            Label
        min_r : float | None, optional
            Min radius position of annotation line. If None, `max(self.r_lim)` is set.
        max_r : float | None, optional
            Max radius position of annotation line. If None, `min_r + 5` is set.
        label_size : float, optional
            Label size
        shorten : int | None, optional
            Shorten label if int value is set.
        line_kws : dict[str, Any] | None, optional
            Patch properties (e.g. `dict(color="red", lw=1, ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        text_kws : dict[str, Any] | None, optional
            Text properties (e.g. `dict(color="red", alpha=0.5, ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html>
        """
        line_kws = {} if line_kws is None else deepcopy(line_kws)
        text_kws = {} if text_kws is None else deepcopy(text_kws)

        if shorten:
            label = label[:shorten] + "..." if len(label) > shorten else label

        # Setup radian, radius coordinates
        min_r = max(self.r_lim) if min_r is None else min_r
        max_r = min_r + 5 if max_r is None else max_r
        if min_r > max_r:
            raise ValueError(f"{max_r=} must be larger than {min_r=}.")
        rad = self.x_to_rad(x)
        xy, xytext = (rad, min_r), (rad, max_r)

        # Setup annotation line & text property
        line_kws.setdefault("color", "grey")
        line_kws.setdefault("lw", 0.5)
        line_kws.update(dict(shrinkA=0, shrinkB=0, patchA=None, patchB=None))
        line_kws.update(dict(arrowstyle="-", relpos=utils.plot.get_ann_relpos(rad)))
        text_kws.update(utils.plot.get_label_params_by_rad(rad, "vertical"))
        text_kws.update(dict(rotation=0, size=label_size))

        def plot_annotate(ax: PolarAxes) -> None:
            ax.annotate(label, xy, xytext, arrowprops=line_kws, **text_kws)

        self._plot_funcs.append(plot_annotate)

    def xticks(
        self,
        x: NumericArrayLike,
        labels: list[str] | None = None,
        *,
        tick_length: float = 2,
        outer: bool = True,
        show_bottom_line: bool = False,
        label_size: float = 8,
        label_margin: float = 0.5,
        label_orientation: str = "horizontal",
        line_kws: dict[str, Any] | None = None,
        text_kws: dict[str, Any] | None = None,
    ) -> None:
        """Plot xticks & labels on user-specified position

        If you want to plot xticks and their position labels at regular intervals,
        it is recommended to use `track.xticks_by_interval()` instead.

        Parameters
        ----------
        x : NumericArrayLike
            X coordinates
        labels : list[str] | None, optional
            Labels on xticks. If None, only plot ticks line.
        tick_length : float, optional
            Tick length (Radius unit)
        outer : bool, optional
            If True, show ticks on outer. If False, show ticks on inner.
        show_bottom_line : bool, optional
            If True, show bottom line.
        label_size : float, optional
            Label size
        label_margin : float, optional
            Label margin size
        label_orientation : str, optional
            Label orientation (`horizontal` or `vertical`)
        line_kws : dict[str, Any] | None, optional
            Patch properties (e.g. `dict(ec="red", lw=1, ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        text_kws : dict[str, Any] | None, optional
            Text properties (e.g. `dict(color="red", alpha=0.5, ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html>
        """
        line_kws = {} if line_kws is None else deepcopy(line_kws)
        text_kws = {} if text_kws is None else deepcopy(text_kws)

        # Check list length of x & labels
        labels = [""] * len(x) if labels is None else labels
        if len(x) != len(labels):
            raise ValueError(f"List length is not match ({len(x)=}, {len(labels)=})")

        # Plot xticks & labels
        r = max(self.r_lim) if outer else min(self.r_lim)
        tick_r_lim = (r, r + tick_length) if outer else (r - tick_length, r)
        for x_pos, label in zip(x, labels, strict=True):
            # Plot xticks
            if tick_length > 0:
                self._simpleline((x_pos, x_pos), tick_r_lim, **line_kws)
            # Plot labels
            if label != "":
                rad = self.x_to_rad(x_pos)
                if outer:
                    adj_r = max(tick_r_lim) + label_margin
                else:
                    adj_r = min(tick_r_lim) - label_margin
                params = utils.plot.get_label_params_by_rad(
                    rad, label_orientation, outer
                )
                text_kws.update({**params, **dict(size=label_size)})
                self.text(label, x_pos, adj_r, adjust_rotation=False, **text_kws)

        # Plot bottom line
        if show_bottom_line:
            self._simpleline((self.start, self.end), (r, r), **line_kws)

    def xticks_by_interval(
        self,
        interval: Numeric,
        *,
        tick_length: float = 2,
        outer: bool = True,
        show_bottom_line: bool = False,
        show_label: bool = True,
        show_endlabel: bool = True,
        label_size: float = 8,
        label_margin: float = 0.5,
        label_orientation: str = "horizontal",
        label_formatter: Callable[[float], str] | None = None,
        line_kws: dict[str, Any] | None = None,
        text_kws: dict[str, Any] | None = None,
    ) -> None:
        """Plot xticks & position labels by user-specified interval

        `track.xticks_by_interval()` is high-level API function of `track.xticks()`.
        If you want to plot xticks and their labels in any position you like,
        use `track.xticks()` instead.

        Parameters
        ----------
        interval : Numeric
            Xticks interval
        tick_length : float, optional
            Tick length (Radius unit)
        outer : bool, optional
            If True, show ticks on outer. If False, show ticks on inner.
        show_bottom_line : bool, optional
            If True, show bottom line.
        show_label : bool, optional
            If True, show label of xticks interval position.
        show_endlabel : bool, optional
            If False, no display end xtick label.
            Used to prevent overlap of start-end xtick labels.
        label_size : float, optional
            Label size
        label_margin : float, optional
            Label margin size
        label_orientation : str, optional
            Label orientation (`horizontal` or `vertical`)
        label_formatter : Callable[[float], str] | None, optional
            User-defined function for label format. (e.g. `1000 -> '1.0 Kb'`)
        line_kws : dict[str, Any] | None, optional
            Patch properties (e.g. `dict(ec="red", lw=1, ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        text_kws : dict[str, Any] | None, optional
            Text properties (e.g. `dict(color="red", alpha=0.5, ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html>
        """
        line_kws = {} if line_kws is None else deepcopy(line_kws)
        text_kws = {} if text_kws is None else deepcopy(text_kws)

        # Setup xtick positions
        x_list = []
        start_pos, end_pos = self.start - (self.start % interval), self.end + interval
        for x in np.arange(start_pos, end_pos, interval):
            if self.start <= x <= self.end:
                cast_type = int if isinstance(interval, int) else float
                x_list.append(cast_type(x))

        # Setup xticks labels
        labels = None
        if show_label:
            map_func = str if label_formatter is None else label_formatter
            labels = list(map(map_func, x_list))
            # No display end xtick label if 'show_endlabel' is False
            if not show_endlabel:
                labels[-1] = ""

        # Plot xticks by user-specified interval
        self.xticks(
            x=x_list,
            labels=labels,
            tick_length=tick_length,
            outer=outer,
            show_bottom_line=show_bottom_line,
            label_size=label_size,
            label_margin=label_margin,
            label_orientation=label_orientation,
            line_kws=line_kws,
            text_kws=text_kws,
        )

    def yticks(
        self,
        y: NumericArrayLike,
        labels: list[str] | None = None,
        *,
        vmin: float = 0,
        vmax: float | None = None,
        side: str = "right",
        tick_length: float = 1,
        label_size: float = 8,
        label_margin: float = 0.5,
        line_kws: dict[str, Any] | None = None,
        text_kws: dict[str, Any] | None = None,
    ) -> None:
        """Plot yticks & labels on user-specified position

        Parameters
        ----------
        y : NumericArrayLike
            Y coordinates
        labels : list[str] | None, optional
            Labels on yticks. If None, only plot ticks line.
        vmin : float, optional
            Y min value
        vmax : float | None, optional
            Y max value. If None, `max(y)` is set.
        side : str, optional
            Ticks side position (`right` or `left`)
        tick_length : float, optional
            Tick length (Degree unit)
        label_size : float, optional
            Label size
        label_margin : float, optional
            Label margin size
        line_kws : dict[str, Any] | None, optional
            Patch properties (e.g. `dict(ec="red", lw=1, ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        text_kws : dict[str, Any] | None, optional
            Text properties (e.g. `dict(color="red", alpha=0.5, ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html>
        """
        line_kws = {} if line_kws is None else deepcopy(line_kws)
        text_kws = {} if text_kws is None else deepcopy(text_kws)

        # Check y, labels list length
        labels = [""] * len(y) if labels is None else labels
        if len(y) != len(labels):
            raise ValueError(f"List length is not match ({len(y)=}, {len(labels)=})")
        # Set vmax & check if y is in min-max range
        vmax = max(y) if vmax is None else vmax
        self._check_value_min_max(y, vmin, vmax)
        # Temporarily set clockwise=True in this method
        original_clockwise = self.clockwise
        self.parent_sector._clockwise = True

        # Plot yticks & labels
        r = [self._y_to_r(v, vmin, vmax) for v in y]
        for r_pos, label in zip(r, labels, strict=True):
            # Set plot properties
            x_tick_length = (self.size / self.deg_size) * tick_length
            x_label_margin = (self.size / self.deg_size) * label_margin
            if side == "right":
                x_lim = (self.end, self.end + x_tick_length)
                x_text = self.end + (x_tick_length + x_label_margin)
                rad_text = self.x_to_rad(x_text, True)
                ha = "right" if utils.plot.is_lower_loc(rad_text) else "left"
            elif side == "left":
                x_lim = (self.start, self.start - x_tick_length)
                x_text = self.start - (x_tick_length + x_label_margin)
                rad_text = self.x_to_rad(x_text, True)
                ha = "left" if utils.plot.is_lower_loc(rad_text) else "right"
            else:
                raise ValueError(f"{side=} is invalid ('right' or 'left').")
            # Plot yticks
            if tick_length > 0:
                self._simpleline(x_lim, (r_pos, r_pos), **line_kws)
            # Plot ylabels
            if label != "":
                va = "center_baseline"
                _text_kws = deepcopy(text_kws)
                _text_kws.update(
                    dict(ha=ha, va=va, rotation_mode="anchor", size=label_size)
                )
                self.text(label, x_text, r_pos, ignore_range_error=True, **_text_kws)

        # Restore clockwise to original value
        self.parent_sector._clockwise = original_clockwise

    def grid(
        self,
        y_grid_num: int | None = 6,
        x_grid_interval: float | None = None,
        **kwargs,
    ) -> None:
        """Plot grid

        By default, `color="grey", alpha=0.5, zorder=0` line params are set.

        Parameters
        ----------
        y_grid_num : int | None, optional
            Y-axis grid line number. If None, y-axis grid line is not shown.
        x_grid_interval : float | None, optional
            X-axis grid line interval. If None, x-axis grid line is not shown.
        **kwargs : dict, optional
            Axes.plot properties (e.g. `color="red", lw=0.5, ls="--", ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html>
        """
        # Check argument values
        min_grid_num = 2
        if y_grid_num is not None and not y_grid_num >= min_grid_num:
            raise ValueError(f"{y_grid_num=} is invalid (y_grid_num >= 2).")
        if x_grid_interval is not None and not x_grid_interval > 0:
            raise ValueError(f"{x_grid_interval=} is invalid (x_grid_interval > 0).")

        # Set default grid line properties
        default_props = dict(color="grey", alpha=0.5, zorder=0)
        for name, value in default_props.items():
            if name not in kwargs:
                kwargs.update({name: value})

        # Plot y-axis grid line
        if y_grid_num is not None:
            vmin, vmax = 0, y_grid_num - 1
            for y_grid_idx in range(y_grid_num):
                x = [self.start, self.end]
                y = [y_grid_idx, y_grid_idx]
                self.line(x, y, vmin=vmin, vmax=vmax, **kwargs)

        # Plot x-axis grid line
        if x_grid_interval is not None:
            vmin, vmax = 0, 1.0
            x_grid_idx = 0
            while True:
                x_pos = self.start + (x_grid_interval * x_grid_idx)
                if x_pos > self.end:
                    break
                x, y = [x_pos, x_pos], [vmin, vmax]
                self.line(x, y, vmin=vmin, vmax=vmax, **kwargs)
                x_grid_idx += 1

    def line(
        self,
        x: NumericArrayLike,
        y: NumericArrayLike,
        *,
        vmin: float = 0,
        vmax: float | None = None,
        arc: bool = True,
        **kwargs,
    ) -> None:
        """Plot line

        Parameters
        ----------
        x : NumericArrayLike
            X coordinates
        y : NumericArrayLike
            Y coordinates
        vmin : float, optional
            Y min value
        vmax : float | None, optional
            Y max value. If None, `max(y)` is set.
        arc : bool, optional
            If True, plot arc style line for polar projection.
            If False, simply plot linear style line.
        **kwargs : dict, optional
            Axes.plot properties (e.g. `color="red", lw=0.5, ls="--", ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html>
        """
        # Check x, y list length
        if len(x) != len(y):
            raise ValueError(f"List length is not match ({len(x)=}, {len(y)=})")

        # Convert (x, y) to (rad, r)
        rad = list(map(self.x_to_rad, x))
        vmax = max(y) if vmax is None else vmax
        self._check_value_min_max(y, vmin, vmax)
        r = [self._y_to_r(v, vmin, vmax) for v in y]

        if arc:
            # Convert linear line to arc line (rad, r) points
            plot_rad, plot_r = self._to_arc_radr(rad, r)
        else:
            plot_rad, plot_r = rad, r

        # Set default line width
        if "lw" not in kwargs and "linewidth" not in kwargs:
            kwargs.setdefault("lw", 0.5)

        def plot_line(ax: PolarAxes) -> None:
            ax.plot(plot_rad, plot_r, **kwargs)

        self._plot_funcs.append(plot_line)

    def scatter(
        self,
        x: NumericArrayLike,
        y: NumericArrayLike,
        *,
        vmin: float = 0,
        vmax: float | None = None,
        tooltip: list[str] | None = None,
        **kwargs,
    ) -> None:
        """Plot scatter

        Parameters
        ----------
        x : NumericArrayLike
            X position list
        y : NumericArrayLike
            Y position list
        vmin : float, optional
            Y min value
        vmax : float | None, optional
            Y max value. If None, `max(y)` is set.
        tooltip : list[str] | None, optional
            Tooltip labels. If None, y value labels are set.
        **kwargs : dict, optional
            Axes.scatter properties (e.g. `s=9, ec="black", lw=1.0, ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html>
        """
        # Check x, y list length
        if len(x) != len(y):
            raise ValueError(f"List length is not match ({len(x)=}, {len(y)=})")

        # Convert (x, y) to (rad, r)
        rad = list(map(self.x_to_rad, x))
        vmax = max(y) if vmax is None else vmax
        self._check_value_min_max(y, vmin, vmax)
        r = [self._y_to_r(v, vmin, vmax) for v in y]
        labels = [str(v) for v in y] if tooltip is None else tooltip

        # Set default marker size and line width
        if "s" not in kwargs and "sizes" not in kwargs:
            kwargs.setdefault("s", 3**2)
        if "lw" not in kwargs and "linewidth" not in kwargs:
            kwargs.setdefault("lw", 0.0)

        def plot_scatter(ax: PolarAxes) -> None:
            scatter = ax.scatter(rad, r, **kwargs)  # type:ignore
            if config.tooltip.enabled:
                set_collection_tooltip(ax, scatter, labels)

        self._plot_funcs.append(plot_scatter)

    def bar(
        self,
        x: NumericArrayLike,
        height: NumericArrayLike,
        width: float = 0.8,
        bottom: Numeric | NumericArrayLike = 0,
        align: str = "center",
        *,
        vmin: float = 0,
        vmax: float | None = None,
        **kwargs,
    ) -> None:
        """Plot bar

        Parameters
        ----------
        x : NumericArrayLike
            Bar x coordinates
        height : NumericArrayLike
            Bar heights
        width : float, optional
            Bar width
        bottom : Numeric | NumericArrayLike
            Bar bottom(s)
        align : str, optional
            Bar alignment type (`center` or `edge`)
        vmin : float, optional
            Y min value
        vmax : float | None, optional
            Y max value. If None, `np.max(height + bottom)` is set.
        **kwargs : dict, optional
            Axes.bar properties (e.g. `color="tomato", ec="black", lw=0.5, hatch="//"`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html>
        """
        # Check x, height list length
        if len(x) != len(height):
            raise ValueError(f"List length is not match ({len(x)=}, {len(height)=})")

        # Calculate top & vmax
        if isinstance(bottom, (Sequence, np.ndarray)):
            bottom = np.array(bottom)
        else:
            bottom = np.array([bottom])
        top = np.array(height) + bottom
        vmax = float(max(top)) if vmax is None else vmax

        # Check if bottom & top(height + bottom) is in valid min-max range
        self._check_value_min_max(bottom, vmin, vmax)
        self._check_value_min_max(top, vmin, vmax)

        # Calculate bar params
        rad = list(map(self.x_to_rad, x))
        r_bottom = np.array([self._y_to_r(v, vmin, vmax) for v in bottom])
        r_height = [self._y_to_r(v, vmin, vmax) for v in top] - r_bottom
        rad_width = self.rad_size * (width / self.size)

        def plot_bar(ax: PolarAxes) -> None:
            bar = ax.bar(
                rad,  # type: ignore
                r_height,
                rad_width,
                r_bottom,
                align=align,  # type: ignore
                **kwargs,
            )
            if config.tooltip.enabled:
                for p, h in zip(bar.patches, height, strict=True):
                    gid = gen_gid("bar")
                    p.set_gid(gid)
                    self._gid2tooltip[gid] = str(h)

        self._plot_funcs.append(plot_bar)

    def stacked_bar(
        self,
        table_data: str | Path | pd.DataFrame | StackedBarTable,
        *,
        delimiter: str = "\t",
        width: float = 0.6,
        cmap: str | dict[str, str] = "tab10",
        vmax: float | None = None,
        show_label: bool = True,
        label_pos: str = "bottom",
        label_margin: float = 2,
        bar_kws: dict[str, Any] | None = None,
        label_kws: dict[str, Any] | None = None,
    ) -> StackedBarTable:
        """Plot stacked bar from table data

        Parameters
        ----------
        table_data : str | Path | pd.DataFrame | StackedBarTable
            Table file or Table DataFrame or StackedBarTable
        delimiter : str, optional
            Table file delimiter
        width : float, optional
            Bar width ratio (0.0 - 1.0)
        cmap : str | dict[str, str], optional
            Colormap assigned to each stacked bar.
            User can set matplotlib's colormap (e.g. `tab10`, `Set3`) or
            col_name -> color dict (e.g. `dict(A="red", B="blue", C="green", ...)`)
        vmax : float | None, optional
            Stacked bar max value.
            If None, max value in each row values sum is set.
        show_label : bool, optional
            Show table row names as labels
        label_pos : str, optional
            Label position (`bottom`|`top`)
        label_margin : float, optional
            Label margin size
        bar_kws : dict[str, Any] | None, optional
            Axes.bar properties (e.g. `dict(ec="black", lw=0.5, hatch="//", ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html>
        label_kws : dict[str, Any] | None, optional
            Text properties (e.g. `dict(size=12, orientation="vertical", ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html>

        Returns
        -------
        sb_table : StackedBarTable
            Stacked bar table
        """
        bar_kws = {} if bar_kws is None else deepcopy(bar_kws)
        label_kws = {} if label_kws is None else deepcopy(label_kws)

        if not 0.0 <= width <= 1.0:
            raise ValueError(f"{width=} is invalid (0.0 <= width <= 1.0).")

        # Load table data
        if isinstance(table_data, StackedBarTable):
            sb_table = table_data
        else:
            sb_table = StackedBarTable(table_data, delimiter=delimiter)

        # Make column name & color dict
        if isinstance(cmap, str):
            col_name2color = sb_table.get_col_name2color(cmap)
        else:
            col_name2color = cmap

        # Calculate bar plot parameters
        x = sb_table.calc_bar_label_x_list(self.size)
        width = (self.size / len(sb_table.row_names)) * width
        vmax = sb_table.row_sum_vmax if vmax is None else vmax
        heights, bottoms = sb_table.stacked_bar_heights, sb_table.stacked_bar_bottoms

        # Plot bars
        col_names = sb_table.col_names
        for col_name, height, bottom in zip(col_names, heights, bottoms, strict=True):
            color = col_name2color[col_name]
            self.bar(x, height, width, bottom, vmax=vmax, fc=color, **bar_kws)

        # Plot bar labels
        if show_label:
            x_list = sb_table.calc_bar_label_x_list(self.size)
            row_name2sum = sb_table.row_name2sum
            for label, x in zip(sb_table.row_names, x_list, strict=True):
                # Calculate label r position
                if label_pos == "top":
                    bar_r_height = self.r_size * (row_name2sum[label] / vmax)
                    r = min(self.r_lim) + bar_r_height + label_margin
                    outer = True
                elif label_pos == "bottom":
                    r = min(self.r_lim) - label_margin
                    outer = False
                else:
                    raise ValueError(f"{label_pos=} is invalid ('top' or 'bottom').")

                # Set label text properties
                if label_kws.get("orientation") is None:
                    label_kws["orientation"] = "horizontal"
                params = utils.plot.get_label_params_by_rad(
                    self.x_to_rad(x), label_kws["orientation"], outer
                )
                label_kws.update(params)

                self.text(label, x, r, adjust_rotation=False, **label_kws)

        return sb_table

    def stacked_barh(
        self,
        table_data: str | Path | pd.DataFrame | StackedBarTable,
        *,
        delimiter: str = "\t",
        width: float = 0.6,
        cmap: str | dict[str, str] = "tab10",
        bar_kws: dict[str, Any] | None = None,
    ) -> StackedBarTable:
        """Plot horizontal stacked bar from table data

        Parameters
        ----------
        table_data : str | Path | pd.DataFrame | StackedBarTable
            Table file or Table DataFrame or StackedBarTable
        delimiter : str, optional
            Table file delimiter
        width : float, optional
            Bar width ratio (0.0 - 1.0)
        cmap : str | dict[str, str], optional
            Colormap assigned to each stacked bar.
            User can set matplotlib's colormap (e.g. `tab10`, `Set3`) or
            col_name -> color dict (e.g. `dict(A="red", B="blue", C="green", ...)`)
        bar_kws : dict[str, Any] | None, optional
            Patch properties for bar plot (e.g. `dict(ec="black, lw=0.2, ...)`)

        Returns
        -------
        sb_table : StackedBarTable
            Stacked bar table
        """
        bar_kws = {} if bar_kws is None else deepcopy(bar_kws)

        if not 0.0 <= width <= 1.0:
            raise ValueError(f"{width=} is invalid (0.0 <= width <= 1.0).")

        # Load table data
        if isinstance(table_data, StackedBarTable):
            sb_table = table_data
        else:
            sb_table = StackedBarTable(table_data, delimiter=delimiter)

        # Make column name & color dict
        if isinstance(cmap, str):
            col_name2color = sb_table.get_col_name2color(cmap)
        else:
            col_name2color = cmap

        # Calculate bar plot parameters
        r_lim_list = sb_table.calc_barh_r_lim_list(self.r_plot_lim, width)
        heights, bottoms = sb_table.stacked_bar_heights, sb_table.stacked_bar_bottoms

        # Plot bars
        col_names = sb_table.col_names
        for col_name, height, bottom in zip(col_names, heights, bottoms, strict=True):
            color = col_name2color[col_name]
            for r_lim, h, b in zip(r_lim_list, height, bottom, strict=True):
                self.rect(b, b + h, r_lim=r_lim, fc=color, **bar_kws)

        return sb_table

    def fill_between(
        self,
        x: NumericArrayLike,
        y1: NumericArrayLike,
        y2: Numeric | NumericArrayLike = 0,
        *,
        vmin: float = 0,
        vmax: float | None = None,
        arc: bool = True,
        **kwargs,
    ) -> None:
        """Fill the area between two horizontal(y1, y2) curves

        Parameters
        ----------
        x : NumericArrayLike
            X coordinates
        y1 : NumericArrayLike
            Y coordinates (first curve definition)
        y2 : Numeric | NumericArrayLike
            Y coordinate[s] (second curve definition)
        vmin : float, optional
            Y min value
        vmax : float | None, optional
            Y max value. If None, `max(y1 + y2)` is set.
        arc : bool, optional
            If True, plot arc style line for polar projection.
            If False, simply plot linear style line.
        **kwargs : dict, optional
            Axes.fill_between properties (e.g. `fc="red", ec="black", lw=0.1, ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html>
        """
        rad = list(map(self.x_to_rad, x))
        if isinstance(y2, (Sequence, np.ndarray)):
            y_all = list(y1) + list(y2)
        else:
            y_all = [*list(y1), y2]
            y2 = [float(y2)] * len(x)
        vmin = min(y_all) if vmin is None else vmin
        vmax = max(y_all) if vmax is None else vmax
        self._check_value_min_max(y_all, vmin, vmax)

        r2 = [self._y_to_r(v, vmin, vmax) for v in y2]
        r = [self._y_to_r(v, vmin, vmax) for v in y1]
        if arc:
            plot_rad, plot_r2 = self._to_arc_radr(rad, r2)
            _, plot_r = self._to_arc_radr(rad, r)
        else:
            plot_rad, plot_r, plot_r2 = rad, r, r2

        # Set default line width
        if "lw" not in kwargs and "linewidth" not in kwargs:
            kwargs.setdefault("lw", 0.0)

        def plot_fill_between(ax: PolarAxes) -> None:
            ax.fill_between(plot_rad, plot_r, plot_r2, **kwargs)  # type: ignore

        self._plot_funcs.append(plot_fill_between)

    def heatmap(
        self,
        data: NumericArrayLike,
        *,
        vmin: float | None = None,
        vmax: float | None = None,
        start: float | None = None,
        end: float | None = None,
        width: float | None = None,
        cmap: str | Colormap = "bwr",
        show_value: bool = False,
        rect_kws: dict[str, Any] | None = None,
        text_kws: dict[str, Any] | None = None,
    ) -> None:
        """Plot heatmap

        Parameters
        ----------
        data : NumericArrayLike
            Numerical list, numpy 1d or 2d array
        vmin : float | None, optional
            Min value for heatmap plot. If None, `np.min(data)` is set.
        vmax : float | None, optional
            Max value for heatmap plot. If None, `np.max(data)` is set.
        start : float | None, optional
            Start position for heatmap plot (x coordinate).
            If None, `track.start` is set.
        end : float | None, optional
            End position for heatmap plot (x coordinate).
            If None, `track.end` is set.
        width : float | None, optional
            Heatmap rectangle x width size.
            Normally heatmap plots squares of equal width. In some cases,
            it is necessary to reduce the width of only the last column data square.
            At that time, width can be set under the following conditions.
            `(col_num - 1) * width < end - start < col_num * width`
        cmap : str | Colormap, optional
            Colormap (e.g. `viridis`, `Spectral`, `Reds`, `Greys`)
            <https://matplotlib.org/stable/tutorials/colors/colormaps.html>
        show_value : bool, optional
            If True, show data value on heatmap rectangle
        rect_kws : dict[str, Any] | None, optional
            Patch properties (e.g. `dict(ec="black", lw=0.5, ...)`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        text_kws : dict[str, Any] | None, optional
            Text properties (e.g. `dict(size=6, color="red", ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html>
        """
        rect_kws = {} if rect_kws is None else deepcopy(rect_kws)
        text_kws = {} if text_kws is None else deepcopy(text_kws)

        # Check whether array is 1d or 2d (If 1d, reshape 2d)
        data = np.array(data)
        if data.ndim == 1:
            data = data.reshape((1, -1))
        elif data.ndim != 2:
            raise ValueError(f"{data=} is not 1d or 2d array!!")

        # Set default value for None properties
        vmin = np.min(data) if vmin is None else vmin
        vmax = np.max(data) if vmax is None else vmax
        start = self.start if start is None else start
        end = self.end if end is None else end
        self._check_value_min_max(data, vmin, vmax)

        # Calculate radius & x position range list of heatmap rectangle
        row_num, col_num = data.shape
        unit_r_size = self.r_plot_size / row_num
        unit_x_size = (end - start) / col_num
        if width is not None:
            if (col_num - 1) * width < end - start < col_num * width:
                unit_x_size = width
            else:
                raise ValueError(f"{width=} is invalid ({start=}, {end=})")

        r_range_list: list[tuple[float, float]] = []
        for i in range(row_num):
            max_range = max(self.r_plot_lim) - (unit_r_size * i)
            min_range = max_range - unit_r_size
            r_range_list.append((min_range, max_range))
        x_range_list: list[tuple[float, float]] = []
        for i in range(col_num):
            min_range = start + (unit_x_size * i)
            max_range = min_range + unit_x_size
            # Avoid max_range exceeds `track.end` value
            max_range = min(max_range, self.end)
            x_range_list.append((min_range, max_range))

        # Plot heatmap
        colormap = cmap if isinstance(cmap, Colormap) else mpl.colormaps[cmap]  # type: ignore
        norm = Normalize(vmin=vmin, vmax=vmax)
        textcolor = text_kws.get("color")
        for row_idx, row in enumerate(data):
            for col_idx, v in enumerate(row):
                # Plot heatmap rectangle
                rect_start, rect_end = x_range_list[col_idx]
                rect_r_lim = r_range_list[row_idx]
                color = colormap(norm(v))
                rect_kws.update(dict(fc=color, facecolor=color, tooltip=str(v)))
                self.rect(rect_start, rect_end, r_lim=rect_r_lim, **rect_kws)

                if show_value:
                    # Plot value text on heatmap rectangle
                    if textcolor is None:
                        text_kws["color"] = select_textcolor(color)
                    text_value = f"{v:.2f}" if isinstance(v, float) else str(v)
                    text_x = (rect_end + rect_start) / 2
                    text_r = sum(rect_r_lim) / 2
                    self.text(text_value, text_x, text_r, **text_kws)

    def raster(
        self,
        img: str | Path | Image.Image,
        *,
        w: float = 1.0,
        h: float = 1.0,
        rotate: bool = True,
        **kwargs,
    ) -> None:
        """Plot raster image

        Parameters
        ----------
        img : str | Path | Image.Image
            Image data (`File Path`|`URL`|`PIL Image`)
        w : float, optional
            Width ratio (`0.0 - 1.0`)
        h : float, optional
            Height ratio (`0.0 - 1.0`)
        rotate : bool, optional
            If True, rotate image 180 degrees if track is in lower location
            (`-270 <= degree < -90`|`90 <= degree < 270`)
        **kwargs : dict, optional
            Axes.pcolormesh properties
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html>
        """
        # Check range of value
        if not 0.0 < w <= 1.0:
            raise ValueError(f"{w=} is invalid (0.0 < w <= 1.0).")
        if not 0.0 < h <= 1.0:
            raise ValueError(f"{h=} is invalid (0.0 < h <= 1.0).")

        # Calculate radian (size, start, end)
        rad_size = self.rad_size * w
        rad_pad = self.rad_size * ((1.0 - w) / 2)
        rad_start, rad_end = min(self.rad_lim) + rad_pad, max(self.rad_lim) - rad_pad
        # Calculate radius (size, start, end)
        r_size = self.r_size * h
        r_pad = self.r_size * ((1.0 - h) / 2)
        r_start, r_end = min(self.r_lim) + r_pad, max(self.r_lim) - r_pad

        # Load image
        img = utils.load_image(img)

        # Rotate image 180 degrees if track is in lower location
        track_center_deg = sum(self.deg_lim) / 2
        if rotate and utils.plot.is_lower_loc(track_center_deg):
            img = img.rotate(180)

        # Resize image
        pixel_w = int(rad_size / (np.pi / 1000))
        pixel_h = int(r_size * 10)
        resize_img = img.resize((pixel_w, pixel_h))

        # Setup radian & radius positions for plotting image by pcolormesh
        rad_list = np.linspace(rad_start, rad_end, resize_img.width)
        r_list = np.linspace(r_end, r_start, resize_img.height)

        def plot_raster(ax: PolarAxes) -> None:
            ax.pcolormesh(rad_list, r_list, np.array(resize_img), **kwargs)

        self._plot_funcs.append(plot_raster)

    def tree(
        self,
        tree_data: str | Path | Tree,
        *,
        format: str = "newick",
        outer: bool = True,
        align_leaf_label: bool = True,
        ignore_branch_length: bool = False,
        leaf_label_size: float = 12,
        leaf_label_rmargin: float = 2.0,
        reverse: bool = False,
        ladderize: bool = False,
        line_kws: dict[str, Any] | None = None,
        align_line_kws: dict[str, Any] | None = None,
        label_formatter: Callable[[str], str] | None = None,
    ) -> TreeViz:
        """Plot tree

        It is recommended that the track(sector) size be the same as the number of
        leaf nodes in the tree, to make it easier to combine with `bar` and `heatmap`.

        Parameters
        ----------
        tree_data : str | Path | Tree
            Tree data (`File`|`File URL`|`Tree Object`|`Tree String`)
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
        tv : TreeViz
            TreeViz instance
        """
        tv = TreeViz(
            tree_data,
            format=format,
            outer=outer,
            align_leaf_label=align_leaf_label,
            ignore_branch_length=ignore_branch_length,
            leaf_label_size=leaf_label_size,
            leaf_label_rmargin=leaf_label_rmargin,
            reverse=reverse,
            ladderize=ladderize,
            line_kws=line_kws,
            align_line_kws=align_line_kws,
            label_formatter=label_formatter,
            track=self,
        )
        self._trees.append(tv)

        return tv

    def genomic_features(
        self,
        features: SeqFeature | Sequence[SeqFeature],
        *,
        plotstyle: str = "box",
        r_lim: tuple[float, float] | None = None,
        facecolor_handler: Callable[[SeqFeature], str] | None = None,
        **kwargs,
    ) -> None:
        """Plot genomic features

        Parameters
        ----------
        features : SeqFeature | Sequence[SeqFeature]
            Biopython's SeqFeature or SeqFeature list
        plotstyle : str, optional
            Plot style (`box` or `arrow`)
        r_lim : tuple[float, float] | None, optional
            Radius limit range. If None, `track.r_plot_lim` is set.
        facecolor_handler : Callable[[SeqFeature], str] | None, optional
            User-defined function to handle facecolor
        **kwargs : dict, optional
            Patch properties (e.g. `fc="red", ec="blue", lw=1.0, ...`)
            <https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html>
        """
        if isinstance(features, SeqFeature):
            features = [features]

        if r_lim is None:
            r_lim = self.r_plot_lim
        elif not min(self.r_lim) <= min(r_lim) < max(r_lim) <= max(self.r_lim):
            raise ValueError(f"{r_lim=} is invalid track range.\n{self}")

        for feature in features:
            # Set qualifier tag facecolor if exists
            tag_color = feature.qualifiers.get("facecolor", [None])[0]
            if tag_color is not None:
                kwargs.update(dict(fc=tag_color, facecolor=tag_color))
            # Set facecolor by user-defined function
            if facecolor_handler is not None:
                color = facecolor_handler(feature)
                kwargs.update(dict(fc=color, facecolor=color))
            # Plot feature
            try:
                start = int(str(feature.location.parts[0].start))
                end = int(str(feature.location.parts[-1].end))
            except ValueError:
                print(f"Failed to parse feature's start-end position.\n{feature}")
                continue
            if feature.location.strand == -1:
                start, end = end, start
            tooltip = to_feature_tooltip(feature)
            if plotstyle == "box":
                self.rect(start, end, r_lim=r_lim, tooltip=tooltip, **kwargs)
            elif plotstyle == "arrow":
                self.arrow(start, end, r_lim=r_lim, tooltip=tooltip, **kwargs)
            else:
                raise ValueError(f"{plotstyle=} is invalid ('box' or 'arrow').")

    ############################################################
    # Private Method
    ############################################################

    def _y_to_r(self, y: float, vmin: float, vmax: float) -> float:
        """Convert y coordinate to radius in track

        Parameters
        ----------
        y : float
            Y coordinate
        vmin : float
            Min y coordinate
        vmax : float
            Max y coordinate

        Returns
        -------
        r : float
            Converted radius position
        """
        norm = Normalize(vmin, vmax)
        r = min(self.r_plot_lim) + (self.r_plot_size * norm(y))
        return r

    def _to_arc_radr(
        self,
        rad: NumericArrayLike,
        r: NumericArrayLike,
    ) -> tuple[list[float], list[float]]:
        """Convert radian & radius to arc radian & arc radius

        Parameters
        ----------
        rad : NumericArrayLike
            Radian list
        r : NumericArrayLike
            Radius list

        Returns
        -------
        arc_rad : list[float]
            Arc radian list
        arc_r : list[float]
            Arc radius list
        """
        all_arc_rad, all_arc_r = [], []
        for i in range(len(rad) - 1):
            rad1, rad2, r1, r2 = rad[i], rad[i + 1], r[i], r[i + 1]
            if rad1 == rad2:
                all_arc_rad.extend([rad1, rad2])
                all_arc_r.extend([r1, r2])
            else:
                # To obtain finely chopped coordinates, step is reduced by a tenth
                step = config.ARC_RADIAN_STEP / 10
                if rad1 > rad2:
                    step *= -1
                arc_rad = [*list(np.arange(rad1, rad2, step)), rad2]
                all_arc_rad.extend(arc_rad)
                arc_r = np.linspace(r1, r2, len(arc_rad), endpoint=True)
                all_arc_r.extend(arc_r)
        return all_arc_rad, all_arc_r

    def _simpleline(
        self,
        x_lim: tuple[float, float],
        r_lim: tuple[float, float],
        **kwargs,
    ) -> None:
        """Plot simple patch line between two points (x1, r1), (x2, r2)

        Used to plot simple lines such as ticks internally

        Parameters
        ----------
        x_lim : tuple[float, float]
            X start-end limit region
        r_lim : tuple[float, float]
            Radius start-end limit region
        **kwargs : dict, optional
            Patch properties (e.g. `ec="red", lw=1.0, ...`)
            https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html
        """
        rad_lim = tuple(map(self.x_to_rad, x_lim, (True, True)))
        self._patches.append(ArcLine(rad_lim, r_lim, **kwargs))  # type: ignore

    def _check_value_min_max(
        self,
        value: Numeric | NumericArrayLike,
        vmin: float,
        vmax: float,
    ) -> None:
        """Check if value(s) is in valid min-max range

        Parameters
        ----------
        value : Numeric | NumericArrayLike
            Check value(s)
        vmin : float
            Min value
        vmax : float
            Max value
        """
        vmin, vmax = vmin - config.EPSILON, vmax + config.EPSILON
        if isinstance(value, (Sequence, np.ndarray)):
            if isinstance(value, np.ndarray):
                value = list(value.flatten())
            for v in value:
                if not vmin <= v <= vmax:
                    raise ValueError(f"value={v} is not in valid range ({vmin=}, {vmax=})")  # fmt: skip  # noqa: E501
        elif not vmin <= value <= vmax:
            raise ValueError(f"{value=} is not in valid range ({vmin=}, {vmax=})")  # fmt: skip  # noqa: E501

    def __str__(self) -> str:
        min_deg_lim, max_deg_lim = min(self.deg_lim), max(self.deg_lim)
        min_r_lim, max_r_lim = min(self.r_lim), max(self.r_lim)
        return textwrap.dedent(
            f"""
            # Track = '{self.name}' (Parent Sector = '{self.parent_sector.name}')
            # Size = {self.size} ({self.start} - {self.end})
            # Degree Size = {self.deg_size:.2f} ({min_deg_lim:.2f} - {max_deg_lim:.2f})
            # Radius Size = {self.r_size:.2f} ({min_r_lim:.2f} - {max_r_lim:.2f})
            """
        )[1:]
