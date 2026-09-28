# 14 — Simplex → MILP: From LP Vertices to Branch-and-Bound

This module connects the classical simplex method directly to modern mixed-integer linear programming.

## The central story

`LP → simplex/barrier → LP relaxation → branch-and-bound → many related LPs → reoptimization → MILP`

## 1. A tiny LP

\[
\max 3x_1+2x_2
\]
subject to
\[
x_1+x_2\le4,\qquad 2x_1+x_2\le5,\qquad x_1,x_2\ge0.
\]

The feasible region is a polygon. An LP optimum can be found at an extreme point.

## 2. What simplex maintains

For standard form `Ax=b, x>=0`, choose a basis `B`. The basic variables satisfy

\[
x_B=B^{-1}b.
\]

A pivot exchanges one basic and one nonbasic variable and moves to a neighboring basic feasible solution.

## 3. Reduced costs

With `pi^T=c_B^T B^{-1}`, the reduced cost is

\[
\bar c_j=c_j-\pi^Ta_j.
\]

Under this convention, a positive reduced cost gives an improving direction for a maximization problem.

## 4. Revised simplex vs textbook tableau

The tableau is excellent for learning, but practical solvers use revised simplex ideas, sparse linear algebra, scaling, tolerances and sophisticated pricing rules. The important object is the basis and efficient linear solves involving it.

## 5. Why dual simplex matters to MILP

Suppose an LP relaxation is solved and branching changes a bound:

\[
x_j\le\lfloor x_j^*\rfloor
\]

or

\[
x_j\ge\lceil x_j^*\rceil.
\]

The old solution may become primal-infeasible while much of the dual information remains useful. Dual simplex can reoptimize efficiently. This is one reason simplex remains highly relevant inside modern MILP solvers.

## 6. LP relaxation → branch-and-bound

For an ILP, temporarily remove integrality. For maximization,

\[
z_{LP}\ge z_{ILP}.
\]

If the LP solution is fractional, branch on a fractional variable. If an incumbent integer solution has value 100 and a node's LP bound is 93, the whole node can be pruned.

## 7. Modern picture

```text
MILP
  |
presolve/model
  |
LP relaxation
  |
+----------------+
|                |
integer       fractional
|                |
incumbent       branch
                 |
          +------+------+
          |             |
       LP child      LP child
          |             |
      bound           bound
          \             /
           +-----------+
             prune/branch
```

Modern solvers add presolve, cutting planes, primal heuristics, strong branching, symmetry handling, parallel search and other techniques.

## 8. Educational Python simplex

The project contains `ilp_course.simplex.simplex_max`, a deliberately small primal-simplex implementation for

`max c@x` subject to `Ax<=b, x>=0`,

assuming `b>=0` and a finite optimum.

```python
from ilp_course.simplex import simplex_max

r = simplex_max(A=[[1, 1], [2, 1]], b=[4, 5], c=[3, 2])
print(r)
```

It is educational, not production software: no Phase I, no dual simplex, limited numerical safeguards, and dense tableau operations.

## 9. Experiments

1. Trace each pivot: iteration, basis, entering variable, leaving variable, objective.
2. Compare LP relaxation and ILP on small instances.
3. Run the educational branch-and-bound knapsack solver and count nodes/pruned nodes.
4. Compare two equivalent MILP formulations using root relaxation, solve time and node count.

## 10. Feynman test

Explain without notes why an LP relaxation helps solve an integer problem. A complete answer should mention: easier LP; valid bound; fractional solution; branching; pruning; repeated LP reoptimization; cuts and heuristics in modern solvers.
