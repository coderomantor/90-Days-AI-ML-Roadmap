
---

# Day 03 — Pandas Data Cleaning and Filtering Guide

## 1. What I Revised / Learned Today

Day 03 focused on cleaning and filtering data with Pandas. I practiced missing values, data types, duplicate detection, value counts, grouping, filtering, and sorting.

## 2. Why This Topic Matters

Real-world datasets are rarely clean. Before analysis or machine learning, an AI/ML engineer must check missing values, duplicates, incorrect types, and unreliable records.

## 3. Core Concepts

Missing values are unknown or empty values, often shown as `NaN`.

Filtering selects rows that match a condition.

Duplicate detection checks whether records are repeated.

Value counts summarize category frequency.

GroupBy summarizes data by category.

Sorting organizes rows for easier inspection.

## 4. Practical Examples

```python
missing = df.isnull().sum()
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

high_salary = df[df["Salary"] > 55000]
department_salary = df.groupby("Department")["Salary"].mean()
```

## 5. Project Connection

The Employee Data Analyzer creates an employee dataset, fills missing values, checks duplicates, filters salary values, and summarizes salary by department. This is a practical first data-cleaning workflow.

## 6. Common Mistakes

- Filling missing values without understanding why they are missing.
- Ignoring duplicate rows.
- Filtering with the wrong comparison operator.
- Grouping data without checking category names.
- Sorting data but forgetting whether ascending or descending is needed.

## 7. Interview-Style Questions

1. How do you check missing values?
   Use `df.isnull().sum()`.
2. What does `fillna()` do?
   It fills missing values.
3. Why check duplicates?
   Duplicate records can distort analysis.
4. What does `value_counts()` show?
   Frequency of each category.
5. What does `groupby()` do?
   It summarizes data by groups.

## 8. Day Checklist

- [ ] Detect missing values
- [ ] Fill missing numeric values
- [ ] Check duplicates
- [ ] Filter rows
- [ ] Use value counts
- [ ] Use GroupBy summaries
- [ ] Sort records

## 9. Final Takeaway

Data cleaning is one of the most important habits in AI/ML because model quality depends heavily on data quality.
