import streamlit as st
import os
import csv
import pandas as pd
from io import StringIO
import time
import io

CSV_PATH = "notes_data.csv"

def initialize_csv():
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, mode="w", newline="", encoding="latin-1") as f:
            writer = csv.writer(f)
            writer.writerow(['uploaded_files', 'subject_label'])

def save_item_to_csv(item_data):
    with open(CSV_PATH, mode="a", newline="", encoding="latin-1") as f:
        writer = csv.writer(f)
        writer.writerow(item_data)

def load_items_from_csv():
    if os.path.exists(CSV_PATH):
        return pd.read_csv(CSV_PATH)
    else:
        return pd.DataFrame(columns=['uploaded_files', 'subject_label'])
    
def show_notes():
    initialize_csv()
    images = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlVTWL4dqk9ZokaiRQe0kdV3_dNvkB7A3xTw&s", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrfqqNGW1yUTzEtl3OsyaP_X9zHGaLVI_S9A&s", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXZ8ORCFOkes_5zSVPN14Pj_AvxZuguzoizQ&s"]
    noteDict = {"numPics" : 3, "numCols" : 3}

    cols = st.columns(noteDict["numCols"])
    for i, x in enumerate(cols):
            x.image(image = images[i], caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto", use_container_width=False)

    st.write("Num pics is: " + str(noteDict["numPics"]))
    uploadedImages = []
    st.title("Notes")
    with st.form("maform"):
        uploaded_files = st.file_uploader("Image File")
        subject_label = st.selectbox("Select subject", ["Math", "Science", "English", "History"])
        submitted = st.form_submit_button("Upload")
        if submitted:
            if uploaded_files is not None:
                st.write("In progress!")
                stringio = StringIO(uploaded_files.getvalue().decode("latin-1"))
                string_data = stringio.read()
                note_data = [string_data, subject_label]
                save_item_to_csv(note_data)
    load_data()

def load_data():
    df = load_items_from_csv()
    if df.empty:
        st.info("Nothing available yet.")
    else:
        for i, row in df.iterrows():
            tile = st.container(height=250)
            with tile:
                st.image(row['uploaded_files'].read())
                st.markdown(f"**Subject:** {row['subject_label']}")
