from notes import show_notes
from search import show_search
from rent import show_rent
from leaderboard import show_leaderboard
import streamlit as st
from streamlit_option_menu import option_menu
import pathlib


#st.set_page_config(page_title="My webpage", page_icon=":tada", layout="wide")

with open('styles.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Homepage", "Notes", "Rent", "Search", "Leaderboard"],
        icons=["house", "card-list", "coin", "search", "trophy"],
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
        st.title("Study Swap")
        st.subheader("Hey we're Audrey and Anika")
        st.write("this is cool!!!")
elif selected == "Notes":
    show_notes()
elif selected == "Rent":
    show_rent()
elif selected == "Search":
    show_search()
elif selected == "Leaderboard":
    show_leaderboard()