"""CSV export helpers for dashboard download files."""

import pandas as pd

from config import (
    MODEL_COMPARISON_PATH,
    OUTPUT_DIR,
    PREDICTIONS_PATH,
    PROCESSED_DATA_PATH,
    TEST_DATA_PATH,
    TRAIN_DATA_PATH,
    TARGET_COLUMN,
)
from utils import ensure_directory


def save_processed_data(data: pd.DataFrame) -> None:
    """Save the cleaned dataset."""
    ensure_directory(OUTPUT_DIR)
    data.to_csv(PROCESSED_DATA_PATH, index=False)


def save_train_test_data(
    train_data: pd.DataFrame,
    test_data: pd.DataFrame,
) -> None:
    """Save the train and test datasets."""
    ensure_directory(OUTPUT_DIR)
    train_data.to_csv(TRAIN_DATA_PATH, index=False)
    test_data.to_csv(TEST_DATA_PATH, index=False)


def save_predictions(
    x_test: pd.DataFrame,
    y_test: pd.Series,
    predictions,
) -> pd.DataFrame:
    """Save actual and predicted scores to a CSV file."""
    results = x_test.copy()
    results[f"Actual_{TARGET_COLUMN}"] = y_test.values
    results[f"Predicted_{TARGET_COLUMN}"] = predictions.round(2)
    results.to_csv(PREDICTIONS_PATH, index=False)
    return results


def save_model_comparison(comparison_data: pd.DataFrame) -> None:
    """Save model comparison metrics."""
    comparison_data.to_csv(MODEL_COMPARISON_PATH, index=False)
