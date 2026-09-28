# Integer Linear Programming with Python — Full Course

A hands-on course for learning Integer Linear Programming (ILP/MILP) from mathematical foundations to practical optimization.

## What you will learn

1. Linear programming geometry and the LP relaxation
2. Integer variables, binary variables, and mixed-integer models
3. Modelling techniques:
   - logical conditions
   - fixed charges
   - either/or constraints
   - implications
   - cardinality constraints
   - absolute values
   - piecewise-linear costs
   - assignment and scheduling
4. LP relaxation, bounds, integrality gap
5. Branch-and-bound
6. Cutting planes
7. Branch-and-cut
8. Presolve, symmetry, big-M, numerical issues
9. Duality and reduced costs at the LP-relaxation level
10. Python modelling with PuLP and solving with HiGHS
11. Direct use of `scipy.optimize.milp`
12. Reading solver status, objective, bounds, and solution
13. Sensitivity-style reasoning and what changes when data change
14. Real applications: knapsack, facility location, production, assignment, scheduling
15. Statistical/OR ideas: relaxation bounds, optimality gaps, Monte Carlo instance generation
16. A complete capstone project
17. Interactive experimentation with a Gradio app

## Philosophy

The course repeatedly asks:

> "What does the mathematical model mean before we ask the computer to solve it?"

For each model:
- write the decision variables;
- write the objective;
- write every constraint in words;
- translate each statement into mathematics;
- implement it in Python;
- verify the result independently;
- inspect the LP relaxation when useful.

## Environment

This project uses `uv`.

```bash
uv sync
uv run pytest
uv run python -m ilp_course.examples.knapsack
uv run python -m ilp_course.examples.facility_location
uv run python -m ilp_course.examples.scheduling
uv run python -m ilp_course.app
```

Then open the local Gradio URL.

## Course map

| Module | Topic | Main coding |
|---|---|---|
| 01 | LP and ILP foundations | brute force + LP relaxation |
| 02 | Modelling integers/binaries | PuLP |
| 03 | Knapsack | PuLP + SciPy MILP |
| 04 | Logical modelling | binary variables |
| 05 | Assignment | matrix models |
| 06 | Facility location | fixed-charge MILP |
| 07 | Scheduling | time-indexed MILP |
| 08 | LP relaxation and gaps | SciPy/PuLP |
| 09 | Branch-and-bound | educational implementation |
| 10 | Cutting planes | conceptual + small examples |
| 11 | Solver engineering | presolve, big-M, symmetry |
| 12 | Statistics for optimization | random instances + gap distributions |
| 13 | Capstone | supply-chain/network design |

## Suggested 8-week schedule

### Week 1
Modules 01–02. Focus on translating English into constraints.

### Week 2
Module 03. Knapsack from brute force to MILP.

### Week 3
Modules 04–05. Logical constraints and assignment.

### Week 4
Module 06. Facility location and fixed charges.

### Week 5
Module 07. Scheduling.

### Week 6
Modules 08–10. Relaxations, branch-and-bound, cuts.

### Week 7
Modules 11–12. Solver engineering and statistical experiments.

### Week 8
Module 13. Capstone and portfolio-quality report.

## Important distinction

- **LP**: continuous decision variables.
- **ILP**: all decision variables are integer.
- **MILP/MIP**: some variables are integer and others can be continuous.
- **Binary programming**: variables are restricted to 0 or 1.

Most industrial "ILP" work is actually MILP.

## Mathematical core

A generic MILP is

maximize/minimize

    c^T x

subject to

    A x <= b
    A_eq x = b_eq
    l <= x <= u
    x_j integer for selected j.

The LP relaxation removes the integrality restrictions.

The relaxation gives a bound:
- maximization: LP optimum >= integer optimum
- minimization: LP optimum <= integer optimum

This single fact is central to branch-and-bound.

## Portfolio idea

After completing the capstone, create a README containing:
- business problem;
- assumptions;
- variables;
- objective;
- constraints;
- LP relaxation;
- optimality gap;
- computational time;
- sensitivity experiments;
- limitations;
- reproducibility instructions.


## Module 14 — Simplex → MILP

The course now includes a dedicated bridge from LP geometry and simplex to modern MILP: bases and pivots, reduced costs, revised vs tableau simplex, dual simplex and reoptimization, LP relaxation bounds, branching/pruning, and branch-and-cut.

Run its example with:

```bash
uv run python -m ilp_course.examples.simplex
```
