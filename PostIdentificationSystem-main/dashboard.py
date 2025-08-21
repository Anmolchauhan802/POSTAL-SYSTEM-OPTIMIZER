import streamlit as st
import pandas as pd

def render_dashboard():
    st.markdown("""
        <style>
        body {background-color: #121212;}
        h1, h2, h3, p, div {color: white;}
        .stButton>button {
            background-color: #02ab21;
            color: white;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #55C667;
            color: white;
        }
        .dashboard-box {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("📊 Nangara Postal Dashboard")

    st.markdown("<div class='dashboard-box'>", unsafe_allow_html=True)
    st.subheader("Total Parcels Processed:")
    st.metric(label="Parcels", value="12,543")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='dashboard-box'>", unsafe_allow_html=True)
    st.subheader("Failed PIN Code Detections:")
    st.metric(label="Failures", value="142")
    st.markdown("</div>", unsafe_allow_html=True)

    # Example DataTable (optional)
    st.markdown("<div class='dashboard-box'>", unsafe_allow_html=True)
    st.subheader("Recent Logs")
    data = {
        "Date": ["2025-04-13", "2025-04-12", "2025-04-11"],
        "Parcels Processed": [412, 398, 453],
        "PIN Errors": [5, 2, 4],
    }
    df = pd.DataFrame(data)
    st.dataframe(df)
    st.markdown("</div>", unsafe_allow_html=True)
