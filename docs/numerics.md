# Numerical method — notes

_Status: outline. This document gets filled in as each piece is implemented
and validated — claims here must match what the code actually does._

## Equations

2D shallow-water equations in conservative form for $U = (h, hu, hv)$,
with gravity $g$ and Coriolis parameter $f$ (f-plane first, beta-plane later).

## Discretization (planned)

- Regular Cartesian grid, cell-centered conserved variables.
- Finite-volume update with the Rusanov (local Lax-Friedrichs) flux.
- Explicit time stepping.

## Stability

- Time step from the CFL condition:
  $dt \le \mathrm{CFL} \cdot dx / \max(|u| + \sqrt{gh})$, CFL $\le 1$.
- Boundary conditions: TBD (periodic for the first 2D tests; reflective
  walls are the fallback). Record the choice and the reason here.

## Validation plan

1. 1D dam break vs. the analytic solution (height profile + shock speed).
2. Mass conservation in 2D to near machine precision over long runs.
3. Geostrophic balance hold: a balanced vortex should stay coherent
   instead of radiating away in a few time steps.

## Known limitations

- Single-layer, dry, no moisture / latent heat, no boundary-layer friction
  (a simple drag term may be added later and will be documented if so).
- This is an idealized vortex model, not a forecast model.
