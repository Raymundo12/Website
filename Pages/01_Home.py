import pickle
import streamlit as st
import streamlit_authenticator as stauth
from pathlib import Path

st.set_page_config(page_title="01_Home", layout="wide")

st.title ('Welcome to HS Sales HUB')

names = ['John Smith','Rebecca Briggs']
usernames = ['jsmith','rbriggs']
passwords = ['123','456']

hashed_passwords = stauth.Hasher(passwords).generate()


authenticator = stauth.authenticate(names,usernames,hashed_passwords, 
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)

name, authentication_status = authenticator.login('Login','main')

