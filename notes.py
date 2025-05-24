import streamlit as st
import os
import csv
import pandas as pd
import base64
import io

CSV_PATH = "notes_data.csv"

def initialize_csv():
    if not os.path.exists(CSV_PATH) or os.path.getsize(CSV_PATH) == 0:
        with open(CSV_PATH, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(['uploaded_files', 'subject_label'])
            
def save_item_to_csv(item_data):
    encoded_img = base64.b64encode(item_data[0]).decode("utf-8")
    with open(CSV_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([encoded_img, item_data[1]])

def load_items_from_csv():
    if os.path.exists(CSV_PATH):
        return pd.read_csv(CSV_PATH)
    else:
        return pd.DataFrame(columns=['uploaded_files', 'subject_label'])

# Display previously uploaded notes
def load_data():
    df = load_items_from_csv()
    if df.empty:
        st.info("Nothing available yet.")
    else:
        for i, row in df.iterrows():
            try:
                image_bytes = base64.b64decode(row['uploaded_files'])
                image = io.BytesIO(image_bytes)
                tile = st.container(height=300)
                with tile:
                    st.image(image)
                    st.markdown(f"**Subject:** {row['subject_label']}")
            except Exception as e:
                st.error(f"Error loading image: {e}")

# Main app function
def show_notes():
    initialize_csv()
    st.title("Notes")

    # Upload form
    with st.form("maform"):
        uploaded_file = st.file_uploader("Image File", type=["png", "jpg", "jpeg"])
        subject_label = st.selectbox("Select subject", ["Math", "Science", "English", "History"])
        submitted = st.form_submit_button("Upload")

        if submitted:
            if uploaded_file is not None:
                bytes_data = uploaded_file.read()
                note_data = [bytes_data, subject_label]
                save_item_to_csv(note_data)
                st.success("Note uploaded successfully!")
            else:
                st.warning("Please upload a file.")
    load_data()

# Run the app
if __name__ == "__main__":
    show_notes()
