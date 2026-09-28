# 01 — Foundations: LP, ILP, MILP

## 1. The basic optimization problem

An LP has the form

maximize `c^T x`

subject to

`Ax <= b`, `A_eq x = b_eq`, and bounds on `x`.

The difference between LP and ILP is not the linearity. It is the domain of the variables.

Example:

`2x + 3y <= 7`

with `x,y >= 0`.

LP permits `(x,y) = (0.5, 2)`.
ILP does not if both variables must be integers.

## 2. Why integrality changes everything

The feasible set of an LP is a polyhedron. The feasible set of an ILP is the integer points inside that polyhedron.

This can destroy the convexity that makes LP so tractable.

## 3. LP relaxation

Remove integrality.

For a maximization problem:

`integer optimum <= LP optimum`.

For minimization:

`integer optimum >= LP optimum`.

The difference is a computationally useful bound.

## Exercise

Consider:

maximize `10x + 7y`

subject to

`4x + 3y <= 10`
`x,y >= 0`
`x,y integer`.

1. Solve by inspection/brute force.
2. Solve the LP relaxation.
3. Compute the integrality gap.

The percentage gap can be defined as

`(LP - ILP) / |ILP| * 100%`

for maximization when ILP > 0.

## Coding

Use `ilp_course.algorithms.brute_force_binary_knapsack` for small exact instances.

The point of brute force is not speed. It gives a trusted reference solution for testing more sophisticated algorithms.
