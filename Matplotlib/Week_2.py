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
