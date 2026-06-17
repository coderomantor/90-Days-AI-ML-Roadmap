
---

# Day 04 — Data Visualization with Matplotlib Guide

## 1. What I Revised / Learned Today

Day 04 focused on basic data visualization using Matplotlib. I practiced bar charts, histograms, pie charts, labels, titles, and saving charts as image files.

## 2. Why This Topic Matters

Visualization helps turn numbers into patterns. Before machine learning, charts can reveal distributions, comparisons, imbalance, and unusual values that may not be obvious in raw tables.

## 3. Core Concepts

A bar chart compares categories.

A histogram shows the distribution of numeric values.

A pie chart shows proportions, but should be used carefully.

Chart titles and labels make visualizations easier to understand.

Saving charts helps document projects clearly on GitHub.

## 4. Practical Examples

```python
import matplotlib.pyplot as plt

department_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.savefig("average_salary_by_department.png")
```

## 5. Project Connection

The Employee Salary Dashboard uses Pandas and Matplotlib to create salary-related charts and save them inside the screenshots folder. This makes the project more visual and portfolio-friendly.

## 6. Common Mistakes

- Creating charts without titles or labels.
- Choosing the wrong chart type.
- Using pie charts for too many categories.
- Forgetting `tight_layout()`.
- Not saving charts for GitHub documentation.

## 7. Interview-Style Questions

1. What is Matplotlib used for?
   Creating visualizations in Python.
2. When should you use a bar chart?
   To compare categories.
3. What does a histogram show?
   Distribution of numeric values.
4. Why are labels important?
   They explain what the chart shows.
5. Why save charts?
   To document analysis outputs.

## 8. Day Checklist

- [ ] Create a bar chart
- [ ] Create a histogram
- [ ] Create a pie chart
- [ ] Add chart title and labels
- [ ] Save charts as PNG files
- [ ] Explain what each chart shows

## 9. Final Takeaway

Matplotlib is a foundation tool for communicating data patterns clearly through charts.
