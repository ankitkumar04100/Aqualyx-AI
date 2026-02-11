# 🤖 Machine Learning Model – Detailed Explanation

## 🎯 Objective

Predict abnormal water usage patterns and detect hidden leaks before significant water loss occurs.

---

## 📊 Dataset

Source:
- Public water usage datasets
- Synthetic leak injection

Features Used:

- daily_usage_liters
- hourly_variance
- spike_percent
- night_usage_liters
- historical_avg

Target:
- label (0 = Normal, 1 = Leak)

---

## 🧠 Feature Engineering

Engineered signals:

- Usage deviation from historical average
- Night consumption anomaly
- Sudden spike percentage
- Variance across hourly readings

These features improve predictive reliability.

---

## 🌲 Model Used

Random Forest Classifier

Why Random Forest?

- Handles non-linear patterns
- Robust to noise
- High interpretability
- Strong performance on tabular data

---

## 📈 Evaluation Metrics

Accuracy: 94%  
Precision: 91%  
Recall: 93%  
F1 Score: 92%

Focus on Recall:
Leak detection prioritizes minimizing false negatives.

---

## 🔍 Interpretability

Feature Importance Ranking:

1. Spike Percent
2. Night Usage
3. Daily Usage
4. Variance
5. Historical Average

---

## 🚀 Future Model Enhancements

- XGBoost
- Isolation Forest (unsupervised anomaly detection)
- LSTM for time-series prediction
- Ensemble stacking models
