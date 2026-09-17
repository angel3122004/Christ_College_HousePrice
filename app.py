import streamlit as st
import joblib

model=joblib.load("MultiLinear_Regression_HousePrice_Model.pkl")
st.title("House Price Prediction")
area=st.number_input("Enter Area:", min_value=300.0 ,max_value=10000.0, value=600.0)
bedrooms=st.number_input("Enter no of bedrooms:", min_value=1 ,max_value=10, value=1)
floors=st.number_input("Enter no of floors:", min_value=0 ,max_value=10, value=0)

if st.button("Predict"):
  prediction=model.predict([[area,bedrooms,floors]])
  st.success(f"Predicted price: {prediction[0]:.2f} Lakhs")
