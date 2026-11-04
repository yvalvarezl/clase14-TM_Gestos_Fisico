import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="Mi App Multimodal", 
    page_icon="✨", 
    layout="wide"
)

# 2. Estilos personalizados (CSS con texto visible)
st.markdown("""
    <style>
    /* Fondo principal */
    .stApp {
        background-color: #FAF5F8;
    }
    /* Barra lateral */
    [data-testid="stSidebar"] {
        background-color: #F3E8EE;
    }
    /* Estilo de botones */
    .stButton>button {
        background-color: #E8B4B8;
        color: #2D2D2D !important;
        border-radius: 12px;
        border: none;
        font-weight: bold;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #D89BA2;
        color: white !important;
    }
    /* Tarjetas de contenido y texto oscuro */
    .css-card {
        background-color: #FFFFFF;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);
        margin-bottom: 1rem;
        border: 1px solid #E8B4B8;
    }
    .css-card h3 {
        color: #2D2D2D !important;
        margin-bottom: 0.5rem;
    }
    .css-card p {
        color: #4A4A4A !important;
        font-size: 0.95rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Contenido visible de la página principal
st.title("✨ Centro de Control Multimodal")
st.subheader("Bienvenida a la plataforma de interacción ciberfísica")
st.write("Selecciona una de las opciones en la barra lateral para comenzar la navegación.")

st.markdown("---")

# Organización en columnas para las secciones
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="css-card">
            <h3>📷 Reconocimiento de Gestos</h3>
            <p>Modelos de visión por computador (Teachable Machine) para la interacción directa y control de actuadores físicos.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Explorar Teachable Machine"):
        st.write("Usa el menú lateral para abrir la página del modelo.")

with col2:
    st.markdown("""
        <div class="css-card">
            <h3>🎯 Detección de Objetos (YOLO)</h3>
            <p>Análisis en tiempo real y clasificación visual multiclase para entornos adaptativos.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Explorar YOLO"):
        st.write("Usa el menú lateral para abrir la página de YOLO.")
