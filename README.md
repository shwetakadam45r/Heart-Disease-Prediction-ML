# ❤️ Heart Disease Prediction

A Machine Learning project that predicts whether a person is likely to have **heart disease** based on medical and health-related features.

## 📌 Project Overview

This project uses Machine Learning to analyze patient information and predict the presence of heart disease.

The project includes:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Feature scaling
* Machine Learning model training
* Model evaluation
* Prediction using a Streamlit web application

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data processing
* **NumPy** – Numerical operations
* **Matplotlib / Seaborn** – Data visualization
* **Scikit-learn** – Machine Learning
* **Joblib** – Saving trained models
* **Streamlit** – Web application

## 🤖 Machine Learning Model

The project uses **Logistic Regression** for heart disease prediction.

The trained model and preprocessing objects are saved using Joblib:

```text
LogisticRegression_heart.pkl
scaler.pkl
columns.pkl
```

## 📊 Features

The model uses patient-related features such as:

* Age
* Sex
* Chest pain type
* Resting blood pressure
* Cholesterol
* Fasting blood sugar
* Resting ECG
* Maximum heart rate
* Exercise-induced angina
* ST depression
* Slope
* Number of major vessels
* Thalassemia

## 📁 Project Structure

```text
Heart-Disease-Prediction/
│
├── app.py
├── LogisticRegression_heart.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
├── README.md
│
└── dataset/
    └── heart.csv
```

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/shwetakadam45r/Heart-Disease-Prediction.git
```

### 2. Navigate to the project folder

```bash
cd Heart-Disease-Prediction
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🖥️ Application

The Streamlit application allows users to enter patient information and receive a prediction from the trained Machine Learning model.

### Prediction Output

The application predicts whether the patient is:

* **Likely to have heart disease**
* **Less likely to have heart disease**

## 📈 Machine Learning Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Logistic Regression
   ↓
Model Evaluation
   ↓
Save Model
   ↓
Streamlit Web Application
   ↓
Heart Disease Prediction
```

## 🎯 Objective

The main objective of this project is to demonstrate how Machine Learning can be used to build a simple predictive healthcare application.

> **Disclaimer:** This project is intended for educational purposes only and should not be used as a substitute for professional medical diagnosis or advice.

## 👩‍💻 Author

**Shweta Kadam**

GitHub: `https://github.com/shwetakadam45r`
