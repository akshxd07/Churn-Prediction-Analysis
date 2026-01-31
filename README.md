# Customer Churn Prediction (Telecom Domain)

An end-to-end machine learning project that predicts whether a telecom customer is likely to churn based on demographic, tenure, and billing-related features. The project includes data analysis, model training, and deployment using a Streamlit web application.

---

## Project Overview

Customer churn is a critical business problem in the telecom industry.  
This project helps identify customers at risk of leaving by analyzing historical customer data and applying machine learning techniques.

The application allows real-time churn prediction through a simple web interface.

---

## Objectives

- Analyze customer behavior and churn patterns  
- Perform data cleaning, EDA, and feature scaling  
- Train and optimize machine learning classification models  
- Deploy the trained model using Streamlit  

---

## Dataset Description

The dataset contains telecom customer information such as:

- Age  
- Gender  
- Tenure  
- Monthly Charges  
- Other demographic and usage-related features  

**Target Variable:**  
- Churn (Yes / No)

---

## Tech Stack

**Languages & Libraries**
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  

**Tools & Frameworks**
- Streamlit  
- Jupyter Notebook  
- VS Code  
- Git & GitHub  

---

## Machine Learning Workflow

### 1. Data Preprocessing
- Cleaned and prepared raw data  
- Encoded categorical variables  
- Applied feature scaling using `StandardScaler`  

### 2. Exploratory Data Analysis (EDA)
- Analyzed churn distribution  
- Studied impact of tenure and monthly charges on churn  
- Used visualizations to identify key churn drivers  

### 3. Model Building
- Trained multiple classification models  
- Selected Random Forest as the final model  

### 4. Model Optimization
- Applied GridSearchCV for hyperparameter tuning  
- Achieved **86% accuracy** on test data
  
### 5. Deployment
- Saved trained model and scaler using `.pkl` files  
- Integrated them into a Streamlit web application  
- Enabled real-time predictions based on user input  

---

## Results

- Random Forest achieved **86% accuracy** on unseen test data  
- Tenure and monthly charges were strong indicators of churn  
- Streamlit app provides instant churn predictions  

---

## How to Run the Project Locally

### Clone the Repository
```bash
git clone https://github.com/akshxd07/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction

