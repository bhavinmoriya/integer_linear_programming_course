# 05 — Assignment

There are workers i and jobs j.

Let

`x_ij = 1` if worker i performs job j.

Each worker gets exactly one job:

`sum_j x_ij = 1`.

Each job gets at most one worker:

`sum_i x_ij <= 1`.

Minimize total cost:

`sum_ij c_ij x_ij`.

## Python

```python
from ilp_course.models import solve_assignment

result = solve_assignment([
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1],
])
print(result)
```

## Extension

Add worker eligibility:
- worker 0 cannot do job 2;
- worker 1 cannot do job 0.

Set the corresponding variable upper bound to zero, or add `x_ij = 0`.

## Mathematical insight

Assignment is a binary linear model whose LP relaxation has unusually strong structure. This is a useful example of how the structure of a constraint matrix can make an integer model easier than a generic MILP.
