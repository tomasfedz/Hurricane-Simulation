"""Validation tests — skeletons.

Each test gets un-skipped as the corresponding solver piece lands.
A skipped test here is a promise, not a result.
"""

import pytest


@pytest.mark.skip(reason="solver not implemented yet — week 2 milestone")
def test_dam_break_matches_analytic():
    """1D dam-break height profile vs. the analytic solution."""
    ...


@pytest.mark.skip(reason="solver not implemented yet — week 2-3 milestone")
def test_mass_is_conserved_2d():
    """Total mass in a closed 2D run stays constant to ~1e-10 relative error."""
    ...


@pytest.mark.skip(reason="vortex not implemented yet — week 4-5 milestone")
def test_balanced_vortex_holds():
    """A balanced vortex remains coherent over many rotation periods."""
    ...
