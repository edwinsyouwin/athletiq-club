import streamlit as st
from streamlit_option_menu import option_menu
from dotenv import load_dotenv
import os
import streamlit.components.v1 as components
import sys

load_dotenv(dotenv_path=".env")

st.set_page_config(
        page_title="AI-generated Content for Athletes",
        layout="wide",
)

sys.path.append(os.path.join(os.getcwd(), 'server/scripts'))

from render_svg import render_svg

if os.getenv("OPENAI_API_KEY") is None:
    st.text_input("Enter your OPENAI_API_KEY", key="OPENAI_API_KEY")

f = open(".streamlit/athletiq-logo.svg","r")
lines = f.readlines()
line_string=''.join(lines)

st.title("Content Generation Tools")
st.write("A collection of tools to generate, clean, and ingest content.")

st.divider()

st.header("Display Content")
st.write("A frontend to view generated content.")

st.divider()

if 'menu_options' not in st.session_state:
    st.session_state.menu_options = [""]
with st.sidebar:
    render_svg(line_string)

    selected = option_menu(None, st.session_state.menu_options, 
        icons=['house', 'gear'], default_index=0, orientation="vertical",
    styles={
        # "container": {"display":"inline", "top": "0", "background-color": "#00000", "width": "100%"},
        "icon": {"display": "none", "font-size": "25px"}, 
        "nav-link": {"text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#7289da"},
    }
    )

