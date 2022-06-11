
import pandas as pd
import numpy as np
import streamlit as st
from IPython import get_ipython
import matplotlib.pyplot as plt

import matplotlib
from matplotlib import font_manager, rc
import platform
if platform.system()=="Windows":
    font_name=font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus']=False

import warnings
warnings.filterwarnings("ignore")


df = pd.read_csv("https://raw.githubusercontent.com/Map-Jo/test/main/%EC%9D%B8%EA%B5%AC_%EC%A0%90%ED%8F%AC_%EA%B0%9C%ED%8F%90%EC%97%85_%ED%86%B5%ED%95%A9_2021%20(2).csv")

object_list=['전체 점포수','프랜차이즈 점포수','일반 점포수','길단위 유동인구', '개업수', '폐업수']
for i in object_list:
    df[i]=df[i].str.replace(',', '').astype('int64')

df['지역']=df['지역'].str.strip()


df_a = df[df['지역'] != '서울시 전체']


def total_graph(gu):
    fig, axes = plt.subplots(2, 2)
    fig.set_size_inches((12, 12))
    plt.subplots_adjust(wspace = 0.15, hspace = 0.15)


    fig.suptitle( gu , fontsize=15)

 
    df_x=df[df['지역']==gu]
    axes[0, 0].plot(df_x['분기'],df_x['전체 점포수'], color='blue', marker='o')
    axes[0, 0].set_xlabel('분기', fontsize = 11)
    axes[0, 0].set_ylabel('전체 점포수', fontsize = 11)
    axes[0, 0].set_title('분기별 전체점포수', fontsize = 12)

    l1=axes[0,1].bar(df_x['분기'],df_x['개업률'],width=0.5,alpha=0.5, color='red')
    l2=axes[0,1].bar(df_x['분기'],df_x['폐업률'],width=0.5,alpha=0.5, color='blue')
    axes[0,1].legend([l1,l2],['개업률','폐업률'])
    axes[0, 1].set_xlabel('분기', fontsize = 11)
    axes[0, 1].set_ylabel('비율 %단위', fontsize = 11)
    axes[0, 1].set_title('분기별 개/폐업률\n 빨강:개업률 / 파랑:폐업률', fontsize = 12)

    axes[1, 0].plot(df_x['분기'],df_x['길단위 유동인구'], color='red', marker='o')
    axes[1, 0].set_xlabel('분기', fontsize = 11)
    axes[1, 0].set_ylabel('길단위 유동인구', fontsize = 11)
    axes[1, 0].set_title('분기별 길단위 유동인구', fontsize = 12)

    bar_width = 0.5
    index = np.arange(1)
    label=['']
    l3=axes[1,1].bar(index,df_x['주거 인구'],width=0.5,alpha=0.3, color='green')
    l4=axes[1,1].bar(index+bar_width,df_x['직장 인구'],width=0.5,alpha=0.3, color='blue')
    axes[1,1].legend([l3,l4],['주거인구','직장인구'])
    axes[1, 1].set_xlabel('인구 종류', fontsize = 11)
    axes[1, 1].set_ylabel('', fontsize = 11)
    axes[1, 1].set_title('주거/직장 인구수', fontsize = 12)


    plt.tight_layout()
    return plt.show()




st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("어느 지역에 창업을 계획중이신가요?")
input_reg = st.text_input(label="지역명", value="지역명을 입력해주세요.")


if input_reg == "강남구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "중구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "용산구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "성동구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "광진구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "동대문구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "중랑구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "성북구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "강북구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "도봉구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "노원구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "은평구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "서대문구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "마포구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "양천구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "강서구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "구로구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "금천구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "영등포구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "동작구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "관악구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "서초구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "강남구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "송파구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "강동구":
    st.pyplot(total_graph(input_reg))






st.dataframe(df)






