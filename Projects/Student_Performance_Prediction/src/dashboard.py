"""Streamlit dashboard for Student Performance Prediction."""

from pathlib import Path

import pandas as pd
import streamlit as st

from config import (
    MODEL_COMPARISON_GRAPH_PATH,
    MODEL_COMPARISON_PATH,
    PREDICTIONS_PATH,
    PROCESSED_DATA_PATH,
    TEST_DATA_PATH,
    TRAIN_DATA_PATH,
)
from pipeline import run_pipeline


st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="📊",
    layout="wide",
)


def load_dashboard_data() -> dict[str, object]:
    """Run the pipeline and cache the latest dashboard data."""
    return run_pipeline(create_graphs=True)


@st.cache_data(show_spinner=False)
def read_csv_file(file_path: str) -> bytes:
    """Read a CSV file as bytes for Streamlit download buttons."""
    return Path(file_path).read_bytes()


def inject_styles() -> None:
    """Apply dashboard-level styling."""
    st.markdown(
        """
        <style>
        .stApp {
            background: #F8FAFC;
            color: #0F172A;
            font-family: "Segoe UI", sans-serif;
        }
        .main .block-container {
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
        .metric-card {
            min-height: 128px;
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 1.1rem;
            box-shadow: 0 1px 2px rgba(15, 23, 42, 0.06);
        }
        .metric-icon {
            font-size: 1.25rem;
            margin-bottom: 0.35rem;
        }
        .metric-label {
            color: #64748B;
            font-size: 0.86rem;
            font-weight: 600;
            margin-bottom: 0.35rem;
        }
        .metric-value {
            color: #0F172A;
            font-size: 1.65rem;
            font-weight: 750;
            line-height: 1.1;
            word-break: break-word;
        }
        .section-divider {
            margin-top: 1.8rem;
            margin-bottom: 0.6rem;
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
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_summary_cards(summary: dict[str, object]) -> None:
    """Render preprocessing summary cards."""
    cards = [
        ("▦", "Total Rows", summary["total_rows"]),
        ("▤", "Total Columns", summary["total_columns"]),
        ("!", "Missing Before", summary["missing_values_before"]),
        ("✓", "Missing After", summary["missing_values_after"]),
        ("−", "Duplicates Removed", summary["duplicate_rows_removed"]),
        ("ƒ", "Number of Features", summary["number_of_features"]),
        ("◎", "Target Column", summary["target_column"]),
        ("⇄", "Train/Test Split", summary["train_test_split_ratio"]),
    ]

    for row_start in range(0, len(cards), 4):
        columns = st.columns(4)
        for column, (icon, label, value) in zip(columns, cards[row_start : row_start + 4]):
            with column:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-icon">{icon}</div>
                        <div class="metric-label">{label}</div>
                        <div class="metric-value">{value}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


def highlight_best_model(row: pd.Series, best_model_name: str) -> list[str]:
    """Style the best model row in the comparison table."""
    if row["Model"] == best_model_name:
        return ["background-color: #DCFCE7; color: #14532D; font-weight: 700"] * len(row)
    return [""] * len(row)


def render_download_button(label: str, file_path: Path, file_name: str) -> None:
    """Render one CSV download button if the file exists."""
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


def main() -> None:
    """Render the Streamlit dashboard."""
    inject_styles()

    st.title("Student Performance Dashboard")
    st.markdown(
        '<p class="dashboard-subtitle">'
        "Clean data, compare regression models, inspect predictions, and download "
        "the generated CSV outputs."
        "</p>",
        unsafe_allow_html=True,
    )

    with st.spinner("Running data pipeline..."):
        results = load_dashboard_data()

    st.markdown("### Preprocessing Summary")
    render_summary_cards(results["preprocessing_summary"])

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown("### Model Comparison Results")
    st.caption(f"Best model by highest R2 Score: {results['best_model_name']}")

    comparison_data = results["comparison_data"].copy()
    numeric_columns = ["MAE", "MSE", "RMSE", "R2 Score", "Training Time"]
    comparison_data[numeric_columns] = comparison_data[numeric_columns].round(4)
    styled_comparison = comparison_data.style.apply(
        highlight_best_model,
        best_model_name=results["best_model_name"],
        axis=1,
    )
    st.dataframe(styled_comparison, use_container_width=True, hide_index=True)

    chart_column, prediction_column = st.columns([1.15, 1])
    with chart_column:
        st.markdown("### Model Metrics Chart")
        if MODEL_COMPARISON_GRAPH_PATH.exists():
            st.image(str(MODEL_COMPARISON_GRAPH_PATH), use_container_width=True)

    with prediction_column:
        st.markdown("### Prediction Preview")
        st.dataframe(
            results["prediction_results"].head(12),
            use_container_width=True,
            hide_index=True,
        )

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown("### Download CSV Outputs")
    download_columns = st.columns(5)
    download_items = [
        ("Cleaned Dataset", PROCESSED_DATA_PATH, "processed_data.csv"),
        ("Train Dataset", TRAIN_DATA_PATH, "train_data.csv"),
        ("Test Dataset", TEST_DATA_PATH, "test_data.csv"),
        ("Prediction Results", PREDICTIONS_PATH, "predictions.csv"),
        ("Model Comparison", MODEL_COMPARISON_PATH, "model_comparison.csv"),
    ]

    for column, (label, path, file_name) in zip(download_columns, download_items):
        with column:
            render_download_button(label, path, file_name)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown("### Cleaned Dataset Preview")
    st.dataframe(results["cleaned_data"].head(25), use_container_width=True, hide_index=True)


if __name__ == "__main__":
    main()
