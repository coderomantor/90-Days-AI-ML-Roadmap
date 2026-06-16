# Day 10: Train/Test Split

## Goal

Learn how to split a dataset into training and testing sets before building a machine learning model.

Day 09 focused on feature scaling. Day 10 focuses on one of the most important machine learning habits: keeping separate data for training and evaluation.

## Topics Covered

- Train/test split
- Features and target
- Training dataset
- Testing dataset
- Shuffling data
- Test size
- Random state
- Data leakage basics

## Learning Objectives

- Create a small student dataset using Pandas
- Identify feature columns and target column
- Shuffle a dataset before splitting
- Split data into training and testing sets
- Understand why testing data should stay unseen
- Save train and test datasets as CSV files
- Connect train/test split to the machine learning workflow

## Concepts Learned

### Train/Test Split

Train/test split means dividing a dataset into two parts:

- Training data: used to teach the model
- Testing data: used to evaluate the model on unseen data

This helps check whether a model learned useful patterns or only memorized the training data.

### Features and Target

Features are the input columns used by a model.

```python
features = df[["StudyHours", "Attendance", "PracticeTests"]]
```

The target is the output column the model tries to predict.

```python
target = df["Passed"]
```

### Training Data

Training data is used by the model to learn patterns.

Example:

```python
train_df = shuffled_df.iloc[test_count:]
```

### Testing Data

Testing data is kept separate and used only after training.

Example:

```python
test_df = shuffled_df.iloc[:test_count]
```

### Shuffling

Shuffling changes the row order before splitting.

```python
shuffled_df = df.sample(frac=1, random_state=42)
```

This helps avoid biased splits when the original data has an order.

### Random State

`random_state` makes the random shuffle reproducible.

If the same random state is used again, the split will be the same.

### Data Leakage

Data leakage happens when information from the testing data accidentally influences training.

This can make model results look better than they really are.

## Mini Project: Dataset Splitting Tool

The project creates a student dataset and splits it into training and testing datasets.

The project includes:

- Student DataFrame creation
- Feature and target explanation
- Dataset shuffling
- Train/test split
- Split summary
- Target distribution check
- CSV export of training and testing datasets

## Project Structure

```text
Day-10/
├── README.md
├── resources.md
├── project/
│   ├── dataset_splitting_tool.py
│   └── requirements.txt
└── screenshots/
```

## How To Run

From the `Day-10/project/` folder:

```bash
pip install -r requirements.txt
python dataset_splitting_tool.py
```

## Output

The project prints:

- Original student dataset
- Feature columns and target column
- Training dataset
- Testing dataset
- Split summary
- Target distribution in train and test sets
- Final notes

The project also saves:

- `student_train_dataset.csv`
- `student_test_dataset.csv`

After running the project, save a terminal screenshot in the `screenshots/` folder.

## Skills Demonstrated

- Creating Pandas DataFrames
- Identifying features and target
- Shuffling datasets
- Splitting data into train and test sets
- Checking split size and target distribution
- Saving train and test data as CSV files
- Writing beginner-friendly machine learning preparation code

## Real-World Applications

Train/test split is used in almost every supervised machine learning project.

Examples:

- Student pass/fail prediction
- House price prediction
- Customer churn prediction
- Loan approval prediction
- Sales forecasting

## Key Takeaway

Train/test split helps evaluate a model honestly. The model learns from training data, then testing data checks how well it performs on examples it has not seen before.

## Interview Questions

1. What is train/test split?
2. Why do we split data before model training?
3. What is training data used for?
4. What is testing data used for?
5. Why should testing data stay unseen during training?
6. What does shuffling do before splitting?
7. What is `random_state` used for?
8. What is data leakage?
9. What does `test_size=0.3` mean?
10. Why should we check target distribution after splitting?

## Reflection

Today I learned that evaluating a model fairly starts before training. If I train and test on the same data, the result can be misleading.

The biggest lesson from Day 10 is that a clean split helps measure whether a model can work on new unseen examples.

## Next Step

Continue with Day 11 and review the full machine learning workflow before starting linear regression theory.
