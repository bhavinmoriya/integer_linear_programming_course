# 08 — LP Relaxation and Integrality Gap

The LP relaxation is one of the most important ideas in MILP.

For maximization:

`z_LP >= z_ILP`.

Define the absolute gap:

`z_LP - z_ILP`.

A relative gap can be

`(z_LP - z_ILP) / max(|z_ILP|, epsilon)`.

## Why it matters

Suppose the LP relaxation gives 101 and the best integer solution is 100.

The solver has a very strong bound.

If LP gives 1000 and integer solution gives 500, the relaxation is weak.

A weak relaxation usually means branch-and-bound has more work.

## Exercise

For random knapsack instances:
1. solve LP relaxation;
2. solve ILP;
3. calculate the gap;
4. plot a histogram;
5. investigate how the gap changes with number of items.

## Statistical thinking

If you compare formulations, do not compare one instance only.

Use repeated random instances and report:
- median solve time;
- interquartile range;
- fraction solved within a time limit;
- median root gap.

Optimization benchmarking is an experimental science.
