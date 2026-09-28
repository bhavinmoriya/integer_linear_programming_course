# 06 — Facility Location

Choose facilities to open and decide how much each facility serves each customer.

Variables:
- `y_f ∈ {0,1}`: facility f is open.
- `x_fc >= 0`: quantity shipped from f to customer c.

Objective:

fixed opening cost + transportation cost.

Demand:

`sum_f x_fc = d_c`.

Capacity:

`sum_c x_fc <= capacity_f y_f`.

The capacity constraint is a classic linking constraint.

## Why the linking constraint is important

Without `y_f`, the model could ship from every facility without paying opening cost.

With

`sum_c x_fc <= capacity_f y_f`

we connect the discrete decision to the continuous decision.

## Python

See `solve_facility_location`.

## Extension

Add:
- maximum number of open facilities;
- customer-facility eligibility;
- minimum service from a facility;
- carbon cost;
- fixed + variable transportation cost.

## Portfolio extension

Turn this into a location-planning study:
- generate demand scenarios;
- solve each scenario;
- compare facility-opening stability.
