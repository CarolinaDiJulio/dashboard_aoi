import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

def mostrar_grafico_barras(df_hoy):   
    df_hoy_total = df_hoy[['Paneles total', 'Paneles correctos', 'Paneles erroneos']].sum() 
    fig = px.bar(df_hoy_total,  
                x=df_hoy_total.index,  
                y=df_hoy_total.values, 
                labels={'x': 'Categoría', 'y': 'Número de Paneles'},
                color=df_hoy_total.index, 
                height=400
                )

    # bargap
    fig.update_layout(bargap=0.2) 

    st.plotly_chart(fig)