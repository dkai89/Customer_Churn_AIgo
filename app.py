# Step 10-11 — FastAPI Customer Churn Prediction API

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib


# ============================================================
# Step 10-7 — Customer Input Schema
# ============================================================

class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float | None = None


# ============================================================
# Step 10-11 — Prediction Response Schema
# ============================================================

class PredictionResponse(BaseModel):
    prediction: str
    prediction_code: int
    churn_probability: float
    no_churn_probability: float


# ============================================================
# FastAPI Application
# ============================================================

app = FastAPI(
    title="Customer Churn Prediction API",
    description="API for predicting customer churn",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ============================================================
# Saved ML Pipeline Load करें
# ============================================================

model = joblib.load("final_churn_pipeline.joblib")


# ============================================================
# Home Endpoint
# ============================================================

@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running!"
    }


# ============================================================
# Model Status Endpoint
# ============================================================

@app.get("/model-status")
def model_status():
    return {
        "model_loaded": True,
        "model_type": type(model).__name__
    }


# ============================================================
# Step 10-10 / Step 10-11 — Prediction Endpoint
# ============================================================

# Step 10-13 — Prediction Endpoint Error Handling

@app.post("/predict", response_model=PredictionResponse)
def predict(customer: CustomerData):

    try:
        # Customer data को DataFrame में बदलें
        customer_df = pd.DataFrame([customer.model_dump()])

        # Prediction करें
        prediction = model.predict(customer_df)[0]
        probability = model.predict_proba(customer_df)[0]

        # Prediction को readable label में बदलें
        prediction_label = "Churn" if prediction == 1 else "No Churn"

        # Response भेजें
        return {
            "prediction": prediction_label,
            "prediction_code": int(prediction),
            "churn_probability": round(float(probability[1]), 4),
            "no_churn_probability": round(float(probability[0]), 4)
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(error)}"
        )