# Customer Churn Prediction API

A production-style Customer Churn Prediction system built using Machine Learning and FastAPI.

## 📌 Project Overview

Customer churn prediction helps businesses identify customers who are likely to stop using their services.

This project uses a Machine Learning pipeline to predict whether a customer is likely to churn based on customer demographic, service, contract, and billing information.

The trained Machine Learning model is integrated with a FastAPI backend and exposed through a REST API.

---

## 🎯 Business Problem

Customer churn can negatively affect business revenue and customer retention.

The goal of this project is to predict potential customer churn so that businesses can identify high-risk customers and take proactive retention actions.

---

## 🤖 Machine Learning

### Model

Random Forest Classifier

### Preprocessing

The production pipeline includes:

- Numerical missing-value imputation using median
- Categorical missing-value imputation using most frequent value
- One-hot encoding for categorical features
- Unknown-category handling
- Random Forest classification

All preprocessing and the model are combined into a single Scikit-learn Pipeline.

This helps ensure that training and prediction use the same preprocessing logic.

---

## 📊 Model Performance

The final production pipeline was evaluated on a held-out test dataset.

| Metric | Result |
|---|---:|
| Accuracy | 76.86% |
| Churn Precision | 55% |
| Churn Recall | 72% |
| Churn F1 Score | 62% |

### Confusion Matrix

```text
                 Predicted
               No Churn  Churn

Actual
No Churn          812     223
Churn             103     271