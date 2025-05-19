import pandas as pd
import streamlit as st
import plotly.express as px

def mostrar_tabla(df): 
    df = df.sort_values(by='Fecha', ascending=False)
    df_ultimos_7 = df.head(7)
    df_ultimos_7 = df_ultimos_7.reset_index(drop=True)

    st.dataframe(df_ultimos_7)