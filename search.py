import streamlit as st
import pandas as pd
import csv

def show_search():
    st.title("Search")
    st.text_input("hihi ", "dogs")
    df = pd.read_excel("/nodes_data.csv")
    st.write(df)