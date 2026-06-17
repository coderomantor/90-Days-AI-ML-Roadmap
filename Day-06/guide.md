# Day 06 — Exploratory Data Analysis (EDA) Guide

## 1. What I Revised / Learned Today

Day 06 focused on Exploratory Data Analysis. I practiced dataset overview, missing value checks, duplicate checks, visualizations, correlation analysis, and writing final insights.

## 2. Why This Topic Matters

EDA matters because machine learning starts with understanding data. Before training a model, I need to know whether the dataset is clean, reliable, balanced, and meaningful.

## 3. Core Concepts

EDA means exploring a dataset before making decisions or building models.

Dataset overview uses `head()`, `shape`, `info()`, and `describe()`.

Missing values show where data is incomplete.

Duplicate records can distort analysis.

Univariate analysis studies one column at a time.

Bivariate analysis studies relationships between two columns.

Outlier detection helps identify unusual values.

Correlation analysis shows relationships between numeric columns.

## 4. Practical Examples

```python
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
```

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(data=df, x="Salary", bins=6)
plt.title("Salary Distribution")
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
```

## 5. Project Connection

The Employee Data Analysis Report creates an employee dataset, checks data quality, saves EDA charts, and prints final insights. The project connects Pandas summaries with Matplotlib and Seaborn visualizations.

## 6. Common Mistakes

- Creating charts without asking a clear question.
- Ignoring missing values or duplicates.
- Treating correlation as causation.
- Removing outliers without investigation.
- Not writing final insights after creating charts.
- Jumping to model training before understanding the dataset.

## 7. Interview-Style Questions

1. What is EDA?
   EDA is the process of exploring data before analysis or modeling.
2. Why do EDA before ML?
   It helps find data quality issues and useful patterns.
3. What does `df.info()` show?
   Column names, data types, and non-null counts.
4. What does a histogram show?
   Distribution of a numeric column.
5. What does a boxplot show?
   Spread and possible outliers.
6. What does a heatmap show?
   Numeric relationships such as correlation.
7. Why write insights?
   Insights explain what the charts and summaries mean.

## 8. Day Checklist

- [ ] Preview data with `head()`
- [ ] Check shape, info, and summary statistics
- [ ] Check missing values
- [ ] Check duplicate records
- [ ] Create useful visualizations
- [ ] Analyze outliers and correlations
- [ ] Write final insights

## 9. Final Takeaway

EDA turns raw data into understanding. A good AI/ML workflow starts by inspecting, visualizing, and explaining the dataset before modeling.
