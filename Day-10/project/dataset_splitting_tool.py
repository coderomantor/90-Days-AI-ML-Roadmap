"""Dataset Splitting Tool using Pandas.

Day 10 project for the 90 Days AI/ML Engineer Roadmap.
The goal is to practice splitting data into training and testing sets.
"""

from pathlib import Path

import pandas as pd


OUTPUT_DIR = Path(__file__).resolve().parent
TRAIN_PATH = OUTPUT_DIR / "student_train_dataset.csv"
TEST_PATH = OUTPUT_DIR / "student_test_dataset.csv"


def build_student_dataframe():
    """Create a small student dataset for train/test split practice."""
    student_data = {
        "Student": [
            "Ali",
            "Sara",
            "Ahmed",
            "Ayesha",
            "Usman",
            "Fatima",
            "Zain",
            "Hira",
            "Bilal",
            "Maha",
        ],
        "StudyHours": [2, 3, 4, 5, 6, 7, 4, 8, 5, 6],
        "Attendance": [60, 65, 70, 80, 85, 90, 75, 95, 78, 88],
        "PracticeTests": [1, 1, 2, 2, 3, 4, 2, 5, 3, 4],
        "PreviousScore": [55, 58, 64, 72, 78, 86, 69, 91, 74, 82],
        "Passed": [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    }

    return pd.DataFrame(student_data)


def split_dataset(df, test_size=0.3, random_state=42):
    """Shuffle and split a dataset into train and test sets using Pandas."""
    shuffled_df = df.sample(frac=1, random_state=random_state).reset_index(drop=True)

    test_count = int(len(shuffled_df) * test_size)
    test_df = shuffled_df.iloc[:test_count].reset_index(drop=True)
    train_df = shuffled_df.iloc[test_count:].reset_index(drop=True)

    return train_df, test_df


def print_section(title):
    """Print a consistent terminal section header."""
    print(f"\n{title}")
    print("-" * 70)


def explain_features_and_target(df):
    """Print feature and target column details."""
    feature_columns = ["StudyHours", "Attendance", "PracticeTests", "PreviousScore"]
    target_column = "Passed"

    print_section("Features and Target")
    print(f"Feature columns: {feature_columns}")
    print(f"Target column: {target_column}")
    print()
    print("Feature preview:")
    print(df[feature_columns].head().to_string(index=False))
    print()
    print("Target preview:")
    print(df[target_column].head().to_string(index=False))


def print_split_summary(train_df, test_df):
    """Print a short summary of the train/test split."""
    total_rows = len(train_df) + len(test_df)
    train_percentage = (len(train_df) / total_rows) * 100
    test_percentage = (len(test_df) / total_rows) * 100

    print_section("Split Summary")
    print(f"Total rows: {total_rows}")
    print(f"Training rows: {len(train_df)} ({train_percentage:.0f}%)")
    print(f"Testing rows: {len(test_df)} ({test_percentage:.0f}%)")
    print()
    print("Training target distribution:")
    print(train_df["Passed"].value_counts().sort_index().to_string())
    print()
    print("Testing target distribution:")
    print(test_df["Passed"].value_counts().sort_index().to_string())


def main():
    student_df = build_student_dataframe()

    print("Dataset Splitting Tool")
    print("=" * 70)

    print_section("Original Dataset")
    print(student_df.to_string(index=False))

    explain_features_and_target(student_df)

    train_df, test_df = split_dataset(student_df, test_size=0.3, random_state=42)

    print_section("Training Dataset")
    print(train_df.to_string(index=False))

    print_section("Testing Dataset")
    print(test_df.to_string(index=False))

    print_split_summary(train_df, test_df)

    train_df.to_csv(TRAIN_PATH, index=False)
    test_df.to_csv(TEST_PATH, index=False)

    print_section("Final Notes")
    print("1. Training data is used to teach the model patterns.")
    print("2. Testing data is used to check performance on unseen data.")
    print("3. Shuffling helps avoid biased splits when data has an order.")
    print(f"4. Training dataset saved to: {TRAIN_PATH}")
    print(f"5. Testing dataset saved to: {TEST_PATH}")


if __name__ == "__main__":
    main()
