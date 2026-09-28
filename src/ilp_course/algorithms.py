from __future__ import annotations
from dataclasses import dataclass
from math import floor, ceil
import numpy as np


@dataclass
class BnBResult:
    best_x: tuple[int, ...] | None
    best_value: float
    nodes: int


def brute_force_binary_knapsack(values, weights, capacity):
    """Exact reference solver for small binary knapsack instances."""
    n = len(values)
    best_value = -float("inf")
    best_x = None
    nodes = 0

    for mask in range(1 << n):
        nodes += 1
        x = tuple((mask >> i) & 1 for i in range(n))
        total_weight = sum(weights[i] * x[i] for i in range(n))
        if total_weight <= capacity:
            value = sum(values[i] * x[i] for i in range(n))
            if value > best_value:
                best_value = value
                best_x = x

    return BnBResult(best_x, best_value, nodes)


def fractional_knapsack_bound(values, weights, capacity, fixed_x):
    """Upper bound for maximization by filling remaining capacity fractionally."""
    n = len(values)
    weight = sum(weights[i] * fixed_x[i] for i in range(n))
    value = sum(values[i] * fixed_x[i] for i in range(n))
    if weight > capacity:
        return -float("inf")

    candidates = [
        (values[i] / weights[i], i)
        for i in range(n)
        if fixed_x[i] is None
    ]
    candidates.sort(reverse=True)

    remaining = capacity - weight
    bound = value
    for ratio, i in candidates:
        take = min(1.0, remaining / weights[i])
        bound += take * values[i]
        remaining -= take * weights[i]
        if remaining <= 1e-12:
            break
    return bound


def branch_and_bound_knapsack(values, weights, capacity):
    """Educational branch-and-bound for binary knapsack.

    This is intentionally simple rather than industrial-strength.
    """
    n = len(values)
    best_value = -float("inf")
    best_x = None
    nodes = 0

    def recurse(partial, depth):
        nonlocal best_value, best_x, nodes
        nodes += 1

        bound = fractional_knapsack_bound(values, weights, capacity, partial)
        if bound <= best_value + 1e-12:
            return

        if depth == n:
            x = tuple(int(v) for v in partial)
            value = sum(values[i] * x[i] for i in range(n))
            weight = sum(weights[i] * x[i] for i in range(n))
            if weight <= capacity and value > best_value:
                best_value = value
                best_x = x
            return

        # Try 1 first because this is maximization.
        for decision in (1, 0):
            partial.append(decision)
            recurse(partial, depth + 1)
            partial.pop()

    recurse([None] * n, 0)
    return BnBResult(best_x, best_value, nodes)
