
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
print(df.isnull()) # In dataset, all of these will be False since there is no missing data!

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

print("--- 1. Original Dataset ---")
print(df)
print("\nMissing Values Count:")
print(df.isnull().sum())

# 2. Data Cleaning
# Drop rows where all three critical columns (Age, Course, Marks) are missing (drops Zara)
df_clean = df.dropna(subset=['Age', 'Course', 'Marks'], how='all').copy()

# Fill missing Age with the median age of the remaining students
median_age = df_clean['Age'].median()
df_clean['Age'] = df_clean['Age'].fillna(median_age)

# Fill missing Course with 'Unknown'
df_clean['Course'] = df_clean['Course'].fillna('Unknown')

# Fill missing Marks with the average marks of the class
mean_marks = df_clean['Marks'].mean()
df_clean['Marks'] = df_clean['Marks'].fillna(mean_marks)

print("\n--- 2. Cleaned Dataset ---")
print(df_clean)

# 3. Extracting Insights
print("\n--- 3. Dataset Insights ---")
print(f"Total valid students: {len(df_clean)}")
print(f"Average Marks: {df_clean['Marks'].mean():.2f}")
print(f"Highest Marks: {df_clean['Marks'].max()} (Scored by: {df_clean.loc[df_clean['Marks'].idxmax(), 'Name']})")

print("\nStudents scoring above 85:")
print(df_clean[df_clean['Marks'] > 85][['Name', 'Marks']])

print("\nAverage Marks by Course:")
print(df_clean.groupby('Course')['Marks'].mean().round(2).to_string())

# 1. Create a mock student dataset
data = {
    'Student_ID': range(1, 13),
    'Name': ['Aarav', 'Neha', 'Rohan', 'Priya', 'Aditya', 'Kavya', 
             'Vikram', 'Sneha', 'Rahul', 'Ananya', 'Karan', 'Meera'],
    'Department': ['CSE (AI)', 'Data Science', 'CSE (AI)', 'Mechanical', 'CSE (Core)', 
                   'Data Science', 'CSE (AI)', 'CSE (Core)', 'Mechanical', 'CSE (AI)', 
                   'CSE (Core)', 'Data Science'],
    'CGPA': [9.4, 6.8, 8.5, 7.1, 9.6, 6.5, 8.8, 7.9, 6.2, 9.8, 8.1, 9.1],
    'City': ['Lucknow', 'Delhi', 'Gorakhpur', 'Lucknow', 'Pune', 
             'Delhi', 'Gorakhpur', 'Pune', 'Lucknow', 'Gorakhpur', 
             'Delhi', 'Pune']
}

df = pd.DataFrame(data)


# 1. Total number of students
# Function used: count()
total_students = df['Student_ID'].count()
print(f"Total Students: {total_students}")

# 2. Average CGPA
# Function used: mean()
avg_cgpa = df['CGPA'].mean()
print(f"Average CGPA: {avg_cgpa:.2f}")

# 3. Highest CGPA
# Function used: max()
highest_cgpa = df['CGPA'].max()
print(f"Highest CGPA: {highest_cgpa}")

# 4. Lowest CGPA
# Function used: min()
lowest_cgpa = df['CGPA'].min()
print(f"Lowest CGPA: {lowest_cgpa}")

# 5. Students with CGPA above 9
# Functions used: count() with boolean masking
above_9 = df[df['CGPA'] > 9]['Student_ID'].count()
print(f"Students with CGPA > 9: {above_9}")

# 6. Students below 7
# Functions used: count() with boolean masking
below_7 = df[df['CGPA'] < 7]['Student_ID'].count()
print(f"Students with CGPA < 7: {below_7}")

print("\n--- Department-wise Student Count ---")
# 7. Department-wise student count
# Functions used: groupby(), count()
dept_count = df.groupby('Department')['Student_ID'].count()
print(dept_count)

print("\n--- Department-wise Average CGPA (Sorted) ---")
# 8. Department-wise average CGPA
# Functions used: groupby(), mean(), sort_values()
dept_avg_cgpa = df.groupby('Department')['CGPA'].mean().sort_values(ascending=False)
print(dept_avg_cgpa)

print("\n--- City-wise Student Distribution ---")
# 9. City-wise student distribution
# Function used: value_counts()
city_dist = df['City'].value_counts()
print(city_dist)