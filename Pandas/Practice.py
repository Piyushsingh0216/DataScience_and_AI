
import pandas as pd

# 1. Create the sample data
data = {
    'Student Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Age': [20, 21, 19, 22, 20, 21, 19],
    'Branch': ['CSE', 'Mechanical', 'Electrical', 'Civil', 'CSE', 'Mechanical', 'IT'],
    'CGPA': [8.5, 7.2, 9.1, 6.8, 8.9, 7.5, 9.3]
}

# 2. Create the DataFrame
df = pd.DataFrame(data)

print("--- Full DataFrame ---")
print(df)
print("\n")

# --- Practice: head() ---
# Returns the first 5 rows of the DataFrame by default. 
# Useful for a quick glance at the top of your data.
print("--- df.head() ---")
print(df.head())
print("\n")

# --- Practice: tail() ---
# Returns the last 5 rows of the DataFrame by default.
# Useful to verify the end of your dataset.
print("--- df.tail() ---")
print(df.tail())
print("\n")

# --- Practice: info() ---
# Prints a concise summary of the DataFrame, including the index dtype, 
# column dtypes, non-null values, and memory usage.
print("--- df.info() ---")
df.info() 
print("\n")

# --- Practice: describe() ---
# Generates descriptive statistics (count, mean, standard deviation, min, max, quartiles)
# Note: By default, this only applies to numerical columns (Age and CGPA).
print("--- df.describe() ---")
print(df.describe())
print("\n")

# --- Practice: shape ---
# Returns a tuple representing the dimensionality of the DataFrame (rows, columns).
# Note: shape is an attribute, not a method, so it does not use parentheses ().
print("--- df.shape ---")
print(f"The DataFrame has {df.shape[0]} rows and {df.shape[1]} columns.")
print(df.shape)

# Read the CSV file
students = pd.read_csv("students.csv")

# Display the first 5 rows
print("First 5 Rows:")
print(students.head())

# Display the last 5 rows
print("\nLast 5 Rows:")
print(students.tail())

# Information about the dataset
print("\nDataset Information:")
students.info()

# Statistical summary
print("\nStatistical Summary:")
print(students.describe())

# Shape of the dataset
print("\nShape:")
print(students.shape)

# Column names
print("\nColumns:")
print(students.columns)

# Display only one column
print("\nName Column:")
print(students["Name"])

# Display two columns
print("\nName and Marks:")
print(students[["Name", "Marks"]])

# Filter rows where Age > 20
print("\nStudents with Age > 20:")
print(students[students["Age"] > 20])