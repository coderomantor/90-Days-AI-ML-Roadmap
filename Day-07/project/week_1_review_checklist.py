"""Week 1 Review Checklist.

Day 07 project for the 90 Days AI/ML Engineer Roadmap.
The goal is to review completed topics, projects, and interview questions.
"""


COMPLETED_DAYS = [
    ("Day 01", "NumPy Fundamentals", "Student Marks Analyzer"),
    ("Day 02", "Pandas Introduction", "Student Performance Analyzer"),
    ("Day 03", "Pandas Data Cleaning", "Employee Data Analyzer"),
    ("Day 04", "Matplotlib Visualization", "Employee Salary Dashboard"),
    ("Day 05", "Seaborn Visualization", "Employee Insights Dashboard"),
    ("Day 06", "Exploratory Data Analysis", "Employee Data Analysis Report"),
]

SKILLS_PRACTICED = [
    "NumPy arrays and vectorized calculations",
    "Pandas DataFrames and column operations",
    "Missing value and duplicate checks",
    "Filtering, sorting, value counts, and GroupBy",
    "Matplotlib charts saved as PNG files",
    "Seaborn statistical visualizations",
    "Exploratory Data Analysis with final insights",
    "Professional GitHub documentation",
]

INTERVIEW_QUESTIONS = [
    "What is the difference between NumPy and Pandas?",
    "What is a DataFrame?",
    "Why do we check missing values before analysis?",
    "What does axis=0 mean?",
    "What does axis=1 mean?",
    "What is Exploratory Data Analysis?",
    "Why are visualizations useful before machine learning?",
    "What does a correlation heatmap show?",
    "What is the purpose of a boxplot?",
    "Why is clean documentation important for a GitHub portfolio?",
]


def print_section(title):
    """Print a consistent section header."""
    print(f"\n{title}")
    print("-" * 60)


def print_completed_days():
    """Print completed Week 1 days and projects."""
    print_section("Completed Days")

    for day, topic, project in COMPLETED_DAYS:
        print(f"{day}: {topic} - {project}")


def print_skills_practiced():
    """Print the main skills practiced during Week 1."""
    print_section("Skills Practiced")

    for index, skill in enumerate(SKILLS_PRACTICED, start=1):
        print(f"{index}. {skill}")


def print_interview_questions():
    """Print interview questions to review before moving forward."""
    print_section("Interview Questions")

    for index, question in enumerate(INTERVIEW_QUESTIONS, start=1):
        print(f"{index}. {question}")


def print_next_focus():
    """Print the recommended next focus."""
    print_section("Next Focus")
    print("Day 08: Feature Engineering Basics and Encoding")
    print("Review weak areas before moving deeper into machine learning.")


def main():
    print("Week 1 Review Checklist")
    print("=" * 60)
    print("Goal: Review the first week and prepare for Day 08.")

    print_completed_days()
    print_skills_practiced()
    print_interview_questions()
    print_next_focus()


if __name__ == "__main__":
    main()
