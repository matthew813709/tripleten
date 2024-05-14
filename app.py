import pandas as pd;
import plotly_express as px;
import numpy as np;
import seaborn as sns;
import matplotlib as plt;
from scipy import stats;
import streamlit as sl;


vehicles = pd.read_csv("vehicles_us.csv");

fig = px.bar(vehicles, x="model_year", y="price", title='Average Price per Car Model Year');
fig.show();
