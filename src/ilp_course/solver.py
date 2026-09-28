from dataclasses import dataclass
from typing import Sequence
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


@dataclass
class MILPResult:
    success: bool
    status: int
    message: str
    objective: float | None
    x: np.ndarray | None
    mip_gap: float | None
    mip_node_count: int | None


def solve_milp(
    c: Sequence[float],
    A_ub=None,
    b_ub=None,
    A_eq=None,
    b_eq=None,
    integrality=None,
    lower=None,
    upper=None,
    maximize=False,
    options=None,
) -> MILPResult:
    """Small educational wrapper around scipy.optimize.milp."""
    c = np.asarray(c, dtype=float)
    if maximize:
        c = -c

    constraints = []
    if A_ub is not None:
        constraints.append(
            LinearConstraint(np.asarray(A_ub, dtype=float), -np.inf, np.asarray(b_ub, dtype=float))
        )
    if A_eq is not None:
        b_eq = np.asarray(b_eq, dtype=float)
        constraints.append(
            LinearConstraint(np.asarray(A_eq, dtype=float), b_eq, b_eq)
        )

    n = len(c)
    if lower is None:
        lower = np.zeros(n)
    if upper is None:
        upper = np.full(n, np.inf)

    if integrality is None:
        integrality = np.zeros(n, dtype=int)

    result = milp(
        c,
        integrality=np.asarray(integrality),
        bounds=Bounds(np.asarray(lower), np.asarray(upper)),
        constraints=constraints,
        options=options or {},
    )

    x = None if result.x is None else np.asarray(result.x)
    objective = None
    if result.fun is not None:
        objective = float(-result.fun if maximize else result.fun)

    return MILPResult(
        success=bool(result.success),
        status=int(result.status),
        message=str(result.message),
        objective=objective,
        x=x,
        mip_gap=getattr(result, "mip_gap", None),
        mip_node_count=getattr(result, "mip_node_count", None),
    )
