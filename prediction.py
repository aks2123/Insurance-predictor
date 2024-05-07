import streamlit as st
import pickle
import numpy as np

with open ('model.pkl', 'rb') as f:

    model = pickle.load (f)

def predict (data):
    return model.predict (data)
