import streamlit as st
import keras
from PIL import Image, ImageOps
import numpy as np

# 1. Configuración de la página
st.set_page_config(
    page_title="Cerradura Inteligente", 
    page_icon="🔐", 
    layout="wide"
)

# 2. Estilos personalizados (Misma paleta de colores que Inicio.py)
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

    /* Forzar color oscuro en Títulos y Textos */
    h1, h2, h3, h4, h5, h6, span, p, label {
        color: #3D2B32 !important;
    }

    /* Estilo de botones */
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

    /* Tarjetas de contenido con borde rosado */
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

# 3. Encabezado principal
st.title("🔐 Control de Cerradura Inteligente")
st.write("Verificación de acceso presencial en tiempo real para control de apertura o cierre de puertas.")

st.markdown("---")

# 4. Organización en 2 columnas: Instrucciones y Cámara
col_info, col_cam = st.columns([1, 1.2])

with col_info:
    st.markdown("""
        <div class="css-card">
            <h3>✨ Control de Acceso Visual</h3>
            <p>1. Ubícate frente a la cámara web.</p>
            <p>2. Toma una foto para validar tu identidad con el modelo de Keras.</p>
            <p>3. Si el sistema detecta a <b>Carlos</b>, concederá el acceso y abrirá la cerradura.</p>
            <p>4. Si no detecta presencia autorizada, la cerradura se mantendrá bloqueada.</p>
        </div>
    """, unsafe_allow_html=True)

with col_cam:
    st.markdown("""
        <div class="css-card">
            <h3>📸 Captura de Verificación</h3>
        </div>
    """, unsafe_allow_html=True)
    img_file_buffer = st.camera_input("Capturar rostro para verificación")

# 5. Procesamiento del modelo de Teachable Machine
if img_file_buffer is not None:
    # Cargar el modelo guardado en el repositorio
    model = keras.models.load_model('keras_model.h5', compile=False)
    
    # Cargar etiquetas (labels.txt)
    with open('labels.txt', 'r') as f:
        class_names = f.readlines()

    # Preprocesar imagen para Keras (224x224)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(img_file_buffer)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    # Predicción
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = float(prediction[0][index])

    st.markdown("---")
    
    # 6. Evaluación de la etiqueta para conceder o denegar acceso
    res_col1, res_col2 = st.columns(2)
    
    # Si la clase es "0 Carlos" (o contiene Carlos)
    if "0 Carlos" in class_name or "Carlos" in class_name:
        with res_col1:
            st.markdown("""
                <div class="css-card" style="border-color: #4CAF50 !important;">
                    <h3 style="color: #2E7D32 !important;">🔓 Estado del Acceso</h3>
                    <h2 style="color: #2E7D32 !important;">Acceso Concedido</h2>
                    <p>Usuario autorizado identificado.</p>
                </div>
            """, unsafe_allow_html=True)
        with res_col2:
            st.markdown(f"""
                <div class="css-card">
                    <h3>🟢 Acción del Servomotor</h3>
                    <h2 style="color: #8C3A4D !important;">Abriendo Puerta...</h2>
                    <p>Confianza: <b>{confidence_score * 100:.1f}%</b></p>
                </div>
            """, unsafe_allow_html=True)
    else:
        with res_col1:
            st.markdown("""
                <div class="css-card" style="border-color: #E53935 !important;">
                    <h3 style="color: #C62828 !important;">🔒 Estado del Acceso</h3>
                    <h2 style="color: #C62828 !important;">Acceso Denegado</h2>
                    <p>Sin presencia autorizada.</p>
                </div>
            """, unsafe_allow_html=True)
        with res_col2:
            st.markdown(f"""
                <div class="css-card">
                    <h3>🔴 Acción del Servomotor</h3>
                    <h2 style="color: #8C3A4D !important;">Cerrando Puerta...</h2>
                    <p>Confianza: <b>{confidence_score * 100:.1f}%</b></p>
                </div>
            """, unsafe_allow_html=True)
