import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Area Sales 2023",
                   page_icon="bar_chart:",
                   layout="wide")

df = pd.read_excel("dfstoreTotal.xlsx")

##---------------Sidebar------------------

st.sidebar.header('Welcome to the Sales Report by Area:')


Week = st.sidebar.selectbox(
    "Select the Week:",
    options=df["Week"].unique())

Area = st.sidebar.selectbox(
 "Select the Area:",
  options=df["AREA"].unique(),)


##Store = st.sidebar.multiselect(
  ##"Select the Store:", 
  ##options=df["Stores"])

st.markdown("##")

##Week1 = st.sidebar._selectbox(
  ##"Select the Store:",
    ##options=df1["Week"].unique())

df_selection = df.query("Week == @Week & AREA == @Area")
##df_selection1 = df2.query("Week == @Week1")

st.title(":bar_chart: Sales Report by Area 2023")
st.markdown("##")

total_sales = int(df_selection["Sales Report"].sum())
total_units = int(df_selection["LY"].sum())


left_column,right_column = st.columns(2)

with left_column:
 st.subheader("Total Sales:")
 st.subheader(f"EU € {total_sales:,}")   

with right_column :
 st.subheader("Last Year Sales 2022:")
 st.subheader(f"EU € {total_units:,}")   

st.markdown("---")

dfchart = px.bar(df_selection,
                 x = "Stores", y="Sales Report", text_auto=',',
                 title="<b>Sales by Area</b>", height=600,
                color_discrete_sequence=["#d7aef3"] * len(df_selection),
    template="simple_white",)
dfchart.update_traces(textfont_size=15, textangle=0, textposition="outside", cliponaxis=False)
     

##st.plotly_chart(dfchart)
##st.dataframe(df_selection)
st.write(':loudspeaker: From Week 29 *Area Manager Changed!* :heavy_exclamation_mark:')

st.plotly_chart(dfchart, use_container_width=True)



st.markdown("---")

st.write(':loudspeaker: From Week 29 *Area Manager Changed!* :heavy_exclamation_mark:')
df_selection

st.markdown("---")


##fig_sales = px.bar(df,
  ##x="Sales Report",
   ## y="Stores",
##title="<b>Sales</b>",
  ##   color_discrete_sequence=["#0085B8"],
    ##  template="simple_white",)



##Sales = (
 ##df_selection.groupby(by=["ItemGroup"]).sum()[["SALES"]].sort_values(by="SALES"))

##fig_sales = px.bar(sales_by_Category,
  ##    x="SALES",
    ##  y=sales_by_Category.index,
     ## title="<b>Sales by Category</b>",
     ## color_discrete_sequence=["#0085B8"] *len (sales_by_Category),
      ##template="simple_white",)


##sales_by_SubCategory = (
 ##df_selection.groupby(by=["ItemSubGrp_Id"]).sum()[["SALES"]].sort_values(by="SALES") 
##)

#fig_Subsales = px.bar(sales_by_SubCategory,
 ##     x="SALES",
   ##   y=sales_by_SubCategory.index,
     ## title="<b>Sales by SubCategory</b>",
     ## color_discrete_sequence=["#0095B8"] *len (sales_by_SubCategory),
     ## template="simple_white",)
