import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="Mi App Multimodal", 
    page_icon="✨", 
    layout="wide"
)

# 2. Estilos personalizados (CSS con rosados oscuros y texto legible)
st.markdown("""
    <style>
    /* Fondo principal */
    .stApp {
        background-color: #FAF4F6 !important;
    }
    
    /* Barra lateral */
    [data-testid="stSidebar"] {
        background-color: #F0E0E6 !important;
    }

    /* Forzar color oscuro en Títulos y Subtítulos de Streamlit */
    h1, h2, h3, h4, h5, h6, span, p, label {
        color: #3D2B32 !important;
    }

    /* Estilo de botones (Rosado más oscuro y llamativo) */
    .stButton>button {
        background-color: #D88A96 !important;
        color: #FFFFFF !important;
        border-radius: 12px !important;
        border: none !important;
        font-weight: bold !important;
        padding: 0.6rem 1.2rem !important;
    }
    .stButton>button:hover {
        background-color: #C46D7B !important;
        color: #FFFFFF !important;
        box-shadow: 0px 4px 12px rgba(196, 109, 123, 0.4) !important;
    }

    /* Tarjetas de contenido con borde rosado oscuro */
    .css-card {
        background-color: #FFFFFF !important;
        padding: 1.5rem !important;
        border-radius: 15px !important;
        box-shadow: 0px 4px 12px rgba(180, 100, 120, 0.12) !important;
        margin-bottom: 1rem !important;
        border: 2px solid #D88A96 !important;
    }
    .css-card h3 {
        color: #8C3A4D !important;
        margin-bottom: 0.5rem !important;
    }
    .css-card p {
        color: #4A3A40 !important;
        font-size: 0.95rem !important;
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
