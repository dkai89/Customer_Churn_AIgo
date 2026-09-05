# Step 10-12 — FastAPI Prediction API Automated Test

import requests


# ============================================================
# API URL
# ============================================================

url = "http://127.0.0.1:8000/predict"


# ============================================================
# Test Customer Data
# ============================================================

customer_data = {
    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "DSL",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 55.50,
    "TotalCharges": 666.00
}


# ============================================================
# Send Request to API
# ============================================================

response = requests.post(
    url,
    json=customer_data
)


# ============================================================
# Display Test Result
# ============================================================

print("Status Code:", response.status_code)

print("Response:")
print(response.json())


# ============================================================
# Basic Validation
# ============================================================

if response.status_code == 200:
    print("\nAPI TEST PASSED ✅")
else:
    print("\nAPI TEST FAILED ❌")