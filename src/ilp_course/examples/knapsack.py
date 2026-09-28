from ilp_course.models import solve_knapsack
from ilp_course.algorithms import brute_force_binary_knapsack, branch_and_bound_knapsack

values = [10, 13, 17, 8, 20]
weights = [5, 7, 9, 4, 11]
capacity = 20

print("MILP:", solve_knapsack(values, weights, capacity))
print("Brute force:", brute_force_binary_knapsack(values, weights, capacity))
print("Branch and bound:", branch_and_bound_knapsack(values, weights, capacity))
