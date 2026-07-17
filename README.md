# Heart Disease Prediction (UCI Dataset)

End-to-end ML pipeline on the UCI Heart Disease dataset: data cleaning, dimensionality reduction, feature selection, supervised and unsupervised modeling, hyperparameter tuning, and a Streamlit app for live predictions.

## Results

Best model: **SVM (linear kernel, C=0.1)**, selected via hyperparameter tuning.

| Metric | Score |
|---|---|
| Accuracy | 0.84 |
| Precision (macro) | 0.84 |
| Recall (macro) | 0.83 |
| F1 (macro) | 0.83 |

## Pipeline

1. **Preprocessing** (`01_data_preprocessing.ipynb`) - cleaning, encoding, scaling
2. **PCA analysis** (`02_pca_analysis.ipynb`) - dimensionality reduction, variance analysis
3. **Feature selection** (`03_feature_selection.ipynb`)
4. **Supervised learning** (`04_supervised_learning.ipynb`) - trains and compares classifiers
5. **Unsupervised learning** (`05_unsupervised_learning.ipynb`) - clustering analysis
6. **Hyperparameter tuning** (`06_hyperparameter_tuning.ipynb`) - grid search, final model selection

## Project structure

data/         raw dataset (heart_disease.csv)
notebooks/    the six pipeline stages above
models/       final_model.pkl (trained SVM)
ui/           app.py — Streamlit interface for live predictions
deployment/   ngrok setup for exposing the local app
results/      evaluation_metrics.txt


## Run it
bash
pip install -r requirements.txt
streamlit run ui/app.py


## Stack
Python, scikit-learn, pandas, Streamlit, matplotlib/seaborn
