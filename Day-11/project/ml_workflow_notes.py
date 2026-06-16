"""Machine Learning Workflow Notes.

Day 11 project for the 90 Days AI/ML Engineer Roadmap.
The goal is to understand the beginner-friendly machine learning workflow.
"""

import pandas as pd


ML_WORKFLOW_STEPS = [
    (
        "1. Define the problem",
        "Decide what the model should predict and why the prediction matters.",
    ),
    (
        "2. Collect or prepare data",
        "Gather the dataset and make sure it contains useful input features.",
    ),
    (
        "3. Explore the data",
        "Use EDA to understand patterns, missing values, outliers, and relationships.",
    ),
    (
        "4. Preprocess features",
        "Clean, encode, scale, and prepare features for machine learning.",
    ),
    (
        "5. Split the dataset",
        "Separate data into training and testing parts to evaluate fairly.",
    ),
    (
        "6. Train a model",
        "Let the algorithm learn patterns from the training data.",
    ),
    (
        "7. Evaluate the model",
        "Check how well the model performs on unseen testing data.",
    ),
    (
        "8. Improve and explain",
        "Tune the workflow, compare results, and explain conclusions clearly.",
    ),
]


def build_sample_dataset():
    """Create a small dataset to explain features, target, and prediction."""
    student_data = {
        "StudyHours": [2, 3, 4, 5, 6, 7],
        "Attendance": [60, 65, 70, 80, 85, 90],
        "PracticeTests": [1, 1, 2, 2, 3, 4],
        "Passed": ["No", "No", "Yes", "Yes", "Yes", "Yes"],
    }

    return pd.DataFrame(student_data)


def print_section(title):
    """Print a consistent terminal section header."""
    print(f"\n{title}")
    print("-" * 70)


def explain_features_and_target(df):
    """Explain the difference between input features and target column."""
    feature_columns = ["StudyHours", "Attendance", "PracticeTests"]
    target_column = "Passed"

    print_section("Features and Target")
    print("Features are the input columns used by a machine learning model.")
    print(f"Feature columns: {feature_columns}")
    print()
    print("The target is the output column the model tries to predict.")
    print(f"Target column: {target_column}")
    print()
    print("Feature preview:")
    print(df[feature_columns].to_string(index=False))
    print()
    print("Target preview:")
    print(df[target_column].to_string(index=False))


def print_workflow_steps():
    """Print the main machine learning workflow steps."""
    print_section("Machine Learning Workflow")

    for title, description in ML_WORKFLOW_STEPS:
        print(title)
        print(f"   {description}")


def print_model_examples():
    """Print beginner-friendly examples of ML task types."""
    examples = [
        ("Regression", "Predict a number, such as house price or salary."),
        ("Classification", "Predict a category, such as pass/fail or spam/not spam."),
        ("Clustering", "Group similar records without predefined labels."),
    ]

    print_section("Common Machine Learning Task Types")

    for task_type, explanation in examples:
        print(f"{task_type}: {explanation}")


def print_final_notes():
    """Print practical beginner-friendly conclusions."""
    print_section("Final Notes")
    print("1. Machine learning is not only about choosing an algorithm.")
    print("2. Clean data and clear problem definition come first.")
    print("3. Features are inputs, and the target is what we want to predict.")
    print("4. A professional ML workflow must include evaluation and explanation.")
    print("5. The next step is learning how to split data into train and test sets.")


def main():
    sample_df = build_sample_dataset()

    print("Introduction to Machine Learning")
    print("=" * 70)

    print_section("Sample Dataset")
    print(sample_df.to_string(index=False))

    explain_features_and_target(sample_df)
    print_workflow_steps()
    print_model_examples()
    print_final_notes()


if __name__ == "__main__":
    main()
