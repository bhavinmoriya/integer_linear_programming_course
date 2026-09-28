# 04 — Logical Constraints

Integer programming becomes powerful when binary variables represent decisions.

## Example: project selection

Let x_i ∈ {0,1}.

### Dependency

Project A requires B:

`x_A <= x_B`.

### Mutual exclusion

Cannot select A and B together:

`x_A + x_B <= 1`.

### Exactly one

`x_A + x_B = 1`.

### At least one

`x_A + x_B >= 1`.

### If A then at least two of B,C,D

`x_A <= x_B + x_C + x_D - 1`.

Check the formulation carefully: when A=1, the right-hand side must permit at least two selections. A cleaner formulation is

`x_B + x_C + x_D >= 2 x_A`.

This is a general modelling pattern: use the activating binary variable as a multiplier on the required quantity.

## Fixed charge

Suppose production q costs variable cost c per unit plus fixed setup cost F.

Let y ∈ {0,1} indicate whether production occurs.

`q <= M y`

and objective contains

`c q + F y`.

If q > 0, y must be 1. If y = 0, q = 0.

## Exercise

Build a small product-selection model with:
- budget;
- project dependencies;
- mutual exclusion;
- maximum number of projects;
- fixed setup cost.
