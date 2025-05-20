import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go 

def mostrar_record(df): 
    df_ordenado = df.sort_values(by=['Tiempo medio', 'Paneles total'], ascending=[True, False])
        
    # Tomar el primer registro como el "mejor día"
    mejor_dia = df_ordenado.iloc[0]

    fecha_mejor_dia = mejor_dia['Fecha'].strftime('%Y-%m-%d')
    tiempo = mejor_dia['Tiempo medio']

    fig = go.Figure(go.Indicator(
        mode = "number",
        value = tiempo,
        number = {'suffix': " seg", 'font': {'size': 48}},
        title = {'text': f"Día {fecha_mejor_dia} <br> Tiempo medio record:", 'font': {'size': 18}}
    ))

    st.plotly_chart(fig, use_container_width=True)