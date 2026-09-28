# 03 — Knapsack: Your First Serious ILP

Given items i with value v_i and weight w_i, choose items without exceeding capacity C.

Decision:

`x_i in {0,1}`.

Objective:

`maximize sum(v_i x_i)`.

Constraint:

`sum(w_i x_i) <= C`.

## Python

```python
from ilp_course.models import solve_knapsack

result = solve_knapsack(
    values=[10, 13, 17, 8],
    weights=[5, 7, 9, 4],
    capacity=15,
)

print(result)
```

## Why this model matters

Knapsack appears directly or as a subproblem inside many larger optimization problems.

## Experiment

Generate random values and weights. Compare:
1. greedy by value/weight;
2. brute force;
3. MILP.

Greedy is fast but is not generally exact for 0-1 knapsack.

## Statistical experiment

Generate 100 random instances and measure the percentage of instances on which greedy agrees with the exact optimum.

Do not report only the mean. Also inspect:
- median;
- standard deviation;
- quartiles;
- worst case.

That is a useful first lesson in computational statistics.
