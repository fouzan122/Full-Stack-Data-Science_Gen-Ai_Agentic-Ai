# Salary Prediction — Simple Linear Regression

A simple linear regression model that predicts salary based on years of experience.

## Overview

This project trains a `LinearRegression` model (scikit-learn) on the classic `Salary_Data.csv` dataset, evaluates it with R², MSE, and RMSE, visualizes the fit on the training and test sets, and saves the trained model to disk with `pickle`.

## Dataset

The script expects a CSV file named `Salary_Data.csv` with two columns:

| YearsExperience | Salary |
|---|---|
| 1.1 | 39343 |
| 1.3 | 46205 |
| ... | ... |

Place `Salary_Data.csv` in the same folder as `salary_prediction.py`, or update the file path in the script.

## Requirements

```
numpy
pandas
matplotlib
scikit-learn
statsmodels
streamlit
```

Install with:

```bash
pip install numpy pandas matplotlib scikit-learn statsmodels streamlit
```

## Usage

### Train the model

```bash
python salary_prediction.py
```

This produces `linear_regression_model.pkl` in the same folder.

### Run the prediction web app

Once the model has been trained (or if `linear_regression_model.pkl` is already in this folder), launch the Streamlit app:

```bash
streamlit run app.py
```

This opens a browser page where you can enter years of experience and get a predicted salary.

## What the script does

1. Loads and splits the dataset into training (80%) and test (20%) sets.
2. Fits a `LinearRegression` model on the training data.
3. Predicts salaries on the test set and prints an actual vs. predicted comparison table.
4. Plots the regression line against both the training and test sets.
5. Predicts salary for 12 and 20 years of experience.
6. Reports model performance: R² (train/test), MSE, RMSE.
7. Saves the trained model as `linear_regression_model.pkl`.
8. Prints an OLS regression summary table via `statsmodels`.

## Files

- `salary_prediction.py` — trains the model, evaluates it, and saves it to disk
- `app.py` — a Streamlit web app that loads the saved model and predicts salary from user-entered years of experience
- `linear_regression_model.pkl` — generated after running `salary_prediction.py` (not included in the repo; train the model to create it)

## Output

- Two matplotlib plots (training set fit, test set fit)
- Console output of predictions, performance metrics, and the OLS summary table
- `linear_regression_model.pkl` — the saved trained model

## Notes

- Random state is fixed (`random_state=0`) for reproducible train/test splits.
- This is a single-feature (simple) linear regression — it assumes a roughly linear relationship between years of experience and salary.
