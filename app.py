import streamlit as st
import pickle
import pandas as pd

# Load model
with open('model/linear_sale.pkl', 'rb') as f : 
    model = pickle.load(f)

st.title('App test deploy')
st.write('Nhập giá và chi phí quảng cáo')

price = st.number_input("Price", min_value=0.0, step=0.1)
ads_cost = st.number_input("Ads Cost", min_value=0.0, step=0.1)

if st.button("Predict"):
    input_data = pd.DataFrame({
        "Price": [price],
        "Ads_Cost": [ads_cost]
    })

    prediction = model.predict(input_data)
    st.success(f"Predicted Sales Volume: {prediction[0][0]:.2f}")
