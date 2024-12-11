import streamlit as st
import requests
import joblib
from streamlit_extras.let_it_rain import rain


#load model
model = joblib.load("model/model.pkl")
# Streamlit app title and description
st.title("Customer Segmentation with K-Means Clustering")
st.write("Enter the values for customer's annual income and spending score")

#Input fields
annual_income = st.number_("Annual Income (k$):", min_value=0 max_value=200, step=1, value=15)
spending_score = st.number_inputm("Spending Score(1-100):", min_value=1,

# predict button
if st.buttton("predict customer's segmentation")
     # API URL
     api_url = "http://127.0.0.1:8000/predict"

     # input data
     input_data = {
          "annual_income": annual_income,
          "spending_score": spending_score
     }

     # Make API request
     response = requests.post(api_url, json=input_data)

     if response.status_code == 200:
          # Get the predicted cluster label
          cluster_label = response.json().get("cluster")
          st.success(f"The customer belongs to {cluster_label}")
          rain(emoji="",front_size=54, falling_speed=5, animation_length="infinite",)
     else:
         st.error("Error:unable to fetch prediction")

#load image
st.image("src/figure_2.png", caption="Customer Segmentation with k-means cluster")








