# 🧪 Datacheckr

**datacheckr** is a lightweight, developer-friendly Python package for performing fast, flexible, and professional-grade validation on `pandas` DataFrames.

It detects common data quality issues like missing values, duplicates, outliers, and schema mismatches — and even suggests smart fixes. Perfect for analysts, engineers, and QA teams.

---

## 🚀 Features

- ✅ Detect missing values and calculate % per column  
- ✅ Identify duplicate rows  
- ✅ Flag noisy categorical columns (too many unique values)  
- ✅ Detect outliers using z-scores  
- ✅ Validate schema (expected columns and data types)  
- ✅ Summarize each column (dtype, % missing, unique count)  
- ✅ Suggest intelligent auto-fixes (fill nulls, convert types, drop dupes)  
- ✅ Save report to `.txt` for sharing or documentation  
- ✅ Easily embeddable in pipelines or Jupyter notebooks

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/datacheckr.git
cd datacheckr
```

---

## 🧑‍💻 Usage

```python
from datacheckr.validator import validate
import pandas as pd

# Sample data
data = {
    'name': ['Alice', 'Bob', None, 'Bob'],
    'age': [25, None, 30, 25],
    'city': ['NY', 'LA', 'LA', 'NY']
}
df = pd.DataFrame(data)

# Optional: Define expected schema
expected_schema = {
    'name': 'object',
    'age': 'int64',
    'city': 'object',
    'joined_date': 'datetime64[ns]'
}

# Run datacheckr
validate(
    df,
    expected_schema=expected_schema,
    suggest_fixes=True,
    save_report=True
)
```

> This will print a full validation report in the terminal and save it to `datacheckr_report.txt`.

---

## 📊 Example Output

```
Running datacheckr on your DataFrame...

⚠️  Column 'name' has 1 missing values (25.0%)
❌ DataFrame has 1 duplicate rows.
⚠️  Column 'status' has 91% value 'active' — low variance
✅ Column 'age' has no strong outliers
📐 Column 'joined_date' is missing from DataFrame
🛠 Suggestion: Fill 'name' with most common value 'Bob'
🛠 Suggestion: Drop 1 duplicate row
🛠 Suggestion: Convert 'age' to 'int64'
```

---

## 📂 Folder Structure

```
datacheckr/
├── datacheckr/
│   ├── __init__.py
│   └── validator.py
├── tester.py
└── README.md
```

---

## 📌 Roadmap

- [ ] Export to `.xlsx` or styled HTML  
- [ ] Add `apply_fixes=True` mode (with logs)  
- [ ] Streamlit-based visual UI  
- [ ] CLI usage: `python -m datacheckr file.csv`  
- [ ] GitHub Actions integration  

---

## 🤝 Contributing

Pull requests are welcome!  
If you’ve got a cool check idea or enhancement, submit an issue or PR. Let’s make `datacheckr` smarter together.

---

## 📄 License

MIT License

---
---
Built with ❤️ by [Tirth Bhatt](https://github.com/tirthmagnus)
