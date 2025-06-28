#!/usr/bin/env python3
"""
main.py – COCOMO II FastAPI Service
===================================

Exposes endpoints to estimate:
 • SLOC from Function Points
 • ESLOC from reused code
 • Adjusted SLOC with REVL
 • Effort (PM) and Schedule (TDEV)

Author : Aayush Gid | License : MIT
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Literal, Optional

from cocomo.constants import DEFAULT_EMS, DEFAULT_SFS
from cocomo.sizing import FPCount, FPType, weight_fp_items, ufp_to_sloc, compute_size
from cocomo.reuse import ReuseParams, calc_esloc, su_from_rating, aa_from_rating, unfm_from_rating
from cocomo.effort import calculate_effort
from cocomo.schedule import calculate_schedule

app = FastAPI(title="COCOMO II Estimation API", version="1.0")

# ─────────────────────────────────────────────────────────────
# Models
# ─────────────────────────────────────────────────────────────

class FPItemInput(BaseModel):
    fp_type: Literal["ILF", "EIF", "EI", "EO", "EQ"]
    det: int
    ftr_or_ret: int

class SizingRequest(BaseModel):
    fp_items: List[FPItemInput]
    language: str

class ReuseRequest(BaseModel):
    asloc: float
    dm: float
    cm: float
    im: float
    su_rating: Literal["VL", "L", "N", "H", "VH"]
    aa_rating: Literal["0", "2", "4", "6", "8"]
    unfm_rating: Literal["CF", "MF", "SF", "CFa", "MU", "CU"]
    at: float = 0.0

class SLOCAdjustmentRequest(BaseModel):
    new_sloc: float
    adapted_esloc: float = 0.0
    revl_percent: float = 0.0

class EffortScheduleRequest(BaseModel):
    sloc_ksloc: float
    sced_rating: Literal["VL", "L", "N", "H", "VH"] = "N"

# ─────────────────────────────────────────────────────────────
# Endpoints
# ─────────────────────────────────────────────────────────────

@app.post("/size/from_function_points")
def size_from_fp(request: SizingRequest):
    fp_counts = [FPCount(fp_type=FPType(it.fp_type), det=it.det, ftr_or_ret=it.ftr_or_ret) for it in request.fp_items]
    ufp = weight_fp_items(fp_counts)
    sloc = ufp_to_sloc(ufp, request.language)
    return {
        "ufp": ufp,
        "sloc": sloc
    }

@app.post("/size/from_reuse")
def size_from_reuse(request: ReuseRequest):
    su = su_from_rating(request.su_rating)
    aa = aa_from_rating(request.aa_rating)
    unfm = unfm_from_rating(request.unfm_rating)

    reuse_params = ReuseParams(
        asloc=request.asloc,
        dm=request.dm,
        cm=request.cm,
        im=request.im,
        su=su,
        aa=aa,
        unfm=unfm,
        at=request.at
    )

    esloc = calc_esloc(reuse_params)
    return {"esloc": esloc}

@app.post("/size/adjust_with_revl")
def adjust_with_revl(request: SLOCAdjustmentRequest):
    result = compute_size(
        new_sloc=request.new_sloc,
        adapted_esloc=request.adapted_esloc,
        revl_percent=request.revl_percent
    )
    return {
        "sloc_total": result.sloc,
        "sloc_after_revl": result.sloc_after_revl
    }

@app.post("/estimate/effort_schedule")
def estimate_effort_schedule(request: EffortScheduleRequest):
    pm, E = calculate_effort(
        size_ksloc=request.sloc_ksloc,
        ems=DEFAULT_EMS,
        sfs=DEFAULT_SFS
    )
    tdev = calculate_schedule(
        pm=pm,
        E=E,
        sced_rating=request.sced_rating,
        pm_includes_sced=True
    )
    return {
        "person_months": round(pm, 2),
        "development_time_months": round(tdev, 2),
        "avg_team_size": round(pm / tdev, 2)
    }

# ─────────────────────────────────────────────────────────────
# Root
# ─────────────────────────────────────────────────────────────

@app.get("/")
def root():
    return {
        "message": "Welcome to COCOMO II Estimation API 🚀",
        "endpoints": [
            "/size/from_function_points",
            "/size/from_reuse",
            "/size/adjust_with_revl",
            "/estimate/effort_schedule"
        ]
    }
