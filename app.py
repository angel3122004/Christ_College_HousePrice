import streamlit as st
import joblib
model = joblib.load("MultiLinear_Regression_HousePrice_Model.pkl")
st.title("House Price Prediction")

area = st.number_input("Enter Area:", value=600.0)
bedrooms = st.number_input("Enter no of bedrooms:", value=1)
floors = st.number_input("Enter no of floors:", value=0)

if st.button("Predict"):
    if area < 600 or area > 5000:
        st.error("Area must be within 600-5000") 
        st.stop() 
    elif bedrooms <= 0:
        st.error("Bedrooms cannot be 0")
        st.stop()
    elif bedrooms > 10:
        st.error("Number of Bedrooms must be less than or equal to 10")
        st.stop()
    elif floors < 0 or floors > 10:
        st.error("Number of floors must be between 0 and 10")
        st.stop()
    prediction = model.predict([[area, bedrooms, floors]])
    st.success(f"Predicted price: {prediction[0]:.2f} Lakhs")
