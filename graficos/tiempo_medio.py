import pandas as pd
import streamlit as st
import plotly.graph_objects as go 


def mostrar_tiempo_medio(df_hoy):    
    tiempo_medio = df_hoy['Tiempo medio'].iloc[0] 

    fig = go.Figure(go.Indicator(
        mode = "number",
        value = tiempo_medio,
        number = {'suffix': " seg", 'font': {'size': 48}},
        title = {'text': "Tiempo medio", 'font': {'size': 20}}
    ))

    # Mostrar en Streamlit
    st.plotly_chart(fig, use_container_width=True) 

