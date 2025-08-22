# 🏦 Bank Customer Churn Prediction

## 📑 Table of Contents
- [🚀 Introduction](#-introduction)
- [✨ Features](#-features)
- [📊 Dataset](#-dataset)
- [⚙️ Installation](#️-installation)
- [▶️ Usage](#️-usage)

---

## 🚀 Introduction
This project presents an interactive web application built with **Streamlit** to predict customer churn in a banking context. By leveraging several pre-trained machine learning models, the application helps banks identify customers at risk of leaving, enabling proactive retention strategies. The app offers a user-friendly interface to test predictions in real-time by inputting various customer details.

---

## ✨ Features
- **Interactive UI:** A clean and intuitive user interface powered by Streamlit.
- **Multiple Models:** Predict churn using a choice of three machine learning models:
    - Logistic Regression
    - Random Forest Classifier
    - XGBoost Classifier
- **Real-time Prediction:** Get an instant churn prediction result based on the entered customer data.
- **Model Comparison:** Easily switch between different models to compare their predictions for the same set of inputs.

---

## 📊 Dataset
The models are trained on the **Bank Churn Modeling dataset**, a popular dataset for churn prediction tasks.

**Key Features:**
- **CreditScore:** Customer’s credit rating.
- **Age:** Age of the customer.
- **Tenure:** Number of years the customer has been with the bank.
- **Balance:** Account balance.
- **NumOfProducts:** Number of bank products the customer uses.
- **HasCrCard:** Indicates if the customer has a credit card (`1` for yes, `0` for no).
- **IsActiveMember:** Indicates if the customer is an active user of bank services (`1` for yes, `0` for no).
- **EstimatedSalary:** Approximate annual salary.
- **Geography:** Customer’s country of residence (France, Spain, Germany).
- **Gender:** Male or Female.

**Target Variable:**
- **Exited:** The target variable, where `1` signifies the customer has churned and `0` signifies they have not.

---

## ⚙️ Installation
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/bank-churn-prediction.git](https://github.com/your-username/bank-churn-prediction.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd bank-churn-prediction
    ```

3.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

4.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: Ensure you have a `requirements.txt` file containing `streamlit`, `scikit-learn`, `pandas`, and `xgboost`.)*

---

## ▶️ Usage
1.  **Ensure all necessary files are in the project directory.** This includes the main script (`app.py`), and the pre-trained model files (`scaler.pkl`, `logistic_regression.pkl`, `random_forest.pkl`, `xgboost.pkl`).

2.  **Run the Streamlit application from your terminal:**
    ```bash
    streamlit run app.py
    ```

3.  **Interact with the app:**
    - The application will open in your default web browser.
    - Select a machine learning model from the dropdown menu.
    - Enter the customer's details using the interactive input fields.
    - Click the **🔮 Predict Churn** button to see the prediction result.
