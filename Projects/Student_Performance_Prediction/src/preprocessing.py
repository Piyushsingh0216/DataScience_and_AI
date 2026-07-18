"""Data cleaning, feature engineering, and preprocessing summaries."""

from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from config import (
    CATEGORICAL_COLUMNS,
    FEATURE_COLUMNS,
    NUMERIC_COLUMNS,
    RANDOM_STATE,
    TARGET_COLUMN,
    TEST_SIZE,
)
from utils import format_ratio


@dataclass(frozen=True)
class PreprocessingSummary:
    """Beginner-friendly summary of the preprocessing workflow."""

    original_dataset_shape: str
    final_dataset_shape: str
    total_rows: int
    total_columns: int
    missing_values_before: int
    missing_values_after: int
    duplicate_rows_removed: int
    missing_values_handled: str
    duplicate_rows_status: str
    columns_encoded: str
    columns_scaled: str
    features_selected: str
    feature_selection_method: str
    number_of_features: int
    target_column: str
    train_test_split_ratio: str


def validate_dataset_columns(data: pd.DataFrame) -> None:
    """Validate that the dataset contains every required project column."""
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Dataset must be a pandas DataFrame.")

    if data.empty:
        raise ValueError("The dataset is empty. Please provide valid student data.")

    required_columns = FEATURE_COLUMNS + [TARGET_COLUMN]
    missing_columns = [
        column for column in required_columns if column not in data.columns
    ]

    if missing_columns:
        missing_list = ", ".join(missing_columns)
        raise ValueError(f"Missing required dataset columns: {missing_list}.")


def get_dataset_overview(data: pd.DataFrame) -> dict[str, object]:
    """Return high-level dataset statistics for dashboard display."""
    numeric_count = int(data.select_dtypes(include=[np.number]).shape[1])
    categorical_count = int(
        data.select_dtypes(include=["object", "category", "bool"]).shape[1]
    )
    memory_mb = data.memory_usage(deep=True).sum() / (1024**2)

    return {
        "Total Rows": len(data),
        "Total Columns": len(data.columns),
        "Number of Numerical Features": numeric_count,
        "Number of Categorical Features": categorical_count,
        "Target Column": TARGET_COLUMN,
        "Dataset Memory Usage": f"{memory_mb:.3f} MB",
        "Missing Values": int(data.isna().sum().sum()),
        "Duplicate Rows": int(data.duplicated().sum()),
    }


def get_numeric_statistics(data: pd.DataFrame) -> pd.DataFrame:
    """Build a compact numeric statistics table."""
    numeric_data = data.select_dtypes(include=[np.number])
    if numeric_data.empty:
        return pd.DataFrame(
            columns=[
                "Feature",
                "Mean",
                "Median",
                "Standard Deviation",
                "Minimum",
                "Maximum",
            ]
        )

    statistics = pd.DataFrame(
        {
            "Feature": numeric_data.columns,
            "Mean": numeric_data.mean().values,
            "Median": numeric_data.median().values,
            "Standard Deviation": numeric_data.std().values,
            "Minimum": numeric_data.min().values,
            "Maximum": numeric_data.max().values,
        }
    )
    return statistics.round(3)


def clean_dataset(data: pd.DataFrame) -> tuple[pd.DataFrame, PreprocessingSummary]:
    """Clean missing values, duplicate rows, and data types."""
    validate_dataset_columns(data)
    cleaned_data = data.copy()
    original_shape = f"{len(cleaned_data)} rows x {len(cleaned_data.columns)} columns"
    missing_before = int(cleaned_data.isna().sum().sum())

    for column in NUMERIC_COLUMNS:
        cleaned_data[column] = pd.to_numeric(cleaned_data[column], errors="coerce")

    for column in NUMERIC_COLUMNS:
        median_value = cleaned_data[column].median()
        if pd.isna(median_value):
            raise ValueError(
                f"Column '{column}' has no valid numeric values after conversion."
            )
        cleaned_data[column] = cleaned_data[column].fillna(median_value)

    for column in CATEGORICAL_COLUMNS:
        mode_values = cleaned_data[column].mode(dropna=True)
        if mode_values.empty:
            raise ValueError(
                f"Column '{column}' has no valid categorical values to fill."
            )
        mode_value = mode_values.iloc[0]
        cleaned_data[column] = cleaned_data[column].fillna(mode_value)

    duplicate_rows_removed = int(cleaned_data.duplicated().sum())
    cleaned_data = cleaned_data.drop_duplicates().reset_index(drop=True)
    cleaned_data["Assignments_Completed"] = cleaned_data[
        "Assignments_Completed"
    ].astype(int)
    missing_after = int(cleaned_data.isna().sum().sum())

    if cleaned_data.empty:
        raise ValueError("Preprocessing removed every row from the dataset.")

    encoded_columns = (
        ", ".join(CATEGORICAL_COLUMNS) if CATEGORICAL_COLUMNS else "Not Applied"
    )
    selected_features = (
        ", ".join(FEATURE_COLUMNS) if FEATURE_COLUMNS else "Not Applied"
    )
    final_shape = f"{len(cleaned_data)} rows x {len(cleaned_data.columns)} columns"

    summary = PreprocessingSummary(
        original_dataset_shape=original_shape,
        final_dataset_shape=final_shape,
        total_rows=len(cleaned_data),
        total_columns=len(cleaned_data.columns),
        missing_values_before=missing_before,
        missing_values_after=missing_after,
        duplicate_rows_removed=duplicate_rows_removed,
        missing_values_handled="Yes" if missing_before else "Not Applied",
        duplicate_rows_status=(
            f"{duplicate_rows_removed} removed"
            if duplicate_rows_removed
            else "Not Applied"
        ),
        columns_encoded=encoded_columns,
        columns_scaled="Not Applied",
        features_selected=selected_features,
        feature_selection_method="Not Applied",
        number_of_features=len(FEATURE_COLUMNS),
        target_column=TARGET_COLUMN,
        train_test_split_ratio=format_ratio(TEST_SIZE),
    )
    return cleaned_data, summary


def prepare_features(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Separate features and target, then one-hot encode categorical values."""
    validate_dataset_columns(data)
    features = data[FEATURE_COLUMNS]
    target = data[TARGET_COLUMN]
    encoded_features = pd.get_dummies(features, drop_first=True)

    if encoded_features.empty or target.empty:
        raise ValueError("Feature preparation produced empty training data.")
    if encoded_features.isna().any().any() or target.isna().any():
        raise ValueError("Feature preparation produced invalid missing values.")

    return encoded_features, target


def split_dataset(
    features: pd.DataFrame,
    target: pd.Series,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split features and target into training and testing sets."""
    if len(features) < 2:
        raise ValueError("At least two records are required for train/test split.")

    return train_test_split(
        features,
        target,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
    )


def combine_features_and_target(
    features: pd.DataFrame,
    target: pd.Series,
    target_name: str = TARGET_COLUMN,
) -> pd.DataFrame:
    """Combine feature and target data for CSV export."""
    combined_data = features.copy()
    combined_data[target_name] = target.values
    return combined_data
