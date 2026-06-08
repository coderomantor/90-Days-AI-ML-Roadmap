"""Employee EDA Report using Pandas, Matplotlib, and Seaborn.

Day 06 project for the 90 Days AI/ML Engineer Roadmap.
The goal is to practice a beginner-friendly Exploratory Data Analysis workflow.
"""

from io import StringIO
from pathlib import Path

import matplotlib
import pandas as pd


# Use a non-interactive backend so charts can be saved without opening windows.
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns


SCREENSHOTS_DIR = Path(__file__).resolve().parents[1] / "screenshots"
NUMERIC_COLUMNS = [
    "Age",
    "Salary",
    "Experience",
    "PerformanceScore",
    "TrainingHours",
]


def build_employee_dataframe():
    """Create a small employee dataset for EDA practice."""
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
            "Bilal",
            "Maha",
            "Danish",
            "Iqra",
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
            "Marketing",
            "Finance",
            "IT",
            "HR",
        ],
        "Age": [24, 28, 29, 31, 27, 34, 30, 26, 32, 33, 35, 25],
        "Salary": [
            50000,
            62000,
            57000,
            58000,
            54000,
            65000,
            60000,
            59000,
            56000,
            67000,
            72000,
            53000,
        ],
        "Experience": [2, 4, 5, 6, 3, 7, 4, 3, 5, 8, 9, 2],
        "PerformanceScore": [78, 86, 82, 88, 80, 91, 85, 83, 81, 92, 94, 79],
        "TrainingHours": [12, 18, 16, 20, 14, 24, 19, 15, 17, 25, 26, 13],
    }

    return pd.DataFrame(employee_data)


def setup_chart_style():
    """Apply a clean Seaborn style for all EDA charts."""
    sns.set_theme(style="whitegrid")


def dataframe_info_as_text(df):
    """Return df.info() output as text so it can be printed neatly."""
    buffer = StringIO()
    df.info(buf=buffer)
    return buffer.getvalue()


def print_dataset_overview(df):
    """Print core EDA overview output."""
    print("Employee Data Analysis Report")
    print("=" * 60)

    print("\nFirst Five Rows")
    print("-" * 60)
    print(df.head().to_string(index=False))

    print("\nDataset Shape")
    print("-" * 60)
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    print("\nDataset Info")
    print("-" * 60)
    print(dataframe_info_as_text(df))

    print("\nSummary Statistics")
    print("-" * 60)
    print(df.describe().to_string())

    print("\nMissing Values")
    print("-" * 60)
    print(df.isnull().sum().to_string())

    print("\nDuplicate Rows")
    print("-" * 60)
    print(f"Duplicate row count: {df.duplicated().sum()}")


def save_salary_distribution_chart(df):
    """Save a histogram to show salary distribution."""
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x="Salary", bins=6, kde=True, color="#59A14F")
    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Number of Employees")
    plt.tight_layout()
    plt.savefig(SCREENSHOTS_DIR / "salary_distribution.png")
    plt.close()


def save_salary_outliers_boxplot(df):
    """Save a boxplot to inspect salary spread and possible outliers."""
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x="Salary", color="#F28E2B")
    plt.title("Salary Outlier Check")
    plt.xlabel("Salary")
    plt.tight_layout()
    plt.savefig(SCREENSHOTS_DIR / "salary_outliers_boxplot.png")
    plt.close()


def save_experience_vs_salary_chart(df):
    """Save a scatterplot to explore experience and salary relationship."""
    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=df,
        x="Experience",
        y="Salary",
        hue="Department",
        s=90,
    )
    plt.title("Experience vs Salary")
    plt.xlabel("Experience in Years")
    plt.ylabel("Salary")
    plt.tight_layout()
    plt.savefig(SCREENSHOTS_DIR / "experience_vs_salary.png")
    plt.close()


def save_correlation_heatmap(df):
    """Save a heatmap to analyze correlation between numeric columns."""
    correlation_matrix = df[NUMERIC_COLUMNS].corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5,
    )
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(SCREENSHOTS_DIR / "correlation_heatmap.png")
    plt.close()


def save_department_distribution_chart(df):
    """Save a countplot to show employee count by department."""
    plt.figure(figsize=(8, 5))
    sns.countplot(
        data=df,
        x="Department",
        hue="Department",
        palette="Set2",
        legend=False,
    )
    plt.title("Employee Count by Department")
    plt.xlabel("Department")
    plt.ylabel("Number of Employees")
    plt.tight_layout()
    plt.savefig(SCREENSHOTS_DIR / "department_distribution.png")
    plt.close()


def print_final_insights(df):
    """Print beginner-friendly conclusions from the EDA."""
    highest_salary_employee = df.loc[df["Salary"].idxmax()]
    lowest_salary_employee = df.loc[df["Salary"].idxmin()]
    average_salary_by_department = df.groupby("Department")["Salary"].mean()
    top_department = average_salary_by_department.idxmax()
    salary_experience_correlation = df["Salary"].corr(df["Experience"])

    print("\nFinal Insights")
    print("=" * 60)
    print(f"1. The dataset contains {df.shape[0]} employees and {df.shape[1]} columns.")
    print("2. There are no missing values or duplicate rows in this dataset.")
    print(
        "3. "
        f"{highest_salary_employee['Employee']} has the highest salary "
        f"({highest_salary_employee['Salary']})."
    )
    print(
        "4. "
        f"{lowest_salary_employee['Employee']} has the lowest salary "
        f"({lowest_salary_employee['Salary']})."
    )
    print(
        "5. "
        f"{top_department} has the highest average salary "
        f"({average_salary_by_department[top_department]:.2f})."
    )
    print(
        "6. "
        f"Salary and experience have a correlation of "
        f"{salary_experience_correlation:.2f}, which suggests a positive relationship."
    )


def main():
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    setup_chart_style()

    employee_df = build_employee_dataframe()

    print_dataset_overview(employee_df)

    save_salary_distribution_chart(employee_df)
    save_salary_outliers_boxplot(employee_df)
    save_experience_vs_salary_chart(employee_df)
    save_correlation_heatmap(employee_df)
    save_department_distribution_chart(employee_df)

    print_final_insights(employee_df)

    print("\nCharts saved in:")
    print(SCREENSHOTS_DIR)


if __name__ == "__main__":
    main()
