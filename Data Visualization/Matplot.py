from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Distribution Histogram
base_dir = Path(__file__).resolve().parent
csv_path = base_dir / 'students.csv'
df = pd.read_csv(csv_path)

series = pd.to_numeric(df['CGPA'], errors='coerce').dropna()
plt.hist(series, bins=20, edgecolor='black')
plt.xlabel('CGPA')
plt.ylabel('Frequency')
plt.title('CGPA Distribution')
plt.show()

# Students per Department Bar Chart
department_counts = df['Department'].value_counts()
plt.bar(department_counts.index, department_counts.values)
plt.xlabel('Department')
plt.ylabel('Number of Students')
plt.title('Number of Students per Department')
plt.xticks(rotation=45)
plt.show()

# City-wise Student Count
city_counts = df['City'].value_counts()
plt.bar(city_counts.index, city_counts.values)
plt.xlabel('City')
plt.ylabel('Number of Students')
plt.title('Number of Students per City')
plt.xticks(rotation=45)
plt.show()

# Top 5 Students Bar Graph
top_students = df.nlargest(5, 'CGPA')
plt.bar(top_students['Name'], top_students['CGPA'])
plt.xlabel('Student Name')
plt.ylabel('CGPA')
plt.title('Top 5 Students by CGPA')
plt.xticks(rotation=45)
plt.show()

# CGPA vs Age Scatter Plot
Age = df['Age']
CGPA = df['CGPA']
plt.scatter(Age, CGPA, color='blue', alpha=0.7)

plt.title('CGPA vs Age Scatter Plot')
plt.xlabel('Age (Years)')
plt.ylabel('Cumulative Grade Point Average (CGPA)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# Department-wise Average CGPA Bar Chart
dept_avg = df.groupby('Department')['CGPA'].mean()

plt.bar(dept_avg.index, dept_avg.values, color='skyblue', edgecolor='black')
plt.title('Average CGPA by Department')
plt.xlabel('Department')
plt.ylabel('Average CGPA')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Histogram of CGPA
cgpa = df['CGPA']
plt.hist(cgpa, bins=10, color='lightgreen', edgecolor='black')
plt.title('Distribution of CGPA')
plt.xlabel('CGPA')
plt.ylabel('Number of Students')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Pie Chart of Department Distribution
dept_counts = df['Department'].value_counts()
plt.pie(
    dept_counts.values, 
    labels=dept_counts.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=plt.cm.Paired.colors # Uses a built-in color palette
)
plt.title('Student Distribution by Department')
plt.axis('equal')
plt.show()

import numpy as np

# --- Shared Mock Data ---
# For the Trend Line
semesters = [1, 2, 3, 4, 5, 6, 7, 8]
trend_cgpa = [7.1, 7.25, 7.2, 7.5, 7.6, 7.75, 7.9, 8.1]

# For the other charts
np.random.seed(42)
roll_numbers = np.arange(1001, 1101)
cgpa = np.clip(np.random.normal(7.5, 1.2, 100), 4.0, 10.0)

# Categorical data (Counts for Bar and Pie charts)
departments = ['Computer Science', 'Electrical', 'Mechanical', 'Civil', 'Information Tech']
dept_counts = [35, 20, 15, 10, 20]

cities = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai']
city_counts = [40, 25, 15, 10, 10]

# CGPA Trend Line Chart
plt.figure(figsize=(8, 5))

# Create the line plot with markers
plt.plot(semesters, trend_cgpa, color='blue', marker='o', linestyle='-', linewidth=2, markersize=6)

# Add titles and labels
plt.title('CGPA Trend Over 8 Semesters')
plt.xlabel('Semester')
plt.ylabel('Average CGPA')

# Set y-axis limits for better visibility
plt.ylim(6.5, 8.5)

# Add a grid
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()

#Department Comparison Bar Chart
plt.figure(figsize=(8, 5))

# Create the bar chart
bars = plt.bar(departments, dept_counts, color=['#4C72B0', '#55A868', '#C44E52', '#8172B3', '#CCB974'])

# Add titles and labels
plt.title('Number of Students per Department')
plt.xlabel('Department')
plt.ylabel('Number of Students')

# Rotate x-axis labels so they don't overlap
plt.xticks(rotation=15)

# Add a grid on the y-axis
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# City Distribution Pie Chart
plt.figure(figsize=(7, 7))

# Colors and "explode" (pulling out the first slice slightly)
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']
explode = (0.05, 0, 0, 0, 0) 

# Create the pie chart
plt.pie(city_counts, labels=cities, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)

# Add title
plt.title('Student Distribution by City')

plt.tight_layout()
plt.show()

# CGPA Histogram
plt.figure(figsize=(8, 5))

# Create the histogram (dividing data into 15 bins)
plt.hist(cgpa, bins=15, color='purple', edgecolor='black', alpha=0.7)

# Add titles and labels
plt.title('Distribution of Student CGPAs')
plt.xlabel('CGPA')
plt.ylabel('Frequency (Number of Students)')

# Add a grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# CGPA vs Roll Number Scatter Plot
plt.figure(figsize=(9, 5))

# Create the scatter plot
plt.scatter(roll_numbers, cgpa, color='teal', alpha=0.7, edgecolors='white', s=50)

# Add titles and labels
plt.title('CGPA vs Roll Number')
plt.xlabel('Roll Number')
plt.ylabel('CGPA')

# Add a horizontal line representing the passing or average mark
plt.axhline(y=7.5, color='red', linestyle='--', alpha=0.5, label='Average CGPA (7.5)')
plt.legend()

# Add a grid
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
