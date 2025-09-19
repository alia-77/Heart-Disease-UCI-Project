# Heart Disease UCI Project

This project analyzes the UCI Heart Disease dataset, builds supervised and unsupervised models,
applies PCA and feature selection, and includes a Streamlit UI for real-time predictions.

## Folder structure
- data/ → contains `heart_disease.csv`
- notebooks/ → Jupyter notebooks for each step
- models/ → trained models in `.pkl` format
- ui/ → `app.py` (Streamlit UI)
- deployment/ → ngrok setup instructions
- results/ → evaluation metrics
- README.md, requirements.txt, .gitignore

## Quick setup
```bash
pip install -r requirements.txt
streamlit run ui/app.py
