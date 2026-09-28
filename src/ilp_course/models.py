from dataclasses import dataclass
from typing import Sequence
import numpy as np
import pulp


def solve_knapsack(values: Sequence[float], weights: Sequence[float], capacity: float):
    n = len(values)
    model = pulp.LpProblem("Knapsack", pulp.LpMaximize)
    x = [pulp.LpVariable(f"x_{i}", cat="Binary") for i in range(n)]
    model += pulp.lpSum(values[i] * x[i] for i in range(n))
    model += pulp.lpSum(weights[i] * x[i] for i in range(n)) <= capacity
    model.solve(pulp.PULP_CBC_CMD(msg=False))
    chosen = [i for i, v in enumerate(x) if v.value() > 0.5]
    return {
        "status": pulp.LpStatus[model.status],
        "objective": pulp.value(model.objective),
        "chosen": chosen,
        "x": [v.value() for v in x],
    }


def solve_facility_location(
    fixed_costs: Sequence[float],
    capacities: Sequence[float],
    demands: Sequence[float],
    transport_costs: Sequence[Sequence[float]],
):
    """Uncapacitated/ capacitated fixed-charge facility-location style model."""
    F = range(len(fixed_costs))
    C = range(len(demands))
    model = pulp.LpProblem("FacilityLocation", pulp.LpMinimize)

    y = {f: pulp.LpVariable(f"open_{f}", cat="Binary") for f in F}
    x = {
        (f, c): pulp.LpVariable(f"ship_{f}_{c}", lowBound=0)
        for f in F for c in C
    }

    model += (
        pulp.lpSum(fixed_costs[f] * y[f] for f in F)
        + pulp.lpSum(transport_costs[f][c] * x[f, c] for f in F for c in C)
    )

    for c in C:
        model += pulp.lpSum(x[f, c] for f in F) == demands[c]

    for f in F:
        model += pulp.lpSum(x[f, c] for c in C) <= capacities[f] * y[f]

    model.solve(pulp.PULP_CBC_CMD(msg=False))

    return {
        "status": pulp.LpStatus[model.status],
        "objective": pulp.value(model.objective),
        "open_facilities": [f for f in F if y[f].value() > 0.5],
        "shipments": {(f, c): x[f, c].value() for f in F for c in C},
    }


def solve_assignment(costs: Sequence[Sequence[float]]):
    costs = np.asarray(costs, dtype=float)
    m, n = costs.shape
    model = pulp.LpProblem("Assignment", pulp.LpMinimize)
    x = {
        (i, j): pulp.LpVariable(f"x_{i}_{j}", cat="Binary")
        for i in range(m) for j in range(n)
    }
    model += pulp.lpSum(costs[i, j] * x[i, j] for i in range(m) for j in range(n))
    for i in range(m):
        model += pulp.lpSum(x[i, j] for j in range(n)) == 1
    for j in range(n):
        model += pulp.lpSum(x[i, j] for i in range(m)) <= 1
    model.solve(pulp.PULP_CBC_CMD(msg=False))
    return {
        "status": pulp.LpStatus[model.status],
        "objective": pulp.value(model.objective),
        "assignment": [(i, j) for (i, j), v in x.items() if v.value() > 0.5],
    }


def solve_production(
    profit: Sequence[float],
    resource_matrix: Sequence[Sequence[float]],
    resource_capacity: Sequence[float],
    integer=True,
):
    n = len(profit)
    model = pulp.LpProblem("Production", pulp.LpMaximize)
    cat = "Integer" if integer else "Continuous"
    x = [pulp.LpVariable(f"x_{j}", lowBound=0, cat=cat) for j in range(n)]
    model += pulp.lpSum(profit[j] * x[j] for j in range(n))
    for r, cap in enumerate(resource_capacity):
        model += pulp.lpSum(resource_matrix[r][j] * x[j] for j in range(n)) <= cap
    model.solve(pulp.PULP_CBC_CMD(msg=False))
    return {
        "status": pulp.LpStatus[model.status],
        "objective": pulp.value(model.objective),
        "x": [v.value() for v in x],
    }
