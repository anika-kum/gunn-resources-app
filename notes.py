import streamlit as st
import pandas as pd
from io import StringIO

def show_notes():
    #variables
    options = ["science", "math", "english", "art", "cs"]
    images = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlVTWL4dqk9ZokaiRQe0kdV3_dNvkB7A3xTw&s", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrfqqNGW1yUTzEtl3OsyaP_X9zHGaLVI_S9A&s", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXZ8ORCFOkes_5zSVPN14Pj_AvxZuguzoizQ&s"]
    numPics = 0
    numCols = 3
    cols = st.columns(numCols)
    uploadedImages = []

    def update_Images(numPics, x):
        colLocation = index
        for i in range(x):
            st.image(uploadedImages[numPics + i])
        numPics += x
        """
        for i, x in enumerate(cols):
            x.image(image = images[i], caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto", use_container_width=False)
            x.image(uploadedImages[i])
        """

    st.title("Notes")

    with st.form("maform"):
        uploadedFiles = st.file_uploader("Image File")
        submitted = st.form_submit_button("Upload")
    if submitted:
        if uploadedFiles is not None:
            if isinstance(uploadedFiles, list):
                st.write("In progress!")
            else:
                bytes_data = uploadedFiles.getvalue()

                stringio = StringIO(uploadedFiles.getvalue().decode("latin-1"))
                string_data = stringio.read()
                uploadedImages.append(uploadedFiles)
                update_Images(numPics,1)




