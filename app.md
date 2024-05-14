import pandas as pd;
import numpy as np;
import seaborn as sns;
import matplotlib as plt;
from scipy import stats;
import streamlit as st;
import plotly.express as px

vehicles = pd.read_csv("C:\\Users\\Administrator\\Desktop\\pandasapp\\tripleten\\vehicles_us.csv");



# Assuming you have a DataFrame 'vehicles' with columns 'model_year' and 'price'
fig = px.scatter(vehicles, x="model_year", y="price", title="Average Price per Car Model Year")
fig = px.box(vehicles, x="model_year", y="price", title="Average Price per Car Model Year")

# Show the figure in Streamlit
st.plotly_chart(fig)
fig.show()