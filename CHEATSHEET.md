# ILP Cheat Sheet

## Standard form

min/max `c^T x`

subject to

`Ax <= b`
`Aeq x = beq`
`l <= x <= u`

with selected integer variables.

## Common patterns

| Requirement | Linear formulation |
|---|---|
| A selected | `x_A = 1` |
| At most k | `sum x <= k` |
| At least k | `sum x >= k` |
| Exactly k | `sum x = k` |
| A implies B | `A <= B` |
| Not both | `A + B <= 1` |
| At least one | `A + B >= 1` |
| Exactly one | `A + B = 1` |
| Fixed charge | `q <= M y` |
| Facility capacity | `flow <= capacity*y` |

## Optimization logic

LP relaxation -> bound
Branching -> divide search space
Incumbent -> best known integer solution
Pruning -> discard node that cannot improve incumbent
Cuts -> remove fractional regions without removing integer feasible points
Branch-and-cut -> all of the above

## Debugging

If results look strange:
1. print variables;
2. print constraint residuals;
3. test a tiny instance by brute force;
4. inspect LP relaxation;
5. verify units;
6. check big-M.
