"""Initial conditions — SKELETON.

Planned:
- dam_break_1d(): the classic validation case (high water left, low right),
  which has an analytic solution to compare against.
- rankine_vortex(): a Rankine combined vortex (solid-body rotation inside the
  radius of maximum wind, decaying outside it) with the height field balanced
  against the wind field, so the vortex starts in approximate geostrophic /
  gradient-wind balance instead of immediately exploding.
"""

from __future__ import annotations


def dam_break_1d(nx: int, h_left: float = 2.0, h_right: float = 1.0):
    raise NotImplementedError("TODO: week 2 — 1D dam-break initial state")


def rankine_vortex(nx: int, ny: int, vmax: float, rmax: float):
    raise NotImplementedError("TODO: week 4-5 — balanced hurricane-like vortex")
