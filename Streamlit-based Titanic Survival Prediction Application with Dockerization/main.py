import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model
model = joblib.load('titanic_model.pkl')

# Set page config for a clean layout
st.set_page_config(page_title="Titanic Survival Prediction", layout="wide")

# Streamlit UI with Enhanced CSS
st.markdown(
    """
    <style>
    /* Global Styles */
    body {
        background-color: #f7fafc;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        margin: 0;
        padding: 0;
    }
    .title {
        color: #4a90e2; /* Lightened title color */
        font-size: 48px;
        font-weight: 600;
        text-align: center;
        margin-top: 50px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .subtitle {
        color: #4a5568;
        font-size: 20px;
        text-align: center;
        margin-bottom: 30px;
        font-style: italic;
    }
    .form-container {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 35px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        margin-top: 50px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }

    /* Form Inputs Styling */
    .stSlider, .stNumberInput, .stSelectbox {
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
        border: 1px solid #4a5568; /* Darkened borders */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .stSlider > div, .stNumberInput, .stSelectbox {
        margin-bottom: 25px;
    }

    /* Buttons Styling */
    .stButton > button {
        background-color: #3182ce;
        color: white;
        padding: 14px 24px;
        font-size: 18px; /* Increased font size for button */
        font-weight: 600;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.3s;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #2b6cb0;
        transform: scale(1.05);
    }

    /* Success/Error Messages */
    .stSuccess {
        color: #38a169;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .stError {
        color: #e53e3e;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }

    /* Footer */
    .footer {
        font-size: 16px;
        color: #6b7280;
        text-align: center;
        margin-top: 50px;
        padding: 10px;
    }

    </style>
    """, unsafe_allow_html=True)

# Title and subtitle
st.markdown('<div class="title">Titanic Survival Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter the passenger details below to predict survival chances.</div>', unsafe_allow_html=True)

# Input fields organized using columns for better alignment
col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox("Passenger Class (Pclass)", [1, 2, 3])
    sex = st.selectbox("Sex", ['male', 'female'])
    age = st.slider("Age", 0, 80, 25)

with col2:
    sibsp = st.number_input("Number of Siblings/Spouses Aboard (SibSp)", 0, 10, 0)
    parch = st.number_input("Number of Parents/Children Aboard (Parch)", 0, 10, 0)
    fare = st.slider("Fare", 0, 500, 20)


# Container for prediction button and result
with st.container():
    # Predict button with a sleek, interactive design
    if st.button("Predict", key="predict_button"):
        with st.spinner("Making prediction..."):
            # Convert inputs to model-ready format
            sex = 1 if sex == 'female' else 0
            inputs = pd.DataFrame([[pclass, sex, age, sibsp, parch, fare]], 
                                  columns=['Pclass', 'Sex', 'Age', 'Siblings/Spouses Aboard', 'Parents/Children Aboard', 'Fare'])

            # Prediction
            prediction = model.predict(inputs)
            result = "Survived" if prediction[0] == 1 else "Did not survive"

            # Display result with a dynamic, clean design
            if result == "Survived":
                st.markdown(f"<div class='stSuccess'>{result}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='stError'>{result}</div>", unsafe_allow_html=True)

 


