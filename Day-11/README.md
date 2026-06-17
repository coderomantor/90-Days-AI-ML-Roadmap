# Day 11: Introduction to Machine Learning

## Goal

Understand what machine learning is, how a basic ML workflow works, and how features, targets, training, prediction, and evaluation connect together.

Day 10 focused on train/test split. Day 11 introduces the full machine learning workflow at a beginner-friendly level before moving into linear regression.

## Topics Covered

- Introduction to machine learning
- Features and target
- Supervised learning
- Regression
- Classification
- Training and prediction
- Model evaluation
- Machine learning workflow

## Learning Objectives

- Understand the basic meaning of machine learning
- Identify features and target columns in a dataset
- Understand the difference between regression and classification
- Learn the main steps in a machine learning workflow
- Understand why data preparation happens before model training
- Understand why evaluation is needed after training
- Connect previous data preparation days to future ML projects

## Concepts Learned

### Machine Learning

Machine learning is a way for computers to learn patterns from data and use those patterns to make predictions or decisions.

Instead of writing every rule manually, we provide data and allow an algorithm to learn from examples.

### Features

Features are the input columns used by a machine learning model.

Example:

```python
features = df[["StudyHours", "Attendance", "PracticeTests"]]
```

Features are also called input variables or independent variables.

### Target

The target is the output column the model tries to predict.

Example:

```python
target = df["Passed"]
```

The target is also called the label or dependent variable.

### Supervised Learning

Supervised learning means the dataset contains both input features and the correct target values.

Examples:

- Predicting whether a student passes or fails
- Predicting house prices
- Predicting whether an email is spam

### Regression

Regression is used when the target is a number.

Examples:

- House price prediction
- Salary prediction
- Sales forecasting

### Classification

Classification is used when the target is a category.

Examples:

- Pass or fail prediction
- Spam or not spam
- Loan approved or rejected

### ML Workflow

A simple machine learning workflow is:

1. Define the problem
2. Collect or prepare data
3. Explore the data
4. Clean and preprocess features
5. Split the data
6. Train a model
7. Evaluate the model
8. Improve and explain results

## Mini Project: ML Workflow Notes

The project prints a beginner-friendly explanation of the machine learning workflow in the terminal.

The project includes:

- A small student dataset
- Feature and target explanation
- Machine learning workflow steps
- Regression, classification, and clustering examples
- Final beginner-friendly notes

## Project Structure

```text
Day-11/
├── README.md
├── resources.md
├── project/
│   ├── ml_workflow_notes.py
│   └── requirements.txt
└── screenshots/
```

## How To Run

From the `Day-11/project/` folder:

```bash
pip install -r requirements.txt
python ml_workflow_notes.py
```

## Output

The project prints:

- Sample student dataset
- Feature columns and target column
- Machine learning workflow steps
- Common machine learning task types
- Final notes for beginners

After running the project, save a terminal screenshot in the `screenshots/` folder.

## Skills Demonstrated

- Understanding the ML workflow
- Identifying features and target columns
- Explaining supervised learning
- Comparing regression and classification
- Writing beginner-friendly ML notes in Python
- Connecting data preparation to model training
- Maintaining professional GitHub documentation

## Real-World Applications

These ideas are used in every machine learning project.

Examples:

- Defining a prediction problem clearly
- Preparing datasets before model training
- Choosing whether a problem is regression or classification
- Explaining model workflow to teammates or interviewers
- Building stronger foundations before using ML libraries

## Key Takeaway

Machine learning is a workflow, not just one line of code. A good ML project starts with a clear problem, useful features, clean data, and a reliable way to evaluate results.

## Interview Questions

1. What is machine learning?
2. What is a feature?
3. What is a target column?
4. What is supervised learning?
5. What is the difference between regression and classification?
6. Why do we prepare data before training a model?
7. Why do we split data before evaluation?
8. What does model training mean?
9. What does model evaluation mean?
10. Why is the ML workflow important?

## Reflection

Today I learned that machine learning is more than choosing an algorithm. It is a complete workflow that starts with problem definition and data understanding.

The most important lesson from Day 11 is that clean features, clear targets, and proper evaluation are the foundation of reliable machine learning.

## Next Step

Continue to Day 12 and start linear regression theory.
