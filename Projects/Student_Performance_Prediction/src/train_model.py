"""Backward-compatible model training script."""

import numpy as np
import pandas as pd

from config import DATA_PATH, LINEAR_MODEL_PATH
from data_loader import load_dataset
from downloads import save_predictions as export_predictions
from evaluation import evaluate_regression_model
from models import save_model_package
from pipeline import run_pipeline
from preprocessing import prepare_features, split_dataset
from sklearn.linear_model import LinearRegression


def load_data() -> pd.DataFrame:
    """Load the cleaned student dataset."""
    return load_dataset(DATA_PATH)


def split_data(
    x: pd.DataFrame,
    y: pd.Series,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split the data into training and testing sets."""
    return split_dataset(x, y)


def train_model(x_train: pd.DataFrame, y_train: pd.Series) -> LinearRegression:
    """Train a Linear Regression model."""
    model = LinearRegression()
    model.fit(x_train, y_train)
    return model


def evaluate_model(
    model: LinearRegression,
    x_test: pd.DataFrame,
    y_test: pd.Series,
) -> tuple[np.ndarray, dict[str, float]]:
    """Evaluate a model using common regression metrics."""
    predictions = model.predict(x_test)
    metrics = evaluate_regression_model("Linear Regression", y_test, predictions, 0.0)
    legacy_metrics = {
        "MAE": float(metrics["MAE"]),
        "MSE": float(metrics["MSE"]),
        "RMSE": float(metrics["RMSE"]),
        "R2": float(metrics["R2 Score"]),
    }
    return predictions, legacy_metrics


def save_model(
    model: LinearRegression,
    feature_columns: pd.Index,
    model_path=LINEAR_MODEL_PATH,
) -> None:
    """Save the trained model and feature column order using pickle."""
    save_model_package(model, feature_columns, model_path, "Linear Regression")


def save_predictions(
    x_test: pd.DataFrame,
    y_test: pd.Series,
    predictions: np.ndarray,
) -> None:
    """Save actual and predicted scores to a CSV file."""
    export_predictions(x_test, y_test, predictions)


def main() -> None:
    """Run the full model training and comparison workflow."""
    results = run_pipeline(create_graphs=True)
    comparison_data = results["comparison_data"]

    print("\nModel Comparison Results")
    print(comparison_data.round(4).to_string(index=False))
    print(f"\nBest model based on R2 Score: {results['best_model_name']}")
    print("\nOutputs saved in the outputs/ folder.")


if __name__ == "__main__":
    main()
