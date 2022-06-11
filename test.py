
import pandas as pd
import numpy as np
import streamlit as st
from IPython import get_ipython
import matplotlib.pyplot as plt


df = pd.read_csv("https://raw.githubusercontent.com/Map-Jo/test/main/%EC%9D%B8%EA%B5%AC_%EC%A0%90%ED%8F%AC_%EA%B0%9C%ED%8F%90%EC%97%85_%ED%86%B5%ED%95%A9_2021%20(2).csv")



object_list=['전체 점포수','프랜차이즈 점포수','일반 점포수','길단위 유동인구', '개업수', '폐업수']
for i in object_list:
    df[i]=df[i].str.replace(',', '').astype('int64')




df['지역']=df['지역'].str.strip()



df_a = df[df['지역'] != '서울시 전체']


st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("어느 지역에 창업을 계획중이신가요?")
input_reg = st.text_input(label="지역명", value="gu")




st.dataframe(df)
