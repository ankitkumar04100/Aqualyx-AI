# 🌊 Aqualyx AI: Intelligence That Protects Every Drop

![Thumbnail](https://github.com/user-attachments/assets/258a98d7-b58a-4dbd-942f-63b4d0889ba5)

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18-blue)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.105-green)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

---

## Table of Contents
1. [Inspiration](#inspiration)
2. [What it Does](#what-it-does)
3. [Tech Stack](#tech-stack)
4. [How We Built It](#how-we-built-it)
5. [Machine Learning Model](#machine-learning-model)
6. [Dataset](#dataset)
7. [Architecture](#architecture)
8. [Frontend](#frontend)
9. [Backend](#backend)
10. [App Demo & Screenshots](#app-demo)
11. [Deployment](#deployment)
12. [Challenges](#challenges)
13. [Accomplishments](#accomplishments)
14. [Future Scope](#future-scope)
15. [License](#license)
16. [Contact](#contact)


## 🚀 Overview

Aqualyx AI is an **AI-powered predictive water management system** that detects hidden leaks and abnormal water usage patterns **before they cause damage or waste**. By combining **machine learning, real-time analytics, and a clean dashboard**, it empowers homes, campuses, and cities to **save water, money, and resources**.  

This project demonstrates **innovation, technical depth, and environmental impact**—perfect for hackathon submissions.

---

## 🌟 Features

- Predicts water leaks using **machine learning**  
- Detects abnormal usage patterns and anomalies  
- Classifies usage: **Normal, Warning, Critical**  
- Provides actionable insights: **water saved, cost saved, environmental impact**  
- Clean, responsive **dashboard**  
- Cloud-ready architecture for **easy deployment**  

---

## 💡 Inspiration

Water scarcity is a growing global problem. Most monitoring systems only report consumption **after waste has occurred**, providing little preventive value.  

As a **B.Tech CSE student**, I wanted to create a **system that predicts leaks and abnormal usage** using **AI**, shifting water management from reactive to **proactive intelligence**.  

> *“What if we could detect leaks before they cause damage?”* — this question inspired **Aqualyx AI**.

---

## 🛠️ Tech Stack

**Languages & Frameworks:** Python, JavaScript, React, Tailwind CSS  
**Machine Learning & Data:** Scikit-learn, Pandas, NumPy, Matplotlib, Plotly  
**Backend & APIs:** FastAPI, SQLite  
**Cloud & Deployment:** Render (Backend), Vercel (Frontend)  
**Tools & Productivity:** Git, GitHub, Figma, Canva  
**Concepts:** Time-series analysis, anomaly detection, predictive modeling  
**Dataset:** Public water consumption datasets + simulated leak data  

---

## 🏗️ How We Built It

Aqualyx AI is **full-stack, end-to-end**:

1. **Data Collection:** Gathered sample water usage dataset, injected simulated leak events.  
2. **Feature Engineering:** Calculated daily usage, variance, spikes, historical averages, and time-of-day metrics.  
3. **Model Training:** Random Forest classifier trained to predict leak probability.  
4. **Backend:** FastAPI serves predictions via `/predict` API.  
5. **Frontend:** React dashboard shows risk scores, usage stats, and estimated savings.  
6. **Deployment:** Backend on Render, frontend on Vercel.

---

## 🤖 Machine Learning Model

### Features
- Daily water consumption  
- Hourly variance  
- Sudden spike percentage  
- Historical average usage  
- Time-of-day consumption patterns

### Model
Random Forest Classifier predicts **leak probability**:

\[
f(X) \rightarrow P(\text{Leak})
\]

Where `X` = usage features  
Output = probability of leakage

### Evaluation Metrics
\[
\text{Accuracy}, \quad \text{Precision}, \quad \text{Recall}, \quad \text{F1 Score}
\]

python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy*100:.2f}%")

---

## 🗂️ Dataset

`sample_water_usage.csv` contains:

| timestamp          | usage_liters |
|-------------------|--------------|
| 2026-01-01 00:00  | 0.5          |
| 2026-01-01 01:00  | 0.6          |

- Real-world public datasets augmented with **simulated leak data**  
- Features engineered for **predictive anomaly detection**

---

## 🏛️ Architecture

**Flow:**
- User → React Dashboard → FastAPI Backend → ML Model → Risk Score & Insights

---

**Components:**

- **Frontend:** Dashboard & visualization  
- **Backend:** API & database  
- **ML Model:** Leak detection & risk scoring  
- **Insights Engine:** Cost/water/environmental impact metrics

---

## 💻 Frontend

- Built with **React + Tailwind CSS**  
- Pages: Home, Analytics, Savings  
- Components: Risk Meter, Usage Graph, Savings Report  
- Fully **responsive & mobile-friendly**

---

## ⚙️ Backend

- **FastAPI** server exposes `/predict` endpoint  
- Serves ML model predictions  
- Stores historical usage in **SQLite**  
- Supports **scalable cloud deployment**

---

## 🎬 App Demo

[Aqualyx-AI](https://aqualyxai.lovable.app)

### Screenshots
![IMG_20260113_191604](https://github.com/user-attachments/assets/dc960f6e-7fce-4bd0-ba6d-83c43dee609a)

![IMG_20260113_191551](https://github.com/user-attachments/assets/56fca102-6768-4015-b7e3-3a75cc8fa635)

![IMG_20260113_191527](https://github.com/user-attachments/assets/cd52be06-1a37-4e14-ac77-8f3f773a5220)

![IMG_20260113_191509](https://github.com/user-attachments/assets/2e6d3cf1-ded3-4af8-9986-d1c68fe194dc)

![IMG_20260113_191447](https://github.com/user-attachments/assets/b4f49db0-ff91-4d6d-8c8f-02e64844ab44)

---

## 🌐 Deployment

- **Backend:** Render  
- **Frontend:** Vercel  
- **Live Demo:** `[Add live link here]`

---

## ⚠️ Challenges

- Limited labeled leak data  
- Balancing ML accuracy vs interpretability  
- Full-stack + ML development as a **solo developer**  
- Designing scalable architecture under **hackathon time limits**

---

## 🏅 Accomplishments

- End-to-end **predictive water intelligence system**  
- Professional-grade **dashboard UI**  
- Predictive focus (**prevention, not just analytics**)  
- Solo implementation demonstrating **technical depth + innovation**

---

## 🌱 Future Scope

- Integrate **IoT smart meters**  
- Real-time streaming & anomaly detection  
- Mobile notifications / SMS alerts  
- Campus-level / smart city deployment  
- Advanced predictive models & ML optimization

---

## 📜 License

MIT License © 2026 

---

## 📬 Contact

- **Email:** [ankitkumarforall@gmail.com]  
- **LinkedIn:** [www.linkedin.com/in/ankit-kumar-247259381]  

---
