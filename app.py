import streamlit as st
from prediction import predict
import numpy as np
import pickle

st.title ('Insurance predictor')
st.write ('Please select age')
a = st.number_input ('select', min_value= 0, max_value= 120)
st.write ('Please select gender: 0 for male and 1 for female')
b = st.number_input ('select', min_value= 0, max_value= 1)
st.write ('Please select bmi')
c = st.number_input ('select', min_value= 0, max_value= 70)
st.write ('Please select children')
d = st.number_input ('select', min_value= 0, max_value= 20)
st.write ('Please select smoking status: 0 for smoker, 1 for non-smoker ')
e = st.number_input ('select', min_value= 0, max_value= 2)

f = [[a, b, c, d, e]]

model = pickle.load(open('model.pkl','rb'))

if st.button ('Predict Insurance'):
    GPA = model.predict (f)
    st.write ('Insurance would be', GPA)
