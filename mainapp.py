import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import openpyxl

st.set_page_config(page_title="HS Sales HUB 2023",
                   page_icon="bar_chart:",
                   layout="wide")

st.title('Welcome to :green[HS Sales HUB]')

df = pd.read_excel("dfstoreTotal.xlsx")

st.markdown("##")

st.sidebar.header('Please select the Week:')

Week = st.sidebar.multiselect(
    "Select the Week:",
    options=df["Week"].unique())

Store = st.sidebar.selectbox(
 "Select the Store:",
  options=df["Stores"].unique())

Store2 = st.sidebar.selectbox(
 "Select the Store to Compare:",
  options=df["Stores"].unique())

st.markdown("##")