
---

# Day 02 — 2D NumPy Arrays and Pandas DataFrames Guide

## 1. What I Revised / Learned Today

Day 02 focused on 2D NumPy arrays and an introduction to Pandas DataFrames. I practiced representing student performance data in table form and explored basic column operations.

## 2. Why This Topic Matters

Most real AI/ML datasets are tabular. Pandas DataFrames make it easier to inspect, clean, transform, and analyze rows and columns before model training.

## 3. Core Concepts

A 2D NumPy array stores data in rows and columns.

A Pandas DataFrame is a table-like structure with labeled rows and columns.

Columns usually represent features. Rows usually represent records.

`axis=0` means working down rows by column. `axis=1` means working across columns by row.

## 4. Practical Examples

```python
import pandas as pd

df = pd.DataFrame({
    "Student": ["Ali", "Sara", "Ahmed"],
    "Math": [80, 90, 75],
    "Science": [85, 88, 70],
})

df["Average"] = df[["Math", "Science"]].mean(axis=1)
print(df)
```

## 5. Project Connection

The Student Performance Analyzer uses NumPy and Pandas to create a student DataFrame, calculate totals or averages, and explore tabular data. This mirrors the first steps of many data analysis workflows.

## 6. Common Mistakes

- Confusing rows and columns.
- Misunderstanding `axis=0` and `axis=1`.
- Forgetting that DataFrames can hold different column types.
- Creating new columns without checking the result.
- Not using clear column names.

## 7. Interview-Style Questions

1. What is a DataFrame?
   A table-like data structure with rows and columns.
2. What does `axis=0` mean?
   Operations down rows for each column.
3. What does `axis=1` mean?
   Operations across columns for each row.
4. Why is Pandas useful?
   It makes tabular data analysis easier.
5. What is a feature column?
   An input column that describes each record.

## 8. Day Checklist

- [ ] Create a DataFrame
- [ ] Understand rows and columns
- [ ] Calculate a new column
- [ ] Explain `axis=0` and `axis=1`
- [ ] Run the Student Performance Analyzer project

## 9. Final Takeaway

Pandas DataFrames are essential for turning raw tabular data into something that can be explored, cleaned, and prepared for machine learning.
