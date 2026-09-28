# 12 — Statistics for Optimization

Optimization and statistics meet naturally when data are uncertain.

## Random instance experiments

Suppose we compare two formulations A and B.

For each of 100 generated instances record:
- number of variables;
- number of constraints;
- LP objective;
- integer objective;
- root gap;
- solve time;
- node count.

Use Polars for analysis.

Example:

```python
import polars as pl

df = pl.DataFrame({
    "formulation": ["A", "A", "B", "B"],
    "time": [0.12, 0.15, 0.08, 0.11],
})

print(
    df.group_by("formulation")
      .agg([
          pl.col("time").median().alias("median_time"),
          pl.col("time").mean().alias("mean_time"),
      ])
)
```

## Statistical caution

Optimization runtimes are often highly skewed.

Therefore:
- mean alone can be misleading;
- median is robust;
- quantiles are useful;
- censored runs matter when a time limit is imposed.

## Suggested experiment

Generate 200 knapsack instances.

Compare:
- greedy;
- brute force;
- MILP.

Measure correctness and runtime.

Then vary:
- number of items;
- capacity ratio;
- value/weight distribution.

This turns the course into a small computational research project.
