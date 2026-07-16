# Student Performance Prediction using Machine Learning

## Project Overview

This beginner-friendly Data Science project predicts a student's final exam score using study habits and background information. The project includes a Streamlit dashboard, reusable Python modules, and a complete machine learning workflow: data loading, cleaning, exploration, feature engineering, model training, evaluation, prediction, output export, and model saving.

If the dataset does not exist, the project automatically generates a realistic CSV file with more than 1000 student records.

## Features

- Generates a realistic student performance dataset
- Loads data using Pandas
- Cleans missing values and duplicate rows
- Performs exploratory data analysis with Matplotlib
- Saves graphs automatically in `outputs/graphs`
- Trains Linear Regression, Decision Tree Regressor, and Random Forest Regressor models
- Evaluates models using MAE, MSE, RMSE, R2 Score, and Training Time
- Compares models and highlights the best model by R2 Score
- Saves trained models using pickle
- Predicts exam scores for new student data
- Saves processed, train, test, prediction, and model comparison CSV files in `outputs/`
- Provides a dashboard with preprocessing cards, charts, tables, and download buttons

## Folder Structure

```text
Student_Performance_Prediction/
|
|-- data/
|   `-- students.csv
|
|-- notebooks/
|   `-- analysis.ipynb
|
|-- src/
|   |-- config.py
|   |-- data_loader.py
|   |-- preprocessing.py
|   |-- visualization.py
|   |-- models.py
|   |-- evaluation.py
|   |-- downloads.py
|   |-- utils.py
|   |-- pipeline.py
|   |-- dashboard.py
|   |-- data_cleaning.py
|   |-- train_model.py
|   `-- predict.py
|
|-- models/
|   |-- linear_regression.pkl
|   `-- best_model.pkl
|
|-- outputs/
|   |-- graphs/
|   |-- processed_data.csv
|   |-- train_data.csv
|   |-- test_data.csv
|   |-- predictions.csv
|   `-- model_comparison.csv
|
|-- requirements.txt
|-- README.md
`-- .gitignore
```

## Dataset Description

The dataset contains the following columns:

| Column | Description |
| --- | --- |
| `Hours_Studied` | Number of hours the student studies per day |
| `Attendance` | Attendance percentage |
| `Sleep_Hours` | Average sleep hours per night |
| `Previous_Score` | Student's previous exam score |
| `Assignments_Completed` | Number of assignments completed |
| `Internet_Access` | Whether the student has internet access |
| `Family_Income` | Family income category: Low, Medium, or High |
| `Exam_Score` | Final exam score to be predicted |

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Jupyter Notebook
- Pickle

## Installation

1. Clone or download this project.
2. Open a terminal in the project folder.
3. Install the required libraries:

```bash
pip install -r requirements.txt
```

## Usage

Run the files in this order:

```bash
python src/data_cleaning.py
python src/visualization.py
python src/train_model.py
python src/predict.py
```

Run the dashboard:

```bash
streamlit run src/dashboard.py
```

You can also open the notebook:

```bash
jupyter notebook notebooks/analysis.ipynb
```

## Results

The models are evaluated using:

- **MAE**: Average absolute difference between actual and predicted scores
- **MSE**: Average squared difference between actual and predicted scores
- **RMSE**: Prediction error in the same unit as exam scores
- **R2 Score**: How much variation in exam scores is explained by the model
- **Training Time**: Time needed to train each model

The original Linear Regression model is still saved at:

```text
models/linear_regression.pkl
```

The best model by R2 Score is saved at:

```text
models/best_model.pkl
```

The prediction results are saved at:

```text
outputs/predictions.csv
```

## Dashboard Features

The Streamlit dashboard displays preprocessing summary cards, model comparison results, a model metrics chart, prediction previews, cleaned data previews, and CSV download buttons. The layout uses consistent spacing, aligned sections, modern colors, and responsive columns.

## Model Comparison

The pipeline trains and compares:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

The comparison table includes Model, MAE, MSE, RMSE, R2 Score, and Training Time. The best model is selected automatically based on the highest R2 Score.

The model comparison chart is saved at:

```text
outputs/graphs/model_comparison.png
```

## Preprocessing Summary

The dashboard summary cards show:

- Total Rows
- Total Columns
- Missing Values Before Cleaning
- Missing Values After Cleaning
- Duplicate Rows Removed
- Number of Features
- Target Column
- Train/Test Split Ratio

## Download Options

The dashboard provides buttons for downloading:

- Cleaned Dataset: `outputs/processed_data.csv`
- Train Dataset: `outputs/train_data.csv`
- Test Dataset: `outputs/test_data.csv`
- Prediction Results: `outputs/predictions.csv`
- Model Comparison: `outputs/model_comparison.csv`

## Project Architecture

The project uses reusable modules:

- `data_loader.py`: Loads or generates the dataset
- `preprocessing.py`: Cleans data, prepares features, and builds preprocessing summaries
- `models.py`: Trains, saves, loads, and predicts with regression models
- `evaluation.py`: Calculates regression metrics
- `visualization.py`: Creates EDA and model comparison graphs
- `downloads.py`: Saves CSV outputs
- `pipeline.py`: Runs the full machine learning pipeline
- `dashboard.py`: Displays the Streamlit dashboard
- `utils.py`: Stores small shared helper functions

The pipeline follows this flow:

```text
Load Data -> Clean Data -> Feature Engineering -> Train Models
-> Evaluate Models -> Generate Predictions -> Save Outputs
```

## Screenshots Placeholder

Graphs generated by the project are saved in `outputs/graphs`:

- Histogram of exam scores
- Scatter plot of hours studied vs exam score
- Box plot of exam scores
- Correlation heatmap
- Bar graph of average exam score by internet access
- Model comparison chart

Add dashboard screenshots here after running:

```text
screenshots/dashboard_home.png
screenshots/model_comparison.png
screenshots/downloads.png
```

## Future Improvements

- Add more student behavior features
- Perform deeper feature engineering
- Add more visual analysis in the notebook
- Add model explainability charts
- Add cross-validation for more reliable model comparison
- Add filters to the dashboard for category-level analysis

## License

This project is open source and available for learning and portfolio use.
