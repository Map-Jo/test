
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import koreanize_matplotlib

from pyproj import Proj, transform
import folium
import pyproj

import seaborn as sns
import plotly.express as px
import cufflinks as cf
import plotly.graph_objects as go
import json
cf.go_offline(connected=True)


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
st.title("서울시 내에 창업을 계획중이신가요?")
input_reg = st.text_input(label="지역명 ex)", value="지역명을 입력해주세요.")


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
elif input_reg == "종로구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "송파구":
    st.pyplot(total_graph(input_reg))
elif input_reg == "강동구":
    st.pyplot(total_graph(input_reg))

a = pd.read_csv("https://raw.githubusercontent.com/Map-Jo/test/main/%EC%84%9C%EC%9A%B8%EC%8B%9C_%EC%9A%B0%EB%A6%AC%EB%A7%88%EC%9D%84%EA%B0%80%EA%B2%8C_%EC%83%81%EA%B6%8C%EB%B6%84%EC%84%9D%EC%84%9C%EB%B9%84%EC%8A%A4(%EC%8B%A0_%EC%83%81%EA%B6%8C_%EC%B6%94%EC%A0%95%EB%A7%A4%EC%B6%9C)_2021%EB%85%84.csv",encoding='euc-kr')
b = pd.read_csv("https://raw.githubusercontent.com/Map-Jo/test/main/%EC%84%9C%EC%9A%B8%EC%8B%9C%20%EC%9A%B0%EB%A6%AC%EB%A7%88%EC%9D%84%EA%B0%80%EA%B2%8C%20%EC%83%81%EA%B6%8C%EB%B6%84%EC%84%9D%EC%84%9C%EB%B9%84%EC%8A%A4(%EC%83%81%EA%B6%8C%EC%98%81%EC%97%AD).csv",encoding='euc-kr', usecols=['상권_코드_명',"행정동_코드","시군구_코드",'엑스좌표_값','와이좌표_값'])
c = pd.read_csv("https://raw.githubusercontent.com/Map-Jo/test/main/%EC%84%9C%EC%9A%B8%EC%8B%9C%20%EC%9A%B0%EB%A6%AC%EB%A7%88%EC%9D%84%EA%B0%80%EA%B2%8C%20%EC%83%81%EA%B6%8C%EB%B6%84%EC%84%9D%EC%84%9C%EB%B9%84%EC%8A%A4(%EC%9E%90%EC%B9%98%EA%B5%AC%EB%B3%84%20%EC%83%81%EA%B6%8C%EB%B3%80%ED%99%94%EC%A7%80%ED%91%9C).csv",encoding='euc-kr', usecols=["시군구_코드","시군구_코드_명"])
c = c.drop_duplicates()

a = a.merge(b, on="상권_코드_명", how="left")

k = pd.read_csv("https://raw.githubusercontent.com/Map-Jo/test/main/%EC%84%9C%EC%9A%B8%EC%8B%9C%20%EC%9A%B0%EB%A6%AC%EB%A7%88%EC%9D%84%EA%B0%80%EA%B2%8C%20%EC%83%81%EA%B6%8C%EB%B6%84%EC%84%9D%EC%84%9C%EB%B9%84%EC%8A%A4(%EC%83%81%EA%B6%8C%EC%98%81%EC%97%AD).csv",encoding='euc-kr', usecols=["엑스좌표_값","와이좌표_값"])
k["엑스좌표_값"] = pd.to_numeric(k["엑스좌표_값"], errors="coerce")
k["와이좌표_값"] = pd.to_numeric(k["와이좌표_값"], errors="coerce")

k = k.dropna()
k.index=range(len(k))
k.tail()

def project_array(coord, p1_type, p2_type):
    """
    좌표계 변환 함수
     - coord: x, y 좌표 정보가 담긴 NumPy Array
    - p1_type: 입력 좌표계 정보 ex) epsg:5181
    - p2_type: 출력 좌표계 정보 ex) epsg:4326
    """
    p1 = pyproj.Proj(init=p1_type)
    p2 = pyproj.Proj(init=p2_type)
    fx, fy = pyproj.transform(p1, p2, coord[:, 0], coord[:, 1])
    return np.dstack([fx, fy])[0]
coord = np.array(k)


p1_type = "epsg:5181"
p2_type = "epsg:4326"

# project_array() 함수 실행
result = project_array(coord, p1_type, p2_type)


k["위도"] = result[:,1]
k["경도"] = result[:,0]


a = a.merge(k, on="엑스좌표_값", how="left")

for col in df.columns :
    dtype_name = df[col].dtypes.name
    if dtype_name.startswith("int"):
        df[col] = pd.to_numeric(df[col], downcast = "unsigned")
    elif dtype_name.startswith("float"):
        df[col] = pd.to_numeric(df[col], downcast = "float")
    elif dtype_name == "bool":
        df[col] = df[col].astype("int8")

a= a.merge(c, on="시군구_코드", how="left")

a = a.dropna()
a = a.drop(columns=["엑스좌표_값","와이좌표_값_x","와이좌표_값_y"])    

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.text('서울시 인구·점포·개·폐업 정보')
    st.write(df)
    st.text('서울시 상권 추정매출')
    st.write(a)


df_c = pd.read_csv("https://raw.githubusercontent.com/Map-Jo/test/main/%EC%9D%B8%EA%B5%AC_%EC%A0%90%ED%8F%AC_%EA%B0%9C%ED%8F%90%EC%97%85_%ED%86%B5%ED%95%A9_2021%20(2).csv")
object_list=['전체 점포수','프랜차이즈 점포수','일반 점포수','길단위 유동인구', '개업수', '폐업수']
for i in object_list:
    df_c[i]=df_c[i].str.replace(',', '').astype('int64')

df_c['지역'] = df_c['지역'].str.strip()
df_a = df_c[df_c['지역'] != '서울시 전체']

analysis_type =sidebar.radio("Analysis Type", ["Single", "Multiple"])
st.markdown(f"Analysis Mode: {analysis_type}")
# st.sidebar.header("사이드바 메뉴")
# st.sidebar.selectbox("메뉴를 선택하세요.", ["점포 정보"])
if analysis_type=="Single":

    plt.figure(figsize=(12, 10))
    sns.barplot(data=df_a.sort_values('전체 점포수'),x='전체 점포수',y='지역', ci=None)
    _ = plt.title('서울시 구별 21년도 전체 점포수')
    st.pyplot()    
#         st.subheader("전체 개업수")
#         plt.figure(figsize=(12, 10))
#         sns.barplot(data=df_a.sort_values('개업수'),x='개업수',y='지역', ci=None)
#         _ = plt.title('서울시 구별 21년도 개업수')    
#         st.pyplot()

#         st.subheader("전체 폐업수")
#         plt.figure(figsize=(12, 10))
#         sns.barplot(data=df_a.sort_values('폐업수'),x='폐업수',y='지역', ci=None)
#         _ = plt.title('서울시 구별 21년도 폐업수')    
#         st.pyplot()

#         st.subheader("주거인구")
#         plt.figure(figsize=(12, 10))
#         sns.barplot(data=df_a.sort_values('주거 인구'),x='주거 인구',y='지역', ci=None)
#         _ = plt.title('서울시 구별 21년도 주거인구')
#         st.pyplot()

#         st.subheader("직장인구")
#         plt.figure(figsize=(12, 10))
#         sns.barplot(data=df_a.sort_values('직장 인구'),x='직장 인구',y='지역', ci=None)
#         _ = plt.title('서울시 구별 21년도 직장인구')
#         st.pyplot()

df_a_nf = df_a.groupby('지역')['프랜차이즈 점포수', '일반 점포수'].mean()
# 틀만들기
fig, axs = plt.subplots(ncols=2, sharey=True, 
                        figsize=(10, 8), gridspec_kw={"wspace":0})

c_f = "green"
c_n = "darkorange"

#바 그래프 생성하기
axs[0].barh(df_a_nf.index, df_a_nf["프랜차이즈 점포수"], color=c_f)
axs[1].barh(df_a_nf.index, df_a_nf["일반 점포수"], color=c_n)

#단위 맞쳐주기
xmax = 5500
x2max=65000
axs[0].set_xlim(xmax, 0)
axs[1].set_xlim(0, x2max)

#제목 설정하기
for ax,title in zip(axs,['프랜차이즈 점포수','일반 점포수']):
    ax.set_title(title, color="gray", fontweight="bold", pad=16)

    
#꾸미기
for ax in axs:
    for i, p in enumerate(ax.patches):
        w = p.get_width()
        if ax == axs[0]:
            ha = "right"
            c = c_f
        else:
            ha = "left"
            c = c_n
        
        ax.text(w, i, f" {format(w, ',')} ", 
                c=c, fontsize=13, va="center", ha=ha, 
                fontweight="bold", alpha=0.5)
fig.suptitle("구별 프랜차이즈, 일반 점포수 비교", fontweight="bold")
fig.tight_layout()
st.pyplot()


df_u = pd.read_csv("https://raw.githubusercontent.com/Map-Jo/test/main/%EC%9D%B8%EA%B5%AC_%EC%A0%90%ED%8F%AC_%EA%B0%9C%ED%8F%90%EC%97%85_%ED%86%B5%ED%95%A9_2021%20(2).csv")
df3 = pd.read_csv("https://raw.githubusercontent.com/Map-Jo/test/main/%ED%96%89%EC%A0%95%EA%B5%AC%EC%97%AD_%EA%B5%AC%EB%B3%84__20220610170356.csv",encoding='euc-kr' )
df3=df3[["자치구","2019"]]
df3.columns=["지역","면적"]
df_u['지역'] = df_u['지역'].apply(lambda x: str(x).replace(u'\xa0', u''))
def remove_comma(x):
    return x.replace(',', '')

columns = ["전체 점포수", "프랜차이즈 점포수","일반 점포수","길단위 유동인구", "개업수", "폐업수"]

for column in columns:
    df_u[column]=df_u[column].apply(remove_comma).astype(int)
def make_qt(x):
    return x.replace("분기","")

df_u = pd.merge(df_u,df3,on="지역",how="left")
df_u["전체 점포수"] = df_u["전체 점포수"] / df_u["면적"]
df_u["총인구"]=df_u["길단위 유동인구"]+df_u["주거 인구"]+df_u["직장 인구"]





pop_mar = {}
for place in df_u["지역"].unique():
    pop_mar[place]=(df_u[df_u["지역"] == place][["전체 점포수", "총인구"]].corr()["총인구"]["전체 점포수"])
df_pop_mar = pd.DataFrame.from_dict(pop_mar, orient='index').rename(columns={0:"상관계수"})    
df_pop_mar.plot.barh(title="지역별 인구수와 점포수 상관관계", figsize=(12,10), rot = 0, color="orange")
st.pyplot()

# 유동인구 비율 데이터 추가
df_u["유동인구 비율"] = df_u["길단위 유동인구"] / df_u["총인구"] *100
df_u["직장인구 비율"] = df_u["직장 인구"] / df_u["총인구"] *100
df_u["주거인구 비율"] = df_u["주거 인구"] / df_u["총인구"] *100


df_per=df_u["유동인구 비율"].groupby(df_u["지역"]).mean().sort_values()
colors= ['orange' if x == "서울시 전체" else 'blue' for x in df_per.index]
df_per.plot.barh(title="구별 유동인구 비율",figsize=(12,10), color = colors)
plt.xlabel('%')
plt.xlim(98,100)
st.pyplot()

df_u[["지역","유동인구 비율", "직장인구 비율","주거인구 비율"]].groupby(df_u["지역"]).mean().plot.bar(figsize = (12,10), stacked=True,rot=30)
plt.ylim(98,100)
st.pyplot()

a.groupby("기준_분기_코드")[["월요일_매출_금액","화요일_매출_금액","수요일_매출_금액","목요일_매출_금액","금요일_매출_금액","토요일_매출_금액","일요일_매출_금액"]].mean().plot(kind="bar", rot=0)
st.pyplot()

a.groupby("기준_분기_코드")[['시간대_00~06_매출_금액','시간대_06~11_매출_금액','시간대_11~14_매출_금액','시간대_14~17_매출_금액','시간대_17~21_매출_금액','시간대_21~24_매출_금액']].mean().plot(kind="bar", rot=0)
st.pyplot()

a.groupby("기준_분기_코드")[['연령대_10_매출_금액','연령대_20_매출_금액','연령대_30_매출_금액','연령대_40_매출_금액','연령대_50_매출_금액','연령대_60_이상_매출_금액']].mean().plot(kind="bar", rot=0)
st.pyplot()


geo_path = pd.read_json("https://raw.githubusercontent.com/Map-Jo/test/main/seoul_municipalities_geo_simple%20(1).json")

geo_json = json.load(open(geo_path, encoding="utf-8"))
df_pop = pd.read_csv("https://raw.githubusercontent.com/Map-Jo/test/main/%EC%9D%B8%EA%B5%AC_%EC%A0%90%ED%8F%AC_%EA%B0%9C%ED%8F%90%EC%97%85_%ED%86%B5%ED%95%A9_2021%20(2).csv")

df_popular= df_pop.groupby("지역")["직장 인구"].sum().reset_index()
df_popular['지역']=df_popular['지역'].str.strip()

m = folium.Map(location=[df["위도"].mean(), df["경도"].mean()], zoom_start=12)



folium.Choropleth(
    geo_data=geo_json,
    name="choropleth",
    data=df_popular,
    columns=["지역","직장 인구"],
    key_on="feature.properties.name",
    fill_color = "YlGn",
    fill_opacity=0.8,
    line_opacity = 0.2,
    legend_name="직장인구 수",
).add_to(m)
m








