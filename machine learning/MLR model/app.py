import streamlit as st
import pickle
import pandas as pd


model = pickle.load(open("C:\Users\fouza\OneDrive\Desktop\Data science nit\6th july - mlr\Housing prediction\model.pkl", "rb"))

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("House Price Prediction")

st.write("### Enter the house details to predict the price")


# user input
area = st.number_input('Area (Square feet)',min_value = 100, max_value = 10000, value = 1000 )
bedrooms = st.number_input('Number of Bedrooms', min_value = 1, max_value= 10, value=2)
bathrooms = st.number_input('Number of Bathrooms', min_value = 1, max_value=10, value=2)

prediction = model.predict(input_data)
st.success(f'Predict House price: ₹ {prediction[0]:, .2f}')