import streamlit as st

def intro():
    import streamlit as st

st.title('Welcome to :green[HS Sales HUB]')

email=st.text_input('Email Address')
password=st.text_input('Password', type='password')


st.button('Login')