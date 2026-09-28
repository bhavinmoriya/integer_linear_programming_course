from __future__ import annotations
from dataclasses import dataclass
import numpy as np

@dataclass
class SimplexResult:
    status: str
    objective: float | None
    x: np.ndarray | None
    iterations: int

def simplex_max(A, b, c, tol=1e-10, max_iter=10_000):
    """Educational primal simplex for max c@x, Ax<=b, x>=0.
    Assumes b>=0 and a finite optimum. Not a production solver.
    """
    A=np.asarray(A,dtype=float); b=np.asarray(b,dtype=float); c=np.asarray(c,dtype=float)
    if A.ndim != 2: raise ValueError('A must be a matrix')
    m,n=A.shape
    if b.shape!=(m,) or c.shape!=(n,): raise ValueError('incompatible shapes')
    if np.any(b < -tol): raise ValueError('requires b >= 0')
    T=np.zeros((m+1,n+m+1)); T[:m,:n]=A; T[:m,n:n+m]=np.eye(m); T[:m,-1]=b; T[-1,:n]=-c
    basis=list(range(n,n+m)); it=0
    while it<max_iter:
        it+=1
        cand=np.where(T[-1,:-1] < -tol)[0]
        if len(cand)==0:
            x=np.zeros(n)
            for i,col in enumerate(basis):
                if col<n: x[col]=T[i,-1]
            return SimplexResult('optimal',float(T[-1,-1]),x,it-1)
        entering=int(cand[0]); col=T[:m,entering]; pos=np.where(col>tol)[0]
        if len(pos)==0: return SimplexResult('unbounded',None,None,it)
        ratios=T[pos,-1]/col[pos]; r=pos[np.argmin(ratios)]; pivot=T[r,entering]
        T[r,:]/=pivot
        for i in range(m+1):
            if i!=r: T[i,:]-=T[i,entering]*T[r,:]
        basis[r]=entering
    return SimplexResult('iteration_limit',None,None,it)
