import streamlit as st
import pandas as pd
import csv

def show_search():
    df = pd.read_csv("notes_data.csv")

    st.title("Search")
    search_term = st.text_input("Search: ", "")

    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]

    st.dataframe(filtered_df)