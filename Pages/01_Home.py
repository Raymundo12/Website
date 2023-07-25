import pickle
import streamlit as st
import streamlit_authenticator as stauth
from pathlib import Path

st.set_page_config(page_title="01_Home", layout="wide")

st.title ('Welcome to HS Sales HUB')


username = st.text_input('User Name')
password = st.text_input('Password', type='password')

st.button('Login')

