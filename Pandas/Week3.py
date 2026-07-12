import pandas as pd
import numpy as np

# ---------------------------------------------------------
# SETUP: Creating a "messy" mock student dataset
# ---------------------------------------------------------
data = {
    'Student_ID': ['S001', 'S002', 'S003', 'S004', 'S005'],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Hours_Studied': [10, 15, np.nan, 20, 5],        # Missing 1 value
    'Attendance_Percentage': [90, 95, 80, 100, np.nan], # Missing 1 value
    'Previous_Score': [85, 88, 70, 92, 60],
    'Extracurriculars': [1, 0, 1, 1, 0],
    'Pass_Fail': [1, 1, 0, 1, 0]
}

# Load into DataFrame
df = pd.DataFrame(data)
print("--- Original Dataset ---")
print(df)
print("\n")

# ---------------------------------------------------------
# STEP 1: Remove unnecessary columns
# ---------------------------------------------------------
# Machine learning models only work with numbers, and names/IDs don't hold predictive value.
# We drop 'Student_ID' and 'Name'.
df_cleaned = df.drop(columns=['Student_ID', 'Name'])
print("--- After Removing Unnecessary Columns ---")
print(df_cleaned.head(), "\n")

# ---------------------------------------------------------
# STEP 2: Check (and handle) missing values
# ---------------------------------------------------------
# Checking for missing values
print("--- Missing Values Count ---")
print(df_cleaned.isnull().sum(), "\n")

# Handling missing values: We will fill the empty (NaN) spots with the average (mean) of that column
df_cleaned['Hours_Studied'] = df_cleaned['Hours_Studied'].fillna(df_cleaned['Hours_Studied'].mean())
df_cleaned['Attendance_Percentage'] = df_cleaned['Attendance_Percentage'].fillna(df_cleaned['Attendance_Percentage'].mean())

# ---------------------------------------------------------
# STEP 3: Separate features (X) and target (y)
# ---------------------------------------------------------
# X = Everything EXCEPT 'Pass_Fail'
X = df_cleaned.drop(columns=['Pass_Fail'])

# y = ONLY 'Pass_Fail'
y = df_cleaned['Pass_Fail']

print("--- Features (X) ---")
print(X.head(), "\n")
print("--- Target (y) ---")
print(y.head(), "\n")

# ---------------------------------------------------------
# STEP 4: Save the cleaned dataset
# ---------------------------------------------------------
# index=False ensures Pandas doesn't save the row numbers (0, 1, 2, 3...) as a new column
df_cleaned.to_csv('student_cleaned.csv', index=False)
print("✅ Cleaned dataset successfully saved as 'student_cleaned.csv'!")