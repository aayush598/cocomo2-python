from cocomo.effort import calculate_effort

def test_effort():
    pm, E = calculate_effort(100)
    assert round(pm, 1) == 586.6
    assert round(E, 2) == 1.15
