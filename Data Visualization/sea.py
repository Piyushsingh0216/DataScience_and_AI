import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. GENERATE SYNTHETIC DATASET
# ==========================================
# Set seed for reproducibility
np.random.seed(42)

n_students = 200
departments = ['Computer Science', 'Electrical', 'Mechanical', 'Civil', 'Business']

# Create the data dictionary
data = {
    'StudentID': range(1, n_students + 1),
    'Department': np.random.choice(departments, n_students),
    'StudyHoursPerWeek': np.random.randint(5, 40, n_students)
}

# Add some correlation between study hours and CGPA (capped between 4.0 and 10.0)
data['CGPA'] = np.round((data['StudyHoursPerWeek'] * 0.08 + 
                         np.random.normal(5.0, 0.8, n_students)).clip(4.0, 10.0), 2)

# Convert to DataFrame
df = pd.DataFrame(data)

# Optional: Save to CSV for your records
df.to_csv('synthetic_student_dataset.csv', index=False)


# ==========================================
# 2. CREATE VISUALIZATIONS
# ==========================================
# Set a clean theme for the plots
sns.set_theme(style="whitegrid")

# Plot 1: Department Count Plot
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Department', order=df['Department'].value_counts().index, palette='viridis')
plt.title('Department Count Plot')
plt.xlabel('Department')
plt.ylabel('Number of Students')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: CGPA Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['CGPA'], bins=15, kde=True, color='skyblue')
plt.title('CGPA Distribution')
plt.xlabel('CGPA')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Plot 3: Box Plot of CGPA
plt.figure(figsize=(8, 2.5))
sns.boxplot(x=df['CGPA'], color='lightgreen')
plt.title('Box Plot of CGPA')
plt.xlabel('CGPA')
plt.tight_layout()
plt.show()

# Plot 4: Scatter Plot (CGPA vs Study Hours per Week)
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='StudyHoursPerWeek', y='CGPA', hue='Department', palette='deep', alpha=0.8)
plt.title('Scatter Plot: CGPA vs Study Hours per Week')
plt.xlabel('Study Hours per Week')
plt.ylabel('CGPA')
# Move legend outside the plot so it doesn't cover data points
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
