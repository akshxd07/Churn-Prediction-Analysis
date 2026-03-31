# Customer Churn Prediction (Telecom Domain)

A machine learning web app that predicts whether a telecom customer is likely to churn.

🔗 **Live Demo:** https://churn-prediction-analysis-9ubgfebdaxhgjgunhimnd5.streamlit.app

## Overview
Built an end-to-end ML pipeline to predict customer churn using demographic 
and usage features. Optimized a Random Forest classifier using GridSearchCV 
achieving 86% accuracy on test data.

## Features
- Real-time churn prediction from customer inputs
- Clean interactive UI built with Streamlit
- Trained model and scaler persisted as .pkl files

## Tech Stack
- Python, Pandas, NumPy, Scikit-learn
- Random Forest Classifier + GridSearchCV
- Streamlit (deployment)

## Model Performance
- Accuracy: 86% on test data

## Input Features
Age, Gender, Tenure, Monthly Charges, and usage-based features

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Author
Akshad Yadav — [LinkedIn](https://linkedin.com/in/akshad-yadav-360724374) | [GitHub](https://github.com/akshxd07)
