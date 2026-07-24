import pandas as pd
import numpy as np
import matplotlib.pyplot import plt
import seaborn as sns

# 1. Generate Data with Built-in Correlations
np.random.seed(42)
n_students = 500

study_hours = np.random.normal(12, 4, n_students).clip(0, 40)
attendance = np.random.normal(85, 12, n_students).clip(0, 100)
extracurriculars = np.random.normal(5, 3, n_students).clip(0, 20)

# Final score is mathematically tied to study hours and attendance to create realistic correlations
final_score = (study_hours * 1.5) + (attendance * 0.5) + np.random.normal(10, 8, n_students)
final_score = final_score.clip(0, 100)

df = pd.DataFrame({
    'Study_Hours': study_hours,
    'Attendance_Rate': attendance,
    'Extracurriculars': extracurriculars,
    'Final_Score': final_score
})

# Add categorical bins
df['Performance_Category'] = pd.cut(
    df['Final_Score'], 
    bins=[0, 59, 74, 89, 100], 
    labels=['Fail', 'Average', 'Good', 'Excellent']
)

# 2. Set up the Visualization Dashboard (2x2 Grid)
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Student Performance EDA Dashboard', fontsize=16)

# Plot A: Count Plot
sns.countplot(data=df, x='Performance_Category', palette='viridis', ax=axes[0, 0])
axes[0, 0].set_title('Count of Students by Performance Category')
axes[0, 0].set_ylabel('Number of Students')

# Plot B: Histogram
sns.histplot(data=df, x='Final_Score', bins=20, kde=True, color='skyblue', ax=axes[0, 1])
axes[0, 1].set_title('Distribution of Final Scores')
axes[0, 1].set_xlabel('Final Score')

# Plot C: Scatter Plot
sns.scatterplot(data=df, x='Attendance_Rate', y='Final_Score', alpha=0.6, color='coral', ax=axes[1, 0])
axes[1, 0].set_title('Attendance vs. Final Score')

# Plot D: Heatmap
# Calculate correlation matrix for numeric columns only
corr = df[['Study_Hours', 'Attendance_Rate', 'Extracurriculars', 'Final_Score']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=axes[1, 1], vmin=-1, vmax=1)
axes[1, 1].set_title('Feature Correlation Matrix')

plt.tight_layout()
plt.show()





from sklearn.ensemble import RandomForestClassifier

# 1. Generate Synthetic Data
np.random.seed(42)
n_samples = 500
data = {
    'Hours_Studied': np.random.normal(loc=15, scale=5, size=n_samples),
    'Attendance_Pct': np.random.normal(loc=85, scale=10, size=n_samples).clip(0, 100),
    'Previous_Scores': np.random.normal(loc=70, scale=15, size=n_samples).clip(0, 100),
    'Extracurriculars': np.random.randint(0, 4, size=n_samples)
}
df = pd.DataFrame(data)

# Target: Pass (1) or Fail (0) based on weighted features
score = (df['Hours_Studied'] * 2 + df['Attendance_Pct'] * 0.5 + df['Previous_Scores'] * 0.3)
df['Passed'] = (score > score.median() + np.random.normal(0, 5, n_samples)).astype(int)

# 2. Train Model for Feature Importance
X = df.drop('Passed', axis=1)
y = df['Passed']
rf = RandomForestClassifier(random_state=42, n_estimators=100)
rf.fit(X, y)
importances = rf.feature_importances_

# 3. Create Plots
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Plot 1: Feature Importance Bar Chart
sns.barplot(x=importances, y=X.columns, ax=axes[0, 0], palette='viridis')
axes[0, 0].set_title('Feature Importance (Predicting Pass/Fail)')
axes[0, 0].set_xlabel('Relative Importance')

# Plot 2: Correlation Heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=axes[0, 1], fmt='.2f')
axes[0, 1].set_title('Correlation Heatmap')

# Plot 3: Histogram
sns.histplot(df['Hours_Studied'], bins=20, kde=True, ax=axes[1, 0], color='skyblue')
axes[1, 0].set_title('Distribution of Hours Studied')
axes[1, 0].set_xlabel('Hours Studied')

# Plot 4: Scatter Plot
sns.scatterplot(data=df, x='Hours_Studied', y='Previous_Scores', hue='Passed', 
                ax=axes[1, 1], palette='Set1', alpha=0.7)
axes[1, 1].set_title('Scatter Plot: Hours Studied vs Previous Scores')

plt.tight_layout()
plt.show()





from sklearn.ensemble import RandomForestClassifier

# 1. Generate the synthetic dataset
np.random.seed(42)
n_samples = 1000

attendance = np.random.normal(75, 15, n_samples).clip(0, 100)
study_hours = np.random.normal(15, 8, n_samples).clip(0, 50)
prev_grade = np.random.normal(65, 20, n_samples).clip(0, 100)
sleep_hours = np.random.normal(7, 1.5, n_samples).clip(0, 12)

prob_pass = (attendance * 0.4 + study_hours * 1.5 + prev_grade * 0.5 + sleep_hours * 2) / 100
target = np.where(prob_pass + np.random.normal(0, 0.2, n_samples) > 0.65, 1, 0)

df = pd.DataFrame({
    'Attendance': attendance,
    'StudyHours': study_hours,
    'PrevGrade': prev_grade,
    'SleepHours': sleep_hours,
    'Passed': target
})

X = df.drop('Passed', axis=1)
y = df['Passed']

# Train model to get feature importances
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X, y)
importances = rf.feature_importances_

# 2. Set up the visualization grid
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Student Performance Data Analysis', fontsize=16, fontweight='bold')

# --- Chart 1: Feature Importance Bar Chart ---
sns.barplot(x=importances, y=X.columns, ax=axes[0, 0], palette="viridis")
axes[0, 0].set_title('Feature Importance for Predicting "Pass"')
axes[0, 0].set_xlabel('Importance Score')
axes[0, 0].set_ylabel('Features')

# --- Chart 2: Box Plot ---
sns.boxplot(x='Passed', y='StudyHours', data=df, ax=axes[0, 1], palette="Set2")
axes[0, 1].set_title('Study Hours Distribution by Pass/Fail Status')
axes[0, 1].set_xlabel('Passed (0 = No, 1 = Yes)')
axes[0, 1].set_ylabel('Study Hours / Week')

# --- Chart 3: Histogram ---
sns.histplot(df['Attendance'], bins=20, kde=True, ax=axes[1, 0], color='skyblue')
axes[1, 0].set_title('Distribution of Student Attendance')
axes[1, 0].set_xlabel('Attendance (%)')
axes[1, 0].set_ylabel('Count')

# --- Chart 4: Scatter Plot ---
sns.scatterplot(x='StudyHours', y='SleepHours', hue='Passed', data=df, alpha=0.7, palette="coolwarm", ax=axes[1, 1])
axes[1, 1].set_title('Study Hours vs Sleep Hours (Colored by Target)')
axes[1, 1].set_xlabel('Study Hours / Week')
axes[1, 1].set_ylabel('Sleep Hours / Night')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()









# ==========================================
# 1. GENERATE SYNTHETIC DATA
# ==========================================
np.random.seed(42)
n_samples = 500

data = {
    'Department': np.random.choice(['Math', 'Physics', 'Literature', 'History', 'Biology'], n_samples),
    'Study_Hours': np.random.normal(15, 5, n_samples),
    'Attendance': np.random.normal(85, 10, n_samples),
    'Past_Score': np.random.normal(70, 12, n_samples),
    'Stress_Level': np.random.randint(1, 10, n_samples)
}
df = pd.DataFrame(data)

# Generate target variable (Marks) based on features
df['Marks'] = (df['Study_Hours'] * 1.5 + 
               df['Attendance'] * 0.4 + 
               df['Past_Score'] * 0.5 - 
               df['Stress_Level'] * 1.2 + 
               np.random.normal(0, 5, n_samples))
df['Marks'] = df['Marks'].clip(0, 100)

# ==========================================
# 2. CALCULATE FEATURE IMPORTANCE
# ==========================================
X = df[['Study_Hours', 'Attendance', 'Past_Score', 'Stress_Level']]
y = df['Marks']

rf = RandomForestRegressor(random_state=42)
rf.fit(X, y)

feat_imp = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf.feature_importances_
}).sort_values(by='Importance', ascending=False)

# ==========================================
# 3. CREATE VISUALIZATIONS (2x2 Grid)
# ==========================================
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Student Performance Analysis Dashboard', fontsize=18, fontweight='bold')

# A. Correlation Heatmap (Top Left)
numeric_cols = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=axes[0, 0])
axes[0, 0].set_title('Correlation Heatmap', fontsize=14)

# B. Feature Importance Bar Chart (Top Right)
sns.barplot(x='Importance', y='Feature', data=feat_imp, palette='viridis', ax=axes[0, 1])
axes[0, 1].set_title('Feature Importance (Random Forest)', fontsize=14)

# C. Box Plot (Bottom Left)
sns.boxplot(x='Department', y='Marks', data=df, palette='Set2', ax=axes[1, 0])
axes[1, 0].set_title('Marks Distribution by Department', fontsize=14)

# D. Scatter Plot (Bottom Right)
sns.scatterplot(x='Study_Hours', y='Marks', hue='Department', data=df, alpha=0.7, ax=axes[1, 1])
axes[1, 1].set_title('Study Hours vs. Marks', fontsize=14)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()