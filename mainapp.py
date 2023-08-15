import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="HS Sales HUB 2023",
                   page_icon="bar_chart:",
                   layout="wide")

st.title('Welcome to :green[HS Sales HUB]')

df = pd.read_pickle("dfstoreTotal1.pkl")

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


df_selection = df.query("Week == @Week & Stores == @Store")
df_selection2 = df.query("Week == @Week & Stores == @Store2")

st.title(":bar_chart: Sales Report by Store 2023")
st.markdown("##")

total_sales = int(df_selection["Sales Report"].sum())
total_units = int(df_selection["LY"].sum())
Top_5 = str(df_selection.groupby(by=["Stores"]).sum()[["Sales Report"]].sort_values(by="Sales Report").head(3))

left_column, middle_column, right_column = st.columns(3)

with left_column:
 st.subheader("Total Sales:")
 st.subheader(f"EU € {total_sales:,}")   

with middle_column:
 st.subheader("Last Year Sales 2022:")
 st.subheader(f"EU € {total_units:,}")   

st.markdown("---")

dfchart = px.line(df_selection,
                 x = "Week", y="Sales Report", text="Sales Report", color="STORE PROFILE", markers=True,
                 title="<b>Sales 2023</b>",
  color_discrete_sequence=["#12A6A6"] * len(df_selection),
    template="simple_white",)

dfchart1 = px.line(df_selection2,
                 x = "Week", y="Sales Report2", text= "Sales Report2", color="STORE PROFILE", markers=True,
                 title="<b>Sales</b>",
  color_discrete_sequence=["#fa6e0a"] * len(df_selection),
    template="simple_white",)

left_column, right_column = st.columns(2)
left_column.plotly_chart(dfchart, use_container_width=True)
right_column.plotly_chart(dfchart1, use_container_width=True)

##st.plotly_chart(dfchart)
##st.dataframe(df_selection)

st.markdown("---")

st.write(':loudspeaker: From Week 29 *Area Manager Changed!* :heavy_exclamation_mark:')

df_selection
df_selection2

st.markdown("---")

