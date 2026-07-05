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
