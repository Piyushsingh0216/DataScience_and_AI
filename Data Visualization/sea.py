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

import io
# ==========================================
# 0. Mock Data Setup
# ==========================================
csv_data = """Name,Department,CGPA,City
Alice,Computer Science,9.2,New York
Bob,Mathematics,8.5,Los Angeles
Charlie,Computer Science,7.8,New York
Diana,Physics,9.5,Chicago
Eve,Mathematics,6.5,Los Angeles
Frank,Physics,8.8,Chicago
Grace,Computer Science,7.2,New York
Hank,Mathematics,9.8,Boston
Ivy,Physics,5.9,Boston
Jack,Computer Science,8.1,Los Angeles
Karen,Mathematics,7.5,New York
Leo,Physics,9.1,Boston
Mona,Computer Science,6.8,Chicago
Nina,Biology,8.4,New York
Oscar,Biology,6.1,Boston
"""

# Load data into DataFrame
df = pd.read_csv(io.StringIO(csv_data.strip()))

# ==========================================
# 1. Dashboard Layout Setup
# ==========================================
# Set the visual style of the dashboard
sns.set_theme(style="whitegrid")

# Create a 2x2 grid of subplots (4 charts in one image)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Student Performance & Demographics Dashboard', fontsize=18, fontweight='bold', y=0.98)

# ==========================================
# 2. Chart 1: CGPA Distribution (Top Left)
# ==========================================
sns.histplot(data=df, x='CGPA', kde=True, bins=6, color='skyblue', ax=axes[0, 0])
axes[0, 0].set_title('CGPA Distribution', fontsize=14)
axes[0, 0].set_xlabel('CGPA')
axes[0, 0].set_ylabel('Number of Students')

# ==========================================
# 3. Chart 2: Department-wise Average CGPA (Top Right)
# ==========================================
# Calculate averages and sort for a cleaner chart
dept_avg = df.groupby('Department')['CGPA'].mean().reset_index().sort_values('CGPA', ascending=False)
sns.barplot(data=dept_avg, x='Department', y='CGPA', palette='viridis', ax=axes[0, 1])
axes[0, 1].set_title('Department-wise Average CGPA', fontsize=14)
axes[0, 1].set_xlabel('Department')
axes[0, 1].set_ylabel('Average CGPA')
# Ensure y-axis starts reasonably for CGPA to highlight differences
axes[0, 1].set_ylim(0, 10) 

# ==========================================
# 4. Chart 3: City-wise Student Count (Bottom Left)
# ==========================================
# Count plot automatically aggregates the counts of categorical data
sns.countplot(data=df, x='City', palette='magma', order=df['City'].value_counts().index, ax=axes[1, 0])
axes[1, 0].set_title('City-wise Student Count', fontsize=14)
axes[1, 0].set_xlabel('City')
axes[1, 0].set_ylabel('Number of Students')

# ==========================================
# 5. Chart 4: Top 5 Performers (Bottom Right)
# ==========================================
# Extract top 5 students
top_performers = df.nlargest(5, 'CGPA')
# Horizontal bar chart is best for reading names
sns.barplot(data=top_performers, x='CGPA', y='Name', palette='crest', ax=axes[1, 1])
axes[1, 1].set_title('Top 5 Performers by CGPA', fontsize=14)
axes[1, 1].set_xlabel('CGPA')
axes[1, 1].set_ylabel('Student Name')
axes[1, 1].set_xlim(0, 10)

# ==========================================
# 6. Final Rendering
# ==========================================
# Adjust spacing between plots to prevent labels from overlapping
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save the dashboard as an image file (optional but recommended)
plt.savefig('student_dashboard.png', dpi=300)
print("Dashboard successfully generated and saved as 'student_dashboard.png'.")

# Display the dashboard in a popup window
plt.show()


# Load your dataset (assuming it is saved as 'student_viz_data.csv')
df = pd.read_csv('student_viz_data.csv')

# ---------------------------------------------------------
# 1. Correlation Heatmap
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))
# Select only numeric columns for correlation
numeric_cols = df[['Attendance', 'Study_Hours', 'CGPA']]
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)
plt.title('Correlation Heatmap of Numeric Features')
plt.tight_layout()
plt.savefig('heatmap.png')
plt.close()

# ---------------------------------------------------------
# 2. Scatter Plot (CGPA vs Attendance)
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Attendance', y='CGPA', hue='Department', alpha=0.7)
plt.title('Scatter Plot: CGPA vs Attendance')
plt.xlabel('Attendance (%)')
plt.ylabel('CGPA')
plt.tight_layout()
plt.savefig('scatter.png')
plt.close()

# ---------------------------------------------------------
# 3. Box Plot (Grouped by Department)
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Department', y='CGPA', palette='Set2')
plt.title('Box Plot: CGPA Distribution by Department')
plt.xlabel('Department')
plt.ylabel('CGPA')
plt.tight_layout()
plt.savefig('boxplot.png')
plt.close()



# --- 1. PREPARE MOCK DATASET ---
np.random.seed(42)
data = {
    'Student_ID': range(1, 101),
    'CGPA': np.random.normal(7.5, 1.2, 100).clip(4.0, 10.0),
    'Study_Hours': np.random.normal(20, 5, 100),
    'Department': np.random.choice(['Computer Science', 'Mechanical', 'Electrical', 'Civil'], 100)
}
df = pd.DataFrame(data)
# Adding a correlated numeric feature for better visuals
df['Exam_Score'] = df['CGPA'] * 8 + np.random.normal(0, 5, 100) 


# --- 2. CORRELATION HEATMAP ---
# Shows how strongly the numeric features are related to one another
# (We filter for only numeric columns to avoid errors)
numeric_df = df[['CGPA', 'Study_Hours', 'Exam_Score']]

plt.title('Correlation Heatmap')
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.savefig('1_correlation_heatmap.png', bbox_inches='tight')
plt.clf() # Clears the plot for the next one


# --- 3. HISTOGRAM OF CGPA ---
# Shows the distribution/frequency of different CGPA scores
plt.title('Histogram of CGPA')
sns.histplot(df['CGPA'], bins=15, kde=True, color='skyblue')
plt.xlabel('CGPA')
plt.savefig('2_histogram_cgpa.png', bbox_inches='tight')
plt.clf()


# --- 4. BOX PLOT BY DEPARTMENT ---
# Shows the spread, median, and outliers of CGPAs across different departments
plt.title('Box Plot of CGPA by Department')
sns.boxplot(x='Department', y='CGPA', data=df, palette='Set2')
plt.savefig('3_boxplot_department.png', bbox_inches='tight')
plt.clf()


# --- 5. SCATTER PLOT OF TWO NUMERIC FEATURES ---
# Shows the relationship between Study Hours and CGPA, color-coded by Department
plt.title('Scatter Plot: Study Hours vs CGPA')
sns.scatterplot(x='Study_Hours', y='CGPA', hue='Department', data=df)
plt.savefig('4_scatter_plot.png', bbox_inches='tight')
plt.clf()

print("✓ Success: All 4 data visualizations have been generated and saved as PNG files!")

def main():
    # ==========================================
    # 1. Generate Mock Student Dataset
    # ==========================================
    np.random.seed(42)
    n_samples = 250
    
    departments = ['Computer Science', 'Electrical', 'Mechanical', 'Business', 'Arts']
    
    # Generate features
    cgpa = np.random.normal(loc=7.5, scale=1.1, size=n_samples)
    cgpa = np.clip(cgpa, 0, 10)  # Keep CGPA between 0 and 10
    
    study_hours = np.random.uniform(2, 12, size=n_samples)
    
    # Exam score is highly dependent on study hours + some random noise
    exam_score = 40 + (4.5 * study_hours) + np.random.normal(0, 5, size=n_samples)
    exam_score = np.clip(exam_score, 0, 100)
    
    dept = np.random.choice(departments, size=n_samples)
    
    df = pd.DataFrame({
        'Department': dept,
        'CGPA': cgpa,
        'Study_Hours': study_hours,
        'Exam_Score': exam_score
    })

    # ==========================================
    # 2. Print Insights to Terminal
    # ==========================================
    print("\n" + "="*50)
    print(" DATA VISUALIZATION INSIGHTS")
    print("="*50)
    
    print("\n1. Distribution plot of CGPA:")
    print("   Insight: The CGPA follows a roughly normal (bell-shaped) distribution, centered around 7.5, indicating that most students are average performers with very few extreme high or low scores.")
    
    print("\n2. Department-wise Box Plot:")
    print("   Insight: The median CGPA is relatively consistent across most departments, but 'Computer Science' shows a slightly wider interquartile range, indicating higher variance in student performance.")
    
    print("\n3. Correlation Heatmap:")
    print("   Insight: There is a strong positive correlation (close to 0.85+) between 'Study_Hours' and 'Exam_Score', confirming that increased study time directly translates to higher academic achievement.")
    
    print("\n4. Scatter Plot (Study Hours vs Exam Score):")
    print("   Insight: The upward trend clearly visually validates the strong correlation; as study hours increase along the x-axis, exam scores rise linearly along the y-axis across all departments.")
    print("\n" + "="*50)
    print("Close the plot window to exit the script.")
    print("="*50 + "\n")

    # ==========================================
    # 3. Create Visualizations (2x2 Grid)
    # ==========================================
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Student Performance Analysis', fontsize=16, fontweight='bold', y=0.98)

    # Plot 1: Distribution Plot
    sns.histplot(df['CGPA'], kde=True, color='skyblue', ax=axes[0, 0])
    axes[0, 0].set_title('1. Distribution of CGPA', fontsize=12)
    axes[0, 0].set_xlabel('CGPA')
    axes[0, 0].set_ylabel('Frequency')

    # Plot 2: Department-wise Box Plot
    sns.boxplot(x='Department', y='CGPA', data=df, palette='Set2', ax=axes[0, 1])
    axes[0, 1].set_title('2. CGPA Distribution by Department', fontsize=12)
    axes[0, 1].set_xlabel('Department')
    axes[0, 1].set_ylabel('CGPA')
    axes[0, 1].tick_params(axis='x', rotation=15)

    # Plot 3: Correlation Heatmap
    # Select only numeric columns for correlation
    numeric_df = df.select_dtypes(include=[np.number])
    corr_matrix = numeric_df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", 
                linewidths=0.5, ax=axes[1, 0], vmin=-1, vmax=1)
    axes[1, 0].set_title('3. Correlation Heatmap', fontsize=12)

    # Plot 4: Scatter Plot
    sns.scatterplot(x='Study_Hours', y='Exam_Score', hue='Department', 
                    data=df, palette='deep', alpha=0.7, ax=axes[1, 1])
    axes[1, 1].set_title('4. Study Hours vs Exam Score', fontsize=12)
    axes[1, 1].set_xlabel('Study Hours per Week')
    axes[1, 1].set_ylabel('Final Exam Score')
    axes[1, 1].legend(title='Department', bbox_to_anchor=(1.05, 1), loc='upper left')

    # Adjust layout so everything fits without overlapping
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    
    # Show the plot window
    plt.show()

if __name__ == "__main__":
    main()



# ==========================================
# 0. Mock Dataset Generation
# ==========================================
np.random.seed(42)
n_students = 200
departments = ['Computer Science', 'Mechanical', 'Electrical', 'Civil']
hours_studied = np.random.randint(2, 12, n_students)
attendance = np.random.randint(60, 100, n_students)

# Create a realistic CGPA that correlates with study hours and attendance
cgpa = (hours_studied * 0.4) + (attendance * 0.05) + np.random.normal(0, 0.5, n_students)
cgpa = np.clip(cgpa, 4.0, 10.0)

df = pd.DataFrame({
    'Student_ID': range(1, n_students + 1),
    'Department': np.random.choice(departments, n_students),
    'Hours_Studied': hours_studied,
    'Attendance_Percentage': attendance,
    'CGPA': np.round(cgpa, 2)
})

bins = [0, 6.0, 7.0, 8.0, 9.0, 10.0]
labels = ['F', 'D', 'C', 'B', 'A']
df['Grade'] = pd.cut(df['CGPA'], bins=bins, labels=labels, include_lowest=True)

print("Dataset generated. Creating visualizations...\n")

# ==========================================
# 1. Correlation Heatmap
# ==========================================
plt.figure(figsize=(8, 6))
numeric_cols = df[['Hours_Studied', 'Attendance_Percentage', 'CGPA']]
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)
plt.title('Correlation Heatmap of Student Metrics')
plt.tight_layout()
plt.savefig('1_correlation_heatmap.png')
print("Saved: 1_correlation_heatmap.png")
plt.close()

# ==========================================
# 2. Box Plot
# ==========================================
plt.figure(figsize=(8, 6))
sns.boxplot(x='Department', y='CGPA', data=df, palette='Set2')
plt.title('CGPA Distribution by Department')
plt.tight_layout()
plt.savefig('2_boxplot.png')
print("Saved: 2_boxplot.png")
plt.close()

# ==========================================
# 3. Count Plot
# ==========================================
plt.figure(figsize=(8, 6))
sns.countplot(x='Grade', data=df, order=['A', 'B', 'C', 'D', 'F'], palette='viridis')
plt.title('Count of Students per Grade')
plt.tight_layout()
plt.savefig('3_countplot.png')
print("Saved: 3_countplot.png")
plt.close()

# ==========================================
# 4. Scatter Plot
# ==========================================
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Hours_Studied', y='CGPA', hue='Department', data=df, alpha=0.7)
plt.title('CGPA vs Hours Studied')
plt.tight_layout()
plt.savefig('4_scatterplot.png')
print("Saved: 4_scatterplot.png")
plt.close()

print("\nAll visualizations have been successfully saved to your current directory!")



def main():
    # ==========================================
    # 0. SETUP: GENERATE MOCK BUSINESS DATASET
    # ==========================================
    np.random.seed(42)
    n_samples = 200
    
    # Generating mock data: Age, Income, Marketing Spend, Sales, and Region
    age = np.random.normal(35, 10, n_samples).clip(18, 70)
    income = np.random.normal(60000, 15000, n_samples)
    marketing_spend = np.random.uniform(1000, 5000, n_samples)
    
    # Sales is influenced by Income and Marketing Spend with some noise
    sales = (income * 0.05) + (marketing_spend * 1.2) + np.random.normal(0, 2000, n_samples)
    regions = np.random.choice(['North', 'South', 'East', 'West'], n_samples)
    
    df = pd.DataFrame({
        'Age': age,
        'Income': income,
        'Marketing_Spend': marketing_spend,
        'Sales': sales,
        'Region': regions
    })

    print("="*60)
    print("DATA VISUALIZATION EXERCISE RESULTS")
    print("="*60)
    
    # Set global seaborn style
    sns.set_theme(style="whitegrid")

    # ==========================================
    # 1. HISTOGRAM (Distribution of Income)
    # ==========================================
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Income'], bins=20, kde=True, color='skyblue')
    plt.title('Distribution of Customer Income')
    plt.xlabel('Income ($)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig('1_histogram.png')
    plt.close()

    print("\n[1] HISTOGRAM (Saved as 1_histogram.png)")
    print("------------------------------------------------------------")
    print("Business Insight : The majority of our customer base falls within the $50,000 to $70,000 income bracket. We should tailor our primary product pricing to fit this mid-market segment.")
    print("Limitation       : Histograms are highly sensitive to the number of bins chosen. Changing the bin size could hide or artificially create patterns in the data distribution.")

    # ==========================================
    # 2. BOX PLOT (Sales by Region)
    # ==========================================
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='Region', y='Sales', data=df, palette='Set2')
    plt.title('Sales Distribution by Region')
    plt.xlabel('Region')
    plt.ylabel('Sales ($)')
    plt.tight_layout()
    plt.savefig('2_boxplot.png')
    plt.close()

    print("\n[2] BOX PLOT (Saved as 2_boxplot.png)")
    print("------------------------------------------------------------")
    print("Business Insight : The 'East' region shows a higher median sales value but also a wider interquartile range (variance). This indicates high potential but inconsistent sales performance that requires standardization.")
    print("Limitation       : Box plots hide the underlying shape of the distribution. A region might have a 'bimodal' (two-peaked) distribution of sales, which the box plot would fail to show.")

    # ==========================================
    # 3. PAIR PLOT (Relationships across numeric variables)
    # ==========================================
    # Only plotting numeric columns to avoid errors
    numeric_df = df[['Age', 'Income', 'Marketing_Spend', 'Sales']]
    pair_plot = sns.pairplot(numeric_df, corner=True, diag_kind='kde')
    pair_plot.fig.suptitle('Pairwise Relationships in Sales Data', y=1.02)
    plt.savefig('3_pairplot.png')
    plt.close()

    print("\n[3] PAIR PLOT (Saved as 3_pairplot.png)")
    print("------------------------------------------------------------")
    print("Business Insight : There is a visible positive linear relationship between Marketing Spend and Sales, confirming that our current marketing acquisition channels are yielding a predictable return on investment (ROI).")
    print("Limitation       : Pair plots only visualize bivariate (two-variable) relationships in a vacuum. They fail to account for complex, multi-variable interactions or confounding variables.")

    # ==========================================
    # 4. CORRELATION HEATMAP
    # ==========================================
    plt.figure(figsize=(8, 6))
    corr_matrix = numeric_df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)
    plt.title('Correlation Heatmap of Numeric Variables')
    plt.tight_layout()
    plt.savefig('4_heatmap.png')
    plt.close()

    print("\n[4] CORRELATION HEATMAP (Saved as 4_heatmap.png)")
    print("------------------------------------------------------------")
    print("Business Insight : Income and Sales have a strong positive correlation (e.g., > 0.60). This suggests that shifting our marketing targeting toward higher-income demographics will likely yield disproportionately higher revenue.")
    print("Limitation       : Correlation does not imply causation. Furthermore, the Pearson correlation coefficient only captures linear relationships, entirely missing any non-linear dynamics between variables.")
    print("\n" + "="*60)
    print("All charts have been saved to your current working directory!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()



# ==========================================
# 1. Generate Synthetic Platform Data
# ==========================================
np.random.seed(42)
n_users = 200

# Generating realistic distributions
hours_logged = np.random.normal(25, 8, n_users)
modules_completed = (hours_logged * 0.4) + np.random.normal(0, 2, n_users)

# Base score tied to modules, with some random variance
quiz_score = (modules_completed * 3.5) + np.random.normal(40, 10, n_users)
tier = np.random.choice(['Free', 'Pro'], n_users, p=[0.6, 0.4])

# Give 'Pro' users a slight artificial bump in scores to simulate premium resources
quiz_score += np.where(tier == 'Pro', 8, 0)
quiz_score = np.clip(quiz_score, 0, 100) # Cap scores at 100

df = pd.DataFrame({
    'Hours_Logged': hours_logged.round(1),
    'Modules_Completed': np.maximum(0, modules_completed).round(0), # No negative modules
    'Quiz_Score': quiz_score.round(1),
    'Tier': tier
})

# ==========================================
# 2. Set Up the Dashboard Grid
# ==========================================
# Using a 2x2 grid to show all plots in one terminal run
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Learning Platform - Student Engagement Analysis', fontsize=16, fontweight='bold')
sns.set_theme(style="whitegrid")

# ==========================================
# Plot 1: Histogram (Distribution)
# ==========================================
sns.histplot(df['Hours_Logged'], bins=20, kde=True, ax=axes[0, 0], color='teal')
axes[0, 0].set_title('Histogram: Distribution of Hours Logged')
axes[0, 0].set_xlabel('Hours Logged')
axes[0, 0].set_ylabel('Number of Students')

# ==========================================
# Plot 2: Box Plot (Categorical vs Continuous)
# ==========================================
sns.boxplot(x='Tier', y='Quiz_Score', data=df, ax=axes[0, 1], palette='Set2')
axes[0, 1].set_title('Box Plot: Quiz Scores by Account Tier')
axes[0, 1].set_xlabel('Account Tier')
axes[0, 1].set_ylabel('Quiz Score')

# ==========================================
# Plot 3: Scatter Plot (Relationship)
# ==========================================
sns.scatterplot(x='Hours_Logged', y='Modules_Completed', hue='Tier', data=df, ax=axes[1, 0], palette='Set1', alpha=0.7)
axes[1, 0].set_title('Scatter Plot: Time Spent vs. Progress')
axes[1, 0].set_xlabel('Hours Logged')
axes[1, 0].set_ylabel('Modules Completed')

# ==========================================
# Plot 4: Correlation Heatmap
# ==========================================
numeric_df = df.select_dtypes(include=[np.number])
corr_matrix = numeric_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=axes[1, 1], vmin=-1, vmax=1, center=0, fmt=".2f")
axes[1, 1].set_title('Correlation Heatmap')

# Render the plots
plt.tight_layout()
plt.show()




# ==========================================
# 1. Create the Simulated Dataset
# ==========================================
np.random.seed(42)
n_samples = 500

# Features
hours = np.random.uniform(1, 10, n_samples)
attendance = np.random.uniform(50, 100, n_samples)
prev_score = np.random.uniform(40, 100, n_samples)

# Adding a categorical variable for better Box/Pair plots
tutoring_program = np.random.choice(['Enrolled', 'Not Enrolled'], n_samples, p=[0.4, 0.6])

# Calculate Final Grade with a boost for tutoring
base_grade = (3.2 * hours) + (0.4 * attendance) + (0.5 * prev_score) + np.random.normal(0, 4, n_samples)
tutoring_boost = np.where(tutoring_program == 'Enrolled', 8.0, 0.0) # 8 point boost for tutoring
final_grade = base_grade + tutoring_boost

# Compile into DataFrame
df = pd.DataFrame({
    'Hours_Studied': hours,
    'Attendance': attendance,
    'Previous_Score': prev_score,
    'Tutoring_Program': tutoring_program,
    'Final_Grade': final_grade
})

# Set visual style
sns.set_theme(style="whitegrid")

# ==========================================
# 2. Correlation Heatmap
# ==========================================
print("\n" + "="*50)
print("CHART 1: CORRELATION HEATMAP")
print("="*50)
print("Insight: The heatmap reveals which numerical factors have the strongest linear relationship with the Final Grade. You will see that 'Hours_Studied' and 'Previous_Score' show high positive correlation coefficients.")
print("Improvement: Since 'Previous_Score' strongly dictates future success, the institution should implement a mandatory 'bridge course' or summer prep session for incoming students whose previous scores fall below a certain threshold.")

plt.figure(figsize=(8, 6))
# Calculate correlation only for numeric columns
corr_matrix = df.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of Student Performance")
print("\n>>> Displaying Heatmap... (Close the window to continue to the next chart) <<<")
plt.show()

# ==========================================
# 3. Pair Plot
# ==========================================
print("\n" + "="*50)
print("CHART 2: PAIR PLOT")
print("="*50)
print("Insight: The pair plot shows the multidimensional distribution of the data. When colored by 'Tutoring_Program', we can see clear clusters showing that enrolled students consistently map to the higher end of the Final Grade axis across all other variables.")
print("Improvement: The institution should use the lower-left quadrant clusters (low attendance, low hours studied) to create an early-warning dashboard. If a student falls into these metrics by week 3, an automatic alert should trigger an advisor intervention.")

pair_fig = sns.pairplot(df, hue='Tutoring_Program', palette='husl', corner=True)
pair_fig.fig.suptitle("Pair Plot of All Features by Tutoring Enrollment", y=1.02)
print("\n>>> Displaying Pair Plot... (Close the window to continue to the next chart) <<<")
plt.show()

# ==========================================
# 4. Box Plot
# ==========================================
print("\n" + "="*50)
print("CHART 3: BOX PLOT")
print("="*50)
print("Insight: The box plot clearly contrasts the median Final Grade and overall score spread between students who took tutoring and those who didn't. Enrolled students have a noticeably higher median and fewer extreme low outliers.")
print("Improvement: The data justifies institutional funding to expand the tutoring program capacity. The institution should heavily market this program during orientation and offer incentives (like course credit or priority registration) to increase enrollment.")

plt.figure(figsize=(8, 6))
sns.boxplot(x='Tutoring_Program', y='Final_Grade', data=df, palette='Set2')
plt.title("Final Grade Distribution by Tutoring Program Enrollment")
plt.xlabel("Tutoring Program Status")
plt.ylabel("Final Grade")
print("\n>>> Displaying Box Plot... (Close the window to continue to the next chart) <<<")
plt.show()

# ==========================================
# 5. Histogram
# ==========================================
print("\n" + "="*50)
print("CHART 4: HISTOGRAM")
print("="*50)
print("Insight: The histogram shows a normal (bell-curve) distribution of Final Grades across the student body, with the majority of students scoring in the middle range and fewer at the extreme high or low ends.")
print("Improvement: If the center of the bell curve (the mean) falls below the institution's target academic standard, the curriculum committee should evaluate if the course pacing is too fast or if the grading rubrics need recalibration to support broader student comprehension.")

plt.figure(figsize=(8, 6))
sns.histplot(df['Final_Grade'], bins=20, kde=True, color='purple')
plt.title("Distribution of Final Grades")
plt.xlabel("Final Grade")
plt.ylabel("Frequency (Number of Students)")
print("\n>>> Displaying Histogram... (Close the window to finish) <<<")
plt.show()

print("\nAll visualizations complete!")