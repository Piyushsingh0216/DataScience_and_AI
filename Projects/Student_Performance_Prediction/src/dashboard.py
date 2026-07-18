"""Streamlit dashboard for Student Performance Prediction."""

import logging
from pathlib import Path
from typing import Any

import pandas as pd
import streamlit as st

from config import (
    APP_LOG_PATH,
    LOG_DIR,
    MODEL_COMPARISON_GRAPH_PATH,
    MODEL_COMPARISON_PATH,
    PREDICTIONS_PATH,
    PROCESSED_DATA_PATH,
    TEST_DATA_PATH,
    TRAIN_DATA_PATH,
)
from downloads import save_processed_data
from models import predict_exam_score
from pipeline import run_pipeline
from utils import ensure_directory


st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
)


def configure_dashboard_logging() -> None:
    """Configure dashboard logging for user-facing error handling."""
    ensure_directory(LOG_DIR)
    if not logging.getLogger().handlers:
        logging.basicConfig(
            filename=APP_LOG_PATH,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        )


@st.cache_data(show_spinner=False)
def load_dashboard_data() -> dict[str, object]:
    """Run the pipeline and cache the latest dashboard data."""
    return run_pipeline(create_graphs=True)


@st.cache_data(show_spinner=False)
def read_csv_file(file_path: str) -> bytes:
    """Read a CSV file as bytes for Streamlit download buttons."""
    return Path(file_path).read_bytes()


def format_metric(value: Any) -> str:
    """Format dashboard metric values consistently."""
    if isinstance(value, (float, int)) and not isinstance(value, bool):
        return f"{value:.3f}"
    return str(value)


def get_metric_status(metric_name: str, value: float) -> str:
    """Return a visual status class for regression metrics."""
    if metric_name == "R2 Score":
        if value >= 0.80:
            return "good"
        if value >= 0.50:
            return "average"
        return "poor"

    if metric_name in {"MAE", "RMSE"}:
        if value <= 5:
            return "good"
        if value <= 10:
            return "average"
        return "poor"

    return "neutral"


def inject_styles() -> None:
    """Apply dashboard-level styling."""
    st.markdown(
        """
        <style>
        .stApp {
            background: #F8FAFC;
            color: #0F172A;
            font-family: "Segoe UI", Arial, sans-serif;
        }
        .main .block-container {
            max-width: 1280px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }
        h1, h2, h3 {
            color: #0F172A;
            letter-spacing: 0;
        }
        .dashboard-subtitle {
            color: #475569;
            font-size: 1rem;
            margin-bottom: 1.2rem;
        }
        .section-divider {
            margin-top: 1.9rem;
            margin-bottom: 0.75rem;
        }
        .section-header {
            border-left: 4px solid #2563EB;
            padding-left: 0.8rem;
            margin: 1.4rem 0 0.8rem;
        }
        .section-header h3 {
            font-size: 1.35rem;
            margin: 0;
        }
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
            gap: 0.85rem;
            margin-bottom: 0.8rem;
        }
        .metric-card {
            min-height: 126px;
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 1rem;
            box-shadow: 0 1px 2px rgba(15, 23, 42, 0.06);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .metric-card.best {
            border-color: #22C55E;
            box-shadow: 0 0 0 2px rgba(34, 197, 94, 0.16);
        }
        .metric-label {
            color: #64748B;
            font-size: 0.84rem;
            font-weight: 650;
            margin-bottom: 0.35rem;
        }
        .metric-value {
            color: #0F172A;
            font-size: 1.45rem;
            font-weight: 760;
            line-height: 1.15;
            overflow-wrap: anywhere;
        }
        .status-pill {
            align-self: flex-start;
            border-radius: 999px;
            font-size: 0.72rem;
            font-weight: 700;
            padding: 0.18rem 0.55rem;
            margin-top: 0.75rem;
        }
        .status-good {
            background: #DCFCE7;
            color: #166534;
        }
        .status-average {
            background: #FEF3C7;
            color: #92400E;
        }
        .status-poor {
            background: #FEE2E2;
            color: #991B1B;
        }
        .status-neutral {
            background: #E0F2FE;
            color: #075985;
        }
        .table-wrap {
            overflow-x: auto;
            width: 100%;
        }
        div[data-testid="stDataFrame"] {
            overflow-x: auto;
        }
        div[data-testid="stDownloadButton"] > button {
            width: 100%;
            border-radius: 8px;
            border: 1px solid #CBD5E1;
            background: #FFFFFF;
            color: #0F172A;
            font-weight: 650;
        }
        div[data-testid="stDownloadButton"] > button:hover {
            border-color: #2563EB;
            color: #2563EB;
        }
        @media (max-width: 768px) {
            .main .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }
            .metric-card {
                min-height: 112px;
            }
            .metric-value {
                font-size: 1.25rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_section_header(title: str) -> None:
    """Render a consistent dashboard section header."""
    st.markdown(
        f'<div class="section-header"><h3>{title}</h3></div>',
        unsafe_allow_html=True,
    )


def render_cards(cards: list[dict[str, str]]) -> None:
    """Render responsive equal-sized metric cards."""
    html = ['<div class="cards-grid">']
    for card in cards:
        status = card.get("status", "neutral")
        best_class = " best" if card.get("highlight") == "true" else ""
        html.append(
            f"""
            <div class="metric-card{best_class}">
                <div>
                    <div class="metric-label">{card["label"]}</div>
                    <div class="metric-value">{card["value"]}</div>
                </div>
                <div class="status-pill status-{status}">{card["status_label"]}</div>
            </div>
            """
        )
    html.append("</div>")
    st.markdown("".join(html), unsafe_allow_html=True)


def render_dataset_overview(overview: dict[str, object]) -> None:
    """Render the dataset overview cards."""
    cards = [
        {
            "label": label,
            "value": str(value),
            "status": "neutral",
            "status_label": "Dataset",
        }
        for label, value in overview.items()
    ]
    render_cards(cards)


def render_model_evaluation_cards(
    comparison_data: pd.DataFrame,
    best_model_name: str,
) -> None:
    """Render evaluation cards for the best-performing model."""
    best_model = comparison_data.loc[
        comparison_data["Model"] == best_model_name
    ].iloc[0]
    metric_names = ["R2 Score", "MAE", "MSE", "RMSE"]
    cards = [
        {
            "label": "Model Name",
            "value": str(best_model_name),
            "status": "good",
            "status_label": "Best Model",
            "highlight": "true",
        }
    ]

    for metric_name in metric_names:
        metric_value = float(best_model[metric_name])
        status = get_metric_status(metric_name, metric_value)
        cards.append(
            {
                "label": metric_name,
                "value": format_metric(metric_value),
                "status": status,
                "status_label": status.title(),
                "highlight": "false",
            }
        )

    render_cards(cards)


def render_preprocessing_summary(summary: dict[str, object]) -> None:
    """Render the detailed feature engineering summary."""
    summary_items = [
        ("Original dataset shape", summary["original_dataset_shape"]),
        ("Final dataset shape", summary["final_dataset_shape"]),
        ("Features used for training", summary["features_selected"]),
        ("Target column", summary["target_column"]),
        ("Categorical columns encoded", summary["columns_encoded"]),
        ("Numerical columns scaled", summary["columns_scaled"]),
        ("Missing values handled", summary["missing_values_handled"]),
        ("Duplicate rows removed", summary["duplicate_rows_status"]),
        ("Feature selection method", summary["feature_selection_method"]),
        ("Train/Test split ratio", summary["train_test_split_ratio"]),
    ]
    cards = [
        {
            "label": label,
            "value": str(value) if value else "Not Applied",
            "status": "neutral" if value == "Not Applied" else "good",
            "status_label": "Info" if value != "Not Applied" else "Not Applied",
        }
        for label, value in summary_items
    ]
    render_cards(cards)


def highlight_best_model(row: pd.Series, best_model_name: str) -> list[str]:
    """Style the best model row in the comparison table."""
    if row["Model"] == best_model_name:
        best_model_style = (
            "background-color: #DCFCE7; color: #14532D; font-weight: 700"
        )
        return [best_model_style] * len(row)
    return [""] * len(row)


def render_download_button(label: str, file_path: Path, file_name: str) -> None:
    """Render one CSV download button if the file exists."""
    try:
        if file_path.exists():
            st.download_button(
                label=label,
                data=read_csv_file(str(file_path)),
                file_name=file_name,
                mime="text/csv",
                use_container_width=True,
            )
        else:
            st.button(label, disabled=True, use_container_width=True)
    except OSError:
        logging.exception("Download file could not be read: %s", file_path)
        st.button(label, disabled=True, use_container_width=True)


def render_processed_dataset_download(cleaned_data: pd.DataFrame) -> None:
    """Export and download the processed dataset with user feedback."""
    try:
        save_processed_data(cleaned_data)
        csv_data = read_csv_file(str(PROCESSED_DATA_PATH))
        downloaded = st.download_button(
            label="Download Processed Dataset",
            data=csv_data,
            file_name="processed_data.csv",
            mime="text/csv",
            use_container_width=True,
        )
        if downloaded:
            st.success(
                f"Processed dataset exported successfully to {PROCESSED_DATA_PATH}."
            )
    except Exception:
        logging.exception("Processed dataset export failed.")
        st.error("The processed dataset could not be exported. Please check the logs.")


def render_error_message(error: Exception) -> None:
    """Display a friendly error and log detailed diagnostics."""
    logging.exception("Dashboard failed to render.")
    st.error(str(error) or "The dashboard could not be loaded.")
    st.info(f"Detailed error logs are stored at: {APP_LOG_PATH}")


def render_prediction_form() -> None:
    """Collect user input for a single prediction and show the result."""
    render_section_header("Predict New Student Scores")
    st.caption("Use the saved model to estimate a new student's exam score.")

    with st.form("prediction_form", clear_on_submit=True):
        prediction_columns = st.columns(2)
        with prediction_columns[0]:
            hours_studied = st.number_input(
                "Hours Studied",
                min_value=0.0,
                max_value=20.0,
                value=6.5,
                step=0.5,
            )
            attendance = st.number_input(
                "Attendance (%)",
                min_value=0.0,
                max_value=100.0,
                value=85.0,
                step=1.0,
            )
            sleep_hours = st.number_input(
                "Sleep Hours",
                min_value=0.0,
                max_value=12.0,
                value=7.0,
                step=0.5,
            )
            previous_score = st.number_input(
                "Previous Score",
                min_value=0.0,
                max_value=100.0,
                value=74.0,
                step=1.0,
            )

        with prediction_columns[1]:
            assignments_completed = st.number_input(
                "Assignments Completed",
                min_value=0,
                max_value=20,
                value=8,
                step=1,
            )
            internet_access = st.selectbox("Internet Access", ["Yes", "No"])
            family_income = st.selectbox("Family Income", ["Low", "Medium", "High"])

        submitted = st.form_submit_button("Predict Score")
        if submitted:
            try:
                if not 0 <= assignments_completed <= 20:
                    raise ValueError(
                        "Assignments Completed must be between 0 and 20."
                    )
                prediction_input = pd.DataFrame(
                    [
                        {
                            "Hours_Studied": hours_studied,
                            "Attendance": attendance,
                            "Sleep_Hours": sleep_hours,
                            "Previous_Score": previous_score,
                            "Assignments_Completed": assignments_completed,
                            "Internet_Access": internet_access,
                            "Family_Income": family_income,
                        }
                    ]
                )
                prediction = predict_exam_score(prediction_input)[0]
                st.success(f"Predicted Exam Score: {prediction:.2f}")
            except Exception as exc:
                render_error_message(exc)


def main() -> None:
    """Render the Streamlit dashboard."""
    configure_dashboard_logging()
    inject_styles()

    st.title("Student Performance Dashboard")
    st.markdown(
        '<p class="dashboard-subtitle">'
        "Clean data, compare regression models, inspect predictions, and download "
        "the generated CSV outputs."
        "</p>",
        unsafe_allow_html=True,
    )

    try:
        with st.spinner("Running data pipeline..."):
            results = load_dashboard_data()
    except Exception as exc:
        render_error_message(exc)
        return

    render_section_header("Dataset Overview")
    render_dataset_overview(results["dataset_overview"])

    render_section_header("Numeric Statistics")
    st.dataframe(
        results["numeric_statistics"],
        use_container_width=True,
        hide_index=True,
    )

    render_section_header("Feature Engineering Summary")
    render_preprocessing_summary(results["preprocessing_summary"])

    render_section_header("Model Evaluation")
    st.caption(f"Best model by highest R2 Score: {results['best_model_name']}")
    render_model_evaluation_cards(
        results["comparison_data"],
        str(results["best_model_name"]),
    )

    render_prediction_form()

    render_section_header("Model Comparison Results")
    comparison_data = results["comparison_data"].copy()
    numeric_columns = ["MAE", "MSE", "RMSE", "R2 Score", "Training Time"]
    comparison_data[numeric_columns] = comparison_data[numeric_columns].round(3)
    styled_comparison = comparison_data.style.apply(
        highlight_best_model,
        best_model_name=results["best_model_name"],
        axis=1,
    )
    st.dataframe(styled_comparison, use_container_width=True, hide_index=True)

    chart_column, prediction_column = st.columns([1.15, 1])
    with chart_column:
        render_section_header("Model Metrics Chart")
        if MODEL_COMPARISON_GRAPH_PATH.exists():
            st.image(str(MODEL_COMPARISON_GRAPH_PATH), use_container_width=True)
        else:
            st.warning("The model comparison chart is not available yet.")

    with prediction_column:
        render_section_header("Prediction Preview")
        st.dataframe(
            results["prediction_results"].head(12),
            use_container_width=True,
            hide_index=True,
        )

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    render_section_header("Download CSV Outputs")
    download_columns = st.columns(5)
    download_items = [
        ("Download Processed Dataset", PROCESSED_DATA_PATH, "processed_data.csv"),
        ("Train Dataset", TRAIN_DATA_PATH, "train_data.csv"),
        ("Test Dataset", TEST_DATA_PATH, "test_data.csv"),
        ("Prediction Results", PREDICTIONS_PATH, "predictions.csv"),
        ("Model Comparison", MODEL_COMPARISON_PATH, "model_comparison.csv"),
    ]

    for index, (column, (label, path, file_name)) in enumerate(
        zip(download_columns, download_items)
    ):
        with column:
            if index == 0:
                render_processed_dataset_download(results["cleaned_data"])
            else:
                render_download_button(label, path, file_name)

    render_section_header("Cleaned Dataset Preview")
    st.dataframe(
        results["cleaned_data"].head(25),
        use_container_width=True,
        hide_index=True,
    )


if __name__ == "__main__":
    main()
