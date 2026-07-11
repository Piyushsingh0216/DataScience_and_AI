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

# ---------------------------------------------------------
# 0. Mock Dataset Creation (Messy strings & varied CGPAs)
# ---------------------------------------------------------
data = {
    'student_name': ['  aLiCe smiTH  ', 'BOB jones\n', ' charlie BROWN', 'DaVid WilliAMS ', 'eve davis'],
    'major': ['  ComPuter ScIence ', 'mAth', '  PHYSICS', 'biology  ', 'ART history'],
    'CGPA': [3.8, 2.4, 3.1, 1.8, 3.9]
}
df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)
print("\n" + "="*50 + "\n")

# ---------------------------------------------------------
# 1. Create a Grade column from CGPA
# ---------------------------------------------------------
# Using a custom function and .apply() to assign letter grades
def assign_grade(cgpa):
    if cgpa >= 3.5: return 'A'
    elif cgpa >= 3.0: return 'B'
    elif cgpa >= 2.0: return 'C'
    else: return 'F'

df['Grade'] = df['CGPA'].apply(assign_grade)

# ---------------------------------------------------------
# 2. Create a Pass/Fail column
# ---------------------------------------------------------
# Using np.where() for a fast, vectorized conditional assignment
df['Status'] = np.where(df['CGPA'] >= 2.0, 'Pass', 'Fail')

# ---------------------------------------------------------
# 3. Categorize CGPA into ranges using cut()
# ---------------------------------------------------------
# cut() assigns data to specific, fixed bins that you define
bins = [0, 2.0, 3.0, 3.5, 4.0]
labels = ['Needs Work', 'Average', 'Good', 'Excellent']
df['CGPA_Range'] = pd.cut(df['CGPA'], bins=bins, labels=labels, include_lowest=True)

# ---------------------------------------------------------
# 4. Create quartiles using qcut()
# ---------------------------------------------------------
# qcut() divides the data into buckets based on sample quantiles (equal-sized groups)
df['CGPA_Quartile'] = pd.qcut(df['CGPA'], q=4, labels=['Q1 (Lowest)', 'Q2', 'Q3', 'Q4 (Highest)'])

# ---------------------------------------------------------
# 5. Clean and standardize string columns
# ---------------------------------------------------------
# Dynamically select all string ('object') columns, strip whitespace, and apply Title Case
string_cols = df.select_dtypes(include=['object']).columns
for col in string_cols:
    df[col] = df[col].str.strip().str.title()

print("--- Cleaned and Processed DataFrame ---")
print(df.to_string())

# ==========================================
# 0. Mock Data Setup
# ==========================================
# Creating a messy dataset with duplicates, inconsistent cases, and whitespaces
csv_data = """StudentID,Name,Department,CGPA,Age
101,Alice, comp sci ,9.2,20
102,Bob,math,8.5,21
103,Charlie,COMP SCI,7.8,22
104,Diana, physics ,9.5,20
101,Alice, comp sci ,9.2,20  
105,Eve,MATH,6.5,21
106,Frank,Physics,8.8,19
107,Grace, Comp Sci ,7.2,23
108,Hank,math,9.8,20
109,Ivy,  physics,5.9,21
110,Jack,comp sci,8.1,22
111,Karen,Math,7.5,20
112,Leo,Physics,9.1,21
113,Mona,comp sci,6.8,22
114,Nina, Biology ,8.4,20
115,Oscar,biology,6.1,23
"""

# Load the data into a DataFrame
df = pd.read_csv(io.StringIO(csv_data.strip()))
print("--- Original DataFrame Shape ---")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")

# ==========================================
# 1. Standardize Department Names
# ==========================================
# Strip leading/trailing whitespaces and convert to Title Case
df['Department'] = df['Department'].str.strip().str.title()

# ==========================================
# 2. Remove Duplicate Records
# ==========================================
# Drops exact duplicate rows (keeps the first occurrence by default)
df = df.drop_duplicates()

# ==========================================
# 3. Convert Numeric Columns to Appropriate Types
# ==========================================
# Enforce float for CGPA and integer for Age. 
# 'errors='coerce'' turns unparseable values into NaN.
df['CGPA'] = pd.to_numeric(df['CGPA'], errors='coerce')
df['Age'] = pd.to_numeric(df['Age'], errors='coerce').astype('Int64') 

print("--- Cleaned DataFrame Info ---")
df.info()
print("\n")

# ==========================================
# 4. Display Top 10 Students by CGPA
# ==========================================
# nlargest is highly optimized for finding top values
top_10 = df.nlargest(10, 'CGPA')
print("--- Top 10 Students by CGPA ---")
print(top_10[['Name', 'Department', 'CGPA']].to_string(index=False))
print("\n")

# ==========================================
# 5. Display Bottom 10 Students
# ==========================================
# nsmallest is highly optimized for finding bottom values
bottom_10 = df.nsmallest(10, 'CGPA')
print("--- Bottom 10 Students by CGPA ---")
print(bottom_10[['Name', 'Department', 'CGPA']].to_string(index=False))