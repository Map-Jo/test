import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px



st.write('Do you need recommend?')

df = pd.read_csv("https://raw.githubusercontent.com/Map-Jo/test/main/%EC%9D%B8%EA%B5%AC_%EC%A0%90%ED%8F%AC_%EA%B0%9C%ED%8F%90%EC%97%85_%ED%86%B5%ED%95%A9_2021%20(2).csv")
fig = px.bar(df, x="지역",y=["길단위 유동인구"])
