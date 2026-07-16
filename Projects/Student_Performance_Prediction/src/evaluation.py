"""Regression model evaluation helpers."""

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_regression_model(
    model_name: str,
    y_true: pd.Series,
    predictions: np.ndarray,
    training_time: float,
) -> dict[str, float | str]:
    """Calculate standard regression metrics for one model."""
    mse = mean_squared_error(y_true, predictions)
    return {
        "Model": model_name,
        "MAE": mean_absolute_error(y_true, predictions),
        "MSE": mse,
        "RMSE": float(np.sqrt(mse)),
        "R2 Score": r2_score(y_true, predictions),
        "Training Time": training_time,
    }


def get_best_model_name(comparison_data: pd.DataFrame) -> str:
    """Return the model name with the highest R2 score."""
    best_index = comparison_data["R2 Score"].idxmax()
    return str(comparison_data.loc[best_index, "Model"])
