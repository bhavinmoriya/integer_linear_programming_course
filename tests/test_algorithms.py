from ilp_course.algorithms import (
    brute_force_binary_knapsack,
    branch_and_bound_knapsack,
)


def test_branch_and_bound_matches_bruteforce():
    values = [10, 13, 17, 8, 20]
    weights = [5, 7, 9, 4, 11]
    capacity = 20

    exact = brute_force_binary_knapsack(values, weights, capacity)
    bnb = branch_and_bound_knapsack(values, weights, capacity)

    assert bnb.best_value == exact.best_value
    assert bnb.best_x == exact.best_x


def test_knapsack_can_choose_nothing():
    result = brute_force_binary_knapsack([5, 6], [10, 11], 0)
    assert result.best_value == 0
    assert result.best_x == (0, 0)
