import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.write('어느 자치구에 개업을 생각 중이신가요?')

st.slidebar.header("Menu")

region = st.sidebar.selectbox("자치구",['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구',
       '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구',
       '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']
                              

# df = pd.read_csv("https://raw.githubusercontent.com/Map-Jo/test/main/%EC%9D%B8%EA%B5%AC_%EC%A0%90%ED%8F%AC_%EA%B0%9C%ED%8F%90%EC%97%85_%ED%86%B5%ED%95%A9_2021%20(2).csv")
# object_list=['전체 점포수','프랜차이즈 점포수','일반 점포수','길단위 유동인구', '개업수', '폐업수']
# for i in object_list:
#     df[i]=df[i].str.replace(',', '').astype('int64')
# df['지역']=df['지역'].str.strip()
# df_a = df[df['지역'] != '서울시 전체']
# def total_graph(gu):
#     f, axes = plt.subplots(2, 2)
#     f.set_size_inches((12, 12))
#     plt.subplots_adjust(wspace = 0.15, hspace = 0.15)

#     #figure 전체 제목
#     f.suptitle( gu , fontsize=15)

#     #분기별 전체 점포수 변화 선 그래프
#     df_x=df[df['지역']==gu]
#     axes[0, 0].plot(df_x['분기'],df_x['전체 점포수'], color='blue', marker='o')
#     axes[0, 0].set_xlabel('분기', fontsize = 11)
#     axes[0, 0].set_ylabel('전체 점포수', fontsize = 11)
#     axes[0, 0].set_title('분기별 전체점포수', fontsize = 12)

#     #분기별 개폐업률 막대 그래프 비교
#     l1=axes[0,1].bar(df_x['분기'],df_x['개업률'],width=0.5,alpha=0.5, color='red')
#     l2=axes[0,1].bar(df_x['분기'],df_x['폐업률'],width=0.5,alpha=0.5, color='blue')
#     axes[0,1].legend([l1,l2],['개업률','폐업률'])
#     axes[0, 1].set_xlabel('분기', fontsize = 11)
#     axes[0, 1].set_ylabel('비율 %단위', fontsize = 11)
#     axes[0, 1].set_title('분기별 개/폐업률\n 빨강:개업률 / 파랑:폐업률', fontsize = 12)

#     #길단위 인구수
#     axes[1, 0].plot(df_x['분기'],df_x['길단위 유동인구'], color='red', marker='o')
#     axes[1, 0].set_xlabel('분기', fontsize = 11)
#     axes[1, 0].set_ylabel('길단위 유동인구', fontsize = 11)
#     axes[1, 0].set_title('분기별 길단위 유동인구', fontsize = 12)

#     #주거, 직장 인구
#     bar_width = 0.5
#     index = np.arange(1)
#     label=['']
#     l3=axes[1,1].bar(index,df_x['주거 인구'],width=0.5,alpha=0.3, color='green')
#     l4=axes[1,1].bar(index+bar_width,df_x['직장 인구'],width=0.5,alpha=0.3, color='blue')
#     axes[1,1].legend([l3,l4],['주거인구','직장인구'])
#     axes[1, 1].set_xlabel('인구 종류', fontsize = 11)
#     axes[1, 1].set_ylabel('', fontsize = 11)
#     axes[1, 1].set_title('주거/직장 인구수', fontsize = 12)


#     plt.tight_layout()
#     return plt.show()
# gu=input("원하시는 구를 입력해주세요: ")
# total_graph(gu)
