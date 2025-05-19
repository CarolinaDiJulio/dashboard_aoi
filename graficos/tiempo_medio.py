import streamlit as st
import plotly.graph_objects as go


def mostrar_tiempo_medio():
    tiempo_medio = 12.5

    fig = go.Figure(go.Indicator(
        mode = "number",
        value = tiempo_medio,
        number = {'suffix': " min", 'font': {'size': 48}},
        title = {'text': "Tiempo medio", 'font': {'size': 20}}
    ))

    # Mostrar en Streamlit
    st.plotly_chart(fig, use_container_width=True)
