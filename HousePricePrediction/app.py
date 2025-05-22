import streamlit as st
import pickle
import numpy as np

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit UI
st.set_page_config(page_title="House Price Predictor", page_icon="🏡")
st.title("🏡 House Price Prediction App")
st.markdown("""
Welcome to the **House Price Predictor**!  
Enter the property details below to estimate the **market price**.
""")

# Form layout for inputs
with st.form("prediction_form"):
    st.subheader("📝 Enter Property Details")

    col1, col2 = st.columns(2)

    with col1:
        area = st.number_input("📏 Area (sq ft)", 500, 10000, step=100, value=1500)
        bedrooms = st.slider("🛏️ Bedrooms", 1, 10, value=3)
        bathrooms = st.slider("🛁 Bathrooms", 1, 10, value=2)

    with col2:
        stories = st.slider("🏢 Stories", 1, 4, value=2)
        parking = st.slider("🚗 Parking Spaces", 0, 4, value=1)

    submit = st.form_submit_button("🔍 Predict Price")

# Prediction
if submit:
    features = np.array([[area, bedrooms, bathrooms, stories, parking]])
    prediction = model.predict(features)

    st.markdown("---")
    st.success(f"💰 **Estimated House Price:** ₹{prediction[0]:,.2f}")
    st.balloons()
