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

# Create a sample DataFrame
data = {
    'Roll Number': [1001, 1002, 1003, 1004, 1005],
    'Name': ['Aarav', 'Priya', 'Rahul', 'Neha', 'Vikram'],
    'City': ['Mumbai', 'Delhi', 'Mumbai', 'Bangalore', 'Delhi'],
    'Department': ['Computer Science', 'Mechanical', 'Electrical', 'Civil', 'Computer Science'],
    'CGPA': [8.5, 7.2, 9.1, 6.8, 8.8]
}

df = pd.DataFrame(data)

# Filter for students from 'Mumbai'
mumbai_students = df[df['City'] == 'Mumbai']

print("--- Students from Mumbai ---")
print(mumbai_students)

# Filter for CGPA greater than 8.0
high_achievers = df[df['CGPA'] > 8.0]

print("--- Students with CGPA > 8.0 ---")
print(high_achievers)

# Define the function that assigns the grade
def calculate_grade(cgpa):
    if cgpa >= 9.0:
        return 'A+'
    elif cgpa >= 8.0:
        return 'A'
    elif cgpa >= 7.0:
        return 'B'
    else:
        return 'C'

# Apply the function to the CGPA column and assign it to a new 'Grade' column
df['Grade'] = df['CGPA'].apply(calculate_grade)

print("--- DataFrame with New Grade Column ---")
print(df)

# Filter using a query string (e.g., CGPA > 8 AND from Delhi)
# Note: String values inside the query need their own quotes
filtered_students = df.query("CGPA > 8.0 and City == 'Delhi'")

print("--- Filtered using query() ---")
print(filtered_students)

# Define the list of departments we care about
target_departments = ['Computer Science', 'Electrical']

# Use isin() to keep rows where the Department is in our target list
selected_departments = df[df['Department'].isin(target_departments)]

print("--- CS and Electrical Students ---")
print(selected_departments)

#1. Number of students
num_students = df.shape[0]
print(f"Number of students: {num_students}")

#2. Average CGPA
avg_cgpa = df['CGPA'].mean()
print(f"Average CGPA: {avg_cgpa}")

#3. Highest & Lowest CGPA
highest_cgpa = df['CGPA'].max()
lowest_cgpa = df['CGPA'].min()

print(f"Highest: {highest_cgpa}, Lowest: {lowest_cgpa}")

# To find the student with the highest CGPA:
top_student = df.loc[df['CGPA'].idxmax(), 'Name']

#4. Department-wise averages
dept_avg = df.groupby('Department')['CGPA'].mean()
print(dept_avg)

#5. Missing values
missing_data = df.isnull().sum()
print(missing_data)

#6. City-wise student count
city_counts = df['City'].value_counts()
print(city_counts)

# 1. Detect duplicates
duplicate_count = df.duplicated().sum()
print(f"Total duplicate rows: {duplicate_count}")

# 2. Remove duplicates
df_cleaned = df.drop_duplicates()
print(f"Rows after removing duplicates: {len(df_cleaned)}")

# 3. Identify missing values
print("\nMissing values per column:")
missing_data = df_cleaned.isnull().sum()
print(missing_data[missing_data > 0]) # Only print columns that actually have missing data

# 4. Find correlations
# Exclude non-numeric columns and ID column to compute a meaningful correlation matrix
numeric_cols = df_cleaned.select_dtypes(include=[np.number]).drop(columns=['Student_ID'])
correlation_matrix = numeric_cols.corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)