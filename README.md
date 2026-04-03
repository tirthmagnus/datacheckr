# 🔍 Datacheckr

> **Production-grade Python data quality package** — plugs into any ETL pipeline to catch schema drift, null trends, and aggregate mismatches before they corrupt downstream BI reports or ML models.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Validation-150458?logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 🧭 Why Datacheckr?

In regulated industries like **financial services** and **insurance**, a single bad data load can trigger compliance failures, corrupt dashboards, or silently break ML models. Standard ETL pipelines have no built-in quality gate.

**Datacheckr** solves this by acting as an automated validation layer between your raw data source and your data warehouse — catching issues *before* they reach production.
```
Data Source → Extract → [Datacheckr Gate] → Transform → Load → BI / ML
                              ↓ FAIL
                        Alert + Pipeline Halt
                        (bad data never reaches warehouse)
```

---

## ✅ What It Detects

| Check | Description |
|---|---|
| 🔴 Missing Values | Detects nulls per column with % breakdown |
| 🔴 Duplicate Rows | Flags exact and near-duplicate records |
| 🟡 Schema Drift | Catches added, dropped, or retyped columns vs baseline |
| 🟡 Outliers | Z-score based anomaly detection per numeric column |
| 🟡 Low Variance | Flags columns with dominant single values (>90% one category) |
| 🟢 Type Validation | Validates dtypes against expected schema |
| 🟢 Auto-Fix Suggestions | Recommends fill strategy, type conversions, dedup actions |

---

## 📦 Installation
```bash
git clone https://github.com/tirthmagnus/datacheckr.git
cd datacheckr
pip install pandas numpy
```

---

## 🚀 Quick Start
```python
from datacheckr.validator import validate
import pandas as pd

df = pd.DataFrame({
    'customer_id': [101, 102, None, 102],
    'revenue':     [5000, None, 3200, 5000],
    'segment':     ['SMB', 'Enterprise', 'SMB', 'SMB']
})

expected_schema = {
    'customer_id': 'int64',
    'revenue':     'float64',
    'segment':     'object',
    'joined_date': 'datetime64[ns]'
}

validate(
    df,
    expected_schema=expected_schema,
    suggest_fixes=True,
    save_report=True
)
```

---

## 📊 Example Output
```
Running datacheckr on your DataFrame...

⚠️  Column 'customer_id' has 1 missing value (25.0%)
⚠️  Column 'revenue' has 1 missing value (25.0%)
❌  DataFrame has 1 duplicate row
📐  Column 'joined_date' missing from DataFrame — schema drift detected
🛠  Suggestion: Fill 'customer_id' with mode value 102
🛠  Suggestion: Fill 'revenue' with median value 4100.0
🛠  Suggestion: Drop 1 duplicate row
🛠  Suggestion: Convert 'customer_id' to int64

Report saved → datacheckr_report.txt
```

---

## 📂 Project Structure
```
datacheckr/
├── datacheckr/
│   ├── __init__.py
│   └── validator.py
├── tester.py
├── datacheckr_report.txt
└── README.md
```

---

## 🏭 Real-World Applications

- **Financial data pipelines** — catch null account IDs before P&L reports run
- **CRM integrations** — validate lead data before uploading to dialer or CRM
- **Insurance data compliance** — enforce schema contracts between source systems and warehouse
- **ML feature pipelines** — prevent silent data corruption from reaching model training

> 💡 Inspired by production data quality work at **ClearBizDebt** and **ISR Info Way**.

---

## 🗺️ Roadmap

- [ ] Export reports to `.xlsx` or styled HTML
- [ ] `apply_fixes=True` mode with full audit log
- [ ] Streamlit-based visual dashboard UI
- [ ] CLI: `python -m datacheckr file.csv`
- [ ] GitHub Actions integration for CI/CD pipelines

---

## 👤 Author

**Tirth Bhatt** — BI & Data Engineer
📍 New Jersey, USA
🔗 [LinkedIn](https://www.linkedin.com/in/tirthrajbhatt) · [Portfolio](https://tirthmagnus.github.io/) · [GitHub](https://github.com/tirthmagnus)

---

## 📄 License

MIT License
