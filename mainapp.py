import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="HS Sales HUB 2023",
                   page_icon="bar_chart:",
                   layout="wide")

st.title('Welcome to :green[HS Sales HUB]')

df = pd.read_parquet("dfstoreTotal1")
df1 = pd.read_parquet("data_for_site")
df20 = pd.read_pickle("SalesSuppier.pkl")

st.markdown("##")

st.sidebar.header('Please select the Week:')
