# tests/test_sizing.py

from cocomo.sizing import (
    FPCount, FPType,
    weight_fp_items,
    ufp_to_sloc,
    compute_size,
    apply_revl
)

def test_weight_fp_items():
    items = [
        FPCount(FPType.ILF, det=25, ftr_or_ret=3),  # Avg → 10
        FPCount(FPType.EI,  det=10, ftr_or_ret=2),  # Avg → 4
        FPCount(FPType.EO,  det=22, ftr_or_ret=4),  # High → 7
    ]
    total = weight_fp_items(items)
    assert total == 21

def test_ufp_to_sloc():
    sloc = ufp_to_sloc(20, "Java")
    assert sloc == 20 * 53

def test_compute_size_and_revl():
    res = compute_size(new_sloc=5000, adapted_esloc=2000, revl_percent=10)
    assert res.sloc == 7000
    assert round(res.sloc_after_revl) == 7700

def test_apply_revl_direct():
    adjusted = apply_revl(10000, 15)  # 15% REVL
    assert round(adjusted) == 11500
