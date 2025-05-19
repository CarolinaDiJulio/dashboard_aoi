import pandas as pd
import streamlit as st
import plotly.express as px
from graficos.tabla import mostrar_tabla
from graficos.grafico_barras import mostrar_grafico_barras
from graficos.tiempo_medio  import mostrar_tiempo_medio

st.set_page_config(layout="wide",page_title="D2 PLUS - AOI") 

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

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
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.markdown('<div class="card">Paneles totales:<br><span class="card-value">100</span></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card">Paneles correctos:<br><span class="card-value">80</span></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card">Paneles incorrectos:<br><span class="card-value">20</span></div>', unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns([2,1])

    with col1:
        mostrar_grafico_barras() 

    with col2:
        mostrar_tiempo_medio()

mostrar_tabla()
