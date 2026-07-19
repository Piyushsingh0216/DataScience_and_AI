import pandas as pd
import numpy as np

# 1. Generate Sample Data (assuming standard 0-100 scales)
np.random.seed(42)
n_samples = 100
df = pd.DataFrame({
    'Student_ID': range(1, n_samples + 1),
    'Hours_Studied': np.random.uniform(2, 10, n_samples).round(1),
    'Attendance': np.random.uniform(60, 100, n_samples).round(1),
    'Final_Score': np.random.uniform(50, 100, n_samples).round(1)
})

# 2. Create 'Grade category' column using pd.cut
# Standard grading scale: F (<60), D (60-69), C (70-79), B (80-89), A (90-100)
grade_bins = [0, 59.9, 69.9, 79.9, 89.9, 100]
grade_labels = ['F', 'D', 'C', 'B', 'A']
df['Grade_Category'] = pd.cut(
    df['Final_Score'], 
    bins=grade_bins, 
    labels=grade_labels, 
    include_lowest=True
)

# 3. Create 'Attendance category' column using pd.cut
# Thresholds: Poor (<75%), Average (75-89%), Excellent (90-100%)
attendance_bins = [0, 74.9, 89.9, 100]
attendance_labels = ['Poor', 'Average', 'Excellent']
df['Attendance_Category'] = pd.cut(
    df['Attendance'], 
    bins=attendance_bins, 
    labels=attendance_labels, 
    include_lowest=True
)

# 4. Create 'Performance level' column using np.select
# This combines metrics to identify holistic performance states
conditions = [
    (df['Final_Score'] >= 80) & (df['Attendance'] >= 90),  # High scores AND high attendance
    (df['Final_Score'] < 65) | (df['Attendance'] < 75)     # Low scores OR low attendance
]
choices = ['High Performer', 'At Risk']
df['Performance_Level'] = np.select(conditions, choices, default='Average Performer')

# 5. Export the data
export_filename = 'student_features.csv'
df.to_csv(export_filename, index=False)

# 6. Display results in terminal
print(f"SUCCESS: Engineered features and exported to '{export_filename}'.\n")
print("--- Data Preview ---")
print(df[['Final_Score', 'Grade_Category', 'Attendance', 'Attendance_Category', 'Performance_Level']].head(8).to_string())