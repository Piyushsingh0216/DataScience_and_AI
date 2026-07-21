import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ==========================================
# 1. Create a Simulated Student Dataset
# ==========================================
np.random.seed(42)
n_samples = 500

# Features: Hours Studied, Attendance (%), Previous Score (%)
X = pd.DataFrame({
    'Hours_Studied': np.random.uniform(1, 10, n_samples),
    'Attendance': np.random.uniform(50, 100, n_samples),
    'Previous_Score': np.random.uniform(40, 100, n_samples)
})

# Target: Final Grade (calculated with some random noise to simulate real life)
y = (3.2 * X['Hours_Studied']) + (0.4 * X['Attendance']) + (0.5 * X['Previous_Score']) + np.random.normal(0, 4, n_samples)

# ==========================================
# 2. Single Train/Test Split Method
# ==========================================
# Split the data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate metrics
split_mae = mean_absolute_error(y_test, y_pred)
split_mse = mean_squared_error(y_test, y_pred)
split_rmse = np.sqrt(split_mse)
split_r2 = r2_score(y_test, y_pred)

# ==========================================
# 3. Cross-Validation Method (5-Fold)
# ==========================================
# Define the metrics we want to track
scoring = {
    'MAE': 'neg_mean_absolute_error',
    'MSE': 'neg_mean_squared_error',
    'R2': 'r2'
}

# Perform 5-fold cross-validation on the entire dataset
cv_results = cross_validate(model, X, y, cv=5, scoring=scoring)

# Extract and average the scores (Scikit-learn makes loss metrics negative, so we multiply by -1)
cv_mae = -cv_results['test_MAE'].mean()
cv_mse = -cv_results['test_MSE'].mean()
cv_rmse = np.sqrt(cv_mse) # RMSE is just the square root of MSE
cv_r2 = cv_results['test_R2'].mean()

# ==========================================
# 4. Compare the Results
# ==========================================
print("=== Linear Regression Performance Metrics ===")
print("-" * 45)
print(f"{'Metric':<10} | {'Train/Test Split':<20} | {'5-Fold Cross-Validation'}")
print("-" * 45)
print(f"{'MAE':<10} | {split_mae:<20.4f} | {cv_mae:.4f}")
print(f"{'MSE':<10} | {split_mse:<20.4f} | {cv_mse:.4f}")
print(f"{'RMSE':<10} | {split_rmse:<20.4f} | {cv_rmse:.4f}")
print(f"{'R² Score':<10} | {split_r2:<20.4f} | {cv_r2:.4f}")
print("-" * 45)

print("\n=== Analysis ===")
print("If the Train/Test Split metrics are noticeably better (lower error, higher R²) than")
print("the Cross-Validation metrics, it often means the model got 'lucky' with an easier")
print("test set during the single split. Cross-Validation provides a more stable, reliable")
print("estimate of how the model will perform on unseen data because it tests across all data chunks.")



from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Generate Synthetic Student Performance Dataset
np.random.seed(42)
n_samples = 500

# Features
hours_studied = np.random.uniform(1, 10, n_samples)
attendance = np.random.uniform(50, 100, n_samples)
previous_score = np.random.uniform(40, 100, n_samples)

# Target: Final Score (Linear relationship + a non-linear "bonus" for studying > 8 hours + noise)
final_score = (
    3 * hours_studied + 
    0.5 * attendance + 
    0.4 * previous_score + 
    np.where(hours_studied > 8, 8, 0) + # Non-linear threshold
    np.random.normal(0, 4, n_samples)   # Random noise
)
final_score = np.clip(final_score, 0, 100) # Keep scores between 0 and 100

data = pd.DataFrame({
    'Hours_Studied': hours_studied,
    'Attendance': attendance,
    'Previous_Score': previous_score,
    'Final_Score': final_score
})

# 2. Split the Data
X = data.drop('Final_Score', axis=1)
y = data['Final_Score']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train the Models
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

dt_model = DecisionTreeRegressor(random_state=42, max_depth=5) # Limited depth to prevent severe overfitting
dt_model.fit(X_train, y_train)

# 4. Evaluation Helper Function
def evaluate_model(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    print(f"--- {model_name} ---")
    print(f"MAE:  {mae:.4f}")
    print(f"MSE:  {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R²:   {r2:.4f}\n")
    
    return r2

# 5. Evaluate and Compare
print("Model Evaluation Results:\n" + "="*25)
lr_r2 = evaluate_model(lr_model, X_test, y_test, "Linear Regression")
dt_r2 = evaluate_model(dt_model, X_test, y_test, "Decision Tree Regressor")

# 6. Identify the Winner
print("--- Conclusion ---")
if lr_r2 > dt_r2:
    print("Linear Regression performed better.")
    print("Why: The underlying data likely has a strong, straight-line relationship between the features and the target. Decision Trees tend to overfit training data and create 'blocky' predictions, which hurts performance on smooth, linear trends.")
elif dt_r2 > lr_r2:
    print("Decision Tree Regressor performed better.")
    print("Why: The underlying data likely contains non-linear relationships or complex interactions between features (e.g., a sudden jump in grades if a student studies more than 8 hours) that a simple straight line cannot capture.")
else:
    print("Both models performed equally well.")




from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ==========================================
# 1. Prepare the Dataset
# ==========================================
# Generating a synthetic "Student Performance" dataset for standalone execution
np.random.seed(42)
n_samples = 1000

# Features: Study Hours, Attendance (%), Previous Score, Sleep Hours
X_data = {
    'Study_Hours': np.random.uniform(1, 10, n_samples),
    'Attendance_pct': np.random.uniform(50, 100, n_samples),
    'Previous_Score': np.random.uniform(40, 100, n_samples),
    'Sleep_Hours': np.random.uniform(4, 10, n_samples)
}
df = pd.DataFrame(X_data)

# Target: Final Score (Linear combination of features + random noise)
df['Final_Score'] = (
    3.5 * df['Study_Hours'] + 
    0.6 * df['Attendance_pct'] + 
    0.4 * df['Previous_Score'] + 
    1.2 * df['Sleep_Hours'] + 
    np.random.normal(0, 4, n_samples) # Random noise to make it realistic
)

# Separate features (X) and target (y)
X = df[['Study_Hours', 'Attendance_pct', 'Previous_Score', 'Sleep_Hours']]
y = df['Final_Score']

# Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 2. Initialize Models
# ==========================================
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
}

# ==========================================
# 3. Train and Evaluate Models
# ==========================================
results = []

for name, model in models.items():
    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    # Store results
    results.append({
        "Model": name,
        "MAE": round(mae, 4),
        "MSE": round(mse, 4),
        "RMSE": round(rmse, 4),
        "R² Score": round(r2, 4)
    })

# ==========================================
# 4. Display Comparison Table
# ==========================================
results_df = pd.DataFrame(results)

print("\n" + "="*60)
print(" MODEL EVALUATION COMPARISON: STUDENT PERFORMANCE ")
print("="*60)
print(results_df.to_string(index=False))
print("="*60 + "\n")




from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score, 
    precision_score, 
    recall_score, 
    f1_score, 
    confusion_matrix
)

# 1. Generate a Synthetic Student Dataset
np.random.seed(42)
n_students = 500

df = pd.DataFrame({
    'Study_Hours_Per_Week': np.random.normal(12, 4, n_students).clip(0, 40),
    'Attendance_Rate': np.random.normal(85, 12, n_students).clip(0, 100),
    'Previous_Test_Score': np.random.normal(70, 15, n_students).clip(0, 100),
    'Extracurricular_Hours': np.random.normal(5, 3, n_students).clip(0, 20)
})

# 2. Create Target Column: 'Needs_Intervention' (1 = At-Risk/Fail, 0 = Safe/Pass)
# We simulate a "true" hidden score based on their habits, adding some random noise
hidden_score = (
    (df['Study_Hours_Per_Week'] * 2.5) + 
    (df['Attendance_Rate'] * 0.4) + 
    (df['Previous_Test_Score'] * 0.5) + 
    np.random.normal(0, 5, n_students)
)

# If the student's hidden score falls in the bottom 30%, they are marked as needing intervention
threshold = np.percentile(hidden_score, 30)
df['Needs_Intervention'] = (hidden_score < threshold).astype(int)

# 3. Prepare Data and Train the DecisionTreeClassifier
X = df.drop('Needs_Intervention', axis=1)
y = df['Needs_Intervention']

# Split into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the model
# Limiting max_depth prevents the tree from massively overfitting our synthetic data
clf = DecisionTreeClassifier(max_depth=4, random_state=42)
clf.fit(X_train, y_train)

# 4. Predict and Evaluate
y_pred = clf.predict(X_test)

print("=== Student Success Predictor Evaluation ===\n")
print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall   : {recall_score(y_test, y_pred):.4f}")
print(f"F1-Score : {f1_score(y_test, y_pred):.4f}\n")

print("=== Confusion Matrix ===")
print("Format: [[True Negatives (TN), False Positives (FP)]")
print("         [False Negatives (FN), True Positives (TP)]]\n")
print(confusion_matrix(y_test, y_pred))