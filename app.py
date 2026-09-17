import streamlit as st
import joblib

model=joblib.load("MultiLinear_Regression_HousePrice_Model.pkl")
st.title("House Price Prediction")
area=st.number_input("Enter Area:", min_value=600.0 ,max_value=5000.0, value=600.0)
bedrooms=st.number_input("Enter no of bedrooms:", min_value=1 ,max_value=10, value=1)
floors=st.number_input("Enter no of floors:", min_value=0 ,max_value=10, value=0)

if st.button("Predict"):
  if area<600.0 or area>3000.0:
    st. error("area must be within 600-5000") 
  elif bedrooms < 1 or bedrooms > 10:
        st.error("Number of bedrooms must be between 1 and 10.")
  elif floors < 0 or floors > 10:
        st.error("Number of floors must be less than 10.")
  prediction=model.predict([[area,bedrooms,floors]])
  st.success(f"Predicted price: {prediction[0]:.2f} Lakhs")
