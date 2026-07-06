from pathlib import Path

import pandas as pd

# Merge two csv files
base_dir = Path(__file__).resolve().parent
students_path = base_dir / 'students.csv'
department_path = base_dir / 'department.csv'

students_df = pd.read_csv(students_path)
department_df = pd.read_csv(department_path)

df = pd.merge(students_df, department_df, on='ID')
print(df)

# Remove duplicate records.
a = df.drop_duplicates()
print(a)

# Display department-wise statistics.
stats = (
    df.groupby('Department')['CGPA']
    .agg(['count', 'mean', 'min', 'max'])
    .rename(columns={'count': 'student_count', 'mean': 'avg_cgpa', 'min': 'min_cgpa', 'max': 'max_cgpa'})
)
print(stats)

# Top 5 students by CGPA
top_5_students = df.nlargest(5, 'CGPA')
print("--- Top 5 Students by CGPA ---")
print(top_5_students)

# Bottom 5 students
bottom_5_students = df.nsmallest(5, 'CGPA')
print("--- Bottom 5 Students by CGPA ---")
print(bottom_5_students)

# Average CGPA by Department
avg_cgpa = df.groupby('Department')['CGPA'].mean()
print("--- Average CGPA by Department ---")
print(avg_cgpa)

# Student count by City
city_counts = df['City'].value_counts()
print("--- Student Count by City ---")
print(city_counts)

# Create a pivot table summarizing department performance
dept_performance = pd.pivot_table(
    df, 
    index='Department',          # Groups the data by Department
    values='CGPA',               # The column we want to calculate math on
    aggfunc=['mean', 'max', 'min', 'count'] # The calculations to perform
)
dept_performance = dept_performance.round(2)

print("--- Department Performance Summary ---")
print(dept_performance)
