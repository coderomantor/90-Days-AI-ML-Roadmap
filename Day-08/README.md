# Day 08: Feature Engineering Basics and Encoding

## Goal

Learn how to prepare a dataset for machine learning by creating useful features and converting text categories into numeric values.

Day 07 reviewed the first week of learning. Day 08 starts Week 2 by moving from data exploration into dataset preparation, which is one of the most important steps before training machine learning models.

For structured learning notes, see the [Day 08 Guide](guide.md).

## Topics Covered

- Feature engineering basics
- Dataset preparation
- Categorical encoding
- One-hot encoding
- Ordinal encoding
- Binary encoding
- Feature creation
- Saving prepared data

## Learning Objectives

- Create a small employee dataset using Pandas
- Add new useful columns from existing columns
- Convert ordered categories into numeric values
- Convert unordered categories using one-hot encoding
- Convert yes/no values into binary values
- Drop columns that are not useful for model input
- Save a prepared dataset as a CSV file
- Understand why machine learning models need numeric features

## Concepts Learned

### Feature Engineering

Feature engineering means creating or transforming columns so a machine learning model can learn better from the data.

Example:

```python
df["SalaryPerExperience"] = df["Salary"] / df["Experience"]
```

This creates a new feature using two existing numeric columns.

### Encoding

Encoding means converting text categories into numbers.

Machine learning models usually work with numeric input, so columns like `Department`, `City`, or `Education` must be converted before modeling.

### Binary Encoding

Binary encoding is useful when a column has two possible values.

```python
df["PromotionEligible"] = df["PromotionEligible"].map({"No": 0, "Yes": 1})
```

This converts yes/no values into `0` and `1`.

### Ordinal Encoding

Ordinal encoding is useful when categories have a meaningful order.

```python
education_order = {
    "Bachelor": 1,
    "Master": 2,
    "PhD": 3,
}

df["EducationEncoded"] = df["Education"].map(education_order)
```

Education level has an order, so ordinal encoding makes sense here.

### One-Hot Encoding

One-hot encoding is useful when categories do not have a natural order.

```python
pd.get_dummies(df, columns=["Department", "City"], dtype=int)
```

This creates separate numeric columns for each category.

### Binning

Binning means grouping numeric values into categories.

```python
df["ExperienceLevel"] = pd.cut(
    df["Experience"],
    bins=[0, 3, 5, 10],
    labels=["Junior", "Mid", "Senior"],
)
```

This turns experience years into easier-to-understand levels.

## Mini Project: Dataset Preparation

The project creates an employee dataset and prepares it for machine learning.

The project includes:

- Employee DataFrame creation
- Feature engineering using salary, age, and experience
- Binary encoding for promotion eligibility
- Ordinal encoding for education level
- One-hot encoding for department, city, age group, and experience level
- Removing non-model columns
- Saving the prepared dataset as a CSV file

## Project Structure

```text
Day-08/
├── README.md
├── resources.md
├── project/
│   ├── dataset_preparation.py
│   └── requirements.txt
└── screenshots/
```

## How To Run

From the `Day-08/project/` folder:

```bash
pip install -r requirements.txt
python dataset_preparation.py
```

## Output

The project prints:

- Original employee dataset
- Dataset after feature engineering
- Machine learning ready encoded dataset
- Final notes explaining what changed

The project also saves:

- `prepared_employee_dataset.csv`

After running the project, save a terminal screenshot in the `screenshots/` folder.

## Skills Demonstrated

- Creating Pandas DataFrames
- Adding new features from existing columns
- Using `map()` for binary and ordinal encoding
- Using `pd.get_dummies()` for one-hot encoding
- Using `pd.cut()` for binning numeric values
- Preparing data for machine learning input
- Saving prepared data as a CSV file
- Writing readable beginner-friendly Python code

## Real-World Applications

Feature engineering and encoding are used in almost every machine learning project.

Examples:

- Preparing customer data for churn prediction
- Encoding product categories for recommendation systems
- Turning user profile data into model-ready features
- Creating useful columns from raw business data
- Preparing employee, sales, finance, or student datasets for ML models

## Key Takeaway

Machine learning models cannot understand raw text categories directly. Before training a model, an AI/ML engineer must prepare useful numeric features from the original dataset.

## Interview Questions

1. What is feature engineering?
2. Why do machine learning models need numeric input?
3. What is encoding?
4. What is the difference between ordinal encoding and one-hot encoding?
5. When should you use binary encoding?
6. What does `pd.get_dummies()` do?
7. What is binning?
8. Why might we drop an ID or name column before modeling?

## Reflection

Today I learned that preparing data for machine learning is more than cleaning missing values. I also need to create useful columns and convert categories into numeric features.

The most important lesson from Day 08 is that feature engineering connects raw data to machine learning. A model can only learn from the information we prepare for it.

## Next Step

Continue to Day 09 and learn feature scaling, normalization, and standardization.
