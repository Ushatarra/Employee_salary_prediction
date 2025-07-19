import streamlit as st
import joblib
import numpy as np
import os

st.title("Emplyee Salary Prediction App")
st.divider()
st.write("With this app, You can get the salaries of the company employees")
years=st.number_input("Enter the years of company",value=1,step=1,min_value=0)
jobrate=st.number_input("Enter the job rate",value=3.5,step=0.5,min_value=0.0)
x=[years,jobrate]
model_path=os.path.join("employee_salary_prediction/Linearmodel.pkl")
model=joblib.load(model_path)
st.divider()
predict= st.button("Press the button for salary Prediction")
st.divider()
if predict:
    st.balloons()
    x1=np.array([x])
    prediction= model.predict(x1)[0]
    st.write(f" Salary prediction is {prediction:,.2f}")
else:
    "Please  Press the button for app to make the prediction"