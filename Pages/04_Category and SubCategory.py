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

Quarters = st.sidebar.multiselect(
    "Select the Quarter:",
    df["Quarter"].unique())
if not Quarters:
 df3 = df.copy()
else:
 df3 = df[df["Quarter"].isin(Quarters)] 


Weeek = st.sidebar.multiselect(
    "Select the Week:",
    df3["Week"].unique())
if not Weeek:
 df4 = df3.copy()
else:
 df4 = df3[df3["Week"].isin(Weeek)]

AStore = st.sidebar.multiselect(
 "Select the Store:",
  options=df4["Store"].unique())

df_selection = df.query("Quarter == @Quarters & Week == @Weeek & Store == @AStore")

st.sidebar.subheader("Chart")

st.markdown("##")

Quarter1 = st.sidebar.multiselect(
    "Select the Quarter",
    options=df1["Quarters"].unique())
if not Quarter1:
 df5 = df1.copy()
else:
 df5 = df1[df1["Quarters"].isin(Quarter1)] 

Week1 = st.sidebar.multiselect(
    "Select the Week:",
    options=df5["Weeks"].unique())
if not Week1:
 df6 = df5.copy()
else:
 df5 = df1[df1["Weeks"].isin(Week1)]

Store1 = st.sidebar.selectbox(
 "Select the Store:",
  options=df5["Stores"].unique())

Cat1 = st.sidebar.selectbox(
 "Select the Category:",
  options=df5["Cats"].unique())

df_selection1 = df1.query("Quarters == @Quarter1 & Weeks == @Week1 & Stores == @Store1 & Cats == @Cat1")

st.title(":bar_chart: Sales Report by Category 2023")
st.markdown("##")

df_selection

st.markdown("---")

total_sales = int(df_selection1["SALES"].sum())
total_units = int(df_selection1["UNIT"].sum())
##Top_5 = str(df_selection.groupby(by=["Store"]).sum()[["Sales Report"]].sort_values(by="Sales Report").head(3))

left_column, middle_column, right_column = st.columns(3)

with left_column:
 st.subheader("Total Sales by Selected Category:")
 st.subheader(f"EU € {total_sales:,}")   

with right_column:
 st.subheader("Total Units by Selected Category:")
 st.subheader(f"{total_units:}")   

dfchart = px.histogram(df_selection1,
                   x ="Cats", y="SALES", text_auto=',',
               title="<b>Sales by Category</b>",
  color_discrete_sequence=["#0085B8"] * len(df_selection1),
    template="simple_white")

dfchart1 = px.histogram(df_selection1,
                   x ="Sub", y="SALES", text_auto=',',
               title="<b>Total Sales SubCategory</b>", height=600,
  color_discrete_sequence=["#0085B8"] * len(df_selection1),
    template="simple_white",)
dfchart1.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

left_column, right_column = st.columns(2)

st.plotly_chart(dfchart1, use_container_width=True)


st.markdown("---")


st.markdown("---")