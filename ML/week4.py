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



import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score, 
                             recall_score, f1_score, 
                             confusion_matrix, ConfusionMatrixDisplay)

# ==========================================
# 1. GENERATE SYNTHETIC STUDENT DATASET
# ==========================================
np.random.seed(42)
n_samples = 500

data = {
    'Hours_Studied': np.random.normal(loc=15, scale=5, size=n_samples),
    'Attendance_Pct': np.random.normal(loc=85, scale=10, size=n_samples).clip(0, 100),
    'Previous_Scores': np.random.normal(loc=70, scale=15, size=n_samples).clip(0, 100),
    'Extracurricular_Activities': np.random.randint(0, 4, size=n_samples)
}
df = pd.DataFrame(data)

# Target: Pass (1) or Fail (0) based on a noisy combination of features
score = (df['Hours_Studied'] * 2 + df['Attendance_Pct'] * 0.5 + df['Previous_Scores'] * 0.3)
df['Passed'] = (score > score.median() + np.random.normal(0, 5, n_samples)).astype(int)

X = df.drop('Passed', axis=1)
y = df['Passed']

# ==========================================
# 2. SPLIT DATA & TRAIN MODELS
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize both classifiers (limiting depth to prevent heavy overfitting on synthetic data)
dt_model = DecisionTreeClassifier(random_state=42, max_depth=5)
rf_model = RandomForestClassifier(random_state=42, n_estimators=100, max_depth=5)

# Train both models
dt_model.fit(X_train, y_train)
rf_model.fit(X_train, y_train)

# ==========================================
# 3. EVALUATE METRICS
# ==========================================
def evaluate_and_print(name, model, X_test, y_test):
    y_pred = model.predict(X_test)
    print(f"--- {name} ---")
    print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred):.4f}")
    print(f"Recall:    {recall_score(y_test, y_pred):.4f}")
    print(f"F1-Score:  {f1_score(y_test, y_pred):.4f}\n")
    return y_pred

# Print comparisons to the terminal
dt_preds = evaluate_and_print("Decision Tree Classifier", dt_model, X_test, y_test)
rf_preds = evaluate_and_print("Random Forest Classifier", rf_model, X_test, y_test)

# ==========================================
# 4. DISPLAY CHARTS (Confusion Matrix & Feature Importance)
# ==========================================
# Set up a 1x3 grid for our plots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Plot 1: Decision Tree Confusion Matrix
cm_dt = confusion_matrix(y_test, dt_preds)
disp_dt = ConfusionMatrixDisplay(confusion_matrix=cm_dt, display_labels=["Fail", "Pass"])
disp_dt.plot(ax=axes[0], cmap='Blues', colorbar=False)
axes[0].set_title("Decision Tree\nConfusion Matrix")

# Plot 2: Random Forest Confusion Matrix
cm_rf = confusion_matrix(y_test, rf_preds)
disp_rf = ConfusionMatrixDisplay(confusion_matrix=cm_rf, display_labels=["Fail", "Pass"])
disp_rf.plot(ax=axes[1], cmap='Greens', colorbar=False)
axes[1].set_title("Random Forest\nConfusion Matrix")

# Plot 3: Random Forest Feature Importances
importances = rf_model.feature_importances_
features = X.columns
indices = np.argsort(importances)

axes[2].barh(range(len(indices)), importances[indices], color='mediumpurple', align='center')
axes[2].set_yticks(range(len(indices)))
axes[2].set_yticklabels([features[i] for i in indices])
axes[2].set_title("Random Forest\nFeature Importances")
axes[2].set_xlabel("Relative Importance")

plt.tight_layout()
plt.show()




from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 1. Generate a synthetic Student Performance dataset
# Features: Attendance (%), Study Hours/Week, Previous Grade (%), Sleep Hours/Night
# Target: Passed (1) or Failed (0)
np.random.seed(42)
n_samples = 1000

attendance = np.random.normal(75, 15, n_samples).clip(0, 100)
study_hours = np.random.normal(15, 8, n_samples).clip(0, 50)
prev_grade = np.random.normal(65, 20, n_samples).clip(0, 100)
sleep_hours = np.random.normal(7, 1.5, n_samples).clip(0, 12)

# Create a realistic target where higher metrics improve the chance of passing
prob_pass = (attendance * 0.4 + study_hours * 1.5 + prev_grade * 0.5 + sleep_hours * 2) / 100
target = np.where(prob_pass + np.random.normal(0, 0.2, n_samples) > 0.65, 1, 0)

data = pd.DataFrame({
    'Attendance': attendance,
    'StudyHours': study_hours,
    'PrevGrade': prev_grade,
    'SleepHours': sleep_hours,
    'Passed': target
})

X = data.drop('Passed', axis=1)
y = data['Passed']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Function to evaluate and print metrics
def evaluate_model(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)
    print(f"--- {model_name} Metrics ---")
    print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred):.4f}")
    print(f"Recall   : {recall_score(y_test, y_pred):.4f}")
    print(f"F1-Score : {f1_score(y_test, y_pred):.4f}\n")

# 2. Train Default Model
default_rf = RandomForestClassifier(random_state=42)
default_rf.fit(X_train, y_train)
evaluate_model(default_rf, X_test, y_test, "Default RandomForest")

# 3. Hyperparameter Tuning
print("Tuning hyperparameters (n_estimators, max_depth)... Please wait.\n")
param_grid = {
    'n_estimators': [50, 100, 200, 300],
    'max_depth': [None, 5, 10, 15, 20]
}

grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring='f1', # Optimizing for F1-score
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

# 4. Train Tuned Model
tuned_rf = grid_search.best_estimator_
print(f"Best Parameters Found: {grid_search.best_params_}\n")

evaluate_model(tuned_rf, X_test, y_test, "Tuned RandomForest")






from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# ==========================================
# 1. GENERATE SYNTHETIC DATASET (or load yours)
# ==========================================
np.random.seed(42)
n_samples = 1000

# Creating 10 features, some highly predictive, some random noise
data = {
    'study_hours_per_week': np.random.normal(10, 4, n_samples),
    'attendance_rate': np.random.normal(85, 10, n_samples),
    'previous_term_score': np.random.normal(70, 15, n_samples),
    'sleep_hours_per_night': np.random.normal(7, 1.5, n_samples),
    'screen_time_hours': np.random.normal(5, 2, n_samples),
    'extracurricular_activities': np.random.randint(0, 4, n_samples),
    'parent_education_level': np.random.randint(1, 4, n_samples),
    'commute_time_mins': np.random.normal(30, 15, n_samples),
    'tutoring_sessions': np.random.randint(0, 5, n_samples),
    'stress_level': np.random.randint(1, 10, n_samples)
}
df = pd.DataFrame(data)

# Target Variable: 'Passed' (1 for Pass, 0 for Fail)
# The outcome heavily relies on study hours, attendance, and previous scores.
target_threshold = (df['study_hours_per_week'] * 1.5 + 
                    df['attendance_rate'] * 0.5 + 
                    df['previous_term_score'] * 0.8)
df['passed'] = (target_threshold > 115).astype(int)

# Separate features (X) and target (y)
X = df.drop('passed', axis=1)
y = df['passed']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# ==========================================
# 2. TRAIN BASELINE MODEL
# ==========================================
rf_base = RandomForestClassifier(random_state=42)
rf_base.fit(X_train, y_train)
y_pred_base = rf_base.predict(X_test)

def evaluate_model(y_true, y_pred):
    return {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred),
        "Recall": recall_score(y_true, y_pred),
        "F1-Score": f1_score(y_true, y_pred)
    }

base_metrics = evaluate_model(y_test, y_pred_base)


# ==========================================
# 3. IDENTIFY TOP 5 FEATURES
# ==========================================
feature_importances = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf_base.feature_importances_
}).sort_values(by='Importance', ascending=False)

top_5_features = feature_importances['Feature'].head(5).tolist()


# ==========================================
# 4. RETRAIN MODEL WITH TOP 5 FEATURES
# ==========================================
X_train_reduced = X_train[top_5_features]
X_test_reduced = X_test[top_5_features]

rf_reduced = RandomForestClassifier(random_state=42)
rf_reduced.fit(X_train_reduced, y_train)
y_pred_reduced = rf_reduced.predict(X_test_reduced)

reduced_metrics = evaluate_model(y_test, y_pred_reduced)


# ==========================================
# 5. COMPARE RESULTS & PRINT CONCLUSION
# ==========================================
print("\n--- TOP 5 MOST IMPORTANT FEATURES ---")
for i, feature in enumerate(top_5_features, 1):
    print(f"{i}. {feature}")

print("\n--- PERFORMANCE COMPARISON ---")
comparison_df = pd.DataFrame({
    'Baseline Model (10 features)': base_metrics,
    'Reduced Model (Top 5 features)': reduced_metrics
})
print(comparison_df.round(4).to_string())

print("\n--- CONCLUSION ---")
diff_f1 = reduced_metrics['F1-Score'] - base_metrics['F1-Score']
if abs(diff_f1) < 0.02:
    print("CONCLUSION: Reducing the features maintained model performance beautifully. By dropping the bottom 5 noisy/unimportant features, we simplified the model, reduced potential overfitting, and achieved nearly identical accuracy and F1-scores. This makes the model faster to run and easier to explain without sacrificing predictive power.")
elif diff_f1 > 0:
    print("CONCLUSION: Reducing the features actually IMPROVED performance! By removing noise and irrelevant variables, the Random Forest model was able to focus strictly on the core drivers of student success, leading to better generalization on the test set.")
else:
    print("CONCLUSION: Reducing the features caused a slight drop in performance. While the top 5 features capture the majority of the predictive power, the remaining features contained minor, non-negligible signals that the baseline model successfully leveraged.")