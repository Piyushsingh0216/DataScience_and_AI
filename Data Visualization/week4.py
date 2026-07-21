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