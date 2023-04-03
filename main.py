import streamlit as st
import pandas as pd
import plotly.express as px

st.title('In Search For Happiness')
x_axis = st.selectbox('Select The Data For X-axis', ['GDP', 'Happiness', 'Generosity'])
y_axis = st.selectbox('Select The Data For Y-axis', ['GDP', 'Happiness', 'Generosity'])
st.subheader(f'{x_axis} and {y_axis}')

df = pd.read_csv('happy.csv')

match x_axis:
    case 'GDP':
        x = df['gdp']
    case 'Happiness':
        x = df['happiness']
    case 'Generosity':
        x = df['generosity']

match y_axis:
    case 'GDP':
        y = df['gdp']
    case 'Happiness':
        y = df['happiness']
    case 'Generosity':
        y = df['generosity']

figure = px.scatter(x=x, y=y, labels={'x': f'{x_axis}', 'y': f'{y_axis}'})
st.plotly_chart(figure)
