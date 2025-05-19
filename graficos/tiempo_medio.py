import pandas as pd
import streamlit as st
import plotly.graph_objects as go


def mostrar_tiempo_medio(df,hoy):  
    fecha_hoy = pd.to_datetime(hoy, format="%d-%m-%Y")

    df_hoy = df[df['Fecha'] == fecha_hoy]

    if df_hoy.empty:
        df_hoy = df[df['Fecha'] == df['Fecha'].max()] 
    tiempo_medio = df_hoy['Tiempo medio'].iloc[0] 

    fig = go.Figure(go.Indicator(
        mode = "number",
        value = tiempo_medio,
        number = {'suffix': " seg", 'font': {'size': 48}},
        title = {'text': "Tiempo medio", 'font': {'size': 20}}
    ))

    # Mostrar en Streamlit
    st.plotly_chart(fig, use_container_width=True)
