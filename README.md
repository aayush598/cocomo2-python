# 📊 COCOMO II Post-Architecture Estimation Tool

This project implements the **COCOMO II.2000 Post-Architecture** model in Python, providing accurate estimations of:

- 📈 Effort (Person-Months)
- 📆 Schedule (Time to Develop in Months)
- 👥 Team Size
- 🔁 Adaptation & Reuse effort
- 📐 Sizing via KSLOC or Function Points

---

## 🧠 What is COCOMO II?

**COCOMO II (Constructive Cost Model)** is a software cost estimation model developed by Barry Boehm and others. It’s widely used to estimate effort, cost, and schedule when planning software development.

This implementation is based on:
> **COCOMO II.2000 Model Definition Manual**  
> Version 2.1 (2000) – USC Center for Software Engineering

---

## 📁 Folder Structure

```

cocomo2\_project/
├── cocomo/
│   ├── constants.py        # All official model constants (A, B, C, D, EMs, SFs)
│   ├── effort.py           # Effort estimation model (Eq. 11, 12)
│   ├── reuse.py            # Adaptation effort, ESLOC calculation (Eq. 4–6)
│   ├── schedule.py         # Development time estimation (Eq. 14)
│   ├── sizing.py           # KSLOC / Function Point sizing, REVL adjustment
│   └── **init**.py
│
├── tests/                  # ✅ Pytest unit tests
│   ├── test\_effort.py
│   ├── test\_schedule.py
│   ├── test\_sizing.py
│   └── **init**.py
│
├── main.py                 # 🎯 CLI-based Estimator
├── requirements.txt        # Optional: for virtualenv
└── README.md               # 👋 You are here

````

---

## 🚀 Features

- [x] Support for both **KSLOC** and **Function Points**
- [x] **Reuse and Adaptation** model with AAF & AAM
- [x] Full support for all **17 Effort Multipliers** and **5 Scale Factors**
- [x] Schedule estimation using SCED compression/extension
- [x] REVL (%) for volatility/evolution adjustment
- [x] Test suite using `pytest`

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/cocomo2_project.git
cd cocomo2_project
````

### 2. Create & activate virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If no `requirements.txt`, install `pytest`:

```bash
pip install pytest
```

---

## 🧪 Run the Estimator

```bash
python main.py
```

You’ll be prompted to enter:

* KSLOC or Function Point data
* Optional reused code inputs (ASLOC, DM, CM, etc.)
* REVL %, SCED rating

📦 Outputs:

* Person-Months (PM)
* Development Time (TDEV)
* Average Team Size

---

## ✅ Run the Test Suite

```bash
pytest tests/
```

---

## 📊 Example Output

```
──────────────── Estimation Summary ────────────────
Total SLOC (after REVL):     7,700
Effort (Person-Months):      465.32
Development Time (Months):   19.81
Average Team Size:           23.49
────────────────────────────────────────────────────
```

---

## 🛠 Future Improvements

* [ ] GUI with `streamlit` or `tkinter`
* [ ] Save/load project profiles (JSON)
* [ ] Interactive rating selection for all EMs/SFs
* [ ] Export to Excel/CSV
* [ ] Web dashboard (Flask/FastAPI)

---

## 📚 References

* [COCOMO II.2000 Manual PDF (v2.1)](https://csse.usc.edu/tools/COCOMOII/cocomo.html)
* Barry Boehm et al., USC Center for Software Engineering

---

## 👨‍💻 Author

**Aayush Gid**
B.Tech ECE | Embedded & AI Systems
[GitHub](https://github.com/aayush598)

---

## 📝 License

This project is licensed under the **MIT License**.
