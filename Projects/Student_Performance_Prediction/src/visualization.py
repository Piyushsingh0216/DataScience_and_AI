"""Exploratory and model comparison visualizations."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from config import DATA_PATH, GRAPH_DIR, MODEL_COMPARISON_GRAPH_PATH
from data_loader import load_dataset
from utils import ensure_directory


def save_current_plot(file_name: str) -> None:
    """Save the current Matplotlib figure and close it."""
    ensure_directory(GRAPH_DIR)
    output_path = GRAPH_DIR / file_name
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"Saved graph: {output_path}")


def create_histogram(data: pd.DataFrame) -> None:
    """Create a histogram showing the distribution of exam scores."""
    plt.figure(figsize=(8, 5))
    plt.hist(data["Exam_Score"], bins=20, color="#2563EB", edgecolor="#111827")
    plt.title("Distribution of Exam Scores")
    plt.xlabel("Exam Score")
    plt.ylabel("Number of Students")
    save_current_plot("histogram_exam_scores.png")


def create_scatter_plot(data: pd.DataFrame) -> None:
    """Create a scatter plot comparing study hours and exam scores."""
    plt.figure(figsize=(8, 5))
    plt.scatter(
        data["Hours_Studied"],
        data["Exam_Score"],
        alpha=0.65,
        color="#059669",
    )
    plt.title("Hours Studied vs Exam Score")
    plt.xlabel("Hours Studied")
    plt.ylabel("Exam Score")
    save_current_plot("scatter_hours_vs_score.png")


def create_box_plot(data: pd.DataFrame) -> None:
    """Create a box plot for exam score outlier detection."""
    plt.figure(figsize=(7, 5))
    box_plot = plt.boxplot(data["Exam_Score"], orientation="vertical", patch_artist=True)
    box_plot["boxes"][0].set_facecolor("#F59E0B")
    plt.title("Box Plot of Exam Scores")
    plt.ylabel("Exam Score")
    save_current_plot("boxplot_exam_scores.png")


def create_correlation_heatmap(data: pd.DataFrame) -> None:
    """Create a correlation heatmap using only Matplotlib."""
    numeric_data = data.select_dtypes(include=[np.number])
    correlation = numeric_data.corr()

    plt.figure(figsize=(9, 7))
    plt.imshow(correlation, cmap="coolwarm", interpolation="nearest")
    plt.colorbar(label="Correlation")
    plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
    plt.yticks(range(len(correlation.columns)), correlation.columns)

    for row in range(len(correlation.columns)):
        for column in range(len(correlation.columns)):
            plt.text(
                column,
                row,
                f"{correlation.iloc[row, column]:.2f}",
                ha="center",
                va="center",
                color="#111827",
                fontsize=8,
            )

    plt.title("Correlation Heatmap")
    save_current_plot("correlation_heatmap.png")


def create_bar_graph(data: pd.DataFrame) -> None:
    """Create a bar graph comparing average score by internet access."""
    average_scores = data.groupby("Internet_Access")["Exam_Score"].mean()

    plt.figure(figsize=(7, 5))
    plt.bar(average_scores.index, average_scores.values, color=["#DC2626", "#0D9488"])
    plt.title("Average Exam Score by Internet Access")
    plt.xlabel("Internet Access")
    plt.ylabel("Average Exam Score")
    save_current_plot("bar_internet_access_scores.png")


def create_model_comparison_chart(comparison_data: pd.DataFrame) -> None:
    """Create a grouped bar chart comparing MAE, RMSE, and R2 Score."""
    ensure_directory(GRAPH_DIR)
    chart_data = comparison_data.set_index("Model")[["MAE", "RMSE", "R2 Score"]]
    ax = chart_data.plot(
        kind="bar",
        figsize=(10, 6),
        color=["#2563EB", "#F59E0B", "#059669"],
        width=0.78,
    )
    ax.set_title("Model Comparison")
    ax.set_xlabel("Model")
    ax.set_ylabel("Metric Value")
    ax.tick_params(axis="x", rotation=20)
    ax.legend(loc="best")
    plt.tight_layout()
    plt.savefig(MODEL_COMPARISON_GRAPH_PATH, dpi=150)
    plt.close()
    print(f"Saved graph: {MODEL_COMPARISON_GRAPH_PATH}")


def create_all_graphs(data: pd.DataFrame) -> None:
    """Create all exploratory data analysis graphs."""
    create_histogram(data)
    create_scatter_plot(data)
    create_box_plot(data)
    create_correlation_heatmap(data)
    create_bar_graph(data)


def main() -> None:
    """Run all visualization steps."""
    data = load_dataset(DATA_PATH)
    create_all_graphs(data)


if __name__ == "__main__":
    main()
