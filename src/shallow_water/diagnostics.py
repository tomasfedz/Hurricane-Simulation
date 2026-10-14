"""Diagnostics — SKELETON.

Planned checks, computed every N steps during a run:
- total_mass(): integral of h over the domain; must stay ~constant.
- max_wind_speed(): peak horizontal wind speed (hurricane intensity proxy).
- min_height(): lowest central height (inverse intensity proxy).
"""

from __future__ import annotations


def total_mass(h, dx: float, dy: float) -> float:
    raise NotImplementedError("TODO: week 2-3 — domain integral of h")


def max_wind_speed(h, hu, hv) -> float:
    raise NotImplementedError("TODO: week 4-5 — max sqrt(u^2 + v^2)")


def min_height(h) -> float:
    raise NotImplementedError("TODO: week 4-5 — minimum of h")
