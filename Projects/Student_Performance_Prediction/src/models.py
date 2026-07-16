"""Model training, comparison, prediction, and persistence."""

import pickle
import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

from config import BEST_MODEL_PATH, LINEAR_MODEL_PATH, RANDOM_STATE
from evaluation import evaluate_regression_model, get_best_model_name


def build_models() -> dict[str, object]:
    """Create the regression models used in the comparison."""
    return {
        "Linear Regression": LinearRegression(),
        "Decision Tree Regressor": DecisionTreeRegressor(random_state=RANDOM_STATE),
        "Random Forest Regressor": RandomForestRegressor(
            n_estimators=150,
            random_state=RANDOM_STATE,
        ),
    }


def train_and_compare_models(
    x_train: pd.DataFrame,
    x_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
) -> tuple[dict[str, object], pd.DataFrame, str, np.ndarray]:
    """Train all models, evaluate them, and return the best model details."""
    trained_models = {}
    metrics = []
    predictions_by_model = {}

    for model_name, model in build_models().items():
        start_time = time.perf_counter()
        model.fit(x_train, y_train)
        training_time = time.perf_counter() - start_time

        predictions = model.predict(x_test)
        trained_models[model_name] = model
        predictions_by_model[model_name] = predictions
        metrics.append(
            evaluate_regression_model(model_name, y_test, predictions, training_time)
        )

    comparison_data = pd.DataFrame(metrics).sort_values(
        by="R2 Score",
        ascending=False,
    )
    best_model_name = get_best_model_name(comparison_data)
    best_predictions = predictions_by_model[best_model_name]

    return trained_models, comparison_data, best_model_name, best_predictions


def save_model_package(
    model: object,
    feature_columns: pd.Index,
    model_path: Path,
    model_name: str,
) -> None:
    """Save a trained model with the feature column order."""
    model_path.parent.mkdir(parents=True, exist_ok=True)
    model_package = {
        "model": model,
        "model_name": model_name,
        "feature_columns": list(feature_columns),
    }

    with open(model_path, "wb") as file:
        pickle.dump(model_package, file)


def save_compatible_models(
    trained_models: dict[str, object],
    best_model_name: str,
    feature_columns: pd.Index,
) -> None:
    """Save the best model and preserve the existing Linear Regression file."""
    save_model_package(
        trained_models[best_model_name],
        feature_columns,
        BEST_MODEL_PATH,
        best_model_name,
    )
    save_model_package(
        trained_models["Linear Regression"],
        feature_columns,
        LINEAR_MODEL_PATH,
        "Linear Regression",
    )


def load_model_package(model_path: Path = LINEAR_MODEL_PATH) -> dict[str, object]:
    """Load a saved model package from disk."""
    with open(model_path, "rb") as file:
        return pickle.load(file)


def prepare_new_data(new_data: pd.DataFrame, feature_columns: list[str]) -> pd.DataFrame:
    """Convert new student data into the same format used during training."""
    new_data_encoded = pd.get_dummies(new_data, drop_first=True)
    return new_data_encoded.reindex(columns=feature_columns, fill_value=0)


def predict_exam_score(new_student_data: pd.DataFrame) -> np.ndarray:
    """Predict exam scores for one or more new students."""
    model_package = load_model_package()
    prepared_data = prepare_new_data(
        new_student_data,
        model_package["feature_columns"],
    )
    return model_package["model"].predict(prepared_data)
