# Small time-indexed scheduling model
import pulp

jobs = range(4)
machines = range(2)
processing = [2, 3, 1, 2]

model = pulp.LpProblem("TinyScheduling", pulp.LpMinimize)

# x[j,t,m] = 1 if job j starts at time t on machine m
T = range(7)
x = {
    (j, t, m): pulp.LpVariable(f"x_{j}_{t}_{m}", cat="Binary")
    for j in jobs for t in T for m in machines
}

makespan = pulp.LpVariable("makespan", lowBound=0, cat="Integer")
model += makespan

for j in jobs:
    model += pulp.lpSum(x[j, t, m] for t in T for m in machines) == 1

# makespan >= completion time
for j in jobs:
    for t in T:
        for m in machines:
            model += makespan >= (t + processing[j]) * x[j, t, m]

# At most one active job per machine and time.
for m in machines:
    for tau in T:
        active = []
        for j in jobs:
            for t in T:
                if t <= tau < t + processing[j]:
                    active.append(x[j, t, m])
        model += pulp.lpSum(active) <= 1

model.solve(pulp.PULP_CBC_CMD(msg=False))
print("Status:", pulp.LpStatus[model.status])
print("Makespan:", makespan.value())
