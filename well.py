import streamlit as st
import pandas as pd
from PIL import Image
import lasio
import os

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

        temp_file_path = "temp_file.las"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(uploaded_file.getvalue())

        las = lasio.read(temp_file_path)

        os.remove(temp_file_path)

        st.write("Archivo cargado: ", uploaded_file.name)

        st.subheader("Metadatos del Archivo LAS")

        las_df = las.df()
        st.subheader("Vista de Datos del Archivo LAS")
        st.dataframe(las_df)

        st.subheader("Estadísticas Básicas")
        st.write(las_df.describe())


    except Exception as err:
        st.error(f"Error al procesar el archivo LAS: {err}")
else:
    st.info("Por favor, sube un archivo LAS para continuar.")

