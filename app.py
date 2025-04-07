import pandas as pd
import plotly.express as px
import streamlit as st

# importar el archivo de datos
vehicles = pd.read_csv('vehicles_us.csv')

# Poner el título y crear la casilla
hist_button = st.checkbox('Construir histograma')
scatter_button = st.checkbox('Construir gráfico de dispersión')

# Crear la selección de la casilla
if hist_button:
    st.write('Creación de histograma para el conjunto de datos de ventas de carros')

    fig = px.histogram(vehicles, x='odometer', y='price')

    st.plotly_chart(fig, use_container_width=True)


if scatter_button:
    st.write('Creacion de gráfico de dispersión de ventas de carros')

    fig = px.scatter(vehicles, x='odometer', y='price')

    st.plotly_chart(fig, use_container_width=True)