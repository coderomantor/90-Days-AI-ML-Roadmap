# Day 05: Seaborn Fundamentals for Data Visualization

## Goal

Learn how to create cleaner statistical visualizations using Seaborn with Pandas and Matplotlib.

Day 04 introduced Matplotlib for basic charts. Day 05 builds on that by using Seaborn to create more polished visualizations for salary patterns, distributions, relationships, and correlations.

For structured learning notes, see the [Day 05 Guide](guide.md).

## Topics Covered

- Seaborn basics
- Bar plots
- Histograms
- Box plots
- Scatter plots
- Correlation heatmaps
- Pandas DataFrames
- Matplotlib chart saving

## Learning Objectives

- Create an employee dataset using Pandas
- Use Seaborn to compare average salary by department
- Visualize salary distribution with a histogram
- Use a boxplot to understand salary spread and possible outliers
- Use a scatterplot to compare experience and salary
- Create a heatmap to inspect correlation between numeric columns
- Add clear titles, labels, and clean formatting
- Save all chart images in the `screenshots/` folder

## Concepts Learned

### Seaborn

Seaborn is a Python library built on top of Matplotlib. It helps create cleaner and more statistical-looking charts with less code.

```python
import seaborn as sns
```

Seaborn is especially useful for exploring relationships, distributions, and correlations in datasets.

### Barplot

A barplot compares values across categories.

```python
sns.barplot(data=df, x="Department", y="Salary")
```

In this project, the barplot shows average salary by department.

### Histogram

A histogram shows the distribution of numeric data.

```python
sns.histplot(data=df, x="Salary", bins=6)
```

In this project, the histogram shows how employee salaries are spread across different ranges.

### Boxplot

A boxplot shows the spread of data and can help identify possible outliers.

```python
sns.boxplot(data=df, x="Department", y="Salary")
```

In this project, the boxplot compares salary spread across departments.

### Scatterplot

A scatterplot shows the relationship between two numeric columns.

```python
sns.scatterplot(data=df, x="Experience", y="Salary")
```

In this project, the scatterplot shows how experience relates to salary.

### Correlation Heatmap

A correlation heatmap shows how strongly numeric columns are related to each other.

```python
sns.heatmap(df.corr(numeric_only=True), annot=True)
```

This is useful before machine learning because it helps identify relationships between features.

## Mini Project: Employee Insights Dashboard

The project creates a small employee dataset and generates five Seaborn visualizations:

- Average salary by department
- Salary distribution
- Salary spread by department
- Experience vs salary
- Correlation heatmap

Each chart is saved as a PNG file inside the `screenshots/` folder.

## Project Structure

```text
Day-05/
├── README.md
├── resources.md
├── project/
│   ├── employee_insights_dashboard.py
│   └── requirements.txt
└── screenshots/
```

## How To Run

From the `Day-05/project/` folder:

```bash
pip install -r requirements.txt
python employee_insights_dashboard.py
```

## Output

The project saves the following charts:

- [screenshots/average_salary_by_department.png](screenshots/average_salary_by_department.png)
- [screenshots/salary_distribution.png](screenshots/salary_distribution.png)
- [screenshots/salary_spread_by_department.png](screenshots/salary_spread_by_department.png)
- [screenshots/experience_vs_salary.png](screenshots/experience_vs_salary.png)
- [screenshots/numeric_correlation_heatmap.png](screenshots/numeric_correlation_heatmap.png)

## Skills Demonstrated

- Creating Pandas DataFrames
- Using Seaborn for statistical visualization
- Creating barplots, histograms, boxplots, scatterplots, and heatmaps
- Understanding salary distribution and spread
- Exploring relationships between numeric columns
- Saving chart images for GitHub documentation
- Writing clean beginner-friendly data analysis code

## Real-World Applications

These skills are useful in AI/ML, data analysis, and business reporting.

Examples:

- Understanding salary trends in HR data
- Finding possible outliers before analysis
- Checking relationships between features before model training
- Creating simple dashboard visuals for stakeholders
- Communicating data insights more clearly with charts

## Key Takeaway

Seaborn makes data visualization easier, cleaner, and more useful for analysis. It is especially helpful when exploring distributions, relationships, and correlations before building machine learning models.

## Interview Questions

1. What is Seaborn used for?
2. How is Seaborn related to Matplotlib?
3. What does a histogram show?
4. What does a boxplot help you understand?
5. What does a scatterplot show?
6. What is correlation?
7. Why is a heatmap useful before machine learning?

## Reflection

Today I learned how Seaborn can make data visualization cleaner and easier than writing everything directly with Matplotlib. I also learned that different chart types answer different questions.

The most useful chart today was the correlation heatmap because it showed how numeric columns can be compared before machine learning. This helped me understand why visualization is part of the data exploration process, not just a final presentation step.

## Next Step

Continue to Day 06 and practice Exploratory Data Analysis (EDA) using a dataset with multiple columns, summaries, visualizations, and written insights.
