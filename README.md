# Hurricane Simulation

A from-scratch 2D shallow-water-equations (SWE) solver in Python that simulates a
hurricane-like vortex on a rotating plane. Built as a computational physics
portfolio project — the point is the numerics, written and validated by hand.

> **Status:** scaffolding. The solver is in development; see the roadmap below.
> This is *not* a weather forecast model and does not use real storm data.

## The physics in 30 seconds

The shallow-water equations describe a single layer of fluid of depth $h(x, y, t)$
with horizontal velocities $u, v$ under gravity $g$ and Coriolis parameter $f$:

- Mass: $\partial_t h + \partial_x (hu) + \partial_y (hv) = 0$
- x-momentum: $\partial_t (hu) + \partial_x (hu^2 + \tfrac{1}{2}gh^2) + \partial_y (huv) = f\,hv$
- y-momentum: $\partial_t (hv) + \partial_x (huv) + \partial_y (hv^2 + \tfrac{1}{2}gh^2) = -f\,hu$

Plan: discretize with a finite-volume scheme (Rusanov / Lax-Friedrichs flux),
explicit time stepping limited by the CFL condition, then initialize a balanced
Rankine vortex and watch it evolve like an idealized hurricane.

## Roadmap

- [ ] 1D dam-break solver, validated against the analytic solution
- [ ] 2D solver without rotation; mass-conservation checks
- [ ] Coriolis (f-plane, then beta-plane) + balanced vortex initial condition
- [ ] Hurricane run: track minimum central height and maximum wind speed
- [ ] Polished animation (height anomaly + wind vectors) and intensity time series
- [ ] Full numerical documentation and test suite

## Repository structure

```
src/shallow_water/   solver, initial conditions, diagnostics
tests/               validation tests (dam break, conservation, balance)
notebooks/           exploration and validation plots
scripts/             runnable scripts, e.g. make_animation.py
docs/numerics.md     scheme, grid, CFL condition, validation notes
assets/              demo media for this README
```

## Setup

```bash
git clone https://github.com/tomasfedz/Hurricane-Simulation.git
cd Hurricane-Simulation
python -m venv .venv
# Windows:  .venv\Scripts\activate
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt
```

## Development workflow

Code is developed on a laptop (VS Code) and heavy / high-resolution runs are
executed on a desktop with an NVIDIA RTX 5070. GitHub is the bridge between
the two machines — same pinned `requirements.txt` on both, always.

## Stack

Python · NumPy · Numba · Matplotlib · pytest

## Author

Tomas Fernandez — B.S. Computational Physics (in progress), BYU-Idaho.
Data Analyst II at CorVel by day; this is an evenings-and-weekends project.
