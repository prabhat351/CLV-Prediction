# 🛍️ Customer Lifetime Value (CLV) Predictor

This project helps businesses predict **Customer Lifetime Value (CLV)** using RFM metrics: **Recency**, **Frequency**, and **Monetary** value. It features a user-friendly **Streamlit dashboard** for uploading customer data, entering RFM values manually, and visualizing predictions.

---

## 📦 Features

- Upload `.csv` files with customer RFM data
- Manually input Recency, Frequency, Monetary values
- Predict CLV using an XGBoost regression model
- Automatically segment customers: High, Medium, Low value
- Visualizations: Histogram of CLV, Top customers, Segment-wise counts
- Download results as CSV

---

## 📊 Dashboard Preview

- 📈 CLV Distribution by Segment
- 🧮 Top 10 Customers by Predicted CLV
- 🟩 Segment Count Overview

---

## 🧪 Sample Input

### Sample CSV Format
```
CustomerID,Recency,Frequency,Monetary
12345,10,8,12000
54321,25,3,4500
...
```

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🚀 Model Training (Optional)

Train the XGBoost model from RFM features:

```python
from xgboost import XGBRegressor
model = XGBRegressor(n_estimators=100)
model.fit(X_train, y_train)
joblib.dump(model, "xgb_model.pkl")
```

---

## 🧾 Files Included

- `app.py` — Main Streamlit dashboard
- `xgb_model.pkl` — Trained CLV prediction model
- `requirements.txt` — Python dependencies
- `rfm_test.csv` — Sample RFM data

---

## 🤝 Contributors

Made with ❤️ by your prabhat 

