# Day 13 — Linear Regression Implementation Guide

This guide contains my Day 13 implementation notes for House Price Prediction using Linear Regression.

## Importing required libraries

For this project, the main libraries are:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
```

Pandas is used for the dataset, scikit-learn is used for model training and evaluation, NumPy helps with RMSE, and Matplotlib is used for visualization.

## Creating/loading dataset

For beginner practice, the dataset is created manually.

```python
df = pd.DataFrame({
    "Area": [900, 1100, 1300],
    "Bedrooms": [2, 2, 3],
    "Bathrooms": [1, 1, 2],
    "Age": [12, 10, 8],
    "Price": [150000, 180000, 210000],
})
```

In real projects, the dataset may come from a CSV file, database, API, or public dataset.

## Separating X and y

`X` contains the feature columns.

```python
X = df[["Area", "Bedrooms", "Bathrooms", "Age"]]
```

`y` contains the target column.

```python
y = df["Price"]
```

The model learns patterns from `X` to predict `y`.

## Train/test split

Train/test split separates data for learning and evaluation.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
)
```

Training data teaches the model. Testing data checks how well the model performs on unseen examples.

## Training LinearRegression model

Create the model:

```python
model = LinearRegression()
```

Train the model:

```python
model.fit(X_train, y_train)
```

During training, the model learns the intercept and coefficients.

## Making predictions

After training, predictions are made on the test data.

```python
predictions = model.predict(X_test)
```

These predictions can be compared with the actual target values.

## Comparing actual vs predicted values

A simple comparison table helps inspect model performance.

```python
results = pd.DataFrame({
    "ActualPrice": y_test.values,
    "PredictedPrice": predictions,
})
```

This makes it easier to see where the model performed well and where it made larger errors.

## Evaluating with MAE, MSE, RMSE, and R2 Score

### MAE

Mean Absolute Error shows the average absolute prediction error.

```python
mae = mean_absolute_error(y_test, predictions)
```

### MSE

Mean Squared Error squares the errors before averaging them.

```python
mse = mean_squared_error(y_test, predictions)
```

### RMSE

Root Mean Squared Error is the square root of MSE.

```python
rmse = np.sqrt(mse)
```

### R2 Score

R2 Score explains how much variance the model explains.

```python
r2 = r2_score(y_test, predictions)
```

Higher R2 is usually better, but it should always be interpreted carefully.

## Interpreting coefficients

The intercept is the model starting point.

```python
model.intercept_
```

Coefficients show how each feature affects the prediction.

```python
model.coef_
```

Example interpretation:

- A positive Area coefficient means larger area increases predicted price.
- A negative Age coefficient can mean older houses may reduce predicted price.

Coefficients should be interpreted carefully, especially when features are related to each other.

## Visualizing predictions

A simple line chart can compare actual and predicted prices.

```python
plt.plot(results.index, results["ActualPrice"], label="Actual")
plt.plot(results.index, results["PredictedPrice"], label="Predicted")
plt.legend()
plt.show()
```

Visualization helps quickly see whether predictions follow the same pattern as actual values.

## Common implementation mistakes

- Forgetting to separate features and target
- Training and testing on the same data
- Forgetting train/test split
- Evaluating only by looking at predictions manually
- Ignoring MAE, MSE, RMSE, or R2 Score
- Not checking whether features make sense
- Interpreting coefficients without context
- Using testing data during training
- Forgetting to save charts or outputs for documentation

## Interview-style questions

1. How do you separate features and target?
2. Why do we use train/test split?
3. What does `model.fit()` do?
4. What does `model.predict()` do?
5. What is MAE?
6. What is MSE?
7. What is RMSE?
8. What is R2 Score?
9. What is an intercept?
10. What are coefficients?
11. How do you compare actual and predicted values?
12. Why should testing data stay unseen during training?

## Day 13 checklist

- [ ] Import required libraries
- [ ] Create or load dataset
- [ ] Separate `X` and `y`
- [ ] Split data into train and test sets
- [ ] Train `LinearRegression`
- [ ] Make predictions
- [ ] Compare actual vs predicted values
- [ ] Calculate MAE
- [ ] Calculate MSE
- [ ] Calculate RMSE
- [ ] Calculate R2 Score
- [ ] Print intercept and coefficients
- [ ] Save a visualization
