import pandas as pd
import streamlit as st
import plotly.express as px

def mostrar_tabla(): 
    df = pd.read_csv("datos_diarios.csv") 
    # Ordenar de más reciente a más antiguo
    df = df.sort_values(by='Fecha', ascending=False)
    # Filtrar las 7 fechas mas recientes
    df_ultimos_7 = df.head(7)
    df_ultimos_7 = df_ultimos_7.reset_index(drop=True)

    st.dataframe(df_ultimos_7)