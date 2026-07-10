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

np.random.seed(42)
n_students = 500

departments = ['Computer Science', 'Mechanical Engineering', 'Electrical Engineering', 'Civil Engineering', 'Business']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Seattle']

data = {
    'Student_ID': range(1, n_students + 1),
    'Age': np.random.randint(18, 26, n_students),
    # Normally distributed CGPA clipped between 2.0 and 4.0
    'CGPA': np.round(np.random.normal(3.2, 0.4, n_students).clip(2.0, 4.0), 2), 
    'Credits_Completed': np.random.randint(15, 120, n_students),
    'Study_Hours_Week': np.random.randint(5, 40, n_students),
    'Department': np.random.choice(departments, n_students),
    'City': np.random.choice(cities, n_students)
}

df = pd.DataFrame(data)

# Set Seaborn theme for better aesthetics
sns.set_theme(style="whitegrid")

# ==========================================
# Visualization 1: Correlation Heatmap
# ==========================================
plt.figure(figsize=(8, 6))
# Select only numeric columns and drop Student_ID
numeric_df = df.drop(columns=['Student_ID']).select_dtypes(include=[np.number])
corr = numeric_df.corr()

sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)
plt.title('Correlation Heatmap of Numeric Features')
plt.tight_layout()
plt.show()

# ==========================================
# Visualization 2: Pair Plot (Numeric Columns)
# ==========================================
numeric_cols = ['Age', 'CGPA', 'Credits_Completed', 'Study_Hours_Week']
pair_plot = sns.pairplot(df[numeric_cols], diag_kind='kde', plot_kws={'alpha': 0.6, 'edgecolor': 'none'})
pair_plot.fig.suptitle('Pair Plot of Numeric Columns', y=1.02)
plt.show()

# ==========================================
# Visualization 3: Violin Plot (CGPA by Department)
# ==========================================
plt.figure(figsize=(12, 6))
sns.violinplot(x='Department', y='CGPA', data=df, palette='Set2')
plt.title('Violin Plot: CGPA Distribution by Department')
plt.xlabel('Department')
plt.ylabel('CGPA')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# ==========================================
# Visualization 4: Count Plot (City Distribution)
# ==========================================
plt.figure(figsize=(10, 6))
# Order bars by count (descending)
order = df['City'].value_counts().index
sns.countplot(x='City', data=df, palette='viridis', order=order)
plt.title('Count Plot: Distribution of Students by City')
plt.xlabel('City')
plt.ylabel('Number of Students')
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# 1. Create a Mock Student Dataset
# ---------------------------------------------------------
np.random.seed(42)
n = 100
data = {
    'Student_ID': range(1, n+1),
    'Department': np.random.choice(['Computer Science', 'Physics', 'Mathematics', 'Biology'], n),
    'Attendance': np.random.uniform(60, 100, n),
    'Study_Hours': np.random.uniform(5, 40, n)
}

# Generate a CGPA that correlates somewhat with Attendance and Study Hours
data['CGPA'] = 1.0 + (data['Attendance']/100)*1.5 + (data['Study_Hours']/40)*1.5 + np.random.normal(0, 0.2, n)
data['CGPA'] = np.clip(data['CGPA'], 0.0, 4.0) # Ensure CGPA stays within 0 to 4.0

df = pd.DataFrame(data)

# Set the visual style for seaborn
sns.set_theme(style="whitegrid")

# ---------------------------------------------------------
# 2. CGPA vs Attendance Regression Plot
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))
# Using regplot to plot data and a linear regression model fit
sns.regplot(x='Attendance', y='CGPA', data=df, 
            scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'})

plt.title('Regression Plot: CGPA vs Attendance', fontsize=14)
plt.xlabel('Attendance (%)', fontsize=12)
plt.ylabel('CGPA', fontsize=12)
plt.tight_layout()

# Save the chart
plt.savefig('cgpa_vs_attendance_regplot.png')
plt.close() # Close to prevent overlap with the next plot

# ---------------------------------------------------------
# 3. Department Comparison using catplot()
# ---------------------------------------------------------
# catplot is a figure-level function, so we assign it to 'g' to tweak titles/labels
g = sns.catplot(x='Department', y='CGPA', data=df, kind='box', 
                height=6, aspect=1.2, palette='Set2')

# Adding a title slightly higher up (y=1.02) to avoid overlapping
g.fig.suptitle('Department Comparison by CGPA', y=1.02, fontsize=14)
g.set_axis_labels('Academic Department', 'CGPA', fontsize=12)

# Rotate x-axis labels if department names are long
g.tick_params(axis='x', rotation=0) 
plt.tight_layout()

# Save the chart
g.savefig('department_comparison_catplot.png')
plt.close('all')

# ---------------------------------------------------------
# 4. Jointplot for two numeric variables (Study Hours & CGPA)
# ---------------------------------------------------------
# jointplot shows bivariate relationship and univariate distributions (histograms on the edges)
jp = sns.jointplot(x='Study_Hours', y='CGPA', data=df, kind='hex', 
                   height=7, color="#4CB391")

jp.fig.suptitle('Jointplot: Study Hours vs CGPA', y=1.02, fontsize=14)
jp.set_axis_labels('Study Hours (per week)', 'CGPA', fontsize=12)
plt.tight_layout()

# Save the chart
jp.savefig('study_hours_cgpa_jointplot.png')
plt.close('all')

print("All charts have been generated and saved successfully!")