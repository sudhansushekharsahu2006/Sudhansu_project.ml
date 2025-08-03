from typing import Any

import streamlit as st
import numpy as  np
import pickle

from numpy import ndarray, dtype

model=pickle.load(open('model.pkl',"rb"))

st.title("Calories Burnt Prediction")
st.write("Enter your details to predict calories burnt")

gender = st.selectbox("Gender",["Male","Female"])
age= st.number_input("Age",min_value=10,max_value=100,step=1)
height= st.number_input("Height(cm)",min_value=100,max_value=250,step=1)
weight = st.number_input("Weight(kg)",min_value=20,max_value=200,step=1)
duration= st.number_input("Exercise Duration(minutes)",min_value=1,max_value=500,step=1)
heart_rate= st.number_input("average Heart Rate(bpm)",min_value=1,max_value=250,step=1)
body_temp= st.number_input("Body Temperature(c)",min_value=30.0,max_value=45.0,step=0.1)


gender_encode = 1 if gender=="Male" else 0

if st.button("Predict Calories Burnt"):
   rf= np.array([[gender_encode,age,height,weight,duration,heart_rate,body_temp]])
prediction =model.predict(rf)
st.success(f"Estimated Calories Burnt: {prediction[0]:.2f} kcal")
