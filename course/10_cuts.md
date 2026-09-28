# 10 — Cutting Planes and Branch-and-Cut

Suppose the LP relaxation contains fractional points that cannot be integer solutions.

A valid inequality is a constraint satisfied by every integer feasible solution.

If it cuts off some fractional LP solutions, it is a cutting plane.

Common families include:
- Gomory cuts;
- cover cuts;
- clique cuts;
- flow cuts;
- mixed-integer rounding cuts.

Modern MILP solvers usually combine:
- presolve;
- LP relaxations;
- branching;
- cutting planes;
- heuristics;
- primal heuristics;
- symmetry handling.

This combination is branch-and-cut.

## Conceptual exercise

Draw a 2D integer-feasible set and its LP relaxation.

Find a linear inequality that:
1. all integer feasible points satisfy;
2. some fractional points violate.

The purpose is geometric understanding, not memorizing cut names.
