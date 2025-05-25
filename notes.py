import streamlit as st
import os
import csv
import pandas as pd
import base64
import io

CSV_PATH = "notes_data.csv"
CSV_RATING_PATH = "ratings.csv"

with open('styles.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)



def initialize_csv():
    if not os.path.exists(CSV_PATH) or os.path.getsize(CSV_PATH) == 0:
        with open(CSV_PATH, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(['uploaded_files', 'subject_label', 'person_name', 'course_name', 'unit_name', 'other_labels'])
            
def save_item_to_csv(item_data):
    encoded_img = base64.b64encode(item_data[0]).decode("utf-8")
    with open(CSV_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([encoded_img, item_data[1], item_data[2], item_data[3], item_data[4], item_data[5]])

def load_items_from_csv():
    if os.path.exists(CSV_PATH):
        return pd.read_csv(CSV_PATH)
    else:
        return pd.DataFrame(columns=['uploaded_files', 'subject_label', 'person_name', 'course_name', 'unit_name', 'other_labels'])

def initialize_csv_rating():
    if not os.path.exists(CSV_RATING_PATH) or os.path.getsize(CSV_RATING_PATH) == 0:
        with open(CSV_RATING_PATH, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(['person_name', 'ranking'])
            
def save_item_to_csv_rating(item_data):
    with open(CSV_RATING_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(item_data)

def load_items_from_csv_rating():
    if os.path.exists(CSV_RATING_PATH):
        return pd.read_csv(CSV_RATING_PATH)
    else:
        return pd.DataFrame(columns=['person_name', 'ranking'])

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
                tile = st.container(border=True)
                with tile:
                    selected = st.feedback("stars",key=f"feedback_{i}")
                    if selected is not None:
                        save_item_to_csv_rating([row['person_name'], selected+1])
                    st.image(image)
                    st.markdown(f"**Subject:** {row['subject_label']}")
                    st.markdown(f"**Uploaded by:** {row['person_name']}")
                    st.markdown(f"**Course:** {row['course_name']}")
                    st.markdown(f"**Unit/Topic:** {row['unit_name']}")
                    st.markdown(f"**Other labels:** {row['other_labels']}")
            except Exception as e:
                st.error(f"Error loading image: {e}")

# Main app function
def show_notes():
    st.title("Notes")
    add_button = st.button("Add your notes from classes")
    if add_button:
        st.session_state['show_form'] = True
    if st.session_state.get('show_form'):
        add_item_form()
    initialize_csv()
    initialize_csv_rating()
    load_data()

def add_item_form():
    with st.form("maform"):
        uploaded_file = st.file_uploader("Image File", type=["png", "jpg", "jpeg"])
        subject_label = st.selectbox("Select subject", ["Math", "Science", "English", "History"])
        person_name = st.text_input("Your name")
        course_name = st.text_input("Name of Unit/Topic these notes are for")
        unit_name = st.text_input("Name of Course")
        other_labels = st.text_input("Any other labels you think would be useful")
        submitted = st.form_submit_button("Upload")

        if submitted:
            if uploaded_file is not None:
                bytes_data = uploaded_file.read()
                note_data = [bytes_data, subject_label, person_name, course_name, unit_name, other_labels]
            else:
                st.warning("Please upload a file.")
            if not subject_label or not course_name or not unit_name or not person_name:
                st.error("Please fill in all required fields (Subject, Your Name, Course Name, Unit/Topic).")
            else:
                save_item_to_csv(note_data)
                st.success("Note uploaded successfully!")


# Run the app
if __name__ == "__main__":
    show_notes()
