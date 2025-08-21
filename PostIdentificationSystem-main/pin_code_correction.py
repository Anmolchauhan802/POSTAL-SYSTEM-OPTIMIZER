import streamlit as st

def app():
    st.title("Validate Pincode")
    st.write("This module will check if the entered PIN code is valid.")
    
    pincode = st.text_input("Enter PIN code:")
    if pincode:
        if len(pincode) == 6 and pincode.isdigit():
            st.success("Valid PIN code format.")
        else:
            st.error("Invalid PIN code.")
