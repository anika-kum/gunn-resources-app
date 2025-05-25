import streamlit as st
import numpy as np
import pandas as pd
from notes import load_items_from_csv_rating

def show_leaderboard():
    st.title("Leaderboard")
    st.subheader("Check out how useful users rank people's notes!")
    display_leaderboard_dict(leaderboard())

def leaderboard():
    unique_names = []
    name_score_sum = []
    total_names = []
    df = load_items_from_csv_rating()
    for i, row in df.iterrows():
        old = index_existence(unique_names, row[0])
        if old != -1:
            name_score_sum[old] += row[1]
            total_names[old] += 1
        else:
            unique_names.append(row[0])
            name_score_sum.append(row[1])
            old = index_existence(unique_names, row[0])
            total_names.append(1)
    score_averages = divisionFunc(name_score_sum,total_names)
    d = dict(zip(unique_names, score_averages))
    sorted_items = sorted(d.items(), key=lambda kv: (kv[1], kv[0]))
    return sorted_items


def display_leaderboard_dict(d):
    df = pd.DataFrame(d, columns=["Name", "Average Score"])
    df = df.sort_values(by="Average Score", ascending=False)
    st.dataframe(df.style.hide(axis=0))

        
def index_existence(a, value):
    for i, val in enumerate(a):
        if val == value:
            return i
    return -1

def divisionFunc(a, b):
    returnArr = []
    for i, val in enumerate(a):
        returnArr.append(val / b[i])
    return returnArr
