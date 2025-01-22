import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import lasio
import os
import welly


def curves_logs(curves, file, start, stop):
    log = welly.Well.from_las(file)
    df = log.df()
    
    fig, axes = plt.subplots(1, len(curves), figsize=(20, 10))
    
    # Normalizar axes a una lista, incluso si hay solo una curva
    if len(curves) == 1:
        axes = [axes]
    
    for ind, curve in enumerate(curves):
        try:
            segment = log.data[curve].to_basis(start=start, stop=stop)
            segment.plot(ax=axes[ind])
            axes[ind].set_title(curve)
        except Exception as e:
            axes[ind].set_title(f"Error: {curve}")
            axes[ind].text(0.5, 0.5, str(e), ha='center', va='center', transform=axes[ind].transAxes)
    
    axes[0].set_ylabel('Depth (m)', fontsize=14)
    fig.suptitle('Petrophysical Logs', fontsize=16)
    fig.tight_layout()
    return fig

icon = Image.open('logo.jpg')

st.set_page_config(page_title="Petrophysics App", page_icon=icon)

st.title('Petrophysics App')

st.write("""
Esta aplicación permite analizar archivos de registros de pozos 
en formato LAS del campo Volve, Noruega.
""")

image = Image.open('interpretacion-de-registros.png')
st.image(image,  use_container_width=True)

st.write("""
Permite explorar datos petrofísicos clave, como porosidad, saturación de agua y volumen de arcilla, además de visualizar gráficos 
e información detallada sobre las características del subsuelo.
""")


st.write("")
st.header("Importar archivos LAS")
uploaded_file = st.file_uploader("Sube tu archivo LAS aquí:", type=["las"])

if uploaded_file:
    try:
        # Guardar archivo temporal
        temp_file_path = "temp_file.las"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(uploaded_file.getvalue())

        # Leer archivo LAS
        las = lasio.read(temp_file_path)
        
        st.write("Archivo cargado: ", uploaded_file.name)

        # Convertir datos LAS a DataFrame
        las_df = las.df()

        # Mostrar datos
        st.subheader("Vista de Datos del Archivo LAS")
        st.dataframe(las_df)

        # Mostrar estadísticas
        st.subheader("Estadísticas Básicas")
        st.write(las_df.describe())

        # Sección para visualización de registros
        st.subheader("Visualización de Registros")
        curve_to_plot = st.selectbox("Selecciona la curva a visualizar:", las_df.columns)

        if curve_to_plot:
            plt.figure(figsize=(6, 8))
            plt.plot(las_df[curve_to_plot], las_df.index, label=curve_to_plot)
            plt.gca().invert_yaxis()
            plt.xlabel(curve_to_plot)
            plt.ylabel("Profundidad (m)")
            plt.title(f"Registro de {curve_to_plot}")
            plt.legend()
            st.pyplot(plt)

       # Sección para cálculos petrofísicos
        st.subheader("Cálculos Petrofísicos")

        curves = ["PHIF", "SAND_FLAG", "SW", 'VSH']
        file = temp_file_path
        
        # input para profundidad de inicio y fin
        start = st.number_input("Profundidad de inicio (m):", min_value=0, value=0)
        stop = st.number_input("Profundidad de fin (m):", min_value=0, value=1000)

        if st.button("Calcular"):
            fig = curves_logs(curves, file, start, stop)
            st.pyplot(fig) 

        os.remove(temp_file_path)
    except Exception as err:
        st.error(f"Error al procesar el archivo LAS: {err}")
else:
    st.info("Por favor, sube un archivo LAS para continuar.")
