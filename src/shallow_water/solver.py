"""Core shallow-water solver — SKELETON.

Planned implementation (see docs/numerics.md):
- Conservative variables U = (h, hu, hv) on a regular Cartesian grid.
- Finite-volume update with Rusanov (local Lax-Friedrichs) numerical flux.
- Explicit time stepping; dt chosen each step from the CFL condition
  dt <= CFL * dx / max(|u| + sqrt(g*h)).
- Coriolis source terms added after the flux update (operator splitting).

Nothing here is implemented yet on purpose: the 1D dam-break problem comes
first, gets validated against its analytic solution, and only then is the
scheme extended to 2D.
"""

from __future__ import annotations

import numpy as np


class ShallowWaterSolver:
    """2D shallow-water solver on a regular grid. Not yet implemented."""

    def __init__(self, nx: int, ny: int, lx: float, ly: float, g: float = 9.81):
        self.nx, self.ny = nx, ny
        self.lx, self.ly = lx, ly
        self.dx, self.dy = lx / nx, ly / ny
        self.g = g
        # State arrays (h, hu, hv) are allocated in set_initial_conditions().
        self.h: np.ndarray | None = None
        self.hu: np.ndarray | None = None
        self.hv: np.ndarray | None = None

    def set_initial_conditions(self, h, hu, hv) -> None:
        raise NotImplementedError("TODO: week 2-3 — store and copy initial state")

    def stable_dt(self, cfl: float = 0.9) -> float:
        raise NotImplementedError("TODO: week 2-3 — CFL-limited time step")

    def step(self, dt: float) -> None:
        raise NotImplementedError("TODO: week 2-3 — Rusanov flux update")

    def run(self, t_end: float) -> None:
        raise NotImplementedError("TODO: week 2-3 — time loop calling step()")
