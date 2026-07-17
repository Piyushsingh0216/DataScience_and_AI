"""Shared project settings and file paths."""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models"
OUTPUT_DIR = BASE_DIR / "outputs"
GRAPH_DIR = OUTPUT_DIR / "graphs"
LOG_DIR = BASE_DIR / "logs"

DATA_PATH = DATA_DIR / "students.csv"
LINEAR_MODEL_PATH = MODEL_DIR / "linear_regression.pkl"
BEST_MODEL_PATH = MODEL_DIR / "best_model.pkl"

PROCESSED_DATA_PATH = OUTPUT_DIR / "processed_data.csv"
TRAIN_DATA_PATH = OUTPUT_DIR / "train_data.csv"
TEST_DATA_PATH = OUTPUT_DIR / "test_data.csv"
PREDICTIONS_PATH = OUTPUT_DIR / "predictions.csv"
MODEL_COMPARISON_PATH = OUTPUT_DIR / "model_comparison.csv"
MODEL_COMPARISON_GRAPH_PATH = GRAPH_DIR / "model_comparison.png"
APP_LOG_PATH = LOG_DIR / "app.log"

RANDOM_STATE = 42
TEST_SIZE = 0.2
TARGET_COLUMN = "Exam_Score"

FEATURE_COLUMNS = [
    "Hours_Studied",
    "Attendance",
    "Sleep_Hours",
    "Previous_Score",
    "Assignments_Completed",
    "Internet_Access",
    "Family_Income",
]

NUMERIC_COLUMNS = [
    "Hours_Studied",
    "Attendance",
    "Sleep_Hours",
    "Previous_Score",
    "Assignments_Completed",
    "Exam_Score",
]

CATEGORICAL_COLUMNS = ["Internet_Access", "Family_Income"]
