# Network Security — Phishing Detection

An end-to-end machine-learning project for classifying phishing records. It combines data ingestion,
validation, transformation, model training, experiment tracking, and a FastAPI prediction interface.

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white">
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white">
  <img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-models-F7931E?logo=scikitlearn&logoColor=white">
  <img alt="MLflow" src="https://img.shields.io/badge/MLflow-tracking-0194E2?logo=mlflow&logoColor=white">
  <img alt="MongoDB" src="https://img.shields.io/badge/MongoDB-ingestion-47A248?logo=mongodb&logoColor=white">
</p>

## Pipeline

```mermaid
flowchart LR
    Mongo[(MongoDB)] --> Ingest[Data ingestion]
    Ingest --> Validate[Schema validation]
    Validate --> Transform[Preprocessing]
    Transform --> Train[Model training]
    Train --> Track[MLflow]
    Train --> Model[Saved model]
    CSV[Prediction CSV] --> API[FastAPI /predict]
    Model --> API
```

## Repository guide

- `NetworkSecurity/components/` — ingestion, validation, transformation, and training stages.
- `NetworkSecurity/pipeline/` — training and batch-prediction orchestration.
- `NetworkSecurity/data_schema/schema.yaml` — expected input schema.
- `final_model/` — model and preprocessor loaded by the prediction API.
- `app.py` — FastAPI training and CSV prediction routes.
- `network_data/` and `valid_data/` — sample input data.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:MONGODB_URL_KEY = "<your MongoDB connection string>"
python app.py
```

Open `http://localhost:8000/docs` for the interactive API documentation.

| Route | Purpose |
| --- | --- |
| `GET /train` | Run the training pipeline and write fresh experiment artifacts locally. |
| `POST /predict` | Upload a CSV, run the persisted preprocessing/model pipeline, and render predictions. |

## Notes

- Credentials are read from `MONGODB_URL_KEY`; do not commit `.env` files or connection strings.
- MLflow run output, caches, logs, and prediction exports are intentionally ignored.
- The repository includes the model artifacts required by the prediction demo; no performance claim is made
  without a separately reproducible evaluation report.
