"""House Price Prediction Part 1: Linear Regression Theory.

Day 12 project for the 90 Days AI/ML Engineer Roadmap.
This script focuses on understanding the dataset and Area -> Price relationship.
"""

from pathlib import Path

import matplotlib
import pandas as pd


matplotlib.use("Agg")
import matplotlib.pyplot as plt


SCREENSHOTS_DIR = Path(__file__).resolve().parents[1] / "screenshots"
SCATTER_PLOT_PATH = SCREENSHOTS_DIR / "area_vs_price_scatter.png"


def build_house_price_dataset():
    """Create a small house price dataset for theory practice."""
    house_data = {
        "Area": [850, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600],
        "Bedrooms": [2, 2, 3, 3, 3, 4, 3, 4, 4, 5],
        "Bathrooms": [1, 1, 2, 2, 2, 2, 3, 3, 3, 4],
        "Age": [15, 8, 12, 5, 10, 4, 20, 6, 3, 2],
    }

    house_df = pd.DataFrame(house_data)
    house_df["Price"] = (
        50000
        + (house_df["Area"] * 120)
        + (house_df["Bedrooms"] * 18000)
        + (house_df["Bathrooms"] * 12000)
        - (house_df["Age"] * 1500)
        + pd.Series([3000, -2000, 4500, -3500, 2500, 6000, -4000, 3500, -2500, 5000])
    )

    return house_df


def save_area_price_scatter_plot(df):
    """Save a scatter plot to show the Area -> Price relationship."""
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.scatter(df["Area"], df["Price"], color="#2563eb")
    plt.title("Area vs House Price")
    plt.xlabel("Area (square feet)")
    plt.ylabel("Price")
    plt.tight_layout()
    plt.savefig(SCATTER_PLOT_PATH)
    plt.close()


def print_section(title):
    """Print a consistent terminal section header."""
    print(f"\n{title}")
    print("-" * 70)


def main():
    house_df = build_house_price_dataset()

    feature_columns = ["Area", "Bedrooms", "Bathrooms", "Age"]
    target_column = "Price"

    print("House Price Prediction Part 1 - Linear Regression Theory")
    print("=" * 70)

    print_section("Dataset")
    print(house_df.to_string(index=False))

    print_section("Dataset Overview")
    print(f"Rows: {house_df.shape[0]}")
    print(f"Columns: {house_df.shape[1]}")
    print()
    print(house_df.describe().to_string())

    print_section("Features and Target")
    print(f"Feature columns: {feature_columns}")
    print(f"Target column: {target_column}")
    print()
    print("Features preview:")
    print(house_df[feature_columns].head().to_string(index=False))
    print()
    print("Target preview:")
    print(house_df[target_column].head().to_string(index=False))

    print_section("Area -> Price Relationship")
    print("Area is the input feature we use to understand price movement.")
    print("Price is the target value we want to predict later.")
    print("In this simple dataset, larger houses generally have higher prices.")
    print("Day 12 focuses on understanding this relationship before training a model.")

    save_area_price_scatter_plot(house_df)

    print_section("Saved Output")
    print(f"Scatter plot saved to: {SCATTER_PLOT_PATH}")


if __name__ == "__main__":
    main()
