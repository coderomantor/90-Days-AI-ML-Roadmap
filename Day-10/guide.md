
---

# Day 10 — Train/Test Split Guide

## 1. What I Revised / Learned Today

Day 10 focused on splitting data into training and testing sets before model evaluation.

## 2. Why This Topic Matters

Train/test split helps evaluate whether a model can perform on unseen data. Without it, a model may look good only because it memorized the training data.

## 3. Core Concepts

Training data is used to teach the model.

Testing data is used to evaluate performance after training.

Shuffling helps avoid biased splits.

`random_state` makes splits reproducible.

Data leakage happens when test information influences training.

## 4. Practical Examples

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
)
```

## 5. Project Connection

The Dataset Splitting Tool creates a student dataset, separates features and target, shuffles records, creates train/test sets, and saves both as CSV files.

## 6. Common Mistakes

- Training and testing on the same data.
- Not shuffling ordered data.
- Using the test set during training.
- Ignoring target distribution.
- Forgetting to set `random_state` when reproducibility matters.

## 7. Interview-Style Questions

1. What is train/test split?
   Dividing data into training and testing parts.
2. Why keep test data unseen?
   To evaluate generalization honestly.
3. What does `test_size=0.3` mean?
   30% of data is used for testing.
4. What is data leakage?
   When test or future information leaks into training.
5. Why shuffle data?
   To avoid order-based bias.

## 8. Day Checklist

- [ ] Separate features and target
- [ ] Shuffle data
- [ ] Split train and test sets
- [ ] Check split size
- [ ] Check target distribution
- [ ] Explain data leakage

## 9. Final Takeaway

Train/test split is a simple but essential step for honest model evaluation.
