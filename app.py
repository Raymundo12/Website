import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="HS Sales HUB 2023",
                   page_icon="bar_chart:",
                   layout="wide")

st.title('Welcome to :green[HS Sales HUB]')

