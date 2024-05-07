import streamlit as st
from prediction import predict
import numpy as np

st.title ('Insurance predictor')
st.write ('Please select age')
a = st.number_input ('select', min_value= 0, max_value= 120)

if st.button ('Predict GPA'):
    GPA = predict ([[sat]])
    st.write ('GPA would be', GPA)
