import pandas as pd
import streamlit as st

def show_notes():
    st.title("Notes")

    uploadedImages = []

    uploaded_files = st.file_uploader(label="Upload Notes Here!", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
    
    if uploaded_files is not None:
        if isinstance(uploaded_files, list):
            for uploaded_file in uploaded_files:
                 # To convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                st.write(stringio)

                # To read file as string:
                string_data = stringio.read()
                st.write(string_data)
            else:
                # To convert to a string based IO:
                    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                    st.write(stringio)

                    # To read file as string:
                    string_data = stringio.read()
                    st.write(string_data)


                

    options = ["science", "math", "english", "art", "cs"]
    images = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlVTWL4dqk9ZokaiRQe0kdV3_dNvkB7A3xTw&s", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrfqqNGW1yUTzEtl3OsyaP_X9zHGaLVI_S9A&s", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXZ8ORCFOkes_5zSVPN14Pj_AvxZuguzoizQ&s"]

    numCols = 3
    cols = st.columns(numCols)
    for i, x in enumerate(cols):
        x.image(image = images[i], caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto", use_container_width=False)

