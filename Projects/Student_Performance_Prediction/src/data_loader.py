"""Dataset loading and sample data generation."""

from pathlib import Path

import numpy as np
import pandas as pd

from config import DATA_PATH, RANDOM_STATE


def generate_student_dataset(file_path: Path = DATA_PATH, rows: int = 1200) -> None:
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

    duplicates = data.sample(n=15, random_state=RANDOM_STATE)
    data = pd.concat([data, duplicates], ignore_index=True)

    file_path.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(file_path, index=False)


def load_dataset(file_path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the student dataset, generating it first when needed."""
    if not file_path.exists():
        generate_student_dataset(file_path)

    return pd.read_csv(file_path)
