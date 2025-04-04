import sys
sys.path.append(r"C:\Users\Owner\Desktop\datacheckr")  # adjust if needed

from datacheckr.validator import validate
import pandas as pd

data = {
    'name': ['Alice', 'Bob', None, 'Bob'],
    'age': [25, None, 30, 25],
    'city': ['NY', 'LA', 'LA', 'NY']
}
df = pd.DataFrame(data)

expected_schema = {
    'name': 'object',
    'age': 'int64',
    'city': 'object',
    'joined_date': 'datetime64[ns]'  # intentional missing column
}

validate(df, expected_schema=expected_schema, suggest_fixes=True, save_report=True)
