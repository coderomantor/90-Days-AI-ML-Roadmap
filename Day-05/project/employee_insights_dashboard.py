"""Employee Insights Dashboard using Pandas, Matplotlib, and Seaborn.

Day 05 project for the 90 Days AI/ML Engineer Roadmap.
The goal is to practice cleaner statistical visualizations with Seaborn.
"""

from pathlib import Path

import matplotlib
import pandas as pd


# Use a non-interactive backend so charts can be saved without opening windows.
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns


SCREENSHOTS_DIR = Path(__file__).resolve().parents[1] / "screenshots"


def build_employee_dataframe():
    """Create a small employee dataset for Seaborn visualization practice."""
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
        ],
        "Age": [24, 28, 29, 31, 27, 34, 30, 26, 32, 33],
        "Salary": [50000, 62000, 57000, 58000, 54000, 65000, 60000, 59000, 56000, 67000],
        "Experience": [2, 4, 5, 6, 3, 7, 4, 3, 5, 8],
        "PerformanceScore": [78, 86, 82, 88, 80, 91, 85, 83, 81, 92],
        "TrainingHours": [12, 18, 16, 20, 14, 24, 19, 15, 17, 25],
    }

    return pd.DataFrame(employee_data)


def setup_chart_style():
    """Apply a clean Seaborn style for all dashboard charts."""
    sns.set_theme(style="whitegrid")


def save_average_salary_by_department_chart(df):
    """Save a barplot to compare average salary across departments."""
    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=df,
        x="Department",
        y="Salary",
        hue="Department",
        estimator="mean",
        errorbar=None,
        palette="Blues_d",
        legend=False,
    )
    plt.title("Average Salary by Department")
    plt.xlabel("Department")
    plt.ylabel("Average Salary")
    plt.tight_layout()
    plt.savefig(SCREENSHOTS_DIR / "average_salary_by_department.png")
    plt.close()


def save_salary_distribution_chart(df):
    """Save a histogram to show how salaries are distributed."""
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x="Salary", bins=6, kde=True, color="#59A14F")
    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Number of Employees")
    plt.tight_layout()
    plt.savefig(SCREENSHOTS_DIR / "salary_distribution.png")
    plt.close()


def save_salary_spread_by_department_chart(df):
    """Save a boxplot to compare salary spread and possible outliers."""
    plt.figure(figsize=(8, 5))
    sns.boxplot(
        data=df,
        x="Department",
        y="Salary",
        hue="Department",
        palette="Set2",
        legend=False,
    )
    plt.title("Salary Spread by Department")
    plt.xlabel("Department")
    plt.ylabel("Salary")
    plt.tight_layout()
    plt.savefig(SCREENSHOTS_DIR / "salary_spread_by_department.png")
    plt.close()


def save_experience_vs_salary_chart(df):
    """Save a scatterplot to show the relationship between experience and salary."""
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


def save_numeric_correlation_heatmap(df):
    """Save a heatmap to show correlation between numeric columns."""
    numeric_columns = [
        "Age",
        "Salary",
        "Experience",
        "PerformanceScore",
        "TrainingHours",
    ]
    correlation_matrix = df[numeric_columns].corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5,
    )
    plt.title("Correlation Heatmap for Numeric Columns")
    plt.tight_layout()
    plt.savefig(SCREENSHOTS_DIR / "numeric_correlation_heatmap.png")
    plt.close()


def print_dashboard_summary(df):
    """Print a simple summary of the dashboard output."""
    print("Employee Insights Dashboard")
    print("=" * 60)
    print(df.to_string(index=False))

    print("\nAverage Salary by Department")
    print("-" * 60)
    print(df.groupby("Department")["Salary"].mean().to_string())

    print("\nNumeric Correlation Summary")
    print("-" * 60)
    numeric_columns = [
        "Age",
        "Salary",
        "Experience",
        "PerformanceScore",
        "TrainingHours",
    ]
    print(df[numeric_columns].corr().to_string())

    print("\nCharts saved in:")
    print(SCREENSHOTS_DIR)


def main():
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    setup_chart_style()

    employee_df = build_employee_dataframe()

    save_average_salary_by_department_chart(employee_df)
    save_salary_distribution_chart(employee_df)
    save_salary_spread_by_department_chart(employee_df)
    save_experience_vs_salary_chart(employee_df)
    save_numeric_correlation_heatmap(employee_df)

    print_dashboard_summary(employee_df)


if __name__ == "__main__":
    main()
