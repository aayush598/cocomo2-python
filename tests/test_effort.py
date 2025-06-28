# tests/test_effort.py

import pytest
from cocomo.effort import calculate_effort
from cocomo.constants import DEFAULT_EMS, DEFAULT_SFS

def test_effort_nominal():
    pm, E = calculate_effort(size_ksloc=100, ems=DEFAULT_EMS, sfs=DEFAULT_SFS)
    assert round(pm, 2) == 465.32
    assert round(E, 3) == 1.1  # B + 0.01 * SF_sum

def test_effort_zero_size():
    pm, E = calculate_effort(size_ksloc=0.0, ems=DEFAULT_EMS, sfs=DEFAULT_SFS)
    assert pm == 0.0
