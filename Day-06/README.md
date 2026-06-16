# Day 06: Exploratory Data Analysis (EDA)

## Goal

Learn how to explore a dataset before making decisions or building machine learning models.

Day 05 focused on Seaborn visualizations. Day 06 combines Pandas summaries, missing value checks, duplicate checks, visualizations, and written conclusions into a simple EDA workflow.

For a deeper concept explanation, see the [Day 06 EDA Guide](guide.md).

## Topics Covered

- Exploratory Data Analysis (EDA)
- Dataset overview
- Missing value checks
- Duplicate row checks
- Summary statistics
- Salary distribution
- Outlier understanding
- Correlation analysis
- Department distribution
- Final insights and conclusions

## Learning Objectives

- Create an employee dataset using Pandas
- Inspect the first rows using `head()`
- Check dataset shape
- Review column information using `info()`
- Understand summary statistics using `describe()`
- Check missing values and duplicate rows
- Create visualizations with Matplotlib and Seaborn
- Save EDA charts as PNG files
- Write simple final insights from the analysis

## Concepts Learned

### Exploratory Data Analysis

Exploratory Data Analysis means understanding a dataset before deeper analysis or machine learning.

EDA helps answer questions like:

- How many rows and columns are in the dataset?
- Are there missing values?
- Are there duplicate records?
- What do numeric columns look like?
- Are there visible patterns or relationships?

### Dataset Overview

The first step in EDA is checking the basic structure of the data.

```python
df.head()
df.shape
df.info()
df.describe()
```

These methods help understand the data before applying charts or models.

### Missing Values

Missing values can affect analysis and model training.

```python
df.isnull().sum()
```

This shows how many missing values exist in each column.

### Duplicate Rows

Duplicate rows can make analysis misleading because the same record may be counted more than once.

```python
df.duplicated().sum()
```

This counts duplicate rows in the dataset.

### Distribution

A distribution shows how values are spread.

In this project, a salary histogram shows whether salaries are low, high, or balanced across employees.

### Outliers

Outliers are values that are much higher or lower than most other values.

A boxplot helps inspect possible salary outliers.

### Correlation

Correlation shows how strongly numeric columns are related.

In this project, the heatmap compares age, salary, experience, performance score, and training hours.

## Mini Project: Employee Data Analysis Report

The project creates an employee dataset and performs a beginner-friendly EDA workflow.

The project includes:

- Dataset overview using `head()`, `info()`, `shape`, and `describe()`
- Missing value check
- Duplicate row check
- Salary distribution histogram
- Salary outlier boxplot
- Experience vs salary scatterplot
- Correlation heatmap
- Department countplot
- Final printed insights and conclusions

## Project Structure

```text
Day-06/
├── README.md
├── resources.md
├── project/
│   ├── employee_eda_report.py
│   └── requirements.txt
└── screenshots/
```

## How To Run

From the `Day-06/project/` folder:

```bash
pip install -r requirements.txt
python employee_eda_report.py
```

## Output

The project saves the following charts:

- [screenshots/salary_distribution.png](screenshots/salary_distribution.png)
- [screenshots/salary_outliers_boxplot.png](screenshots/salary_outliers_boxplot.png)
- [screenshots/experience_vs_salary.png](screenshots/experience_vs_salary.png)
- [screenshots/correlation_heatmap.png](screenshots/correlation_heatmap.png)
- [screenshots/department_distribution.png](screenshots/department_distribution.png)

The project also prints dataset summaries and final insights in the terminal.

## Skills Demonstrated

- Creating Pandas DataFrames
- Performing beginner-friendly EDA
- Checking dataset shape, info, and summary statistics
- Detecting missing values and duplicates
- Creating histograms, boxplots, scatterplots, heatmaps, and countplots
- Saving chart images for GitHub documentation
- Writing simple insights from data
- Preparing data understanding before machine learning

## Real-World Applications

EDA is used in almost every data science and machine learning project.

Examples:

- Understanding HR, sales, finance, or student datasets
- Checking data quality before model training
- Finding missing values, duplicates, and possible outliers
- Discovering relationships between features
- Creating simple reports for teams and stakeholders

## Key Takeaway

EDA helps turn a dataset from unknown raw data into something understandable. Before building a machine learning model, an AI/ML engineer should inspect the data, visualize patterns, and write clear observations.

## Interview Questions

1. What is Exploratory Data Analysis?
2. Why should EDA be done before machine learning?
3. What does `df.head()` show?
4. What does `df.info()` help you understand?
5. Why do we check missing values?
6. What does a boxplot show?
7. Why is a correlation heatmap useful?

## Reflection

Today I learned how to combine data inspection, visualizations, and written insights into one EDA workflow. I also learned that EDA is not just about creating charts. It is about asking simple questions, checking data quality, and understanding patterns before making decisions.

This project helped me see how Pandas, Matplotlib, and Seaborn work together in a real analysis workflow.

## Next Step

Continue to Day 07 and review Week 1 concepts, practice interview questions, and summarize the first week of learning.
