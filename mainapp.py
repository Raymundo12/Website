import streamlit as st
import pandas as pd

st.set_page_config(page_title="HS Sales HUB 2023",
                   page_icon="bar_chart:",
                   layout="wide")

st.title('Welcome to :green[HS Sales HUB]')

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