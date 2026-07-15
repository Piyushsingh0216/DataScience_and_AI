"""
Train and evaluate a Linear Regression model for student score prediction.

This file loads the cleaned dataset, prepares features and target, splits the
data, trains LinearRegression, evaluates it, and saves the model with pickle.
"""

import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "students.csv"
MODEL_PATH = BASE_DIR / "models" / "linear_regression.pkl"
PREDICTIONS_PATH = BASE_DIR / "outputs" / "predictions.csv"
RANDOM_STATE = 42


FEATURE_COLUMNS = [
    "Hours_Studied",
    "Attendance",
    "Sleep_Hours",
    "Previous_Score",
    "Assignments_Completed",
    "Internet_Access",
    "Family_Income",
]
TARGET_COLUMN = "Exam_Score"


def load_data():
    """Load the cleaned student dataset."""
    return pd.read_csv(DATA_PATH)


def prepare_features(data):
    """
    Separate X and y, then convert categorical columns into numeric columns.

    Linear Regression needs numeric values, so Pandas get_dummies is used for
    Internet_Access and Family_Income.
    """
    x = data[FEATURE_COLUMNS]
    y = data[TARGET_COLUMN]
    x_encoded = pd.get_dummies(x, drop_first=True)
    return x_encoded, y


def split_data(x, y):
    """Split the data into training and testing sets."""
    return train_test_split(x, y, test_size=0.2, random_state=RANDOM_STATE)


def train_model(x_train, y_train):
    """Train a Linear Regression model."""
    model = LinearRegression()
    model.fit(x_train, y_train)
    return model


def evaluate_model(model, x_test, y_test):
    """Evaluate the model using common regression metrics."""
    predictions = model.predict(x_test)

    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)

    print("\nModel Evaluation Results")
    print(f"MAE: {mae:.2f} - Average absolute prediction error.")
    print(f"MSE: {mse:.2f} - Average squared prediction error.")
    print(f"RMSE: {rmse:.2f} - Error in the same unit as Exam_Score.")
    print(f"R2 Score: {r2:.2f} - Percentage of score variation explained.")

    return predictions, {"MAE": mae, "MSE": mse, "RMSE": rmse, "R2": r2}


def save_model(model, feature_columns, model_path=MODEL_PATH):
    """Save the trained model and feature column order using pickle."""
    model_path.parent.mkdir(parents=True, exist_ok=True)
    model_package = {"model": model, "feature_columns": list(feature_columns)}

    with open(model_path, "wb") as file:
        pickle.dump(model_package, file)

    print(f"\nModel saved at: {model_path}")


def save_predictions(x_test, y_test, predictions):
    """Save actual and predicted scores to a CSV file."""
    results = x_test.copy()
    results["Actual_Exam_Score"] = y_test.values
    results["Predicted_Exam_Score"] = predictions.round(2)

    PREDICTIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(PREDICTIONS_PATH, index=False)
    print(f"Predictions saved at: {PREDICTIONS_PATH}")


def main():
    """Run the full model training workflow."""
    data = load_data()
    x, y = prepare_features(data)
    x_train, x_test, y_train, y_test = split_data(x, y)
    model = train_model(x_train, y_train)
    predictions, _ = evaluate_model(model, x_test, y_test)
    save_model(model, x.columns)
    save_predictions(x_test, y_test, predictions)


if __name__ == "__main__":
    main()
