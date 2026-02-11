# 📡 Aqualyx AI – API Documentation

## 🔍 Health Check

### GET /health

Returns service status.

Response:
{
  "status": "healthy"
}

---

## 🔮 Predict Leak Risk

### POST /predict

Request Body:
{
  "daily_usage_liters": 420,
  "hourly_variance": 0.75,
  "spike_percent": 30,
  "night_usage_liters": 40,
  "historical_avg": 320
}

Response:
{
  "leak_probability": 0.87,
  "risk_level": "Critical",
  "estimated_water_loss_liters": 120,
  "estimated_cost_loss": 15.5,
  "environmental_impact_score": 0.92
}

---

## 📊 Model Metrics

### GET /metrics

Response:
{
  "accuracy": 0.94,
  "precision": 0.91,
  "recall": 0.93,
  "f1_score": 0.92
}

---

## 🛑 Error Handling

All errors follow:

{
  "error": "Invalid input data"
}

HTTP Status Codes:
- 200 OK
- 400 Bad Request
- 500 Server Error
