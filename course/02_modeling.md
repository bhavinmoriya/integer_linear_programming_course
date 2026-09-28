# 02 — Modelling: Turning English into Mathematics

This is the most important skill in optimization.

## Binary decisions

Let

`y_i = 1` if facility i is opened, else 0.

Then:
- open at most 3 facilities: `sum(y_i) <= 3`
- open exactly 3: `sum(y_i) = 3`
- open at least 3: `sum(y_i) >= 3`

## Implication

"If A is selected, B must be selected":

`x_A <= x_B`.

## Either/or

"If A or B must be selected":

`x_A + x_B >= 1`.

"If exactly one":

`x_A + x_B = 1`.

## Conditional continuous variable

"If facility i is closed, production x_i must be zero."

Use:

`x_i <= M y_i`.

This is a big-M formulation.

A tight valid M is much better than an unnecessarily huge M.

## Cardinality

At most k projects:

`sum(x_i) <= k`.

At least k:

`sum(x_i) >= k`.

Exactly k:

`sum(x_i) = k`.

## Absolute value

To model `z = |x|`, common linear formulations use

`z >= x`
`z >= -x`

and, when minimizing z, these inequalities become tight at optimum.

For exact equality in a more general context, binary variables or additional structure may be required.

## Exercises

1. Select at most 4 projects.
2. If project 1 is selected, project 4 must be selected.
3. Select project 2 or project 3, but not both.
4. If machine A is used, pay a fixed setup cost.
5. A production variable is zero unless its corresponding plant is open.

For every exercise write the English statement first, then the mathematical statement.
