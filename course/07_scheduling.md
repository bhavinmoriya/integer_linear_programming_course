# 07 — Scheduling

Scheduling is one of the most important practical MILP families.

## Time-indexed idea

Let

`x_{j,t} = 1`

if job j starts at time t.

Then a job starts exactly once:

`sum_t x_{j,t} = 1`.

Machine capacity is enforced by summing all jobs that would be active at each time.

## Alternative formulations

1. Time-indexed formulation
2. Start-time formulation
3. Disjunctive formulation
4. Sequencing variables

The choice of formulation can dramatically affect solver performance.

## Exercise

Schedule 5 jobs on 2 machines with:
- processing times;
- release dates;
- deadlines;
- machine eligibility;
- setup times.

Minimize makespan.

## Key lesson

A mathematically correct model can still be computationally poor.

Formulation is algorithmic performance.
