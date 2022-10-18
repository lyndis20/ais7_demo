from dataclasses import dataclass
import streamlit as st
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import koreanize_matplotlib
import plotly.express as px

st.set_page_config(
    page_title="Likelion AI School 자동차 연비 App",
    page_icon="🚕",
    layout="wide",
)

# st.set_page_config()

st.markdown("# 자동차 연비 🚗")
st.sidebar.markdown("자동차 연비🚗")
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"


@st.cache
def load_data():
    data = pd.read_csv(url)
    return data

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done! (using st.cache)")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(range(data.model_year.min(), data.model_year.max())))

# Sidebar - origin
sorted_unique_origin = sorted(data.origin.unique())
selected_origin = st.sidebar.multiselect('origin', sorted_unique_origin, sorted_unique_origin)


if selected_year > 0 :
   data = data[data.model_year == selected_year]

if len(selected_origin) > 0:
   mpg = data[data.origin.isin(selected_origin)]

st.dataframe(data)

st.line_chart(data["mpg"])

st.bar_chart(data["mpg"])

fig, ax = plt.subplots()
sns.barplot(data=data, x="origin", y="mpg").set_title("origin 별 자동차 연비")
st.pyplot(fig)

sns.countplot(data=data, x="model_year").set_title("표본의 연도별 빈도수")
st.pyplot(fig)

psh = px.histogram(data, x="origin")
psh

st.area_chart(data[["mpg","cylinders"]], use_container_width=True)

#scatterplot
sct, ax = plt.subplots(figsize=(10,3))
sns.scatterplot(data=data, x='origin', y='mpg')
st.pyplot(sct)

sns.swarmplot(data=mpg_year, x="origin", y="horsepower").set_title(f"{selected_year}년 지역별 마력")
