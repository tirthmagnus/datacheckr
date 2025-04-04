
import pandas as pd
import numpy as np

def validate(
    df: pd.DataFrame,
    expected_schema: dict = None,
    suggest_fixes: bool = False,
    save_report: bool = False,
    report_name: str = "datacheckr_report.txt"
):
    messages = []
    messages.append("Running datacheckr on your DataFrame...\n")
    fix_suggestions = []

    # 1. Missing values
    nulls = df.isnull().sum()
    for col, count in nulls.items():
        if count > 0:
            percent = round((count / len(df)) * 100, 2)
            messages.append(f"⚠️  Column '{col}' has {count} missing values ({percent}%)")
            if suggest_fixes:
                fill_value = df[col].mean() if pd.api.types.is_numeric_dtype(df[col]) else df[col].mode().iloc[0]
                fix_suggestions.append(f"🛠 Suggestion: Fill {count} missing in '{col}' with '{fill_value}'")
        else:
            messages.append(f"✅ Column '{col}' has no missing values.")

    # 2. Duplicate rows
    messages.append("")
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        messages.append(f"❌ DataFrame has {duplicates} duplicate rows.")
        if suggest_fixes:
            fix_suggestions.append(f"🛠 Suggestion: Drop {duplicates} duplicate rows")
    else:
        messages.append("✅ No duplicate rows found.")

    # 3. Unique value check (categorical)
    messages.append("")
    for col in df.select_dtypes(include='object').columns:
        unique_vals = df[col].nunique()
        if unique_vals > 50:
            messages.append(f"⚠️  Column '{col}' has {unique_vals} unique values — might be noisy.")
        else:
            messages.append(f"✅ Column '{col}' has {unique_vals} unique values.")

    # 4. Outliers (z-score for numerics)
    messages.append("")
    for col in df.select_dtypes(include=np.number).columns:
        z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
        outliers = (z_scores > 3).sum()
        if outliers > 0:
            messages.append(f"⚠️  Column '{col}' has {outliers} possible outliers (z > 3)")
        else:
            messages.append(f"✅ Column '{col}' has no strong outliers")

    # 5. Column Summary
    messages.append("")
    messages.append("📊 Column Summary:")
    for col in df.columns:
        dtype = str(df[col].dtype)
        unique_vals = df[col].nunique()
        percent_missing = round((df[col].isnull().sum() / len(df)) * 100, 2)
        messages.append(f"🧾 '{col}': dtype={dtype}, missing={percent_missing}%, unique={unique_vals}")

    # 6. Schema check
    if expected_schema:
        messages.append("")
        messages.append("📐 Schema Validation:")
        actual_cols = df.columns.tolist()
        for col, expected_dtype in expected_schema.items():
            if col not in actual_cols:
                messages.append(f"❌ Column '{col}' is missing from DataFrame.")
            else:
                actual_dtype = str(df[col].dtype)
                if actual_dtype != expected_dtype:
                    messages.append(f"⚠️  Column '{col}' has dtype '{actual_dtype}', expected '{expected_dtype}'")
                    if suggest_fixes:
                        fix_suggestions.append(f"🛠 Suggestion: Convert '{col}' to {expected_dtype}")
                else:
                    messages.append(f"✅ Column '{col}' matches expected type '{expected_dtype}'")

    # 7. Auto-fix suggestions
    if suggest_fixes and fix_suggestions:
        messages.append("")
        messages.append("🛠 Auto-Fix Suggestions:")
        messages.extend(fix_suggestions)

    # 8. Final output
    report = "\n".join(messages)
    print(report)

    if save_report:
        with open(report_name, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\n📄 Report saved to '{report_name}'")
