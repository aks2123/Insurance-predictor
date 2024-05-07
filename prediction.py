import streamlit as st
import joblib
import numpy as np

def predict (data):
    lr = joblib.load ('model(1).sav')
    return lr.predict (data)
