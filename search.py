import streamlit as st
import base64
import pandas as pd
import csv
import io
import os


def show_search():
    file_path = "notes_data.csv"

    if os.path.exists(file_path):
        df = pd.read_csv("notes_data.csv")

        st.title("Search")
        search_term = st.text_input("Search: ", "")

        filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]

        popover = st.popover("Filter by Subject")
        math = popover.checkbox("Math", True)
        science = popover.checkbox("Science", True)
        english = popover.checkbox("English", True)
        history = popover.checkbox("History", True)

        if math:
            filtered_df = df[filtered_df.apply(lambda row: row.astype(str).str.contains("Math", case=False).any(), axis=1)]
        if science:
            filtered_df = df[filtered_df.apply(lambda row: row.astype(str).str.contains("Science", case=False).any(), axis=1)]
        if english:
            filtered_df = df[filtered_df.apply(lambda row: row.astype(str).str.contains("English", case=False).any(), axis=1)]
        if history:
            filtered_df = df[filtered_df.apply(lambda row: row.astype(str).str.contains("History", case=False).any(), axis=1)]
    
        def load_results():
            if filtered_df.empty:
                st.info("Nothing found.")
            else:
                for i, row in filtered_df.iterrows():
                    try:
                        image_bytes = base64.b64decode(row['uploaded_files'])
                        image = io.BytesIO(image_bytes)
                        tile = st.container(border=True)
                        with tile:
                            st.image(image)
                            st.markdown(f"**Subject:** {row['subject_label']}")
                            st.markdown(f"**Course:** {row['course_name']}")
                            st.markdown(f"**Unit/Topic::** {row['unit_name']}")
                            st.markdown(f"**Other labels::** {row['other_labels']}")
                    except Exception as e:
                        st.error(f"Error loading image: {e}")
        load_results()
    else:
        st.write("No existing notes")

    