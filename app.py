# Step 15 — Production FastAPI + Frontend Serving

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import pandas as pd
import joblib


# ============================================================
# 1. Customer Input Schema
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
# 2. Prediction Response Schema
# ============================================================

class PredictionResponse(BaseModel):
    prediction: str
    prediction_code: int
    churn_probability: float
    no_churn_probability: float


# ============================================================
# 3. FastAPI Application
# ============================================================

app = FastAPI(
    title="Customer Churn Prediction API",
    description="API for predicting customer churn",
    version="1.0.0"
)


# ============================================================
# 4. CORS Middleware
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# ============================================================
# 5. Load Saved ML Pipeline
# ============================================================

model = joblib.load("final_churn_pipeline.joblib")


# ============================================================
# 6. API Health Check
# ============================================================

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": True,
        "model_type": type(model).__name__
    }


# ============================================================
# 7. Model Status
# ============================================================

@app.get("/model-status")
def model_status():
    return {
        "model_loaded": True,
        "model_type": type(model).__name__
    }


# ============================================================
# 8. Prediction API
# ============================================================

@app.post("/predict", response_model=PredictionResponse)
def predict(customer: CustomerData):

    try:
        customer_df = pd.DataFrame([customer.model_dump()])

        prediction = model.predict(customer_df)[0]

        probability = model.predict_proba(customer_df)[0]

        prediction_label = (
            "Churn"
            if prediction == 1
            else "No Churn"
        )

        return {
            "prediction": prediction_label,
            "prediction_code": int(prediction),
            "churn_probability": round(
                float(probability[1]), 4
            ),
            "no_churn_probability": round(
                float(probability[0]), 4
            )
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(error)}"
        )


# ============================================================
# 9. Serve Frontend
# ============================================================

@app.get("/", include_in_schema=False)
def serve_frontend():
    return FileResponse("frontend/index.html")


# ============================================================
# 10. Serve Frontend Static Files
# ============================================================

app.mount(
    "/",
    StaticFiles(
        directory="frontend",
        html=True
    ),
    name="frontend"
)