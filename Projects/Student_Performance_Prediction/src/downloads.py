"""CSV export helpers for dashboard download files."""

import logging

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

logger = logging.getLogger(__name__)


def save_processed_data(data: pd.DataFrame) -> None:
    """Save the cleaned dataset."""
    try:
        if data.empty:
            raise ValueError("Processed dataset is empty and cannot be exported.")
        ensure_directory(OUTPUT_DIR)
        data.to_csv(PROCESSED_DATA_PATH, index=False)
    except Exception:
        logger.exception("Failed to save processed dataset.")
        raise


def save_train_test_data(
    train_data: pd.DataFrame,
    test_data: pd.DataFrame,
) -> None:
    """Save the train and test datasets."""
    try:
        if train_data.empty or test_data.empty:
            raise ValueError("Train/test export data cannot be empty.")
        ensure_directory(OUTPUT_DIR)
        train_data.to_csv(TRAIN_DATA_PATH, index=False)
        test_data.to_csv(TEST_DATA_PATH, index=False)
    except Exception:
        logger.exception("Failed to save train/test datasets.")
        raise


def save_predictions(
    x_test: pd.DataFrame,
    y_test: pd.Series,
    predictions,
) -> pd.DataFrame:
    """Save actual and predicted scores to a CSV file."""
    try:
        if x_test.empty or y_test.empty:
            raise ValueError("Prediction export data cannot be empty.")
        results = x_test.copy()
        results[f"Actual_{TARGET_COLUMN}"] = y_test.values
        results[f"Predicted_{TARGET_COLUMN}"] = predictions.round(2)
        results.to_csv(PREDICTIONS_PATH, index=False)
        return results
    except Exception:
        logger.exception("Failed to save prediction results.")
        raise


def save_model_comparison(comparison_data: pd.DataFrame) -> None:
    """Save model comparison metrics."""
    try:
        if comparison_data.empty:
            raise ValueError("Model comparison data cannot be empty.")
        comparison_data.to_csv(MODEL_COMPARISON_PATH, index=False)
    except Exception:
        logger.exception("Failed to save model comparison data.")
        raise
