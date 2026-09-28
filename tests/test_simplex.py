import numpy as np
import pytest
from ilp_course.simplex import simplex_max

def test_simplex_basic():
    r=simplex_max([[1,1],[2,1]],[4,5],[3,2])
    assert r.status=='optimal'
    assert abs(r.objective-9)<1e-8
    assert np.allclose(r.x,[1,3])

def test_unbounded():
    assert simplex_max([[-1]],[0],[1]).status=='unbounded'

def test_negative_rhs():
    with pytest.raises(ValueError): simplex_max([[1]],[-1],[1])
