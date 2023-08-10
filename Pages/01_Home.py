import streamlit as st

def app():

st.title('Welcome to HS Sales HUB')

email=st.text_input('Email Address')
password=st.text_input('Password', type='password')

st.button('Login')