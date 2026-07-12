import pandas as pd
from sklearn.model_selection import train_test_split

# ---------------------------------------------------------
# SETUP: Creating a mock student dataset
# ---------------------------------------------------------
data = {
    'Hours_Studied': [10, 15, 8, 20, 5, 12, 18, 25, 6, 14],
    'Attendance_Percentage': [90, 95, 80, 100, 75, 85, 95, 100, 70, 88],
    'Previous_Score': [85, 88, 70, 92, 60, 78, 89, 95, 55, 82],
    'Extracurriculars': [1, 0, 1, 1, 0, 1, 0, 1, 0, 1], # 1 = Yes, 0 = No
    
    'Pass_Fail': [1, 1, 0, 1, 0, 1, 1, 1, 0, 1]         # 1 = Pass, 0 = Fail
}

# Load the data into a Pandas DataFrame
df = pd.DataFrame(data)
print("--- Original Dataset ---")
print(df.head(), "\n")

# ---------------------------------------------------------
# STEP 1 & 2: Define Features (X) and Target (y)
# ---------------------------------------------------------
# List of feature column names
feature_columns = ['Hours_Studied', 'Attendance_Percentage', 'Previous_Score', 'Extracurriculars']

# Extracting Features (X)
X = df[feature_columns]

# Extracting Target (y)
y = df['Pass_Fail']

# ---------------------------------------------------------
# STEP 4: Create the Train/Test Split
# ---------------------------------------------------------
# test_size=0.2 means 20% of data goes to testing, 80% to training.
# random_state=42 ensures we get the exact same split every time we run the code.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Displaying the results of the split
print("--- Train/Test Split Results ---")
print(f"Total students in dataset: {len(df)}")
print(f"Students allocated to Training Data (X_train): {len(X_train)}")
print(f"Students allocated to Testing Data (X_test): {len(X_test)}\n")

print("--- Sample of Training Features (X_train) ---")
print(X_train)
