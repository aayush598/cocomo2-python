# 🚀 COCOMO II Post-Architecture Estimation API (FastAPI)

A complete Python implementation of the **COCOMO II.2000 Post-Architecture** model wrapped in a powerful REST API using FastAPI. This tool lets you estimate:

- 📈 Effort (Person-Months)
- 📆 Schedule (TDEV)
- 👥 Team Size
- 🔁 Equivalent SLOC from Reuse (ESLOC)
- 📐 New SLOC from Function Points

---

## 🧠 What is COCOMO II?

> **COCOMO II** (Constructive Cost Model) is a widely accepted software estimation model developed by Barry Boehm.  
> The Post-Architecture model uses effort multipliers, scale factors, and project sizing (KSLOC/Function Points) to estimate total effort and schedule.

This project is based on the official:
> 📘 **COCOMO II.2000 Model Definition Manual** (v2.1) – USC Center for Software Engineering

---

## 📁 Project Structure

```

cocomo2\_project/
├── cocomo/
│   ├── constants.py         # Constants for EMs, SFs, A/B/C/D
│   ├── effort.py            # Effort = A \* (KSLOC)^E \* ΠEM
│   ├── schedule.py          # TDEV = C \* PM^exponent
│   ├── reuse.py             # Adaptation Model (Eq. 4–6)
│   ├── sizing.py            # UFP → SLOC, REVL support
│   └── **init**.py
│
├── main.py                  # FastAPI App (this is your backend service)
├── tests/                   # Pytest test suite
├── requirements.txt
└── README.md                # 📘 You're reading it!

````

---

## ⚙️ Setup Instructions

### 1. Clone and enter the repo

```bash
git clone https://github.com/aayush598/cocomo2-python.git
cd cocomo2-python
````

### 2. Create a virtual environment and activate

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install fastapi uvicorn pydantic pytest
```

---

## 🚀 Run the API Server

```bash
uvicorn main:app --reload
```

Visit the docs at:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📘 API Endpoints

---

### ✅ `GET /`

Health check and welcome message.

**Response:**

```json
{
  "message": "Welcome to COCOMO II Estimation API 🚀",
  "endpoints": [
    "/size/from_function_points",
    "/size/from_reuse",
    "/size/adjust_with_revl",
    "/estimate/effort_schedule"
  ]
}
```

---

### 📐 `POST /size/from_function_points`

Convert Function Points to SLOC.

**Request:**

```json
{
  "fp_items": [
    { "fp_type": "ILF", "det": 25, "ftr_or_ret": 3 },
    { "fp_type": "EI",  "det": 10, "ftr_or_ret": 2 }
  ],
  "language": "Java"
}
```

**Response:**

```json
{
  "ufp": 14,
  "sloc": 742
}
```

---

### 🔁 `POST /size/from_reuse`

Compute **Equivalent SLOC** (ESLOC) from adapted source code using reuse/adaptation effort model.

**Request:**

```json
{
  "asloc": 3000,
  "dm": 10,
  "cm": 15,
  "im": 5,
  "su_rating": "N",
  "aa_rating": "2",
  "unfm_rating": "SF",
  "at": 10
}
```

**Response:**

```json
{
  "esloc": 3090.6
}
```

---

### 🧮 `POST /size/adjust_with_revl`

Apply REVL (Requirements Evolution and Volatility) to total SLOC.

**Request:**

```json
{
  "new_sloc": 5000,
  "adapted_esloc": 3000,
  "revl_percent": 10
}
```

**Response:**

```json
{
  "sloc_total": 8000.0,
  "sloc_after_revl": 8800.0
}
```

---

### 🧠 `POST /estimate/effort_schedule`

Calculate **Effort (PM)** and **Schedule (TDEV)** from total size.

Uses default nominal values for all 17 Effort Multipliers and 5 Scale Factors.

**Request:**

```json
{
  "sloc_ksloc": 8.8,
  "sced_rating": "N"
}
```

**Response:**

```json
{
  "person_months": 41.38,
  "development_time_months": 17.28,
  "avg_team_size": 2.39
}
```

---

## ✅ Run Unit Tests

```bash
pytest tests/
```

Includes tests for:

* Sizing (UFP, SLOC, REVL)
* Reuse calculation
* Effort and schedule estimation

---

## 📚 Reference

* [COCOMO II Official Site](https://csse.usc.edu/tools/COCOMOII/cocomo.html)
* Barry Boehm et al., USC Center for Software and Systems Engineering

---

## 👤 Author

**Aayush Gid**
B.Tech ECE | Embedded & AI Systems Engineer
[GitHub: @aayush598](https://github.com/aayush598)

---

## 📝 License

This project is licensed under the **MIT License**.
