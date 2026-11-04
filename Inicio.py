import streamlit as st

# Configuración de página
st.set_page_config(page_title="Mi App Multimodal", page_icon="✨", layout="wide")

# Estilos personalizados
st.markdown("""
    <style>
    /* Fondo principal */
    .stApp {
        background-color: #FAF5F8;
    }
    /* Estilo de la barra lateral */
    [data-testid="stSidebar"] {
        background-color: #F3E8EE;
    }
    /* Botones primarios */
    .stButton>button {
        background-color: #E8B4B8;
        color: #2D2D2D;
        border-radius: 12px;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #D89BA2;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)
