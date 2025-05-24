import streamlit as st
import os
import csv
import pandas as pd
import base64
import io


# CSV file path
CSV_PATH = "items_data.csv"

def initialize_csv():
    if not os.path.exists(CSV_PATH) or os.path.getsize(CSV_PATH) == 0:
        with open(CSV_PATH, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(['item_name', 'person_name', 'description', 'photo_url', 'rent_or_buy', 'price'])

def save_item_to_csv(item_data):
    photo_file = item_data[3]
    if photo_file is not None:
        photo_bytes = photo_file.read()
        encoded_img = base64.b64encode(photo_bytes).decode("utf-8")
    else:
        encoded_img = ""

    with open(CSV_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            item_data[0],  # item_name
            item_data[1],  # person_name
            item_data[2],  # description
            encoded_img,   # base64 image string
            item_data[4],  # rent_or_buy
            item_data[5],  # price
        ])



def load_items_from_csv():
    if os.path.exists(CSV_PATH):
        return pd.read_csv(CSV_PATH)
    else:
        return pd.DataFrame(columns=['item_name', 'person_name', 'description', 'photo_url', 'rent_or_buy', 'price'])

def show_rent():
    st.title("Renting and buying tools")
    load_data()
    add_button = st.button("Add product for rent or buy")
    if add_button:
        st.session_state['show_form'] = True
    if st.session_state.get('show_form'):
        add_item_form()
    
    initialize_csv()
    
def add_item_form():
    with st.form("item_form"):
        item_name = st.text_input("Item Name")
        person_name = st.text_input("Your Name and Contact Information")
        description = st.text_area("Description (condition, etc.)")
        photo_url = st.file_uploader("Image File", type=["png", "jpg", "jpeg"])
        rent_or_buy = st.selectbox("Rent or Buy", ["Rent", "Buy"])
        price = st.number_input("Price (in USD)", min_value=0.0, step=1, format="%.2f")

        submitted = st.form_submit_button("Submit")

        if submitted:
            if not item_name or not person_name or not description or not price:
                st.error("Please fill in all required fields (Item Name, Person Name, Description, Price).")
            else:
                # Save to CSV
                item_data = [item_name, person_name, description, photo_url, rent_or_buy, price]
                save_item_to_csv(item_data)
                st.success(f"Thanks {person_name}, your {item_name} successfully uploaded to the website!")

def load_data():
    df = load_items_from_csv()
    if df.empty:
        st.info("Nothing available yet.")
    else:
        for i, row in df.iterrows():
            tile = st.container()
            with tile:
                st.markdown(f"**Item Name:** {row['item_name']}")
                st.markdown(f"**Sold by:** {row['person_name']}")
                st.markdown(f"**Description:** {row['description']}")
                st.markdown(f"**For:** {row['rent_or_buy']}")
                st.markdown(f"**Price:** ${row['price']:.2f}")

                try:
                    if isinstance(row['photo_url'], str) and row['photo_url'].strip() != "":
                        image_bytes = base64.b64decode(row['photo_url'])
                        image = io.BytesIO(image_bytes)
                        st.markdown("**Photo (if available):**")
                        st.image(image)
                except Exception as e:
                    st.error(f"Error loading image: {e}")
