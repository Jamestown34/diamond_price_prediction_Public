# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vF1393MeVrIS2zRzT1id-lF9o-zcj-u5
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import joblib
# import numpy as np
# import gdown
# 
# # Download the model from Google Drive
# url = "https://drive.google.com/uc?id=16lIbjrtVSASFI2BinknETEiH-mEOcKMz"
# output = "model.pkl"
# gdown.download(url, output, quiet=False)
# 
# # Load the trained model
# model = joblib.load(output)
# 
# # Streamlit UI
# st.title("💎 Diamond Price Prediction App")
# st.write("Enter the diamond attributes to get the predicted price.")
# 
# # Input fields
# x_premium = st.number_input("X (Premium)", min_value=0.0, step=0.01)
# y_good = st.number_input("Y (Good)", min_value=0.0, step=0.01)
# volume = st.number_input("Volume", min_value=0.0, step=0.01)
# carat = st.number_input("Carat", min_value=0.0, step=0.01)
# price_per_carat = st.number_input("Price per Carat", min_value=0.0, step=0.01)
# depth_ratio = st.number_input("Depth Ratio", min_value=0.0, step=0.01)
# 
# # Prediction button
# if st.button("Predict Price"):
#     input_data = np.array([[x_premium, y_good, volume, carat, price_per_carat, depth_ratio]])
#     predicted_price = model.predict(input_data)[0]
# 
#     st.success(f"💰 Predicted Diamond Price: ${predicted_price:.2f}")

