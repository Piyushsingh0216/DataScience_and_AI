"""Data cleaning, feature engineering, and preprocessing summaries."""

from dataclasses import dataclass

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

    total_rows: int
    total_columns: int
    missing_values_before: int
    missing_values_after: int
    duplicate_rows_removed: int
    number_of_features: int
    target_column: str
    train_test_split_ratio: str


def clean_dataset(data: pd.DataFrame) -> tuple[pd.DataFrame, PreprocessingSummary]:
    """Clean missing values, duplicate rows, and data types."""
    cleaned_data = data.copy()
    missing_before = int(cleaned_data.isna().sum().sum())

    for column in NUMERIC_COLUMNS:
        cleaned_data[column] = pd.to_numeric(cleaned_data[column], errors="coerce")

    for column in NUMERIC_COLUMNS:
        median_value = cleaned_data[column].median()
        cleaned_data[column] = cleaned_data[column].fillna(median_value)

    for column in CATEGORICAL_COLUMNS:
        mode_value = cleaned_data[column].mode()[0]
        cleaned_data[column] = cleaned_data[column].fillna(mode_value)

    duplicate_rows_removed = int(cleaned_data.duplicated().sum())
    cleaned_data = cleaned_data.drop_duplicates().reset_index(drop=True)
    cleaned_data["Assignments_Completed"] = cleaned_data[
        "Assignments_Completed"
    ].astype(int)

    summary = PreprocessingSummary(
        total_rows=len(cleaned_data),
        total_columns=len(cleaned_data.columns),
        missing_values_before=missing_before,
        missing_values_after=int(cleaned_data.isna().sum().sum()),
        duplicate_rows_removed=duplicate_rows_removed,
        number_of_features=len(FEATURE_COLUMNS),
        target_column=TARGET_COLUMN,
        train_test_split_ratio=format_ratio(TEST_SIZE),
    )
    return cleaned_data, summary


def prepare_features(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Separate features and target, then one-hot encode categorical values."""
    features = data[FEATURE_COLUMNS]
    target = data[TARGET_COLUMN]
    encoded_features = pd.get_dummies(features, drop_first=True)
    return encoded_features, target


def split_dataset(
    features: pd.DataFrame,
    target: pd.Series,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split features and target into training and testing sets."""
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
