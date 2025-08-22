import streamlit as st
import numpy as np
import joblib

# Load scaler
scaler = joblib.load("scaler.pkl")

# Load all models
models = {
    "Logistic Regression": joblib.load("logistic_regression.pkl"),
    "Random Forest": joblib.load("random_forest.pkl"),
    "XGBoost": joblib.load("xgboost.pkl")
}

# Streamlit UI
st.title('🏦 Customer Churn Prediction')
st.write("Predict whether a bank customer will churn (Exit) or not")

# Model selection
selected_model_name = st.selectbox("Choose a model", list(models.keys()))
model = models[selected_model_name]

# Input fields
credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
age = st.number_input("Age", min_value=18, max_value=100, value=35)
tenure = st.number_input("Tenure (Years with Bank)", min_value=0, max_value=20, value=5)
balance = st.number_input("Account Balance", min_value=0.0, max_value=250000.0, value=50000.0, step=1000.0)
num_products = st.slider("Number of Products", 1, 4, 1)
has_cr_card = st.selectbox("Has Credit Card?", ["Yes", "No"])
is_active = st.selectbox("Is Active Member?", ["Yes", "No"])
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, max_value=200000.0, value=50000.0, step=1000.0)
gender = st.selectbox("Gender", ["Male", "Female"])
geography = st.selectbox("Geography", ["France", "Spain", "Germany"])

# Encode categorical variables
has_cr_card = 1 if has_cr_card == 'Yes' else 0
is_active = 1 if is_active == 'Yes' else 0
gender = 1 if gender == "Male" else 0  # Male=1, Female=0
geo_map = {"France": [1, 0], "Spain": [0, 1], "Germany": [0, 0]}
geography_encoded = geo_map[geography]

# Prepare feature vector
features = np.array([[credit_score, age, tenure, balance, num_products,
                      has_cr_card, is_active, estimated_salary, gender] + geography_encoded])

# Scale features
features = scaler.transform(features)

# Prediction button
if st.button("🔮 Predict Churn"):
    pred = model.predict(features)[0]
    if pred == 1:
        st.error(f"⚠️ This customer is likely to CHURN! (Model: {selected_model_name})")
    else:
        st.success(f"✅ This customer is NOT likely to churn. (Model: {selected_model_name})")
