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

def mostrar_tiempo_medio_record(df):
     
    tiempo_medio_record = df['Tiempo medio'].min()
     
    fechas_record = df[df['Tiempo medio'] == tiempo_medio_record]['Fecha']
    
    fecha_record = fechas_record.iloc[0] if not fechas_record.empty else None

    fig = go.Figure(go.Indicator(
        mode = "number",
        value = tiempo_medio_record,
        number = {'suffix': " seg", 'font': {'size': 36}},
        title = {'text': f"Record tiempo medio<br><span style='font-size:16px'>{fecha_record.strftime('%d-%m-%Y') if fecha_record is not None else ''}</span>", 'font': {'size': 20}}
    ))

    st.plotly_chart(fig, use_container_width=True)
    
