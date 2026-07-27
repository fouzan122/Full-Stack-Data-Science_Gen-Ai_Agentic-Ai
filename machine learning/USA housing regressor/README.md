# USA Housing Price Prediction

A Flask web app that predicts house prices in the USA using 13 different regression models trained on the USA Housing dataset. Users pick a model from a dropdown, enter property details, and get an instant price prediction.

## Features

- 13 trained regression models to choose from (Linear, Ridge, Lasso, ElasticNet, Polynomial, SGD, ANN, Random Forest, SVM, LightGBM, XGBoost, KNN, and Robust/Huber Regression)
- Simple web form for entering house features
- Model evaluation results (MAE, MSE, R²) viewable in-app
- Pre-trained `.pkl` models included — no need to retrain before running

## Dataset

`USA_Housing.csv` — contains the following features:

- Avg. Area Income
- Avg. Area House Age
- Avg. Area Number of Rooms
- Avg. Area Number of Bedrooms
- Area Population
- Price (target)
- Address (dropped during training)

## Project Structure

```
.
├── app.py                        # Flask application
├── model.py                      # Trains all models and saves them as .pkl files
├── USA_Housing.csv               # Training dataset
├── model_evaluation_results.csv  # Saved MAE/MSE/R² for each model
├── templates/                    # HTML templates (index.html, results.html, model.html)
├── *.pkl                         # Trained model files (see Model Files note below)
└── README.md
```

## Model Performance

| Model | MAE | MSE | R² |
|---|---|---|---|
| LinearRegression | 82,657.95 | 1.055e+10 | 0.9146 |
| RidgeRegression | 82,659.67 | 1.055e+10 | 0.9146 |
| LassoRegression | 82,657.95 | 1.055e+10 | 0.9146 |
| PolynomialRegression | 84,400.69 | 1.109e+10 | 0.9103 |
| LGBM | 92,133.99 | 1.310e+10 | 0.8940 |
| XGBoost | 101,565.19 | 1.614e+10 | 0.8694 |
| RandomForest | 98,314.87 | 1.495e+10 | 0.8790 |
| ElasticNet | 99,126.81 | 1.508e+10 | 0.8780 |
| KNN | 198,086.24 | 6.040e+10 | 0.5114 |
| ANN | 199,048.34 | 6.139e+10 | 0.5033 |
| RobustRegression | 199,465.56 | 6.166e+10 | 0.5011 |
| SVM | 282,947.69 | 1.235e+11 | 0.0004 |
| SGDRegressor | — | — | diverged (unscaled features) |

Linear-family models (Linear, Ridge, Lasso) perform best on this dataset. SVM and SGDRegressor underperform because features aren't scaled — a good next step is adding a `StandardScaler` step to the pipeline.

## Setup & Installation

```bash
git clone <your-repo-url>
cd <your-repo-folder>
pip install -r requirements.txt
```

### Requirements

```
flask
pandas
scikit-learn
lightgbm
xgboost
```

## Usage

### Run the app

```bash
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

### Retrain models (optional)

`model.py` currently loads the dataset from a local Windows path. Update this line before rerunning:

```python
data = pd.read_csv(r"C:\Users\fouza\Downloads\USA Housing regressor\USA_Housing.csv")
```

to a relative path, e.g.:

```python
data = pd.read_csv("USA_Housing.csv")
```

Then run:

```bash
python model.py
```

This retrains all 13 models and overwrites the `.pkl` files and `model_evaluation_results.csv`.

## Note on Model Files

`RandomForest.pkl` (~35 MB) exceeds GitHub's 25 MB web-upload limit. Options to include it in the repo:

- **Push via `git` CLI** — a normal `git push` allows files up to 100 MB, so cloning and pushing from the command line works fine even though the web uploader rejects it.
- **Git LFS** (recommended for binary model files):
  ```bash
  git lfs install
  git lfs track "*.pkl"
  git add .gitattributes
  git add RandomForest.pkl
  git commit -m "Add RandomForest model via LFS"
  git push
  ```

All other `.pkl` files are well under the size limit and can be uploaded normally.

## Tech Stack

- Python, Flask
- scikit-learn, LightGBM, XGBoost
- Pandas

## License

Add your preferred license here (e.g., MIT).
