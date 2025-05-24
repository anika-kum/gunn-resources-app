# import streamlit as st
# import pandas as pd

# for key in ['item_names', 'people_names', 'item_descriptions', 'item_photos', 'rent_or_buy', 'item_prices']:
#     if key not in st.session_state:
#         st.session_state[key] = []

# def show_rent():
#     st.title("Renting and buying tools")
#     add_button = st.button("Add product for rent or buy")
#     if add_button:
#         st.session_state['show_form'] = True
#     if st.session_state.get('show_form'):
#         addItemForm()
#     st.write(st.session_state['item_names'])
    
# def addItemForm():
#     with st.form("Add Item"):
#         title = st.text_input("Item name")
#         name = st.text_input("Your name")
#         description = st.text_input("Describe what would you like to rent or sell. What condition is it in?")
#         photo = st.text_input("Upload a picture, if you'd like (Optional)")
#         add_selectbox = st.selectbox(
#         "Would you like your product to be rented or bought?",
#         ("Rent", "Buy"))
#         if add_selectbox == "Rent":
#             price = st.text_input("How many dollars/hour or dollars/day would you like?")
#         else:
#             price = st.text_input("For how much would you like to sell your product?")
#         submitted = st.form_submit_button("Click here to finish and upload your product to the website!")
#         if submitted:
#             st.session_state['item_names'].append(title)
#             st.session_state['people_names'].append(name)
#             st.session_state['item_descriptions'].append(description)
#             if photo != '':
#                 st.session_state['item_photos'].append(photo)
#             st.session_state['rent_or_buy'].append(add_selectbox)
#             st.session_state['item_prices'].append(price)

import streamlit as st
import os
import csv
import pandas as pd

# CSV file path
CSV_PATH = "items_data.csv"

def initialize_csv():
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(['item_name', 'person_name', 'description', 'photo_url', 'rent_or_buy', 'price'])

def save_item_to_csv(item_data):
    with open(CSV_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(item_data)

def load_items_from_csv():
    if os.path.exists(CSV_PATH):
        return pd.read_csv(CSV_PATH)
    else:
        return pd.DataFrame(columns=['item_name', 'person_name', 'description', 'photo_url', 'rent_or_buy', 'price'])

def show_rent():
    st.title("Renting and buying tools")

    add_button = st.button("Add product for rent or buy")
    if add_button:
        st.session_state['show_form'] = True
    if st.session_state.get('show_form'):
        add_item_form()
    
    # Initialize CSV file once
    initialize_csv()
    
def add_item_form():
     # Input form
    with st.form("item_form"):
        item_name = st.text_input("Item Name")
        person_name = st.text_input("Your Name and Contact Information")
        description = st.text_area("Description (condition, etc.)")
        photo_url = st.text_input("Photo URL (optional)")
        rent_or_buy = st.selectbox("Rent or Buy", ["Rent", "Buy"])
        price = st.number_input("Price", min_value=0.0, step=0.01, format="%.2f")

        submitted = st.form_submit_button("Submit")

        if submitted:
            if not item_name or not person_name or not description or not price:
                st.error("Please fill in all required fields (Item Name, Person Name, Description, Price).")
            else:
                # Save to CSV
                item_data = [item_name, person_name, description, photo_url, rent_or_buy, price]
                save_item_to_csv(item_data)
                st.success(f"Item '{item_name}' successfully uploaded to the website!")