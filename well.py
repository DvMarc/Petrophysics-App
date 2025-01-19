import streamlit as st
import pandas as pd
from PIL import Image
from pathlib import Path
import lasio
import welly

icon = Image.open('logo.jpg')

st.set_page_config(page_title="Petrophysics App", page_icon=icon)

st.title('Petrophysics App')