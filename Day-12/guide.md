# Day 12 — Linear Regression Theory Guide

This guide contains my Day 12 learning notes for Linear Regression Theory as part of the 90-Days AI/ML Roadmap.

## What is Linear Regression?

Linear regression is a supervised machine learning algorithm used to predict a numeric value.

It tries to learn a straight-line relationship between input features and a target value.

Example:

- Input feature: house area
- Target: house price

If the area increases, the price often increases too. Linear regression tries to model that relationship.

## Regression vs Classification

Regression is used when the target is numeric.

Examples:

- Predicting house price
- Predicting salary
- Predicting sales

Classification is used when the target is a category.

Examples:

- Pass or fail
- Spam or not spam
- Approved or rejected

Simple rule:

- Numeric target: regression
- Category target: classification

## Features and Target

Features are the input columns used by the model.

```python
X = df[["Area", "Bedrooms", "Bathrooms", "Age"]]
```

The target is the output column the model tries to predict.

```python
y = df["Price"]
```

In house price prediction, features describe the house and the target is the price.

## Formula: y = mx + b

The basic linear regression formula is:

```text
y = mx + b
```

Where:

- `y` is the predicted value
- `x` is the input feature
- `m` is the slope
- `b` is the intercept

For house price prediction:

```text
Predicted Price = slope * Area + intercept
```

## Slope

Slope tells us how much the prediction changes when the input feature increases.

If the slope is positive, the predicted value increases as the feature increases.

In house price prediction, a positive slope means larger area usually leads to a higher predicted price.

## Intercept

The intercept is the starting point of the regression line when the input value is zero.

It is part of the model equation and helps position the line correctly.

In real datasets, the intercept may not always have a practical real-world meaning, but it still helps the model fit the data.

## Line of Best Fit

The line of best fit is the line that best represents the relationship between the feature and target.

Linear regression tries to find a line that keeps prediction errors as small as possible.

The goal is not to pass through every point perfectly. The goal is to find the best overall trend.

## Residual/Error

A residual is the difference between the actual value and predicted value.

```text
Residual = Actual Value - Predicted Value
```

Example:

```text
Actual price: 250000
Predicted price: 240000
Residual: 10000
```

Smaller residuals usually mean better predictions.

## Simple vs Multiple Linear Regression

Simple linear regression uses one feature.

Example:

```text
Price = slope * Area + intercept
```

Multiple linear regression uses more than one feature.

Example:

```text
Price = Area + Bedrooms + Bathrooms + Age
```

Day 12 focuses on understanding the theory. Day 13 uses multiple features in implementation.

## Why Linear Regression is important

Linear regression is important because it is one of the simplest and most interpretable machine learning algorithms.

It helps beginners understand:

- Features and target
- Model training
- Prediction
- Error
- Evaluation
- Relationship between variables

Even when more advanced models are used later, linear regression remains a strong foundation.

## Common beginner mistakes

- Confusing regression with classification
- Forgetting that regression predicts numeric values
- Thinking the line must pass through every data point
- Ignoring residuals and prediction error
- Using unrelated features without thinking
- Not separating features and target clearly
- Jumping to implementation without understanding the formula
- Assuming correlation always means causation

## Interview-style questions

1. What is linear regression?
2. When do we use regression?
3. What is the difference between regression and classification?
4. What is a feature?
5. What is a target?
6. What does `y = mx + b` mean?
7. What is slope?
8. What is intercept?
9. What is a residual?
10. What is the line of best fit?
11. What is the difference between simple and multiple linear regression?
12. Why is linear regression important for beginners?

## Day 12 checklist

- [ ] Understand regression vs classification
- [ ] Identify features and target
- [ ] Explain `y = mx + b`
- [ ] Explain slope
- [ ] Explain intercept
- [ ] Understand line of best fit
- [ ] Understand residual/error
- [ ] Understand simple vs multiple linear regression
- [ ] Create a basic Area vs Price scatter plot
- [ ] Prepare for Day 13 implementation
