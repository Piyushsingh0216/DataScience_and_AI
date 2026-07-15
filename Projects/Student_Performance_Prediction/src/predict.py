"""
Make predictions for new students using the saved Linear Regression model.

This file demonstrates how a beginner can load a trained model and predict
exam scores for new student records.
"""

import pickle
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "models" / "linear_regression.pkl"


def load_model(model_path=MODEL_PATH):
    """Load the saved model package from disk."""
    with open(model_path, "rb") as file:
        return pickle.load(file)


def prepare_new_data(new_data, feature_columns):
    """Convert new student data into the same format used during training."""
    new_data_encoded = pd.get_dummies(new_data, drop_first=True)
    new_data_encoded = new_data_encoded.reindex(columns=feature_columns, fill_value=0)
    return new_data_encoded


def predict_exam_score(new_student_data):
    """Predict exam scores for one or more new students."""
    model_package = load_model()
    model = model_package["model"]
    feature_columns = model_package["feature_columns"]

    prepared_data = prepare_new_data(new_student_data, feature_columns)
    predictions = model.predict(prepared_data)
    return predictions


def main():
    """Run a sample prediction for new students."""
    new_students = pd.DataFrame(
        [
            {
                "Hours_Studied": 7.5,
                "Attendance": 88,
                "Sleep_Hours": 7,
                "Previous_Score": 76,
                "Assignments_Completed": 9,
                "Internet_Access": "Yes",
                "Family_Income": "Medium",
            },
            {
                "Hours_Studied": 3,
                "Attendance": 62,
                "Sleep_Hours": 5.5,
                "Previous_Score": 55,
                "Assignments_Completed": 4,
                "Internet_Access": "No",
                "Family_Income": "Low",
            },
        ]
    )

    predictions = predict_exam_score(new_students)
    new_students["Predicted_Exam_Score"] = predictions.round(2)

    print("\nPredictions for new students:")
    print(new_students)


if __name__ == "__main__":
    main()
