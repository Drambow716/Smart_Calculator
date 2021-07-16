import streamlit as st
import sympy as sp
import time

st.header("Weclome to the best math derivative in the market")
st.text("This application was backed by Elon Musk him self :) ")


expr = st.text_input("Please input your formula", "((x**2)/2)-5*x+1")

x = sp.symbols("x")

try:
    Answer = sp.diff(expr)
    my_bar = st.progress(0)

    for something in range(100):
        time.sleep(0.1)
        my_bar += st.progress(0)
    st.text(Answer)
except:
    pass


