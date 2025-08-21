import streamlit as st

def home_page():
    st.markdown("""
        <style>
        .title {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            color: white;
            margin-top: 20px;
        }

        .validate-button > button {
            background-color: #02ab21;
            color: white;
            border-radius: 8px;
            height: 3em;
            width: 12em;
            font-weight: bold;
        }

        .validate-button > button:hover {
            background-color: #55C667;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    # Centered row with image and button
    col1, col2 = st.columns([1.5, 1])

    with col1:
        st.image(r"postal.png", use_container_width=True)


    with col2:
        st.markdown("<div class='title'>Welcome to the Indian Postal System Optimizer</div>", unsafe_allow_html=True)
        st.markdown("###")
        st.markdown("###")
        st.markdown("###")
        if st.button("Validate Pincode", key="validate_btn", help="Start the Pincode Validation"):
            return "validate"

    return "home"
