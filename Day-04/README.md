# Day 04: Data Visualization with Matplotlib

## Goal

Learn how to turn cleaned tabular data into simple visual insights using Matplotlib.

Day 03 focused on cleaning and analyzing employee data with Pandas. Day 04 builds on that by creating charts that make salary patterns and department distribution easier to understand.

For structured learning notes, see the [Day 04 Guide](guide.md).

## Topics Covered

- Data visualization
- Matplotlib basics
- Bar charts
- Histograms
- Pie charts
- Chart titles and labels
- Saving charts as PNG files
- Using Pandas data with Matplotlib

## Learning Objectives

- Create a small employee dataset using Pandas
- Calculate average salary by department
- Create a bar chart for department salary comparison
- Create a histogram for salary distribution
- Create a pie chart for employee distribution by department
- Add clear titles, labels, and formatting to charts
- Save visualization outputs in the `screenshots/` folder

## Concepts Learned

### Data Visualization

Data visualization means using charts to understand data faster.

Tables are useful, but charts make patterns easier to see. For example, a salary table shows exact numbers, while a bar chart quickly shows which department has the highest average salary.

### Bar Chart

A bar chart compares values across categories.

```python
department_average_salary.plot(kind="bar")
```

In this project, the bar chart compares average salary by department.

### Histogram

A histogram shows how numeric values are distributed.

```python
df["Salary"].plot(kind="hist")
```

In this project, the histogram shows how employee salaries are spread across different ranges.

### Pie Chart

A pie chart shows how a full group is divided into categories.

```python
department_counts.plot(kind="pie")
```

In this project, the pie chart shows the employee distribution by department.

### Saving Charts

Charts can be saved as image files for documentation and portfolio use.

```python
plt.savefig("chart-name.png")
```

Saving charts is useful because GitHub visitors can see the project output without running the code.

## Mini Project: Employee Salary Dashboard

The project creates a small employee dataset and generates three charts:

- Average salary by department
- Salary distribution
- Employee distribution by department

Each chart is saved as a PNG file inside the `screenshots/` folder.

## Project Structure

```text
Day-04/
├── README.md
├── resources.md
├── project/
│   ├── employee_salary_dashboard.py
│   └── requirements.txt
└── screenshots/
```

## How To Run

From the `Day-04/project/` folder:

```bash
pip install -r requirements.txt
python employee_salary_dashboard.py
```

## Output

The project saves the following charts:

- [screenshots/average_salary_by_department.png](screenshots/average_salary_by_department.png)
- [screenshots/salary_distribution.png](screenshots/salary_distribution.png)
- [screenshots/employee_distribution_by_department.png](screenshots/employee_distribution_by_department.png)

## Skills Demonstrated

- Creating Pandas DataFrames
- Summarizing data by category
- Creating Matplotlib bar charts
- Creating Matplotlib histograms
- Creating Matplotlib pie charts
- Adding titles, axis labels, and clean formatting
- Saving chart images for GitHub documentation
- Building a beginner-friendly data dashboard script

## Real-World Applications

These skills are useful in many AI/ML and data analysis workflows.

Examples:

- Visualizing salary trends in HR datasets
- Showing customer distribution by segment
- Understanding feature distributions before ML training
- Creating simple dashboard outputs for reports
- Communicating data insights to non-technical people

## Key Takeaway

Data visualization helps turn raw numbers into insights. A clean chart can explain a pattern faster than a table, especially when sharing work in a portfolio or report.

## Interview Questions

1. Why is data visualization important before machine learning?
2. What is a bar chart used for?
3. What is a histogram used for?
4. What is a pie chart used for?
5. Why should charts have clear titles and labels?
6. How do you save a Matplotlib chart as a PNG file?
7. How can Pandas and Matplotlib work together?

## Reflection

Today I learned how to use Matplotlib to create simple visual summaries from employee data. The most important idea was that charts are not only decoration. They help explain patterns, compare groups, and communicate findings clearly.

This project also helped me understand why visualization is useful before machine learning. Before training a model, an AI/ML engineer should understand the data, and charts make that process easier.

## Next Step

Continue to Day 05 and learn Seaborn for cleaner statistical visualizations, correlation charts, heatmaps, and distribution plots.
