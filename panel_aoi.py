import pandas as pd
import streamlit as st
import plotly.express as px
from graficos.tabla import mostrar_tabla
from graficos.grafico_barras import mostrar_grafico_barras
from graficos.tiempo_medio  import mostrar_tiempo_medio
from graficos.tarjetas_paneles  import mostrar_tarjetas_paneles
from graficos.tiempo_medio  import mostrar_tiempo_medio_record

st.set_page_config(layout="wide",page_title="D2 PLUS - AOI") 

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

df = pd.read_csv("datos_diarios.csv", encoding="latin1")
hoy = pd.Timestamp.today().date().strftime("%d-%m-%Y")


with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.markdown('<div class="subtitulo">D2 PLUS</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="titulo">AOI</div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="subtitulo">{hoy}</div>', unsafe_allow_html=True)

with st.container():
    mostrar_tarjetas_paneles(df, hoy)

with st.container():
    col1, col2 = st.columns([2,1])

    with col1:
        mostrar_grafico_barras(df) 

    with col2:
        with st.container:
            mostrar_tiempo_medio(df,hoy)
        with st.container:
            mostrar_tiempo_medio_record(df)

mostrar_tabla(df)
