from ilp_course.models import solve_facility_location

result = solve_facility_location(
    fixed_costs=[100, 80, 120],
    capacities=[10, 12, 15],
    demands=[5, 7, 4, 6],
    transport_costs=[
        [4, 6, 9, 7],
        [5, 4, 8, 6],
        [8, 7, 3, 5],
    ],
)
print(result)
