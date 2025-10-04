import math

import pytest

from pycirclize import config
from pycirclize.sector import Sector


@pytest.fixture
def sector() -> Sector:
    """Sector test fixture"""
    return Sector("test", 1000, (0, math.pi))


def test_property() -> None:
    """Test sector property"""
    # Case1: Set int size
    name, size, rad_lim = "test", 1000, (0, math.pi)
    sector_case1 = Sector(name, size, rad_lim)
    assert sector_case1.name == name
    assert sector_case1.size == size
    assert sector_case1.start == 0
    assert sector_case1.end == size
    assert sector_case1.center == 500
    assert sector_case1.rad_size == math.pi
    assert sector_case1.rad_lim == rad_lim
    assert sector_case1.deg_size == 180
    assert sector_case1.deg_lim == (0, 180)
    assert sector_case1.tracks == []
    assert sector_case1.patches == []
    assert sector_case1.plot_funcs == []

    # Case2: Set tuple[float, float] range
    name, range, rad_lim = "test", (100, 1100), (0, math.pi)
    sector_case2 = Sector(name, range, rad_lim)
    assert sector_case2.size == range[1] - range[0]
    assert sector_case2.start == range[0]
    assert sector_case2.end == range[1]
    assert sector_case2.center == 600


def test_add_track(sector: Sector) -> None:
    """Test add_track()"""
    sector.add_track((90, 100), name="Test01")
    sector.add_track((80, 90))
    assert len(sector.tracks) == 2
    assert [t.name for t in sector.tracks] == ["Test01", "Track02"]


def test_get_track(sector: Sector) -> None:
    """Test `get_track()`"""
    # Case1: No tracks (Error)
    with pytest.raises(ValueError):
        sector.get_track("error")
    # Case2: No exists target name track (Error)
    sector.add_track((90, 100))
    sector.add_track((80, 90))
    with pytest.raises(ValueError):
        sector.get_track("error")
    # Case3: Found track (No error)
    sector.get_track("Track02")


def test_get_lowest_r(sector: Sector) -> None:
    """Test `get_lowest_r()`"""
    # Case1: No tracks
    assert sector.get_lowest_r() == config.MAX_R
    # Case2: Add tracks
    sector.add_track((90, 100))
    sector.add_track((50, 70))
    assert sector.get_lowest_r() == 50


def test_x_to_pad() -> None:
    """Test `x_to_pad()`"""
    # Case1: Set int size
    sector = Sector("test", 1000, (0, math.pi))
    assert sector.x_to_rad(0) == 0
    assert sector.x_to_rad(250) == math.pi / 4
    assert sector.x_to_rad(500) == math.pi / 2
    assert sector.x_to_rad(1000) == math.pi
    with pytest.raises(ValueError):
        sector.x_to_rad(sector.end + 1)

    # Case2: Set tuple[float, float] range
    sector = Sector("test", (100, 1100), (0, math.pi))
    assert sector.x_to_rad(350) == math.pi / 4
    assert sector.x_to_rad(600) == math.pi / 2
    assert sector.x_to_rad(1100) == math.pi
    with pytest.raises(ValueError):
        assert sector.x_to_rad(0) == 0
    with pytest.raises(ValueError):
        sector.x_to_rad(sector.end + 1)
