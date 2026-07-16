import pandas as pd
import numpy as np

# ---------------------------------------------------------
# SETUP: Creating a "messy" mock student dataset
# ---------------------------------------------------------
data = {
    'Student_ID': ['S001', 'S002', 'S003', 'S004', 'S005'],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Hours_Studied': [10, 15, np.nan, 20, 5],        # Missing 1 value
    'Attendance_Percentage': [90, 95, 80, 100, np.nan], # Missing 1 value
    'Previous_Score': [85, 88, 70, 92, 60],
    'Extracurriculars': [1, 0, 1, 1, 0],
    'Pass_Fail': [1, 1, 0, 1, 0]
}

# Load into DataFrame
df = pd.DataFrame(data)
print("--- Original Dataset ---")
print(df)
print("\n")

# ---------------------------------------------------------
# STEP 1: Remove unnecessary columns
# ---------------------------------------------------------
# Machine learning models only work with numbers, and names/IDs don't hold predictive value.
# We drop 'Student_ID' and 'Name'.
df_cleaned = df.drop(columns=['Student_ID', 'Name'])
print("--- After Removing Unnecessary Columns ---")
print(df_cleaned.head(), "\n")

# ---------------------------------------------------------
# STEP 2: Check (and handle) missing values
# ---------------------------------------------------------
# Checking for missing values
print("--- Missing Values Count ---")
print(df_cleaned.isnull().sum(), "\n")

# Handling missing values: We will fill the empty (NaN) spots with the average (mean) of that column
df_cleaned['Hours_Studied'] = df_cleaned['Hours_Studied'].fillna(df_cleaned['Hours_Studied'].mean())
df_cleaned['Attendance_Percentage'] = df_cleaned['Attendance_Percentage'].fillna(df_cleaned['Attendance_Percentage'].mean())

# ---------------------------------------------------------
# STEP 3: Separate features (X) and target (y)
# ---------------------------------------------------------
# X = Everything EXCEPT 'Pass_Fail'
X = df_cleaned.drop(columns=['Pass_Fail'])

# y = ONLY 'Pass_Fail'
y = df_cleaned['Pass_Fail']

print("--- Features (X) ---")
print(X.head(), "\n")
print("--- Target (y) ---")
print(y.head(), "\n")

# ---------------------------------------------------------
# STEP 4: Save the cleaned dataset
# ---------------------------------------------------------
# index=False ensures Pandas doesn't save the row numbers (0, 1, 2, 3...) as a new column
df_cleaned.to_csv('student_cleaned.csv', index=False)
print("✅ Cleaned dataset successfully saved as 'student_cleaned.csv'!")



# Creating a mock dataset with duplicates, missing values, and categories
data = {
    'Student_ID': [1, 2, 3, 4, 5, 5, 6, 7, 8], # Note the duplicate '5'
    'Hours_Studied': [2.5, 3.0, np.nan, 5.0, 6.5, 6.5, 8.0, np.nan, 10.0],
    'Major': ['Science', 'Arts', 'Science', 'Math', 'Arts', 'Arts', 'Math', 'Science', 'Math'],
    'Exam_Score': [55, 60, 68, 72, 78, 78, 88, 92, 95]
}
df = pd.DataFrame(data)

print("--- 1. ORIGINAL DATASET ---")
print(df)
print("\n")

# --- Step 1: Remove duplicates ---
# Drops rows that are exact copies of another row
df_cleaned = df.drop_duplicates()

# --- Step 2: Fill missing values ---
# Filling missing 'Hours_Studied' with the average (mean) of that column
mean_hours = df_cleaned['Hours_Studied'].mean()
df_cleaned['Hours_Studied'] = df_cleaned['Hours_Studied'].fillna(mean_hours)

# --- Step 3: Encode one categorical column ---
# Converting the text-based 'Major' column into numerical format (One-Hot Encoding)
df_encoded = pd.get_dummies(df_cleaned, columns=['Major'], dtype=int)

# --- Step 4: Save the processed dataset ---
output_filename = 'student_ml_ready.csv'
df_encoded.to_csv(output_filename, index=False)

print("--- 2. PROCESSED DATASET ---")
print(df_encoded)
print(f"\n✓ Success: Dataset processed and saved as '{output_filename}'")

def main():
    print("="*50)
    print("  STUDENT DATASET: FEATURE ENGINEERING & OUTLIERS")
    print("="*50)

    # 1. Load / Generate Dataset
    # Generating 100 mock students. Normal CGPA around 7.2.
    np.random.seed(42)
    cgpa_scores = np.random.normal(loc=7.2, scale=1.2, size=100)
    
    df = pd.DataFrame({
        'Student_ID': range(101, 201),
        'Name': [f"Student_{i}" for i in range(101, 201)],
        'CGPA': cgpa_scores
    })

    # Injecting intentional outliers for demonstration purposes
    df.loc[12, 'CGPA'] = 1.2   # Extremely low outlier
    df.loc[45, 'CGPA'] = 3.4   # Low outlier
    df.loc[88, 'CGPA'] = 11.5  # Impossible high outlier (data entry error)

    # 2. Create a Performance Category Column
    # Using pandas.cut to bin the continuous CGPA into discrete categories
    bins = [0, 5.0, 7.0, 8.5, 10.0, float('inf')]
    labels = ['Needs Improvement', 'Average', 'Good', 'Excellent', 'Invalid Data']
    
    df['Performance_Category'] = pd.cut(
        df['CGPA'], 
        bins=bins, 
        labels=labels, 
        right=False # Defines intervals as [lower, upper)
    )
    print("\n[+] Created 'Performance_Category' column successfully.")

    # 3. Detect Potential Outliers in CGPA (Using IQR Method)
    Q1 = df['CGPA'].quantile(0.25)
    Q3 = df['CGPA'].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Create a boolean column tagging the outliers
    df['CGPA_Outlier'] = (df['CGPA'] < lower_bound) | (df['CGPA'] > upper_bound)
    
    outliers_df = df[df['CGPA_Outlier']]
    print(f"[+] Detected {len(outliers_df)} potential outliers in CGPA.")

    # 4. Save the updated dataset
    output_filename = 'student_features.csv'
    df.to_csv(output_filename, index=False)
    print(f"[+] Saved updated dataset to '{output_filename}'.")

    # 5. Display the Results
    print("\n" + "-"*50)
    print("FIRST 5 ROWS OF UPDATED DATASET:")
    print("-"*50)
    print(df[['Student_ID', 'CGPA', 'Performance_Category', 'CGPA_Outlier']].head())

    print("\n" + "-"*50)
    print("DETECTED OUTLIERS:")
    print("-"*50)
    if not outliers_df.empty:
        print(outliers_df[['Student_ID', 'Name', 'CGPA', 'Performance_Category']].to_string(index=False))
    else:
        print("No outliers detected.")
    
    print("\n" + "-"*50)
    print(f"IQR BOUNDARIES -> Lower: {lower_bound:.2f} | Upper: {upper_bound:.2f}")
    print("-"*50 + "\n")

if __name__ == "__main__":
    main()


# ==========================================
# 0. Mock Dataset Generation (Updated)
# ==========================================
# Adding Department and CGPA to match your new requirements
np.random.seed(42)
departments = ['Computer Science', 'Mechanical', 'Electrical', 'Civil']
data = {
    'Student_ID': range(1, 101),
    'Department': np.random.choice(departments, 100),
    'CGPA': np.round(np.random.uniform(5.0, 10.0, 100), 2) 
}
df = pd.DataFrame(data)

# ==========================================
# 1. Create a Grade Column
# ==========================================
# Using pd.cut to map CGPA ranges to letter grades
bins = [0, 6.0, 7.0, 8.0, 9.0, 10.0]
labels = ['F', 'D', 'C', 'B', 'A']
df['Grade'] = pd.cut(df['CGPA'], bins=bins, labels=labels, include_lowest=True)

# ==========================================
# 2. Calculate Department-wise Average CGPA
# ==========================================
# .transform('mean') calculates the group average and aligns it with every row
df['Dept_Avg_CGPA'] = df.groupby('Department')['CGPA'].transform('mean').round(2)

# Printing just the summary table for your terminal output
print("--- Department-wise Average CGPA ---\n")
summary_df = df.groupby('Department')['CGPA'].mean().round(2).reset_index()
print(summary_df.to_string(index=False))
print("\n" + "-"*35 + "\n")

# ==========================================
# 3. Add column for difference from Department Average
# ==========================================
df['CGPA_Diff_From_Dept'] = (df['CGPA'] - df['Dept_Avg_CGPA']).round(2)

print("--- Preview of Processed Dataset ---\n")
print(df.head())
print("\n" + "-"*35 + "\n")

# ==========================================
# 4. Save the processed dataset
# ==========================================
filename = 'processed_students.csv'
df.to_csv(filename, index=False)
print(f"Success: Processed dataset saved locally as '{filename}'.")


def main():
    # ==========================================
    # 0. SETUP: LOAD (OR MOCK) THE DATASET
    # ==========================================
    # Replace this block with: df = pd.read_csv('your_dataset.csv')
    np.random.seed(42)
    departments = ['Computer Science', 'Mechanical', 'Electrical', 'Civil']
    
    # Generating mock data
    data = {
        'Student_ID': range(101, 201),
        'Name': [f"Student_{i}" for i in range(1, 101)],
        'Department': np.random.choice(departments, 100),
        # Normal CGPA around 7.5
        'CGPA': np.random.normal(7.5, 1.2, 100) 
    }
    df = pd.DataFrame(data)
    
    # Inject a few intentional outliers for the exercise
    df.loc[10, 'CGPA'] = 1.5 
    df.loc[45, 'CGPA'] = 9.9 
    
    # Clip to ensure valid CGPA range (0 to 10)
    df['CGPA'] = df['CGPA'].clip(0, 10)

    print("="*50)
    print("INITIAL DATASET PREVIEW (First 5 rows):")
    print("="*50)
    print(df.head(), "\n")

    # ==========================================
    # 1. DEPARTMENT-WISE SUMMARY STATISTICS
    # ==========================================
    print("="*50)
    print("1. DEPARTMENT-WISE CGPA SUMMARY STATISTICS:")
    print("="*50)
    dept_summary = df.groupby('Department')['CGPA'].describe()
    print(dept_summary, "\n")

    # ==========================================
    # 2. TOP 5 STUDENTS IN EACH DEPARTMENT
    # ==========================================
    print("="*50)
    print("2. TOP 5 STUDENTS PER DEPARTMENT:")
    print("="*50)
    # Group by department, get the top 5 by CGPA, and drop the extra index
    top_5_students = df.groupby('Department', group_keys=False).apply(lambda x: x.nlargest(5, 'CGPA'))
    print(top_5_students[['Department', 'Name', 'CGPA']], "\n")

    # ==========================================
    # 3. FLAG POTENTIAL OUTLIERS IN CGPA
    # ==========================================
    # We will use the Interquartile Range (IQR) method to find outliers
    Q1 = df['CGPA'].quantile(0.25)
    Q3 = df['CGPA'].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Create a new column flagging True if outside the bounds, False otherwise
    df['Is_Outlier'] = (df['CGPA'] < lower_bound) | (df['CGPA'] > upper_bound)
    
    print("="*50)
    print("3. OUTLIERS FLAGGED (Showing only outliers):")
    print("="*50)
    outliers = df[df['Is_Outlier'] == True]
    if not outliers.empty:
        print(outliers[['Student_ID', 'Name', 'Department', 'CGPA', 'Is_Outlier']], "\n")
    else:
        print("No outliers detected based on the IQR method.\n")

    # ==========================================
    # 4. SAVE THE PROCESSED DATASET
    # ==========================================
    output_file = 'student_analysis.csv'
    df.to_csv(output_file, index=False)
    
    print("="*50)
    print(f"4. DATA SAVED SUCCESSFULLY!")
    print("="*50)
    print(f"Processed dataset saved as: {output_file}")

if __name__ == "__main__":
    main()