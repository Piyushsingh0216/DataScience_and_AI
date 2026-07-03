import pandas as pd


def load_student_data(csv_path):
    """Load student data from a CSV file."""
    try:
        return pd.read_csv(csv_path)
    except FileNotFoundError:
        print("CSV file not found.")
        return None


def print_title():
    """Print the dashboard title."""
    print("=" * 44)
    print("STUDENT PERFORMANCE DASHBOARD".center(44))
    print("=" * 44)
    print()


def calculate_summary(df):
    """Calculate summary statistics for the dashboard."""
    total_students = len(df)
    average_cgpa = round(df["CGPA"].mean(), 2)
    highest_cgpa = round(df["CGPA"].max(), 2)
    lowest_cgpa = round(df["CGPA"].min(), 2)
    average_attendance = round(df["Attendance"].mean(), 2)

    return {
        "Total Students": total_students,
        "Average CGPA": average_cgpa,
        "Highest CGPA": highest_cgpa,
        "Lowest CGPA": lowest_cgpa,
        "Average Attendance": average_attendance,
    }


def display_overview(summary):
    """Display the main statistics overview."""
    print("Total Students:", summary["Total Students"])
    print("Average CGPA:", summary["Average CGPA"])
    print("Highest CGPA:", summary["Highest CGPA"])
    print("Lowest CGPA:", summary["Lowest CGPA"])
    print("Average Attendance:", str(summary["Average Attendance"]) + "%")
    print("\n" + "-" * 44 + "\n")


def display_department_statistics(df):
    """Display department-wise statistics using groupby."""
    department_stats = df.groupby("Department").agg(
        Avg_CGPA=("CGPA", "mean"),
        Highest_CGPA=("CGPA", "max"),
        Lowest_CGPA=("CGPA", "min"),
        Avg_Attendance=("Attendance", "mean"),
        Students=("Student_ID", "count"),
    )

    department_stats = department_stats.round({"Avg_CGPA": 2, "Avg_Attendance": 2})
    print("=" * 44)
    print("------------ Department Statistics ----------".center(44))
    print("=" * 44)
    print(department_stats.reset_index().to_string(index=False))
    print("\n" + "-" * 44 + "\n")


def display_city_counts(df):
    """Display the number of students in each city."""
    city_counts = df["City"].value_counts()
    print("City-wise Student Count")
    print(city_counts.to_string())
    print("\n" + "-" * 44 + "\n")


def display_top_performers(df):
    """Display the top 10 students by CGPA."""
    top_students = df.sort_values(by="CGPA", ascending=False).head(10)
    print("Top Performers")
    print(top_students[["Student_ID", "Name", "Department", "CGPA"]].to_string(index=False))
    print("\n" + "-" * 44 + "\n")


def display_low_performers(df):
    """Display students with CGPA below 6.5."""
    low_students = df[df["CGPA"] < 6.5]
    print("Low Performers (CGPA below 6.5)")
    if low_students.empty:
        print("No students found with CGPA below 6.5.")
    else:
        print(low_students[["Student_ID", "Name", "Department", "CGPA", "Attendance"]].to_string(index=False))
    print("\n" + "-" * 44 + "\n")


def display_attendance_alert(df):
    """Display students with attendance below 75%."""
    low_attendance = df[df["Attendance"] < 75]
    print("Attendance Alert (Attendance below 75%)")
    if low_attendance.empty:
        print("No students found with attendance below 75%.")
    else:
        print(low_attendance[["Student_ID", "Name", "Department", "Attendance", "CGPA"]].to_string(index=False))
    print("\n" + "-" * 44 + "\n")


def save_summary(csv_path, summary):
    """Save summary statistics to a CSV file."""
    summary_df = pd.DataFrame(
        {
            "Metric": list(summary.keys()),
            "Value": list(summary.values()),
        }
    )
    summary_df.to_csv(csv_path, index=False)


def run_dashboard():
    """Run the dashboard and generate the summary CSV."""
    csv_path = "students.csv"
    summary_path = "summary.csv"

    df = load_student_data(csv_path)
    if df is None:
        return

    print_title()
    summary = calculate_summary(df)
    display_overview(summary)
    display_department_statistics(df)
    display_city_counts(df)
    display_top_performers(df)
    display_low_performers(df)
    display_attendance_alert(df)
    save_summary(summary_path, summary)
    print(f"Summary report saved to {summary_path}")


if __name__ == "__main__":
    run_dashboard()
