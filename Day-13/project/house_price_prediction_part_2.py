"""House Price Prediction Part 2: Linear Regression Implementation.

Day 13 project for the 90 Days AI/ML Engineer Roadmap.
This script trains a LinearRegression model using scikit-learn.
"""

from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


matplotlib.use("Agg")
import matplotlib.pyplot as plt


SCREENSHOTS_DIR = Path(__file__).resolve().parents[1] / "screenshots"
PREDICTION_PLOT_PATH = SCREENSHOTS_DIR / "actual_vs_predicted_prices.png"


def build_house_price_dataset():
    """Create a small house price dataset for linear regression practice."""
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


def save_actual_vs_predicted_plot(results_df):
    """Save a simple actual vs predicted price visualization."""
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.plot(results_df.index, results_df["ActualPrice"], marker="o", label="Actual")
    plt.plot(results_df.index, results_df["PredictedPrice"], marker="o", label="Predicted")
    plt.title("Actual vs Predicted House Prices")
    plt.xlabel("Test Sample")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    plt.savefig(PREDICTION_PLOT_PATH)
    plt.close()


def print_section(title):
    """Print a consistent terminal section header."""
    print(f"\n{title}")
    print("-" * 70)


def main():
    house_df = build_house_price_dataset()

    feature_columns = ["Area", "Bedrooms", "Bathrooms", "Age"]
    target_column = "Price"

    X = house_df[feature_columns]
    y = house_df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42,
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    results_df = pd.DataFrame(
        {
            "ActualPrice": y_test.values,
            "PredictedPrice": predictions.round(2),
            "AbsoluteError": np.abs(y_test.values - predictions).round(2),
        }
    )

    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)

    print("House Price Prediction Part 2 - Linear Regression Implementation")
    print("=" * 70)

    print_section("Dataset")
    print(house_df.to_string(index=False))

    print_section("Features and Target")
    print(f"Feature columns: {feature_columns}")
    print(f"Target column: {target_column}")

    print_section("Train/Test Split")
    print(f"Training rows: {len(X_train)}")
    print(f"Testing rows: {len(X_test)}")

    print_section("Actual vs Predicted Values")
    print(results_df.to_string(index=False))

    print_section("Evaluation Metrics")
    print(f"MAE: {mae:.2f}")
    print(f"MSE: {mse:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R2 Score: {r2:.3f}")

    print_section("Intercept and Coefficients")
    print(f"Intercept: {model.intercept_:.2f}")
    for feature_name, coefficient in zip(feature_columns, model.coef_):
        print(f"{feature_name}: {coefficient:.2f}")

    save_actual_vs_predicted_plot(results_df)

    print_section("Saved Output")
    print(f"Prediction chart saved to: {PREDICTION_PLOT_PATH}")


if __name__ == "__main__":
    main()
