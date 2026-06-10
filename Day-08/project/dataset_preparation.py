"""Dataset Preparation using Pandas.

Day 08 project for the 90 Days AI/ML Engineer Roadmap.
The goal is to practice beginner-friendly feature engineering and encoding.
"""

from pathlib import Path

import pandas as pd


OUTPUT_PATH = Path(__file__).resolve().parent / "prepared_employee_dataset.csv"


def build_employee_dataframe():
    """Create a small employee dataset for feature engineering practice."""
    employee_data = {
        "Employee": [
            "Ali",
            "Sara",
            "Ahmed",
            "Ayesha",
            "Usman",
            "Fatima",
            "Zain",
            "Hira",
        ],
        "Department": [
            "IT",
            "HR",
            "Finance",
            "IT",
            "Marketing",
            "Finance",
            "IT",
            "HR",
        ],
        "Education": [
            "Bachelor",
            "Master",
            "Bachelor",
            "Master",
            "Bachelor",
            "PhD",
            "Master",
            "Bachelor",
        ],
        "City": [
            "Lahore",
            "Karachi",
            "Islamabad",
            "Lahore",
            "Karachi",
            "Islamabad",
            "Lahore",
            "Karachi",
        ],
        "Age": [24, 28, 29, 31, 27, 34, 30, 26],
        "Salary": [50000, 62000, 57000, 58000, 54000, 65000, 60000, 59000],
        "Experience": [2, 4, 5, 6, 3, 7, 4, 3],
        "PerformanceScore": [78, 86, 82, 88, 80, 91, 85, 83],
        "PromotionEligible": ["No", "Yes", "No", "Yes", "No", "Yes", "Yes", "No"],
    }

    return pd.DataFrame(employee_data)


def add_engineered_features(df):
    """Add useful beginner-friendly features before encoding."""
    prepared_df = df.copy()

    prepared_df["SalaryPerExperience"] = (
        prepared_df["Salary"] / prepared_df["Experience"]
    ).round(2)

    prepared_df["IsSenior"] = prepared_df["Experience"].apply(
        lambda experience: 1 if experience >= 5 else 0
    )

    prepared_df["ExperienceLevel"] = pd.cut(
        prepared_df["Experience"],
        bins=[0, 3, 5, 10],
        labels=["Junior", "Mid", "Senior"],
        include_lowest=True,
    )

    prepared_df["AgeGroup"] = pd.cut(
        prepared_df["Age"],
        bins=[20, 25, 30, 40],
        labels=["Early_Career", "Growing", "Experienced"],
        include_lowest=True,
    )

    return prepared_df


def encode_features(df):
    """Convert text categories into numeric columns for machine learning."""
    encoded_df = df.copy()

    education_order = {
        "Bachelor": 1,
        "Master": 2,
        "PhD": 3,
    }
    encoded_df["EducationEncoded"] = encoded_df["Education"].map(education_order)

    encoded_df["PromotionEligible"] = encoded_df["PromotionEligible"].map(
        {"No": 0, "Yes": 1}
    )

    encoded_df = pd.get_dummies(
        encoded_df,
        columns=["Department", "City", "ExperienceLevel", "AgeGroup"],
        dtype=int,
    )

    encoded_df = encoded_df.drop(columns=["Employee", "Education"])

    return encoded_df


def print_section(title):
    """Print a consistent terminal section header."""
    print(f"\n{title}")
    print("-" * 70)


def main():
    employee_df = build_employee_dataframe()

    print("Dataset Preparation Project")
    print("=" * 70)

    print_section("Original Dataset")
    print(employee_df.to_string(index=False))

    engineered_df = add_engineered_features(employee_df)
    print_section("Dataset After Feature Engineering")
    print(engineered_df.to_string(index=False))

    encoded_df = encode_features(engineered_df)
    print_section("Machine Learning Ready Dataset")
    print(encoded_df.to_string(index=False))

    encoded_df.to_csv(OUTPUT_PATH, index=False)

    print_section("Final Notes")
    print("1. New useful columns were created from existing data.")
    print("2. Text categories were converted into numeric features.")
    print("3. The prepared dataset is now closer to machine learning format.")
    print(f"4. Prepared dataset saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
