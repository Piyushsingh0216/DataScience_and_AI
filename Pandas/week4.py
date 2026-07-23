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



import numpy as np
import os

class DataPreprocessor:
    """
    A reusable data preprocessing pipeline using pandas.
    """
    def __init__(self, input_filepath, output_filepath):
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath
        self.df = None

    def load_data(self):
        print(f"[*] Loading data from: {self.input_filepath}")
        self.df = pd.read_csv(self.input_filepath)
        print(f"    Initial shape: {self.df.shape}")
        
    def clean_column_names(self):
        print("[*] Standardizing column names...")
        # Strip whitespace, convert to lowercase, replace spaces with underscores
        self.df.columns = (self.df.columns
                           .str.strip()
                           .str.lower()
                           .str.replace(' ', '_', regex=False)
                           .str.replace(r'[^\w\s]', '', regex=True))

    def clean_text_data(self):
        print("[*] Cleaning string/text values...")
        # Strip leading/trailing whitespaces from object/string columns
        string_cols = self.df.select_dtypes(include=['object']).columns
        for col in string_cols:
            # Only strip strings; leave NaNs alone to be handled later
            self.df[col] = self.df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

    def handle_missing_values(self):
        print("[*] Handling missing values...")
        # Strategy 1: Fill numeric missing values with the median
        num_cols = self.df.select_dtypes(include=[np.number]).columns
        for col in num_cols:
            if self.df[col].isnull().sum() > 0:
                median_val = self.df[col].median()
                self.df[col].fillna(median_val, inplace=True)
                
        # Strategy 2: Fill categorical/string missing values with the mode
        cat_cols = self.df.select_dtypes(include=['object', 'category']).columns
        for col in cat_cols:
            if self.df[col].isnull().sum() > 0:
                mode_val = self.df[col].mode()[0]
                self.df[col].fillna(mode_val, inplace=True)

    def remove_duplicates(self):
        print("[*] Removing duplicate rows...")
        initial_rows = self.df.shape[0]
        self.df.drop_duplicates(inplace=True)
        final_rows = self.df.shape[0]
        print(f"    Dropped {initial_rows - final_rows} duplicate rows.")

    def save_data(self):
        print(f"[*] Saving cleaned dataset to: {self.output_filepath}")
        self.df.to_csv(self.output_filepath, index=False)
        print(f"    Final shape: {self.df.shape}")

    def run(self):
        """Executes the entire preprocessing pipeline sequentially."""
        self.load_data()
        self.clean_column_names()
        self.clean_text_data()
        self.handle_missing_values()
        self.remove_duplicates()
        self.save_data()
        print("[+] Pipeline execution completed successfully!\n")
        return self.df

# ==========================================
# Example Usage / Test Environment
# ==========================================
if __name__ == "__main__":
    # 1. Generate a dirty dataset for testing
    dirty_data_path = "dirty_dataset.csv"
    clean_data_path = "cleaned_dataset.csv"
    
    raw_data = {
        ' Student ID ': [101, 102, 102, 103, np.nan, 105], # Has NaN and a duplicate
        '  First Name': [' Alice ', 'Bob', 'Bob', ' Charlie', 'David', np.nan], # Has whitespace and NaN
        'Age ': [20, 22, 22, np.nan, 21, 23], # Has NaN
        'Score (%)': [85.5, 90.0, 90.0, 78.0, 88.5, np.nan] # Has NaN
    }
    
    pd.DataFrame(raw_data).to_csv(dirty_data_path, index=False)
    print(f"Created dummy dirty dataset: '{dirty_data_path}'\n")

    # 2. Instantiate and run the pipeline
    pipeline = DataPreprocessor(input_filepath=dirty_data_path, output_filepath=clean_data_path)
    cleaned_df = pipeline.run()

    # 3. Display the result
    print("=== FINAL CLEANED DATA ===")
    print(cleaned_df.to_string())





# 1. Generate Base Data (adding 'Department' and 'Final_Score')
np.random.seed(42)
n_students = 500

df = pd.DataFrame({
    'Student_ID': range(1, n_students + 1),
    'Department': np.random.choice(['Engineering', 'Business', 'Arts', 'Science'], n_students),
    'Attendance_Rate': np.random.normal(85, 12, n_students).clip(0, 100),
    'Final_Score': np.random.normal(72, 15, n_students).clip(0, 100)
})

# 2. Create 'Performance Category'
# Bins: 0-59 (Fail), 60-74 (Average), 75-89 (Good), 90-100 (Excellent)
performance_bins = [0, 59, 74, 89, 100]
performance_labels = ['Fail', 'Average', 'Good', 'Excellent']
df['Performance_Category'] = pd.cut(
    df['Final_Score'], 
    bins=performance_bins, 
    labels=performance_labels, 
    include_lowest=True
)

# 3. Create 'Attendance Percentage Group'
# Bins: 0-75 (Low), 75-90 (Moderate), 90-100 (High)
attendance_bins = [0, 75, 90, 100]
attendance_labels = ['Low (<75%)', 'Moderate (75-90%)', 'High (>90%)']
df['Attendance_Group'] = pd.cut(
    df['Attendance_Rate'], 
    bins=attendance_bins, 
    labels=attendance_labels, 
    include_lowest=True
)

# 4. Create Department Statistics Summary
# We group by Department to find average scores, average attendance, and student count
dept_summary = df.groupby('Department').agg(
    Total_Students=('Student_ID', 'count'),
    Avg_Score=('Final_Score', 'mean'),
    Avg_Attendance=('Attendance_Rate', 'mean')
).round(2).reset_index()

# 5. Save the transformed data
# Save the main student dataset
df.to_csv('student_transformed.csv', index=False)

# Optional: Save the department summary to a separate file
dept_summary.to_csv('department_summary.csv', index=False)

print("✅ Data transformation complete.")
print("✅ Saved 'student_transformed.csv'.\n")
print("=== Department Statistics Summary ===")
print(dept_summary)






# 1. Create synthetic dataset
np.random.seed(42)
n_students = 200
departments = ['Computer Science', 'Mechanical', 'Electrical', 'Civil']

data = {
    'Student_ID': range(1, n_students + 1),
    'Department': np.random.choice(departments, n_students),
    'Attendance_Percentage': np.random.uniform(50, 100, n_students).round(2),
    'Marks': np.random.uniform(30, 100, n_students).round(2)
}
df = pd.DataFrame(data)

# 2. Department performance summary
dept_performance = df.groupby('Department')['Marks'].agg(['mean', 'min', 'max', 'count']).round(2)
dept_performance.rename(
    columns={'mean': 'Average_Marks', 'min': 'Min_Marks', 'max': 'Max_Marks', 'count': 'Total_Students'}, 
    inplace=True
)
dept_performance.to_csv('department_performance_summary.csv')

# 3. Attendance analysis
# Categorize attendance into bins
bins_att = [0, 75, 90, 100]
labels_att = ['Low (<75%)', 'Medium (75-90%)', 'High (>90%)']
df['Attendance_Category'] = pd.cut(df['Attendance_Percentage'], bins=bins_att, labels=labels_att)

# Group by department and attendance category
attendance_analysis = df.groupby(['Department', 'Attendance_Category'], observed=True).size().unstack(fill_value=0)
attendance_analysis.to_csv('attendance_analysis.csv')

# 4. Marks distribution report
# Categorize marks into bins
bins_marks = [0, 40, 60, 80, 100]
labels_marks = ['Fail (<40)', 'Pass (40-60)', 'First Class (60-80)', 'Distinction (80-100)']
df['Marks_Category'] = pd.cut(df['Marks'], bins=bins_marks, labels=labels_marks)

# Count students in each grade category
marks_distribution = df['Marks_Category'].value_counts().sort_index().reset_index()
marks_distribution.columns = ['Grade_Category', 'Number_of_Students']
marks_distribution.to_csv('marks_distribution_report.csv')

print("CSV files generated successfully.")