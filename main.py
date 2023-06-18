import streamlit as st
import numpy as np


name = st.text_input('Enter you name')
st.write(name)
num = st.text_input('Enter a number')
if num:
    st.write(np.exp(int(num)))
    st.write(np.exp(variable))
