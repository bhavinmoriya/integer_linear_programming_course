# 13 — Capstone: Multi-Period Supply Chain Network Design

Build a complete MILP.

## Story

A company has:
- plants;
- warehouses;
- customers;
- multiple periods.

You decide:
- which plants to open;
- production quantity;
- warehouse throughput;
- shipments;
- inventory.

## Variables

Example:

`y_p ∈ {0,1}` plant opening.

`q_{p,t} >= 0` production.

`s_{p,w,t} >= 0` plant-to-warehouse shipment.

`r_{w,c,t} >= 0` warehouse-to-customer shipment.

`I_{w,t} >= 0` inventory.

## Objective

Minimize:

fixed plant costs
+ production costs
+ transportation costs
+ warehouse handling costs
+ inventory holding costs.

## Constraints

1. Plant capacity
2. Warehouse capacity
3. Customer demand
4. Flow conservation
5. Inventory balance
6. Opening logic
7. Initial inventory
8. Optional service-level constraints

## Required experiments

### Experiment A
Compare LP relaxation and MILP.

### Experiment B
Increase fixed opening costs.

### Experiment C
Increase demand by 10%.

### Experiment D
Remove one plant.

### Experiment E
Add a service-level constraint.

For each experiment report:
- objective;
- decisions;
- solve time;
- optimality gap;
- interpretation.

## Final deliverable

Create a 5–10 page report with:
- problem statement;
- assumptions;
- mathematical model;
- implementation;
- verification;
- computational results;
- sensitivity analysis;
- limitations.

This is a portfolio-grade optimization project.
