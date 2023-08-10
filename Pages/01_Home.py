import json
import pickle
import streamlit as st
import streamlit_authenticator as stauth
from pathlib import Path
from streamlit_option_menu import option_menu
from streamlit.source_util import _on_pages_changed, get_pages

DEFAULT_PAGE ="01_Home.py"

##def get_all_pages():
    

st.set_page_config(page_title="01_Home", layout="wide")