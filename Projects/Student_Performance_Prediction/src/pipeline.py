"""Reusable end-to-end machine learning pipeline."""

import logging
from dataclasses import asdict

from config import APP_LOG_PATH, DATA_PATH, LOG_DIR
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
    get_dataset_overview,
    get_numeric_statistics,
    prepare_features,
    split_dataset,
)
from utils import ensure_directory
from visualization import create_all_graphs, create_model_comparison_chart


def configure_logging() -> None:
    """Configure file logging once for internal error details."""
    ensure_directory(LOG_DIR)
    if not logging.getLogger().handlers:
        logging.basicConfig(
            filename=APP_LOG_PATH,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        )


def run_pipeline(create_graphs: bool = True) -> dict[str, object]:
    """Run loading, cleaning, training, evaluation, prediction, and export."""
    configure_logging()

    try:
        raw_data = load_dataset(DATA_PATH)
        raw_dataset_overview = get_dataset_overview(raw_data)
        cleaned_data, preprocessing_summary = clean_dataset(raw_data)
        numeric_statistics = get_numeric_statistics(cleaned_data)
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
            "dataset_overview": raw_dataset_overview,
            "numeric_statistics": numeric_statistics,
            "preprocessing_summary": asdict(preprocessing_summary),
            "comparison_data": comparison_data,
            "best_model_name": best_model_name,
            "prediction_results": prediction_results,
            "train_data": train_data,
            "test_data": test_data,
        }
    except Exception:
        logging.exception("Pipeline failed.")
        raise
