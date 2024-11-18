import streamlit as st
import os
from streamlit_navigation_bar import st_navbar as navbar
from Pages import Home, Project1, Project2 , Project3
from PIL import  Image
import pandas as pd
import numpy as np

image = Image.open('img/logo.jpeg')
st.set_page_config(initial_sidebar_state="collapsed")

logo_path = os.path.join(os.path.dirname(__file__), "img", "dino.svg")
pages = ["Home","Project1","Project2","Project3"]

styles = {
    "nav": {
        "background-color": "rgba(133, 133, 254)",
        "display": "flex",
        "justify-content": "center"
    },
    "img": {
        "position": "absolute",
        "left": "-20px",
        "font-size": "15px",
        "top": "4px",
        "width": "100px",
        "height": "40px",
    },
    "div":{
        "max-width":"32rem",
    },
    "span":{
        "border-radius":"0.5rem",
        "color":"rgba(49,51,63)",
        "margin":"0 0.125rem",
        "padding":"0.4375rem 0.625rem",
    },
    "active":{
        "background-color":"rgba(155,114,255,0.25)",
    },
    "hover":{
        "background-color":"rgba(255,255,255,0.35)",
    },
}


page = navbar(pages, styles=styles)

if page == 'Home':
    Home.Home().app()
elif page == 'Project1':
    Project1.Project1().app()
elif page == 'Project2':
    Project2.Project2().app()
elif page == 'Project3':
    Project3.Project3().app()
else:
    Home.Home().app()