# Day 06 — Exploratory Data Analysis (EDA) Guide

This guide summarizes my Day 06 learning on Exploratory Data Analysis as part of the 90 Days AI/ML Engineer Roadmap.

The goal is simple: learn how to understand a dataset before making decisions or building a machine learning model.

## What is EDA?

Exploratory Data Analysis, or EDA, is the process of inspecting, cleaning, summarizing, and visualizing data before deeper analysis or machine learning.

EDA helps answer questions like:

- What columns and rows are in the dataset?
- Which columns are numeric and which are categorical?
- Are there missing values?
- Are there duplicate records?
- Are there outliers?
- What patterns or relationships can be seen?
- What useful conclusions can be written from the data?

EDA is not only about making charts. It is about understanding the data clearly enough to explain it.

## Why EDA matters before Machine Learning

Machine learning models learn from data. If the data has missing values, duplicate records, wrong data types, or unusual outliers, the model can learn poor patterns.

EDA matters because it helps an AI/ML engineer:

- Check data quality before model training
- Understand feature distributions
- Find missing or duplicated records
- Detect possible outliers
- Discover relationships between variables
- Decide what cleaning or preprocessing is needed next
- Explain the dataset in simple language

Before using `model.fit()`, I should first understand the data.

## EDA workflow

A beginner-friendly EDA workflow can look like this:

1. Load or create the dataset
2. Preview rows and columns
3. Check shape, data types, and summary statistics
4. Check missing values
5. Check duplicate records
6. Analyze one variable at a time
7. Analyze relationships between variables
8. Check outliers
9. Analyze correlations between numeric columns
10. Create useful visualizations
11. Write clear insights and next steps

Example setup:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
```

## Dataset overview using `head()`, `shape`, `info()`, `describe()`

The first step in EDA is understanding the basic structure of the dataset.

### `head()`

`head()` shows the first few rows.

```python
df.head()
```

Use this to quickly see column names, example values, and whether the dataset loaded correctly.

### `shape`

`shape` shows the number of rows and columns.

```python
df.shape
```

Example meaning:

- Rows: records or observations
- Columns: features or variables

### `info()`

`info()` shows column names, non-null counts, and data types.

```python
df.info()
```

This helps identify:

- Missing values
- Numeric columns
- Text/category columns
- Data type issues

### `describe()`

`describe()` gives summary statistics for numeric columns.

```python
df.describe()
```

It usually shows:

- Count
- Mean
- Standard deviation
- Minimum value
- Quartiles
- Maximum value

These values help understand the range and spread of numeric data.

## Missing values

Missing values are empty or unknown values in a dataset. In Pandas, they often appear as `NaN`.

Check missing values:

```python
df.isnull().sum()
```

Missing values matter because they can affect analysis, charts, and machine learning models.

Common ways to handle missing values:

- Fill numeric values with mean or median
- Fill categorical values with mode
- Remove rows if very few values are missing
- Investigate why the values are missing

Example:

```python
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
```

Do not fill missing values blindly. First understand why they are missing.

## Duplicate records

Duplicate records happen when the same row appears more than once.

Check duplicates:

```python
df.duplicated().sum()
```

View duplicate rows:

```python
df[df.duplicated()]
```

Remove duplicates:

```python
df = df.drop_duplicates()
```

Duplicates can make analysis misleading because repeated records may be counted more than once.

## Univariate analysis

Univariate analysis means analyzing one variable at a time.

For numeric columns, I can check:

- Minimum and maximum values
- Mean and median
- Distribution
- Outliers

Example:

```python
df["Salary"].describe()
```

For categorical columns, I can check how often each category appears.

```python
df["Department"].value_counts()
```

Useful questions:

- What is the most common department?
- What is the average salary?
- Are values balanced or skewed?
- Are there unusual values?

## Bivariate analysis

Bivariate analysis means analyzing the relationship between two variables.

Examples:

- Salary vs experience
- Department vs average salary
- Age vs performance score
- Training hours vs performance score

GroupBy example:

```python
df.groupby("Department")["Salary"].mean()
```

Scatterplot example:

```python
sns.scatterplot(data=df, x="Experience", y="Salary")
plt.title("Experience vs Salary")
plt.xlabel("Experience in Years")
plt.ylabel("Salary")
plt.show()
```

Useful questions:

- Does salary increase with experience?
- Which department has the highest average salary?
- Do two numeric columns show a visible relationship?

## Outlier detection

Outliers are values that are much higher or lower than most other values.

Outliers can be:

- Data entry mistakes
- Rare but valid cases
- Important signals

Use `describe()` to inspect possible outliers:

```python
df["Salary"].describe()
```

Use a boxplot:

```python
sns.boxplot(data=df, x="Salary")
plt.title("Salary Outlier Check")
plt.xlabel("Salary")
plt.show()
```

Important habit: do not remove outliers automatically. First investigate whether they are errors or meaningful rare cases.

## Correlation analysis

Correlation shows how strongly numeric columns are related.

Create a correlation matrix:

```python
numeric_columns = ["Age", "Salary", "Experience", "PerformanceScore"]
correlation_matrix = df[numeric_columns].corr()
```

Create a heatmap:

```python
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
```

Correlation values usually range from `-1` to `1`.

- Close to `1`: strong positive relationship
- Close to `-1`: strong negative relationship
- Close to `0`: weak or no linear relationship

Important: correlation does not prove causation. It only shows a relationship between numeric columns.

## Useful visualizations: histogram, boxplot, scatterplot, countplot, heatmap

### Histogram

A histogram shows the distribution of a numeric column.

```python
sns.histplot(data=df, x="Salary", bins=6, kde=True)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.show()
```

Use it to answer: How are values spread?

### Boxplot

A boxplot shows spread, median, quartiles, and possible outliers.

```python
sns.boxplot(data=df, x="Salary")
plt.title("Salary Outlier Check")
plt.xlabel("Salary")
plt.show()
```

Use it to answer: Are there unusual values?

### Scatterplot

A scatterplot compares two numeric columns.

```python
sns.scatterplot(data=df, x="Experience", y="Salary", hue="Department")
plt.title("Experience vs Salary")
plt.xlabel("Experience in Years")
plt.ylabel("Salary")
plt.show()
```

Use it to answer: Do two numeric variables have a relationship?

### Countplot

A countplot shows how many records belong to each category.

```python
sns.countplot(data=df, x="Department")
plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.show()
```

Use it to answer: Which categories appear most often?

### Heatmap

A heatmap is useful for visualizing correlations.

```python
sns.heatmap(df[["Age", "Salary", "Experience"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
```

Use it to answer: Which numeric features are related?

## Chart selection guide

| Question | Useful Chart |
| --- | --- |
| How is one numeric column distributed? | Histogram |
| Are there possible outliers? | Boxplot |
| How many records are in each category? | Countplot |
| How do two numeric columns relate? | Scatterplot |
| Which numeric columns are correlated? | Heatmap |
| Which category has the highest average value? | Bar chart or grouped summary |

The best chart depends on the question. Start with the question first, then choose the chart.

## Common EDA mistakes

Common beginner mistakes:

- Creating charts without asking a clear question
- Ignoring missing values
- Ignoring duplicate records
- Looking only at averages and not distributions
- Removing outliers without investigation
- Treating correlation as causation
- Using too many colors or unclear chart labels
- Not writing insights after creating charts
- Jumping to machine learning before understanding the dataset

A good EDA notebook or report should explain what was found, not only show code.

## Mini project connection: Employee Data Analysis Report

In the Day 06 mini project, I built an Employee Data Analysis Report using Pandas, Matplotlib, and Seaborn.

Project file:

- [project/employee_eda_report.py](project/employee_eda_report.py)

The project performs these EDA steps:

- Creates an employee dataset
- Prints the first rows using `head()`
- Checks dataset shape
- Reviews data types using `info()`
- Generates summary statistics using `describe()`
- Checks missing values
- Checks duplicate rows
- Saves a salary distribution histogram
- Saves a salary outlier boxplot
- Saves an experience vs salary scatterplot
- Saves a correlation heatmap
- Saves a department distribution countplot
- Prints final insights and conclusions

Saved visualizations:

- [screenshots/salary_distribution.png](screenshots/salary_distribution.png)
- [screenshots/salary_outliers_boxplot.png](screenshots/salary_outliers_boxplot.png)
- [screenshots/experience_vs_salary.png](screenshots/experience_vs_salary.png)
- [screenshots/correlation_heatmap.png](screenshots/correlation_heatmap.png)
- [screenshots/department_distribution.png](screenshots/department_distribution.png)

This project helped me understand that EDA is a practical workflow, not a single command.

## Interview-style questions

1. What is Exploratory Data Analysis?
2. Why should EDA be done before machine learning?
3. What is the difference between `head()`, `info()`, and `describe()`?
4. How do you check missing values in Pandas?
5. Why can duplicate records be a problem?
6. What is univariate analysis?
7. What is bivariate analysis?
8. What does a histogram show?
9. What does a boxplot help detect?
10. What does a scatterplot show?
11. What does a countplot show?
12. What does a correlation heatmap show?
13. Why does correlation not prove causation?
14. Why should outliers be investigated before removing them?
15. Why is it important to write insights after charts?

## Day 06 checklist

Use this checklist when practicing EDA:

- [ ] Load or create the dataset
- [ ] Preview the first rows with `head()`
- [ ] Check rows and columns with `shape`
- [ ] Review data types with `info()`
- [ ] Review summary statistics with `describe()`
- [ ] Check missing values
- [ ] Check duplicate records
- [ ] Analyze numeric columns
- [ ] Analyze categorical columns
- [ ] Create useful visualizations
- [ ] Check outliers
- [ ] Analyze correlations
- [ ] Write final insights
- [ ] Save charts or outputs for documentation

## Final takeaway

EDA is the bridge between raw data and machine learning.

Before training a model, I need to understand the dataset, check its quality, visualize important patterns, and write clear conclusions. Good EDA makes later machine learning work more reliable and easier to explain.
