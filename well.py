import streamlit as st
import pandas as pd
from PIL import Image
from pathlib import Path
import lasio
import welly

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
    st.write("Archivo cargado: ", uploaded_file.name)


