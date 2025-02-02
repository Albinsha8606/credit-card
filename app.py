import streamlit as st
import pandas as pd
import pickle

file_name = "best_random_forest_model.pkl"
with open('best_random_forest_model.pkl', 'rb') as file:
    best_random_forest_model = pickle.load(file)

# Function to make predictions
def predict_fraud(transaction_data):
    # Convert input data to DataFrame
    input_data = pd.DataFrame([transaction_data])
    # Predict using the loaded model
    prediction = best_random_forest_model.predict(input_data)
    return prediction[0]

# Streamlit app
def main():
    st.title('Credit Card Fraud Detection')
    st.write('Enter transaction details to predict fraudulence.')

    # Input fields for transaction details
    transaction_data = {
        'Time': st.number_input('Time', min_value=0),
        'V1': st.number_input('V1', min_value=0.0),
        'V2': st.number_input('V2', min_value=0.0),
        # Add all other features here
        'V28': st.number_input('V28', min_value=0.0),
        'Amount': st.number_input('Amount', min_value=0.0)
    }

    # Button to make prediction
    if st.button('Predict'):
        result = predict_fraud(transaction_data)
        if result == 1:
            st.error('Fraudulent Transaction Detected!')
        else:
            st.success('Transaction is Legitimate.')