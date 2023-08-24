import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="HS Sales HUB 2023",
                   page_icon="bar_chart:",
                   layout="wide")

st.title('Welcome to :green[HS Sales HUB]')

df = pd.read_parquet("dfstoreTotal1")
df1 = pd.read_parquet("DFW1")
df20 = pd.read_pickle("SalesSuppier.pkl")

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


st.sidebar.header('Sales Report by Area:')


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
                color_discrete_sequence=["#fa6e0a"] * len(df_selection),
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

st.markdown("##")

st.sidebar.header(' Sales by Category:')

st.sidebar.subheader("Table")

Quarters = st.sidebar.multiselect(
    "Select the Quarter:",
    df1["Quarter"].unique())
if not Quarters:
 df3 = df1.copy()
else:
 df3 = df1[df1["Quarter"].isin(Quarters)] 


Weeek = st.sidebar.multiselect(
    "Select the Week:",
    df3["Week"].unique())
if not Weeek:
 df4 = df3.copy()
else:
 df4 = df3[df3["Week"].isin(Weeek)]

AStore = st.sidebar.multiselect(
 "Select the Store:",
  options=df4["Stores"].unique())

df_selection = df1.query("Quarter == @Quarters & Week == @Weeek & Stores == @AStore")

st.sidebar.subheader("Chart")

st.markdown("##")

Quarter1 = st.sidebar.multiselect(
    "Select the Quarter",
    options=df1["Quarter"].unique())
if not Quarter1:
 df5 = df1.copy()
else:
 df5 = df1[df1["Quarter"].isin(Quarter1)] 

Week1 = st.sidebar.multiselect(
    "Select the Week:",
    options=df5["Week"].unique())
if not Week1:
 df6 = df5.copy()
else:
 df5 = df1[df1["Week"].isin(Week1)]

Store1 = st.sidebar.selectbox(
 "Select the Store:",
  options=df5["Stores"].unique())

Cat1 = st.sidebar.selectbox(
 "Select the Category:",
  options=df5["CATEGORY"].unique())

df_selection1 = df1.query("Quarter == @Quarter1 & Week == @Week1 & Stores == @Store1 & CATEGORY == @Cat1")

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
                   x ="CATEGORY", y="SALES", text_auto=',',
               title="<b>Sales by Category</b>",
  color_discrete_sequence=["#12A6A6"] * len(df_selection1),
    template="simple_white")

dfchart1 = px.histogram(df_selection1,
                   x ="SUB  - CATEGORY", y="SALES", text_auto=',',
               title="<b>Total Sales SubCategory</b>", height=600,
  color_discrete_sequence=["#fa6e0a"] * len(df_selection1),
    template="simple_white",)
dfchart1.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

left_column, right_column = st.columns(2)

st.plotly_chart(dfchart1, use_container_width=True)


st.markdown("---")


st.markdown("---")

st.markdown("##")

st.sidebar.header('Sales by Supplier:')

st.sidebar.subheader("Table")

Week = st.sidebar.multiselect(
    "Select the Week:",
    options=df20["Week"].unique())


Supplier = st.sidebar.multiselect(
 "Select the Store:",
  options=df20["Supplier"].unique(),)

df_selection20 = df20.query("Week == @Week & Supplier == @Supplier")

st.sidebar.subheader("Chart")

st.markdown("##")

st.title(":bar_chart: Sales Report by Supplier 2023")
st.markdown("##")

df_selection20

st.markdown("---")


total_sales = int(df_selection20["Total SALES €"].sum())
total_units = int(df_selection20["Total Units"].sum())
##Top_5 = str(df_selection20.groupby(by=["Supplier"]).sum()[["Total SALES €"]].sort_values(by="Total SALES €").head(3))

left_column, middle_column, right_column = st.columns(3)

with left_column:
 st.subheader("Total Sales:")
 st.subheader(f"EU € {total_sales:,}")   

with middle_column:
 st.subheader("Total Units:")
 st.subheader(f" {total_units:,}")   


dfchart = px.line(df_selection20,
                   x ="Week", y="Total SALES €", text="Total SALES €",
               title="<b>Sales by Supplier</b>",
  color_discrete_sequence=["#0085B8"] * len(df_selection20),
    template="simple_white",)

dfchart1 = px.histogram(df_selection20,
                   x ="Supplier", y="Total Units", text_auto=',',
               title="<b>Total Units by Supplier</b>",
  color_discrete_sequence=["#0085B8"] * len(df_selection20),
    template="simple_white",)

left_column, right_column = st.columns(2)
left_column.plotly_chart(dfchart, use_container_width=True)
right_column.plotly_chart(dfchart1, use_container_width=True)


st.markdown("---")


st.markdown("---")