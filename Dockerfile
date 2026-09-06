# Customer Churn Prediction — Docker Configuration

# 1. Python 3.13 का lightweight base image
FROM python:3.13-slim

# 2. Container के अंदर application directory
WORKDIR /app

# 3. Python को unnecessary .pyc files बनाने से रोकना
ENV PYTHONDONTWRITEBYTECODE=1

# 4. Python output को तुरंत terminal में दिखाना
ENV PYTHONUNBUFFERED=1

# 5. Dependencies file को पहले copy करना
COPY requirements.txt .

# 6. Python dependencies install करना
RUN pip install --no-cache-dir -r requirements.txt

# 7. FastAPI application copy करना
COPY app.py .

# 8. Saved ML pipeline copy करना
COPY final_churn_pipeline.joblib .

# 9. Frontend files भी container में रखना
COPY frontend ./frontend

# 10. FastAPI का port document करना
EXPOSE 8000

# 11. Container start होते ही FastAPI चलाना
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]