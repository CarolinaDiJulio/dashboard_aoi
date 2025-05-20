
from datetime import datetime
import pandas as pd
import streamlit as st
import plotly.express as px
from graficos.tabla import mostrar_tabla
from graficos.grafico_barras import mostrar_grafico_barras
from graficos.tiempo_medio  import mostrar_tiempo_medio
from graficos.tarjetas_paneles  import mostrar_tarjetas_paneles 
from graficos.record import mostrar_record

# Configuraciones de pagina
st.set_page_config(layout="wide",page_title="D2 PLUS - AOI") 

# Estilos css
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

hoy_str = pd.Timestamp.today().date().strftime("%d-%m-%Y")
hoy_timestamp= pd.to_datetime(hoy_str, format="%d-%m-%Y")

# Leer el archivo csv
df = pd.read_csv("datos_diarios.csv", encoding="latin1")

# Convierte la columna fecha a datetime de pandas
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Obtener la linea de hoy
df_hoy = df[df['Fecha'] == hoy_timestamp]

 
with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.markdown('<div class="subtitulo">D2 PLUS</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="titulo">AOI</div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="subtitulo">{hoy_str}</div>', unsafe_allow_html=True)
if not df_hoy.empty:
    with st.container():
        mostrar_tarjetas_paneles(df_hoy)

    with st.container():
        col1, col2, col3= st.columns([3, 1, 1]) 
        with col1:
            mostrar_grafico_barras(df_hoy) 
        with col2: 
            mostrar_tiempo_medio(df_hoy) 
        with col3:
             mostrar_record(df)
else:
        st.warning(f"No hay datos para el día de hoy.")

mostrar_tabla(df)
