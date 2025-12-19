import joblib
import streamlit as st


# Load the pre-trained model
model = joblib.load('weather_model.pkl')
st.title("Weather Predictor")
st.write("Enter the weather parameters to predict the weather condition.")
# Input fields for weather parameters
temperature = st.number_input("Hours of sunlight:")
humidity = st.number_input("Humidity (%)")
# Predict button
if st.button("Predict Weather"):
    input_data = [[temperature, humidity]]
    prediction = model.predict(input_data)
    st.write(f"The predicted weather condition is: {prediction[0]}")
    
