import streamlit as st
import pandas as pd

for key in ['item_names', 'people_names', 'item_descriptions', 'item_photos', 'rent_or_buy', 'item_prices']:
    if key not in st.session_state:
        st.session_state[key] = []

def show_rent():
    st.title("Renting and buying tools")
    add_button = st.button("Add product for rent or buy")
    if add_button:
        st.session_state['show_form'] = True
    if st.session_state.get('show_form'):
        addItemForm()
    st.write(st.session_state['item_names'])
    
def addItemForm():
    with st.form("Add Item"):
        title = st.text_input("Item name")
        name = st.text_input("Your name")
        description = st.text_input("Describe what would you like to rent or sell. What condition is it in?")
        photo = st.text_input("Upload a picture, if you'd like (Optional)")
        add_selectbox = st.selectbox(
        "Would you like your product to be rented or bought?",
        ("Rent", "Buy"))
        if add_selectbox == "Rent":
            price = st.text_input("How many dollars/hour or dollars/day would you like?")
        else:
            price = st.text_input("For how much would you like to sell your product?")
        submitted = st.form_submit_button("Click here to finish and upload your product to the website!")
        if submitted:
            st.write(st.session_state['item_names'].append(title))
            st.write(st.session_state['people_names'].append(name))
            st.write(st.session_state['item_descriptions'].append(description))
            if photo != '':
                st.write(st.session_state['item_photos'].append(photo))
            st.write(st.session_state['rent_or_buy'].append(add_selectbox))
            st.write(st.session_state['item_prices'].append(price))

