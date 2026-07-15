"""
Data cleaning and dataset generation for the Student Performance project.

This file creates a realistic sample dataset if one does not already exist,
then cleans it by handling missing values, removing duplicates, and fixing
data types. The cleaned dataset is saved back to data/students.csv.
"""

from pathlib import Path

import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "students.csv"
RANDOM_STATE = 42


def generate_student_dataset(file_path=DATA_PATH, rows=1200):
    """
    Generate a realistic student performance dataset.

    The target column, Exam_Score, is based on study hours, attendance,
    sleep, previous score, assignments, internet access, and family income.
    """
    rng = np.random.default_rng(RANDOM_STATE)

    hours_studied = rng.normal(loc=5.5, scale=2.2, size=rows).clip(0, 12)
    attendance = rng.normal(loc=78, scale=12, size=rows).clip(40, 100)
    sleep_hours = rng.normal(loc=7, scale=1.2, size=rows).clip(3, 10)
    previous_score = rng.normal(loc=68, scale=14, size=rows).clip(25, 100)
    assignments_completed = rng.integers(0, 11, size=rows)
    internet_access = rng.choice(["Yes", "No"], size=rows, p=[0.82, 0.18])
    family_income = rng.choice(
        ["Low", "Medium", "High"],
        size=rows,
        p=[0.30, 0.50, 0.20],
    )

    internet_bonus = np.where(internet_access == "Yes", 2.0, -1.5)
    income_bonus = np.select(
        [family_income == "Low", family_income == "Medium", family_income == "High"],
        [-2.0, 1.0, 3.0],
    )
    noise = rng.normal(loc=0, scale=5, size=rows)

    exam_score = (
        0.35 * attendance
        + 2.4 * hours_studied
        + 0.25 * previous_score
        + 1.4 * assignments_completed
        + 1.1 * sleep_hours
        + internet_bonus
        + income_bonus
        + noise
        - 18
    ).clip(0, 100)

    data = pd.DataFrame(
        {
            "Hours_Studied": hours_studied.round(1),
            "Attendance": attendance.round(1),
            "Sleep_Hours": sleep_hours.round(1),
            "Previous_Score": previous_score.round(1),
            "Assignments_Completed": assignments_completed,
            "Internet_Access": internet_access,
            "Family_Income": family_income,
            "Exam_Score": exam_score.round(1),
        }
    )

    # Add a small number of missing values so beginners can practice cleaning.
    missing_columns = [
        "Hours_Studied",
        "Attendance",
        "Sleep_Hours",
        "Previous_Score",
        "Internet_Access",
        "Family_Income",
    ]
    for column in missing_columns:
        missing_indices = rng.choice(data.index, size=int(rows * 0.015), replace=False)
        data.loc[missing_indices, column] = np.nan

    # Add duplicate rows so the duplicate-removal step has visible impact.
    duplicates = data.sample(n=15, random_state=RANDOM_STATE)
    data = pd.concat([data, duplicates], ignore_index=True)

    file_path.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(file_path, index=False)
    print(f"Dataset generated successfully at: {file_path}")


def load_dataset(file_path=DATA_PATH):
    """Load the student dataset using Pandas."""
    if not file_path.exists():
        generate_student_dataset(file_path)

    return pd.read_csv(file_path)


def display_basic_information(data):
    """Display beginner-friendly dataset information."""
    print("\nFirst 5 rows:")
    print(data.head())

    print("\nDataset shape:")
    print(data.shape)

    print("\nDataset information:")
    data.info()

    print("\nSummary statistics:")
    print(data.describe())


def clean_dataset(data):
    """Clean missing values, duplicates, and data types."""
    cleaned_data = data.copy()

    numeric_columns = [
        "Hours_Studied",
        "Attendance",
        "Sleep_Hours",
        "Previous_Score",
        "Assignments_Completed",
        "Exam_Score",
    ]
    categorical_columns = ["Internet_Access", "Family_Income"]

    # Convert numeric columns to numeric data types.
    for column in numeric_columns:
        cleaned_data[column] = pd.to_numeric(cleaned_data[column], errors="coerce")

    # Fill missing numeric values with the median.
    for column in numeric_columns:
        median_value = cleaned_data[column].median()
        cleaned_data[column] = cleaned_data[column].fillna(median_value)

    # Fill missing categorical values with the most common value.
    for column in categorical_columns:
        mode_value = cleaned_data[column].mode()[0]
        cleaned_data[column] = cleaned_data[column].fillna(mode_value)

    # Remove duplicate rows.
    duplicate_count = cleaned_data.duplicated().sum()
    cleaned_data = cleaned_data.drop_duplicates()

    # Keep assignments as whole numbers.
    cleaned_data["Assignments_Completed"] = cleaned_data[
        "Assignments_Completed"
    ].astype(int)

    print(f"\nDuplicates removed: {duplicate_count}")
    print("Missing values after cleaning:")
    print(cleaned_data.isnull().sum())

    return cleaned_data


def save_cleaned_dataset(data, file_path=DATA_PATH):
    """Save the cleaned dataset to CSV."""
    data.to_csv(file_path, index=False)
    print(f"\nCleaned dataset saved at: {file_path}")


def main():
    """Run all data loading and cleaning steps."""
    data = load_dataset()
    display_basic_information(data)
    cleaned_data = clean_dataset(data)
    save_cleaned_dataset(cleaned_data)


if __name__ == "__main__":
    main()
