"""Employee Salary Dashboard using Pandas and Matplotlib.

Day 04 project for the 90 Days AI/ML Engineer Roadmap.
The goal is to visualize employee salary data with beginner-friendly charts.
"""

from pathlib import Path

import matplotlib
import pandas as pd


# Use a non-interactive backend so charts can be saved without opening windows.
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SCREENSHOTS_DIR = Path(__file__).resolve().parents[1] / "screenshots"


def build_employee_dataframe():
    """Create a small employee dataset for visualization practice."""
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
        "Salary": [50000, 62000, 57000, 58000, 54000, 65000, 60000, 59000],
        "Experience": [2, 4, 5, 6, 3, 7, 4, 3],
    }

    return pd.DataFrame(employee_data)


def save_average_salary_by_department_chart(df):
    """Save a bar chart showing average salary by department."""
    department_average_salary = df.groupby("Department")["Salary"].mean()

    plt.figure(figsize=(8, 5))
    department_average_salary.plot(kind="bar", color="#4C78A8")
    plt.title("Average Salary by Department")
    plt.xlabel("Department")
    plt.ylabel("Average Salary")
    plt.xticks(rotation=0)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(SCREENSHOTS_DIR / "average_salary_by_department.png")
    plt.close()


def save_salary_distribution_chart(df):
    """Save a histogram showing salary distribution."""
    plt.figure(figsize=(8, 5))
    plt.hist(df["Salary"], bins=5, color="#59A14F", edgecolor="black")
    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Number of Employees")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(SCREENSHOTS_DIR / "salary_distribution.png")
    plt.close()


def save_employee_distribution_by_department_chart(df):
    """Save a pie chart showing employees per department."""
    department_counts = df["Department"].value_counts()

    plt.figure(figsize=(7, 7))
    plt.pie(
        department_counts,
        labels=department_counts.index,
        autopct="%1.1f%%",
        startangle=90,
    )
    plt.title("Employee Distribution by Department")
    plt.tight_layout()
    plt.savefig(SCREENSHOTS_DIR / "employee_distribution_by_department.png")
    plt.close()


def print_dashboard_summary(df):
    """Print a simple summary of the dashboard output."""
    print("Employee Salary Dashboard")
    print("=" * 60)
    print(df.to_string(index=False))

    print("\nAverage Salary by Department")
    print("-" * 60)
    print(df.groupby("Department")["Salary"].mean().to_string())

    print("\nCharts saved in:")
    print(SCREENSHOTS_DIR)


def main():
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

    employee_df = build_employee_dataframe()

    save_average_salary_by_department_chart(employee_df)
    save_salary_distribution_chart(employee_df)
    save_employee_distribution_by_department_chart(employee_df)

    print_dashboard_summary(employee_df)


if __name__ == "__main__":
    main()
