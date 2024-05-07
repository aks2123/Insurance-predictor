import streamlit as st
import pickle
import numpy as np

def predict (data):
  with open ('model.pkl', 'rb') as f:

    model = pickle.load (f)
    return model.predict (data)
