import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageOps
import keras

# 1. Configuración de la página
st.set_page_config(
    page_title="Reconocimiento de Gestos", 
    page_icon="📷", 
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
st.title("📷 Reconocimiento de Gestos con IA")
st.write("Identifica patrones y gestos en tiempo real mediante el modelo de Teachable Machine.")

st.markdown("---")

# 4. Organización en 2 columnas: Instrucciones a la izquierda, Cámara a la derecha
col_info, col_cam = st.columns([1, 1.2])

with col_info:
    st.markdown("""
        <div class="css-card">
            <h3>✨ Instrucciones de uso</h3>
            <p>1. Activa o toma una captura usando la cámara de la derecha.</p>
            <p>2. El sistema evaluará el gesto detectado con el archivo <code>keras_model.h5</code>.</p>
            <p>3. El resultado y la probabilidad se mostrarán inmediatamente abajo.</p>
        </div>
    """, unsafe_allow_html=True)

with col_cam:
    st.subheader("Captura de Imagen")
    img_file_buffer = st.camera_input("Toma una Foto para evaluar el gesto")

# 5. Procesamiento del modelo de clasificación
if img_file_buffer is not None:
    # Desactivar compilación del modelo para carga rápida
    model = keras.models.load_model('keras_model.h5', compile=False)
    
    # Cargar etiquetas
    with open('labels.txt', 'r') as f:
        class_names = f.readlines()

    # Preprocesar la imagen
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
    
    # Mostrar resultados en tarjetas destacadas
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.markdown(f"""
            <div class="css-card">
                <h3>🎯 Gesto Detectado</h3>
                <h2 style="color: #8C3A4D !important;">{class_name}</h2>
            </div>
        """, unsafe_allow_html=True)
    
    with res_col2:
        st.markdown(f"""
            <div class="css-card">
                <h3>📊 Nivel de Confianza</h3>
                <h2 style="color: #8C3A4D !important;">{confidence_score * 100:.1f}%</h2>
            </div>
        """, unsafe_allow_html=True)
