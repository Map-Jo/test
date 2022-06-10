import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px



st.write('Do you need recommend?')

url = pd.read_csv("https://raw.githubusercontent.com/Map-Jo/test/main/%EC%9D%B8%EA%B5%AC_%EC%A0%90%ED%8F%AC_%EA%B0%9C%ED%8F%90%EC%97%85_%ED%86%B5%ED%95%A9_2021%20(2).csv")


@st.cache
def load_data(nrows):
      data = pd.read_csv(url, nrows=nrows)
      lowercase = lambda x: str(x).lower()
      data.rename(lowercase, axis='columns', inplace=True)
      data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
      return data
