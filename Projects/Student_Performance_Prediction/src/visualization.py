"""
Exploratory data analysis for the Student Performance project.

This file creates beginner-friendly Matplotlib graphs and saves them inside
outputs/graphs. Each graph is also explained in the console.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "students.csv"
GRAPH_DIR = BASE_DIR / "outputs" / "graphs"


def load_data():
    """Load the cleaned dataset."""
    return pd.read_csv(DATA_PATH)


def save_current_plot(file_name):
    """Save the current Matplotlib figure and close it."""
    GRAPH_DIR.mkdir(parents=True, exist_ok=True)
    output_path = GRAPH_DIR / file_name
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"Saved graph: {output_path}")


def create_histogram(data):
    """Create a histogram showing the distribution of exam scores."""
    plt.figure(figsize=(8, 5))
    plt.hist(data["Exam_Score"], bins=20, color="#3A86FF", edgecolor="black")
    plt.title("Distribution of Exam Scores")
    plt.xlabel("Exam Score")
    plt.ylabel("Number of Students")
    save_current_plot("histogram_exam_scores.png")
    print("Histogram: Shows how exam scores are distributed among students.")


def create_scatter_plot(data):
    """Create a scatter plot comparing study hours and exam scores."""
    plt.figure(figsize=(8, 5))
    plt.scatter(
        data["Hours_Studied"],
        data["Exam_Score"],
        alpha=0.6,
        color="#2A9D8F",
    )
    plt.title("Hours Studied vs Exam Score")
    plt.xlabel("Hours Studied")
    plt.ylabel("Exam Score")
    save_current_plot("scatter_hours_vs_score.png")
    print(
        "Scatter Plot: Shows whether students who study more hours usually "
        "score higher."
    )


def create_box_plot(data):
    """Create a box plot for exam score outlier detection."""
    plt.figure(figsize=(7, 5))
    plt.boxplot(data["Exam_Score"], orientation="vertical", patch_artist=True)
    plt.title("Box Plot of Exam Scores")
    plt.ylabel("Exam Score")
    save_current_plot("boxplot_exam_scores.png")
    print("Box Plot: Helps identify spread, median, and possible outliers.")


def create_correlation_heatmap(data):
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
                color="black",
                fontsize=8,
            )

    plt.title("Correlation Heatmap")
    save_current_plot("correlation_heatmap.png")
    print(
        "Correlation Heatmap: Shows how strongly numeric features relate to "
        "each other and to Exam_Score."
    )


def create_bar_graph(data):
    """Create a bar graph comparing average score by internet access."""
    average_scores = data.groupby("Internet_Access")["Exam_Score"].mean()

    plt.figure(figsize=(7, 5))
    plt.bar(average_scores.index, average_scores.values, color=["#E76F51", "#06D6A0"])
    plt.title("Average Exam Score by Internet Access")
    plt.xlabel("Internet Access")
    plt.ylabel("Average Exam Score")
    save_current_plot("bar_internet_access_scores.png")
    print(
        "Bar Graph: Compares average exam scores for students with and "
        "without internet access."
    )


def main():
    """Run all visualization steps."""
    data = load_data()
    create_histogram(data)
    create_scatter_plot(data)
    create_box_plot(data)
    create_correlation_heatmap(data)
    create_bar_graph(data)


if __name__ == "__main__":
    main()
