"""Reusable end-to-end machine learning pipeline."""

from dataclasses import asdict

from config import DATA_PATH
from data_loader import load_dataset
from downloads import (
    save_model_comparison,
    save_predictions,
    save_processed_data,
    save_train_test_data,
)
from models import save_compatible_models, train_and_compare_models
from preprocessing import (
    clean_dataset,
    combine_features_and_target,
    prepare_features,
    split_dataset,
)
from visualization import create_all_graphs, create_model_comparison_chart


def run_pipeline(create_graphs: bool = True) -> dict[str, object]:
    """Run loading, cleaning, training, evaluation, prediction, and export."""
    raw_data = load_dataset(DATA_PATH)
    cleaned_data, preprocessing_summary = clean_dataset(raw_data)
    features, target = prepare_features(cleaned_data)
    x_train, x_test, y_train, y_test = split_dataset(features, target)

    trained_models, comparison_data, best_model_name, predictions = (
        train_and_compare_models(x_train, x_test, y_train, y_test)
    )

    train_data = combine_features_and_target(x_train, y_train)
    test_data = combine_features_and_target(x_test, y_test)
    prediction_results = save_predictions(x_test, y_test, predictions)

    save_processed_data(cleaned_data)
    save_train_test_data(train_data, test_data)
    save_model_comparison(comparison_data)
    save_compatible_models(trained_models, best_model_name, features.columns)

    if create_graphs:
        create_all_graphs(cleaned_data)
        create_model_comparison_chart(comparison_data)

    return {
        "raw_data": raw_data,
        "cleaned_data": cleaned_data,
        "preprocessing_summary": asdict(preprocessing_summary),
        "comparison_data": comparison_data,
        "best_model_name": best_model_name,
        "prediction_results": prediction_results,
        "train_data": train_data,
        "test_data": test_data,
    }
