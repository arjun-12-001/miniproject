from asyncio.windows_events import NULL
from logging import exception
from turtle import pd
import streamlit as st
import plotly_express as px
import plotly.graph_objects as go
import pandas as pd
import altair as alt
import json
import requests 
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt
import os

st.title("Data Visualization of Fraudulent transactions")

try:
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)
except:
    pass

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_k0rizvsr.json")

path = os.path.abspath("lottiefiles/animate.json")
lottie_coding = load_lottiefile(path)

st_lottie(lottie_hello,key="hello",height=400,width=400)
st.markdown(""" 
    - Check out [RBI infomative webpage](https://www.rbi.org.in/commonperson/English/Scripts/SMSLimitedliability.aspx) for victims of fraud
    - Jump back into the [fraud dectection page](http://127.0.0.1:5000)
    
    ### Analysing data
    - Use a neural net to [what](https://github.com/streamlit/demo-self-driving)
""")

st.sidebar.subheader("Visualization Settings")
uploaded_file = st.sidebar.file_uploader(label="Upload your CSV or excel file(Max - 200MB)",
                        type=['csv','xlsx'])

global data
if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        # st.write(data.head())
    except Exception as e:
        print(e)
        data = pd.read_excel(uploaded_file)
    finally:
        data['name'] = "State : " + data['state']
global num_vals

try:
    num_vals = list(data.select_dtypes(['int','float']).columns)
    fraud = data[['trans_date_trans_time','merchant','category','gender','city','city_pop']]
    st.write(fraud.head(100))
except Exception as e:
    print(e)
    st.write("please upload file !")

try:
    st.markdown("## Here we have geographic representation of fraud transaction in US at 2020 ")
    loc = data[['lat','lon']]
    st.map(loc)
    st.markdown("""- As we can see majority of fraud transactions are happening in major metropolitan areas
    where people have more access to technology services and advancement in it """)
except:
    st.write('geographical locations based on fraudulence is unable to load !')


chart_select = st.sidebar.selectbox(
    label = 'select the chart type',
    options=['Scatterplots','Bar Chart','Line-plot']
)
if chart_select == 'Line-plot':
    try:
        st.markdown("## All fraud transactions losses identified the last 6 months of 2020 ")
        dates = pd.read_csv('recent.csv')
        dates = dates.rename(columns={'date':'index'}).set_index('index')
        st.line_chart(dates.head(6))
    except:
        pass


if chart_select == 'Scatterplots':
    st.sidebar.subheader("Scatterplots Settings")
    try:
        x_val = st.sidebar.selectbox('X axis', options=num_vals)
        y_val = st.sidebar.selectbox('Y axis', options=num_vals)
        plot = px.scatter(data_frame=data, x=x_val, y=y_val)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Bar Chart':
    st.markdown("### Bar Chart of most fraud transacted cities in US")
    priority = pd.read_csv('staterank.csv')
    priority = priority.head(6)
    bar_chart = alt.Chart(priority).mark_bar().encode(
        y = 'fraud frequency',
        x = 'state',
    )
    st.altair_chart(bar_chart, use_container_width=True)

if chart_select == 'Choropleth Map':
    st.sidebar.subheader("Choropleth Map Settings")
    try:
        upload = st.sidebar.file_uploader(label="Upload your CSV or excel Mapping data(Max - 200MB)",
                        type=['csv','xlsx'])
        data_map = pd.read_csv(upload)
        print(data_map.head)
        # mapping function
        data = dict(type = 'choropleth',
            locations = data_map['short'],
            z = data_map['fraud frequency'].astype(float),
            locationmode = 'USA-states',
            colorscale = 'Reds',
            colorbar = {'title' : 'Fraudulent transaction frequency'},
            text = data_map['Text'])

        layout = dict(
            title = '2020 credit fraud in USA',
            geo = dict(scope = 'usa',
               showlakes = True,
               lakecolor = 'rgb(85,173,240)')
)
        choromap = go.Figure(data = [data], layout = layout)
        choromap.show()     
    except:
        st.write('There seems to be an error loading map!')

df = [['female',54],['male',46]]
    # df = pd.DataFrame(df, columns=['gender','percentage'])
    # fig = px.pie(df, values='percentage', names='gender', title='gender and victims')
    # fig.show()
st.markdown(' -Here we can see that women are subjected to higher fraud ')
labels = 'Female','male'
sizes = [54,46]
explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)

st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    # renderer="svg", # canvas
    height=720,
    width=720,
    key=None,
)
st.markdown("#for further information contact ADMIN at [contact page](http://localhost:8502/)")