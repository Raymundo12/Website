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

with st.sidebar:
    selected = option_menu("Sales Menu", ["Home", 'Store Sales', 'Area Sales', 'Category Sales', 'Sales by Supplier'],
    icons=['house-fill', 'shop','globe-europe-africa', 'diagram-3', 'cart3'], menu_icon="bar-chart-line-fill", default_index=1,

    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    })

st.title ('Welcome to HS Sales HUB')

# 4. Manual Item Selection
if st.session_state.get('switch_button', False):
    st.session_state['menu_option'] = (st.session_state.get('menu_option',0) + 1) % 4
    manual_select = st.session_state['menu_option']
else:
    manual_select = None
    
selected4 = option_menu(None, ["Home", 'Store Sales', 'Area Sales', 'Category Sales', 'Sales by Supplier'], 
    icons=['house-fill', 'shop','globe-europe-africa', 'diagram-3', 'cart3'], 
    orientation="horizontal", manual_select=manual_select, key='menu_4')
st.button(f"Move to Next {st.session_state.get('menu_option',1)}", key='switch_button')
selected4

# 5. Add on_change callback
def on_change(key):
    selection = st.session_state[key]
    st.write(f"Selection changed to {selection}")
    
selected5 = option_menu(None, ["Home", 'Store Sales', 'Area Sales', 'Category Sales', 'Sales by Supplier'],
                        icons=['house-fill', 'shop','globe-europe-africa', 'diagram-3', 'cart3'],
                        on_change=on_change, key='menu_5', orientation="horizontal")
selected5