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

data_path = Path('Data/VOLVE-PETROPHYSICAL_INTERPRETATION')
folders = [folder for folder in data_path.iterdir() if folder.is_dir()]
folder_names = [folder.name for folder in folders]

folder = st.selectbox('Selecciona la carpeta', folder_names)