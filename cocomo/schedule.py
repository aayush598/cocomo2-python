# cocomo/schedule.py

from cocomo.constants import C, D, B

def calculate_schedule(pm, E):
    exponent = D + 0.2 * (E - B)
    TDEV = C * (pm ** exponent)
    return round(TDEV, 2)
