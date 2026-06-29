import streamlit as st
import base64


def aplicar_estilo():

    with open("assets/logo_psl.png", "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    css = f"""
    <style>

    .stApp {{
        background-color: #0E1117;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        top: 50%;
        left: 50%;
        width: 700px;
        height: 700px;
        transform: translate(-50%, -50%);
        background-image: url("data:image/png;base64,{encoded}");
        background-repeat: no-repeat;
        background-position: center;
        background-size: contain;
        opacity: 0.08;
        pointer-events: none;
        z-index: 0;
    }}

    [data-testid="stAppViewContainer"] > .main {{
        position: relative;
        z-index: 1;
    }}

    </style>
    """

    st.markdown(css, unsafe_allow_html=True)