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