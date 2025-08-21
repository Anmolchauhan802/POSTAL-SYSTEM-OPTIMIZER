import streamlit as st
import re

def parse_address(address):
    pin_match = re.search(r"\b\d{6}\b", address)
    pin_code = pin_match.group() if pin_match else "Not found"

    lines = address.split(",")
    name = lines[0].strip() if len(lines) >= 1 else "Unknown"
    street = lines[1].strip() if len(lines) >= 2 else "Unknown"
    city = lines[2].strip() if len(lines) >= 3 else "Unknown"

    return {
        "Name": name,
        "Street": street,
        "City": city,
        "PIN Code": pin_code
    }

def app():
    st.title("📬 Address Parsing")
    st.write("Enter an address to parse and extract components.")

    address = st.text_area("Enter Full Address (name, street, city, pincode):")

    if address:
        parsed = parse_address(address)
        st.subheader("🧾 Parsed Address")
        for key, value in parsed.items():
            st.write(f"**{key}:** {value}")
