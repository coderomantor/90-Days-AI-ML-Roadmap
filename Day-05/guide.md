
---

# Day 05 — Seaborn Fundamentals for Data Visualization Guide

## 1. What I Revised / Learned Today

Day 05 focused on Seaborn for cleaner statistical visualizations. I practiced barplots, histograms, boxplots, scatterplots, and correlation heatmaps.

## 2. Why This Topic Matters

Seaborn helps create professional statistical charts with less code. It is useful during EDA because it makes relationships, distributions, outliers, and correlations easier to inspect.

## 3. Core Concepts

Seaborn is built on top of Matplotlib.

A barplot compares category-level values.

A histogram shows numeric distribution.

A boxplot helps inspect spread and possible outliers.

A scatterplot compares two numeric variables.

A heatmap visualizes correlation between numeric columns.

## 4. Practical Examples

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(data=df, x="Experience", y="Salary", hue="Department")
plt.title("Experience vs Salary")
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
```

## 5. Project Connection

The Employee Insights Dashboard uses Seaborn to create multiple visualizations for salary patterns, spread, relationships, and correlations. This connects directly to EDA and early ML feature understanding.

## 6. Common Mistakes

- Using visualizations without a clear question.
- Forgetting to set chart labels.
- Misreading correlation as causation.
- Using too many colors.
- Ignoring outliers shown by boxplots.

## 7. Interview-Style Questions

1. What is Seaborn?
   A Python library for statistical visualization.
2. How is Seaborn related to Matplotlib?
   It is built on top of Matplotlib.
3. What does a boxplot show?
   Spread, median, quartiles, and possible outliers.
4. What does a heatmap show?
   Relationships such as correlation between numeric columns.
5. Why use scatterplots?
   To compare two numeric variables.

## 8. Day Checklist

- [ ] Create a Seaborn barplot
- [ ] Create a histogram
- [ ] Create a boxplot
- [ ] Create a scatterplot
- [ ] Create a heatmap
- [ ] Explain the insight from each chart

## 9. Final Takeaway

Seaborn makes data exploration clearer by helping visualize statistical patterns quickly and professionally.
