import streamlit as st



email=st.text_input('Email Address')
password=st.text_input('Password', type='password')

st.button('Login')