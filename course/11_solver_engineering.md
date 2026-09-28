# 11 — Solver Engineering

A model can be correct and still solve badly.

## Big-M

Bad:

`M = 10^9`

when a valid `M = 100` exists.

Large M can cause:
- weak relaxations;
- numerical scaling problems;
- slower branching.

## Symmetry

If two facilities are identical, the solver may see many equivalent solutions.

A symmetry-breaking constraint can sometimes help.

Example:

`y_1 >= y_2`

when facilities 1 and 2 are truly interchangeable.

## Presolve

Presolve simplifies the model before the main algorithm:
- removes redundant constraints;
- fixes variables;
- tightens bounds;
- detects infeasibility.

## Practical checklist

Before blaming the solver:
1. verify units;
2. tighten variable bounds;
3. derive tight M values;
4. remove redundant variables;
5. exploit network/assignment structure;
6. reduce symmetry;
7. inspect the LP relaxation.
