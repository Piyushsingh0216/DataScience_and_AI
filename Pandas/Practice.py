
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

# 1. read_csv() - Load your data
df = pd.read_csv('student_data.csv')
print("Original DataFrame:\n", df)

# 2. head() - View first 3 rows
print("\n--- head(3) ---")
print(df.head(3))

# 3. tail() - View last 2 rows
print("\n--- tail(2) ---")
print(df.tail(2))

# 4. shape - Dimensions (rows, columns)
print("\n--- shape ---")
print(df.shape)  # Output will be (5, 4)

# 5. columns - View column names
print("\n--- columns ---")
print(df.columns) 

# 6. isnull() - Check for missing data
print("\n--- isnull() ---")
print(df.isnull()) # In your dataset, all of these will be False since there is no missing data!

# 7. dropna() - Drop rows with missing data
print("\n--- 2. dropna() ---")# This will drop ANY row that has at least one missing value
print(df.dropna())

# 8. fillna() - Fill missing data
print("\n--- 3. fillna() ---")

# Let's say we don't want to delete the rows, we want to fix them.
# We can fill missing Ages with the average age, missing Courses with 'Unknown', 
# and missing Marks with a 0.

avg_age = df['Age'].mean()

# We pass a dictionary to tell pandas exactly what to put in each column's blanks
df_filled = df.fillna({
    'Age': avg_age,
    'Course': 'Unknown',
    'Marks': 0
})

print(df_filled)

# 9. sort_values() - Sort by Marks
print("\n--- sort_values() (Sorted by Marks descending) ---")
print(df.sort_values(by='Marks', ascending=False))

# 1. Highest Marks
highest_marks = df['Marks'].max()
print("Highest Marks:", highest_marks) 
# Output: 95

# 2. Lowest Marks
lowest_marks = df['Marks'].min()
print("Lowest Marks:", lowest_marks) 
# Output: 75

# 3. Average Marks
average_marks = df['Marks'].mean()
print("Average Marks:", average_marks) 
# Output: 86.8

# 4. Students above 80 Marks
above_80 = df[df['Marks'] > 80]
print("\nStudents above 80 Marks:\n", above_80)
# Output:
#      Name  Age Course  Marks
# 0  Piyush   21    CSE     88
# 2    Aman   22    CSE     91
# 3   Sneha   19    ECE     85
# 4    Riya   23    CSE     95

# 5. Students from one specific branch (CSE)
cse_students = df[df['Course'] == 'CSE']
print("\nStudents from CSE branch:\n", cse_students)
# Output:
#      Name  Age Course  Marks
# 0  Piyush   21    CSE     88
# 2    Aman   22    CSE     91
# 4    Riya   23    CSE     95