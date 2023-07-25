import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_excel("SalesSuppier.xlsx")


st.markdown("##")

st.sidebar.header('Please select the the Chart or Table:')

st.sidebar.subheader("Table")

Week = st.sidebar.multiselect(
    "Select the Week:",
    options=df["Week"].unique())


Supplier = st.sidebar.selectbox(
 "Select the Store:",
  options=df["Supplier"].unique(),)

df_selection = df.query("Week == @Week & Supplier == @Supplier")

st.sidebar.subheader("Chart")

st.markdown("##")

st.title(":bar_chart: Sales Report by Category 2023")
st.markdown("##")

df_selection

st.markdown("---")


total_sales = int(df_selection["Total SALES €"].sum())
total_units = int(df_selection["Total Units"].sum())
##Top_5 = str(df_selection.groupby(by=["Store"]).sum()[["Sales Report"]].sort_values(by="Sales Report").head(3))

left_column, middle_column, right_column = st.columns(3)

with left_column:
 st.subheader("Total Sales:")
 st.subheader(f"EU € {total_sales:,}")   

with middle_column:
 st.subheader("Total Units:")
 st.subheader(f"EU € {total_units:,}")   

dfchart = px.line(df_selection,
                   x ="Week", y="Total SALES €",
               title="<b>Sales by Supplier</b>",
  color_discrete_sequence=["#0085B8"] * len(df_selection),
    template="simple_white",)

dfchart1 = px.histogram(df_selection,
                   x ="Supplier", y="Total Units", text_auto=',',
               title="<b>Total Units by Supplier</b>",
  color_discrete_sequence=["#0085B8"] * len(df_selection),
    template="simple_white",)

left_column, right_column = st.columns(2)
left_column.plotly_chart(dfchart, use_container_width=True)
right_column.plotly_chart(dfchart1, use_container_width=True)


st.markdown("---")


st.markdown("---")