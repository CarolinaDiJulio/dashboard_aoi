import pandas as pd
import streamlit as st
import plotly.express as px
from graficos.tabla import mostrar_tabla
from graficos.grafico_barras import mostrar_grafico_barras
from graficos.tiempo_medio  import mostrar_tiempo_medio

def mostrar_tarjetas_paneles(df_hoy):  
    paneles_totales = df_hoy['Paneles total'].get(df_hoy.index[0], 0)
    paneles_correctos = df_hoy['Paneles correctos'].get(df_hoy.index[0], 0) 
    paneles_erroneos = df_hoy['Paneles erroneos'].get(df_hoy.index[0], 0)
    
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.markdown(f'<div class="card">Paneles totales:<br><span class="card-value">{paneles_totales}</span></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="card">Paneles correctos:<br><span class="card-value">{paneles_correctos}</span></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="card">Paneles incorrectos:<br><span class="card-value">{paneles_erroneos}</span></div>', unsafe_allow_html=True)
