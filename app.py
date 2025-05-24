from notes import show_notes
from rent import show_rent
import streamlit as st
from streamlit_option_menu import option_menu



st.set_page_config(page_title="My webpage", page_icon=":tada", layout="wide")

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Homepage", "Notes", "Rent"],
        icons=["house", "card-list", "coin"],
        menu_icon="menu-up",
        default_index=0,
        orientation='horizontal',
        styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
    )

if selected == "Homepage":
    with st.container(): 
        st.subheader("Hey we're Audrey and Anika")
        st.title("Gunn students")
        st.write("this is cool!!!")
elif selected == "Notes":
    show_notes()
elif selected == "Rent":
    show_rent()