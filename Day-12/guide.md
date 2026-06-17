# Day 12 — Linear Regression Theory Guide

## 1. What I Revised / Learned Today

Day 12 focused on linear regression theory. I revised regression problems, features and target, the formula `y = mx + b`, slope, intercept, line of best fit, and residual error.

## 2. Why This Topic Matters

Linear regression is one of the simplest machine learning algorithms. It helps build intuition for numeric prediction, model training, error, and evaluation before moving to more advanced models.

## 3. Core Concepts

Regression predicts numeric values. Classification predicts categories.

Features are input columns, such as area, bedrooms, bathrooms, and house age.

The target is the output column, such as price.

The simple linear regression formula is `y = mx + b`.

Slope shows how much the prediction changes when the feature changes.

Intercept positions the line.

The line of best fit represents the trend in the data.

Residual or error is the difference between actual and predicted value.

Simple linear regression uses one feature. Multiple linear regression uses more than one feature.

## 4. Practical Examples

```python
import pandas as pd

df = pd.DataFrame({
    "Area": [900, 1200, 1500],
    "Price": [180000, 250000, 300000],
})

X = df[["Area"]]
y = df["Price"]
```

```text
Predicted Price = slope * Area + intercept
```

## 5. Project Connection

House Price Prediction Part 1 creates a small house dataset, identifies features and target, prints a dataset overview, explains the Area to Price relationship, and saves a scatter plot.

## 6. Common Mistakes

- Confusing regression with classification.
- Forgetting that linear regression predicts numeric values.
- Thinking the line must pass through every point.
- Ignoring residuals and prediction error.
- Not separating features and target clearly.
- Assuming every relationship is linear.

## 7. Interview-Style Questions

1. What is linear regression?
   A regression algorithm for predicting numeric values.
2. What is a feature?
   An input column used by the model.
3. What is a target?
   The output column the model predicts.
4. What does slope mean?
   How much prediction changes as the feature changes.
5. What is intercept?
   The starting point of the regression line.
6. What is a residual?
   The difference between actual and predicted value.
7. What is multiple linear regression?
   Linear regression using more than one feature.

## 8. Day Checklist

- [ ] Explain regression vs classification
- [ ] Identify features and target
- [ ] Explain `y = mx + b`
- [ ] Explain slope and intercept
- [ ] Understand line of best fit
- [ ] Understand residual/error
- [ ] Create an Area vs Price scatter plot

## 9. Final Takeaway

Linear regression is a clear starting point for machine learning because it connects data, prediction, and error in a simple way.
