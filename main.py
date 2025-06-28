#!/usr/bin/env python3
"""
main.py – COCOMO II Estimation CLI Tool
=======================================

Estimates Person-Months (PM), Schedule (TDEV), and Team Size
using full COCOMO II.2000 (Post-Architecture) model.

Integrates:
 • sizing.py       – SLOC calculation from FP or manual input
 • reuse.py        – ESLOC estimation for reused code
 • effort.py       – Effort estimation
 • schedule.py     – Schedule estimation
 • constants.py    – Default EMs & SFs

Author : Aayush Gid | License : MIT
"""

from cocomo.constants import DEFAULT_EMS, DEFAULT_SFS
from cocomo.sizing import weight_fp_items, ufp_to_sloc, compute_size, FPCount, FPType
from cocomo.reuse import (
    calc_esloc, ReuseParams, su_from_rating, aa_from_rating, unfm_from_rating
)
from cocomo.effort import calculate_effort
from cocomo.schedule import calculate_schedule

# For CLI input
def get_float(prompt, default=None):
    try:
        inp = input(prompt).strip()
        return float(inp) if inp else default
    except Exception:
        return default

def get_rating(prompt, options, default="N"):
    r = input(f"{prompt} {options} (default {default}): ").strip().upper()
    return r if r in options else default

# ───────────────────────────────────────────────────────────────
# Main CLI
# ───────────────────────────────────────────────────────────────

def main():
    print("┌────────────────────────────────────────────┐")
    print("│        COCOMO II.2000 Estimator CLI        │")
    print("└────────────────────────────────────────────┘\n")

    # 1. Project Sizing
    sizing_mode = input("Enter sizing mode: [1] KSLOC manually  [2] via Function Points: ").strip()

    if sizing_mode == "2":
        # Tiny hardcoded example
        print("\nExample FP counts:")
        fp_items = [
            FPCount(FPType.ILF, det=25, ftr_or_ret=3),
            FPCount(FPType.EI, det=10, ftr_or_ret=2),
            FPCount(FPType.EO, det=22, ftr_or_ret=4),
        ]
        ufp = weight_fp_items(fp_items)
        language = input("Target language (e.g., Java, C++): ").strip().lower()
        new_sloc = ufp_to_sloc(ufp, language)
        print(f"UFP = {ufp}, SLOC = {new_sloc:.0f}")
    else:
        new_sloc = get_float("Enter size of new code in KSLOC: ", default=100.0) * 1000

    # 2. Reused code
    use_reuse = input("\nReuse code? [y/N]: ").strip().lower() == "y"
    reused_esloc = 0
    if use_reuse:
        asloc = get_float("Adapted SLOC (ASLOC): ", 10000)
        dm = get_float("Design modified % (DM): ", 20)
        cm = get_float("Code modified % (CM): ", 30)
        im = get_float("Integration effort % (IM): ", 40)
        su = su_from_rating(get_rating("Software Understanding (SU)", list("VL H N L VH".split())))
        aa = aa_from_rating(get_rating("Assessment/Assimilation (AA)", ["0", "2", "4", "6", "8"]))
        unfm = unfm_from_rating(get_rating("Programmer Unfamiliarity (UNFM)", ["CF", "MF", "SF", "CFa", "MU", "CU"]))
        at = get_float("Auto translation % (AT): ", 25)

        reuse_params = ReuseParams(asloc=asloc, dm=dm, cm=cm, im=im, su=su, aa=aa, unfm=unfm, at=at)
        reused_esloc = calc_esloc(reuse_params)
        print(f"→ Equivalent SLOC from reuse = {reused_esloc:,.0f}")

    # 3. Requirements Evolution & Volatility
    revl = get_float("\nREVL % (default 10): ", 10)

    # 4. Final SLOC with REVL
    size_result = compute_size(new_sloc, reused_esloc, revl_percent=revl)
    total_ksloc = size_result.sloc_after_revl / 1000

    # 5. Effort estimation
    print("\nCalculating effort using default SFs and EMs (Nominal ratings)...")
    ems = DEFAULT_EMS.copy()
    sfs = DEFAULT_SFS.copy()
    pm, E = calculate_effort(total_ksloc, ems=ems, sfs=sfs)

    # 6. Schedule estimation
    sced = get_rating("Schedule Compression (SCED)", list("VL L N H VH".split()), default="N")
    tdev = calculate_schedule(pm, E, sced_rating=sced, pm_includes_sced=True)

    # 7. Report
    print("\n─────────────── Estimation Summary ───────────────")
    print(f"Total SLOC (after REVL):    {size_result.sloc_after_revl:,.0f}")
    print(f"Effort (PM):                {pm:.2f}")
    print(f"Development Time (months):  {tdev:.2f}")
    print(f"Average Team Size:          {pm / tdev:.2f}")
    print("─────────────────────────────────────────────────")

if __name__ == "__main__":
    main()
