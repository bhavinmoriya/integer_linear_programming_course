from ilp_course.models import (
    solve_assignment,
    solve_knapsack,
    solve_production,
)


def test_knapsack():
    result = solve_knapsack([10, 13, 17, 8], [5, 7, 9, 4], 15)
    assert result["status"] == "Optimal"
    assert abs(result["objective"] - 30) < 1e-8


def test_assignment():
    result = solve_assignment([
        [9, 2, 7],
        [6, 4, 3],
        [5, 8, 1],
    ])
    assert result["status"] == "Optimal"
    assert abs(result["objective"] - 9) < 1e-8


def test_production_integer():
    result = solve_production(
        profit=[20, 30, 40],
        resource_matrix=[[2, 3, 5], [4, 2, 3]],
        resource_capacity=[20, 18],
        integer=True,
    )
    assert result["status"] == "Optimal"
    assert all(abs(x - round(x)) < 1e-8 for x in result["x"])
