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