"""Backward-compatible data cleaning script."""

from config import DATA_PATH
from data_loader import generate_student_dataset, load_dataset
from preprocessing import clean_dataset as clean_dataset_with_summary


def clean_dataset(data):
    """Clean missing values, duplicates, and data types."""
    cleaned_data, _ = clean_dataset_with_summary(data)
    return cleaned_data


def display_basic_information(data):
    """Display beginner-friendly dataset information."""
    print("\nFirst 5 rows:")
    print(data.head())
    print("\nDataset shape:")
    print(data.shape)
    print("\nDataset information:")
    data.info()
    print("\nSummary statistics:")
    print(data.describe())


def save_cleaned_dataset(data, file_path=DATA_PATH):
    """Save the cleaned dataset to CSV."""
    data.to_csv(file_path, index=False)
    print(f"\nCleaned dataset saved at: {file_path}")


def main() -> None:
    """Run all data loading and cleaning steps."""
    data = load_dataset()
    display_basic_information(data)
    cleaned_data, summary = clean_dataset_with_summary(data)
    save_cleaned_dataset(cleaned_data)

    print(f"\nDuplicates removed: {summary.duplicate_rows_removed}")
    print(f"Missing values after cleaning: {summary.missing_values_after}")


if __name__ == "__main__":
    main()
