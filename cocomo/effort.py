# cocomo/effort.py

from cocomo.constants import A, B, DEFAULT_EMS, DEFAULT_SFS
import math

def compute_e(scale_factors):
    sf_sum = sum(scale_factors.values())
    return B + 0.01 * sf_sum

def calculate_effort(size_ksloc, ems=None, sfs=None):
    ems = ems or DEFAULT_EMS
    sfs = sfs or DEFAULT_SFS

    E = compute_e(sfs)
    EM_product = math.prod(ems.values())

    PM = A * (size_ksloc ** E) * EM_product
    return round(PM, 2), E
