"""Make predictions for new students using the saved Linear Regression model."""

import pandas as pd

from models import load_model_package, predict_exam_score, prepare_new_data


def load_model():
    """Load the saved model package from disk."""
    return load_model_package()


def main() -> None:
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
