
---

# Day 01 — Python Refresher and NumPy Basics Guide

## 1. What I Revised / Learned Today

Day 01 focused on refreshing Python fundamentals and starting NumPy for numerical computing. I practiced arrays, basic statistics, and vectorized calculations through a Student Marks Analyzer project.

## 2. Why This Topic Matters

AI/ML work depends heavily on numerical data. NumPy is one of the core libraries behind data science and machine learning in Python because it makes numerical operations faster, cleaner, and easier to scale than regular Python lists.

## 3. Core Concepts

Python basics matter because they help with variables, lists, loops, functions, and readable code.

NumPy arrays are used to store numerical data efficiently.

Vectorization means applying operations to an entire array without writing manual loops.

Basic statistics such as sum, mean, maximum, and minimum help summarize numeric datasets.

## 4. Practical Examples

```python
import numpy as np

marks = np.array([78, 85, 92, 67, 88])

print(marks.mean())
print(marks.max())
print(marks.min())
```

## 5. Project Connection

The Student Marks Analyzer uses NumPy to calculate totals, averages, highest marks, lowest marks, and class-level statistics. This connects directly to how AI/ML engineers summarize numerical data before deeper analysis.

## 6. Common Mistakes

- Treating NumPy arrays exactly like Python lists.
- Forgetting to import NumPy before using `np`.
- Writing manual loops when vectorized operations are simpler.
- Confusing total marks with average marks.
- Not checking the shape or structure of numerical data.

## 7. Interview-Style Questions

1. What is NumPy?
   NumPy is a Python library for efficient numerical computing.
2. Why use NumPy instead of regular lists?
   NumPy arrays support fast vectorized operations.
3. What is vectorization?
   Applying operations to arrays without manual loops.
4. What does `mean()` calculate?
   The average of values.
5. Why are arrays useful in ML?
   ML models usually work with numerical data arranged in arrays.

## 8. Day Checklist

- [ ] Understand why NumPy is useful
- [ ] Create a NumPy array
- [ ] Calculate sum, mean, max, and min
- [ ] Explain vectorization
- [ ] Run the Student Marks Analyzer project

## 9. Final Takeaway

NumPy is one of the first building blocks for AI/ML because it helps work with numerical data clearly and efficiently.
