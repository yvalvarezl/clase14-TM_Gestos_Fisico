import streamlit as st
import torch
import yaml
from PIL import Image

# 1. Configuración de la página
st.set_page_config(
    page_title="Detección YOLO", 
    page_icon="🎯", 
    layout="wide"
)

# 2. Estilos personalizados (Misma paleta de colores)
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

    /* Forzar color oscuro en Títulos, Etiquetas y Textos */
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
st.title("🎯 Detección de Objetos con YOLOv5")
st.write("Identificación multiclase en tiempo real a través de modelos avanzadas de visión artificial.")

st.markdown("---")

# 4. Organización en 2 columnas: Parámetros e Instrucciones
col_config, col_cam = st.columns([1, 1.2])

with col_config:
    st.markdown("""
        <div class="css-card">
            <h3>⚙️ Configuración de Detección</h3>
            <p>Ajusta los umbrales de sensibilidad para la detección de objetos.</p>
        </div>
    """, unsafe_allow_html=True)
    
    conf_threshold = st.slider("Confianza mínima", 0.0, 1.0, 0.25, 0.05)
    iou_threshold = st.slider("Umbral IoU", 0.0, 1.0, 0.45, 0.05)

with col_cam:
    st.markdown("""
        <div class="css-card">
            <h3>📸 Captura de Imagen</h3>
            <p>Toma una foto para procesarla con la red neuronal YOLOv5.</p>
        </div>
    """, unsafe_allow_html=True)
    
    img_file_buffer = st.camera_input("Capturar objeto")

# 5. Carga y ejecución del modelo YOLOv5
@st.cache_resource
def load_yolo_model():
    # Cargar modelo ligero YOLOv5s desde torch hub
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    return model

if img_file_buffer is not None:
    st.markdown("---")
    st.subheader("🔍 Resultados de la Detección")
    
    with st.spinner("Procesando imagen con YOLOv5..."):
        model = load_yolo_model()
        model.conf = conf_threshold
        model.iou = iou_threshold
        
        # Preprocesar imagen
        image = Image.open(img_file_buffer)
        
        # Ejecutar inferencia
        results = model(image)
        
        # Renderizar cajas delimitadoras sobre la imagen
        results.render()
        res_image = Image.fromarray(results.ims[0])
        
        # Mostrar resultado visual en tarjeta destacada
        col_res1, col_res2 = st.columns([1.5, 1])
        
        with col_res1:
            st.image(res_image, caption="Objetos Detectados", use_column_width=True)
            
        with col_res2:
            st.markdown("""
                <div class="css-card">
                    <h3>📊 Resumen de Detección</h3>
                </div>
            """, unsafe_allow_html=True)
            df = results.pandas().xyxy[0]
            if not df.empty:
                st.dataframe(df[['name', 'confidence']])
            else:
                st.write("No se detectaron objetos con el nivel de confianza actual.")
