import pandas as pd
import streamlit as st
import plotly.express as px

def mostrar_tabla(): 
    df = pd.read_csv("datos_diarios.csv")
    st.table(df)