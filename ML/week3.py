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


from sklearn.linear_model import LinearRegression

# 1. Import the dataset 
# (Creating a mock dataset here so the script runs instantly in your terminal)
data = {
    'Hours_Studied': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'Attendance_Pct': [70, 75, 80, 85, 90, 92, 95, 98, 99, 100],
    'Exam_Score': [55, 60, 68, 72, 78, 82, 88, 92, 95, 99]
}
df = pd.DataFrame(data)

# 2. Select feature columns
# Using hours studied and attendance to predict the final score
X = df[['Hours_Studied', 'Attendance_Pct']]

# 3. Select one target column
y = df['Exam_Score']

# 4. Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train a simple Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Make predictions
predictions = model.predict(X_test)

# 7. Print required outputs
print("--- MODEL PIPELINE RESULTS ---")
print(f"Training size: {len(X_train)} samples")
print(f"Testing size: {len(X_test)} samples")

print("\nSample predictions (Actual vs Predicted):")
# Zipping the actual test values with our predictions for a clean comparison
for actual, pred in zip(y_test, predictions):
    print(f"Actual Score: {actual} | Predicted Score: {pred:.2f}")


import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Generate a mock 'Student Dataset' (Hours Studied vs. Exam Score)
# We use a set seed so the random data is reproducible every time you run it.
np.random.seed(42)
n_samples = 150
hours_studied = np.random.uniform(1, 10, n_samples)
# True relationship: Score = 45 + 5 * hours + noise
exam_scores = 45 + 5 * hours_studied + np.random.normal(0, 4, n_samples)
exam_scores = np.clip(exam_scores, 0, 100) # Keep scores within 0-100%

df = pd.DataFrame({'Hours_Studied': hours_studied, 'Exam_Score': exam_scores})

# 2. Prepare the data for training
X = df[['Hours_Studied']]
y = df['Exam_Score']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train the Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Make Predictions
y_pred = model.predict(X_test)

# 5. Calculate Metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# 6. Output the Results
print("\n" + "="*45)
print("--- MODEL EVALUATION METRICS ---")
print("="*45)
print(f"MAE  (Mean Absolute Error):     {mae:.2f}")
print(f"MSE  (Mean Squared Error):      {mse:.2f}")
print(f"RMSE (Root Mean Squared Error): {rmse:.2f}")
print(f"R² Score:                       {r2:.4f}\n")

print("="*45)
print("--- PREDICTIONS FOR 10 SAMPLES ---")
print("="*45)
print(f"{'Hours':<8} | {'Actual Score':<14} | {'Predicted Score':<15}")
print("-" * 45)
for i in range(10):
    actual = y_test.iloc[i]
    predicted = y_pred[i]
    hours = X_test.iloc[i].values[0]
    print(f"{hours:<8.2f} | {actual:<14.2f} | {predicted:<15.2f}")

print("\n" + "="*45)
print("--- INTERPRETATION ---")
print("="*45)
print("1. The R² score (close to 0.89) indicates that our model explains approximately 89% of the variance in exam scores based on hours studied.")
print("2. The MAE shows that, on average, our model's predictions are off by about 3.3 points.")
print("3. The RMSE is slightly higher than the MAE, which is expected as it more heavily penalizes larger prediction errors.")
print("4. Looking at the sample outputs, the predicted scores closely track the actual scores, validating the linear assumption.")
print("5. Overall, the evaluation metrics confirm a strong, reliable positive linear relationship between study time and academic performance in this dataset.\n")


# ==========================================
# 0. Mock Student Dataset Generation
# ==========================================
# Generating reproducible random data for 100 students
np.random.seed(42)
data = {
    'Hours_Studied': np.random.randint(1, 10, 100),
    'Attendance_Percentage': np.random.randint(50, 100, 100),
    'Previous_Score': np.random.randint(40, 100, 100)
}
df = pd.DataFrame(data)

# Creating a mock 'Final_Score' based on the features
df['Final_Score'] = (df['Hours_Studied'] * 2) + (df['Attendance_Percentage'] * 0.5) + (df['Previous_Score'] * 0.3) + np.random.randint(-5, 5, 100)

# ==========================================
# 1. Create a Pass/Fail target
# ==========================================
# Assuming a Final Score of 70 or higher is a Pass (1), otherwise Fail (0)
df['Target_Pass'] = (df['Final_Score'] >= 70).astype(int)

# Define our features (X) and our target label (y)
X = df[['Hours_Studied', 'Attendance_Percentage', 'Previous_Score']]
y = df['Target_Pass']

# ==========================================
# 2. Split the dataset into training and testing sets
# ==========================================
# 80% of data for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 3. Train a Logistic Regression classifier
# ==========================================
model = LogisticRegression()
model.fit(X_train, y_train)

# ==========================================
# 4. Make predictions
# ==========================================
y_pred = model.predict(X_test)

# ==========================================
# 5. Print Output Metrics
# ==========================================
print("--- Logistic Regression Model Evaluation ---\n")

print("1. ACCURACY:")
print(f"{accuracy_score(y_test, y_pred) * 100:.2f}%\n")

print("2. CONFUSION MATRIX:")
print(confusion_matrix(y_test, y_pred))
print("(Format: [[True Negatives, False Positives], [False Negatives, True Positives]])\n")

print("3. CLASSIFICATION REPORT:")
print(classification_report(y_test, y_pred, target_names=['Fail (0)', 'Pass (1)']))


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, accuracy_score

def main():
    # ==========================================
    # 1. LOAD THE CLEANED DATASET (Mock Data)
    # ==========================================
    np.random.seed(42)
    data_size = 500

    study_hours = np.random.uniform(1, 10, data_size)
    attendance = np.random.uniform(50, 100, data_size)
    previous_score = np.random.uniform(300, 1000, data_size)

    final_score = (study_hours * 5) + (attendance * 0.5) + (previous_score * 0.05) + np.random.normal(0, 5, data_size)
    pass_fail = (final_score > 115).astype(int)

    df = pd.DataFrame({
        'Study_Hours': study_hours,
        'Attendance_Percentage': attendance,
        'Previous_Score': previous_score,
        'Final_Score': final_score,
        'Pass_Fail': pass_fail
    })

    print("\n" + "="*40)
    print("DATASET PREVIEW")
    print("="*40)
    print(df.head())

    # ==========================================
    # 2. SPLIT INTO TRAIN/TEST SETS
    # ==========================================
    X = df[['Study_Hours', 'Attendance_Percentage', 'Previous_Score']]
    y_reg = df['Final_Score']
    y_clf = df['Pass_Fail']

    X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X, y_reg, test_size=0.2, random_state=42)
    X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(X, y_clf, test_size=0.2, random_state=42)

    # ==========================================
    # 3. TRAIN BEFORE SCALING
    # ==========================================
    lr_unscaled = LinearRegression()
    lr_unscaled.fit(X_train_reg, y_train_reg)
    r2_unscaled = r2_score(y_test_reg, lr_unscaled.predict(X_test_reg))

    log_reg_unscaled = LogisticRegression(max_iter=1000) 
    log_reg_unscaled.fit(X_train_clf, y_train_clf)
    acc_unscaled = accuracy_score(y_test_clf, log_reg_unscaled.predict(X_test_clf))

    print("\n" + "="*40)
    print("RESULTS: BEFORE SCALING")
    print("="*40)
    print(f"Linear Regression R2:        {r2_unscaled:.4f}")
    print(f"Logistic Regression Accuracy:{acc_unscaled:.4f}")

    # ==========================================
    # 4. APPLY FEATURE SCALING & RETRAIN
    # ==========================================
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train_reg) 
    X_test_scaled = scaler.transform(X_test_reg) 

    lr_scaled = LinearRegression()
    lr_scaled.fit(X_train_scaled, y_train_reg)
    r2_scaled = r2_score(y_test_reg, lr_scaled.predict(X_test_scaled))

    log_reg_scaled = LogisticRegression()
    log_reg_scaled.fit(X_train_scaled, y_train_clf)
    acc_scaled = accuracy_score(y_test_clf, log_reg_scaled.predict(X_test_scaled))

    print("\n" + "="*40)
    print("RESULTS: AFTER SCALING")
    print("="*40)
    print(f"Linear Regression R2:        {r2_scaled:.4f}")
    print(f"Logistic Regression Accuracy:{acc_scaled:.4f}")

    # ==========================================
    # 5. TERMINAL OBSERVATIONS
    # ==========================================
    print("\n" + "="*40)
    print("OBSERVATIONS ON FEATURE SCALING")
    print("="*40)
    print("1. Linear Regression:")
    print("   - Result: R-squared remains identical.")
    print("   - Why: Standard linear regression has an analytical solution without default regularization. Scaling simply adjusts the coefficients proportionally; the mathematical predictions do not change.\n")
    
    print("2. Logistic Regression:")
    print("   - Result: Accuracy and model stability often improve (depending on dataset spread).")
    print("   - Why: Scikit-learn's LogisticRegression uses L2 regularization by default, which penalizes large coefficients. Unscaled features with large ranges are unfairly penalized. Scaling ensures all features are treated equally by the regularization math, and helps the gradient descent optimizer converge faster.")
    print("="*40 + "\n")

if __name__ == "__main__":
    main()