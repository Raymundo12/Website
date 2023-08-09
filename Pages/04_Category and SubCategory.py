import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv("DFW3.csv")
df1 = pd.read_csv("DFW1.csv")

print(df1)
st.markdown("##")

st.sidebar.header('Please select the the Chart or Table:')

st.sidebar.subheader("Table")

Week = st.sidebar.selectbox(
    "Select the Week:",
    df["Week"].unique())

Store = st.sidebar.multiselect(
 "Select the Store:",
  options=df["Store"].unique(),)

df_selection = df.query("Week == @Week & Store == @Store")

st.sidebar.subheader("Chart")

st.markdown("##")

Week1 = st.sidebar.multiselect(
    "Select the Week:",
    options=df1["Weeks"].unique())

Quarter1 = st.sidebar.selectbox(
    "Select the Quarter",
    options=df1["Quarters"].unique())

Store1 = st.sidebar.selectbox(
 "Select the Store:",
  options=df1["Stores"].unique())

Cat1 = st.sidebar.multiselect(
 "Select the Category:",
  options=df1["Cats"].unique())

df_selection1 = df1.query("Weeks == @Week1 & Quarters == @Quarter1 & Stores == @Store1 & Cats == @Cat1")

st.title(":bar_chart: Sales Report by Category 2023")
st.markdown("##")

##df_selection

st.markdown("---")

total_sales = int(df_selection1["SALES"].sum())
total_units = int(df_selection1["UNIT"].sum())
##Top_5 = str(df_selection.groupby(by=["Store"]).sum()[["Sales Report"]].sort_values(by="Sales Report").head(3))

left_column, middle_column, right_column = st.columns(3)

with left_column:
 st.subheader("Total Sales:")
 st.subheader(f"EU € {total_sales:,}")   

with middle_column:
 st.subheader("Total Units:")
 st.subheader(f"{total_units:}")   

dfchart = px.histogram(df_selection1,
                   x ="Cats", y="SALES", text_auto=',',
               title="<b>Sales by Categori</b>",
  color_discrete_sequence=["#0085B8"] * len(df_selection1),
    template="simple_white",)

dfchart1 = px.histogram(df_selection1,
                   x ="Cats", y="UNIT", text_auto=',',
               title="<b>Total Units by Categori</b>",
  color_discrete_sequence=["#0085B8"] * len(df_selection1),
    template="simple_white",)

left_column, right_column = st.columns(2)
left_column.plotly_chart(dfchart, use_container_width=True)
right_column.plotly_chart(dfchart1, use_container_width=True)


st.markdown("---")


st.markdown("---")