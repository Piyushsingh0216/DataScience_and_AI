# Student Performance Dashboard

## Project Overview

The Student Performance Dashboard is a beginner-friendly Python mini project that uses Pandas and CSV data handling to analyze student academic and attendance records. This project reads a student dataset, computes summary statistics, displays departmental and city-level insights, and saves a summary report as a CSV file.

## Features

- Load student data from `students.csv`
- Display total students, average CGPA, highest CGPA, lowest CGPA, and average attendance
- Show department-wise statistics using `groupby()`
- Show city-wise student count using `value_counts()`
- Display the top 10 students by CGPA
- Identify low performers with CGPA below 6.5
- Alert on attendance below 75%
- Generate `summary.csv` automatically when the dashboard runs

## Technologies Used

- Python
- Pandas
- CSV files

## Project Structure

```
Student_Performance_Dashboard/
├── dashboard.py
├── students.csv
├── summary.csv (generated automatically)
└── README.md
```

## How to Run

1. Make sure Python is installed on your computer.
2. Install Pandas if needed:
   ```bash
   pip install pandas
   ```
3. Open a terminal in the `Student_Performance_Dashboard` folder.
4. Run the dashboard:
   ```bash
   python dashboard.py
   ```

## Sample Output

```
============================================
       STUDENT PERFORMANCE DASHBOARD
============================================

Total Students: 50
Average CGPA: 7.92
Highest CGPA: 9.58
Lowest CGPA: 5.95
Average Attendance: 82.84
--------------------------------------------

------------ Department Statistics ----------
============================================
Department  Avg_CGPA  Highest_CGPA  Lowest_CGPA  Avg_Attendance  Students
      AI      9.15          9.58         8.01           91.33        12
     CSE      7.50          8.56         6.88           82.00        12
     Civil      8.15          8.77         7.78           85.33        10
     ECE      6.86          7.48         5.95           77.17        12
      ME      7.62          8.40         6.10           80.33        14

City-wise Student Count
Delhi       10
Lucknow     10
Mumbai      10
Kanpur      10
Gorakhpur   10
Noida       10

Top Performers
...
```

## Learning Outcomes

- Working with CSV files using Pandas
- Filtering and sorting DataFrame rows
- Using `groupby()` for aggregated statistics
- Counting values with `value_counts()`
- Writing clean and readable Python code with functions
- Generating output files automatically from a script

## Future Improvements

- Add user input options for filtering by department or city
- Add charts using Matplotlib or Plotly (after learning visuals)
- Create an interactive web dashboard using Flask or Streamlit
- Add more student details such as semester, project score, or lab attendance
