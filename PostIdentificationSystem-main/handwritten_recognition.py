import streamlit as st
from PIL import Image
import numpy as np
import re
from paddleocr import PaddleOCR

# Load PaddleOCR once
@st.cache_resource
def load_paddle_ocr():
    ocr = PaddleOCR(use_angle_cls=True, lang='en')
    return ocr

# Extract text from image using PaddleOCR
def extract_text_from_image(image, ocr):
    image = np.array(image.convert("RGB"))
    result = ocr.ocr(image, cls=True)
    lines = [line[1][0] for line in result[0]]
    return lines

# Extract address-looking lines from text
def extract_address_parts(text_lines):
    address_lines = []
    for line in text_lines:
        if (
            re.search(r"\d{5,6}", line) or   # Pincode
            re.search(r"\d+[-/][\dA-Z]+", line) or  # House No.
            re.search(r"(HYDERABAD|PUNJAB|BLOCK)", line.upper())
        ):
            address_lines.append(line)
    return address_lines

# Streamlit app
def app():
    st.title("📬 Handwritten Address Extractor (PaddleOCR)")

    uploaded_image = st.file_uploader("Upload handwritten image", type=["png", "jpg", "jpeg"])

    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        with st.spinner("🔍 Running PaddleOCR..."):
            ocr = load_paddle_ocr()
            all_lines = extract_text_from_image(image, ocr)
            address_lines = extract_address_parts(all_lines)

        st.subheader("🏷️ Detected Address Lines:")
        if address_lines:
            for line in address_lines:
                st.success(line)
        else:
            st.warning("⚠️ Couldn't extract any address-like text.")

        st.subheader("🧾 All Extracted Text:")
        for line in all_lines:
            st.code(line)

if __name__ == "__main__":
    app()
