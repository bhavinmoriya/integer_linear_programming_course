# 09 — Branch-and-Bound

Branch-and-bound turns a continuous relaxation into an exact integer solution method.

At a high level:

1. Solve an LP relaxation.
2. If its solution is integer, you have a candidate solution.
3. If not, choose a fractional variable.
4. Branch:
   - `x_j <= floor(x_j*)`
   - `x_j >= ceil(x_j*)`
5. Solve the relaxations of the children.
6. Prune nodes whose bound cannot beat the incumbent.
7. Continue until all relevant nodes are pruned.

## Knapsack example

`ilp_course.algorithms.branch_and_bound_knapsack`

contains a small educational implementation.

It uses a fractional-knapsack upper bound.

## Important distinction

Branch-and-bound is not "try every integer point".

It intelligently avoids many regions using bounds.

## Exercise

Compare node counts:
- brute force;
- branch-and-bound.

Then deliberately create instances where the bound is weak.

Ask:

> What makes a bound strong?

This question leads naturally to cutting planes.
