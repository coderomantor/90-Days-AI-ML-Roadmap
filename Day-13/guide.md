# Day 13 — Linear Regression Implementation Guide

## 1. What I Revised / Learned Today

Day 13 focused on implementing linear regression with scikit-learn. I practiced creating a dataset, separating `X` and `y`, splitting data, training a model, making predictions, evaluating results, and interpreting coefficients.

## 2. Why This Topic Matters

Implementation connects theory to real machine learning workflow. A model is only useful when I can train it, evaluate it, explain its errors, and communicate what the coefficients mean.

## 3. Core Concepts

`X` contains feature columns.

`y` contains the target column.

`train_test_split` separates data for training and testing.

`LinearRegression()` creates the model.

`model.fit()` trains the model.

`model.predict()` generates predictions.

MAE, MSE, RMSE, and R2 Score evaluate model performance.

The intercept and coefficients explain the learned relationship.

## 4. Practical Examples

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X = df[["Area", "Bedrooms", "Bathrooms", "Age"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)
```

## 5. Project Connection

House Price Prediction Part 2 trains a linear regression model using Area, Bedrooms, Bathrooms, and Age to predict Price. It prints actual vs predicted values, evaluation metrics, intercept, coefficients, and saves a chart.

## 6. Common Mistakes

- Forgetting to separate `X` and `y`.
- Training and testing on the same data.
- Ignoring model evaluation metrics.
- Reading coefficients without context.
- Forgetting that small toy datasets can behave differently from real datasets.
- Not saving visual outputs for documentation.

## 7. Interview-Style Questions

1. What does `model.fit()` do?
   It trains the model on training data.
2. What does `model.predict()` do?
   It generates predictions for new inputs.
3. What is MAE?
   Average absolute prediction error.
4. What is MSE?
   Average squared prediction error.
5. What is RMSE?
   Square root of MSE.
6. What is R2 Score?
   A score showing how much variance the model explains.
7. What are coefficients?
   Learned weights for each feature.
8. Why use train/test split?
   To evaluate on unseen data.

## 8. Day Checklist

- [ ] Import required libraries
- [ ] Create or load dataset
- [ ] Separate `X` and `y`
- [ ] Split train and test data
- [ ] Train `LinearRegression`
- [ ] Make predictions
- [ ] Compare actual vs predicted values
- [ ] Calculate MAE, MSE, RMSE, and R2
- [ ] Interpret intercept and coefficients
- [ ] Save a visualization

## 9. Final Takeaway

Linear regression implementation shows the complete beginner ML loop: prepare data, train a model, predict, evaluate, and explain results.
