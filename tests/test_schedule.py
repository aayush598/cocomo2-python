# tests/test_schedule.py

from cocomo.schedule import nominal_tdev, calculate_schedule

def test_nominal_schedule():
    # E = 1.15 from nominal scale factors, PM = 586.61 from 100 KSLOC
    tdev = nominal_tdev(pm_ns=586.61, E=1.15)
    assert round(tdev, 2) == 29.70

def test_schedule_with_sced():
    tdev = calculate_schedule(pm=586.61, E=1.15, sced_rating="N", pm_includes_sced=True)
    assert round(tdev, 2) == 29.70

def test_schedule_with_sced_vl():
    tdev = calculate_schedule(pm=586.61, E=1.15, sced_rating="VL", pm_includes_sced=True)
    # TDEV_NS should still be ~29.70, then reduced by 0.75
    expected = round(3.67 * (465.32 ** (0.28 + 0.2 * (1.10 - 0.91))) * 0.75, 2)
    assert round(tdev, 2) == 19.81

