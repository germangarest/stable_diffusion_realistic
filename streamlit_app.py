import streamlit as st
import requests
import base64
from io import BytesIO
from PIL import Image

# ===============================
# Opcional: Inyectar CSS personalizado para mejorar el estilo
# ===============================
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .title {
        font-size: 2.5em;
        font-weight: bold;
        color: #333333;
        text-align: center;
    }
    .prompt-display {
        background-color: #ffffff;
        border-left: 5px solid #4b4b4b;
        padding: 10px 15px;
        margin: 10px 0;
        font-size: 1.1em;
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

# ===============================
# Funciones Auxiliares
# ===============================
def decode_image(image_data):
    """
    Decodifica la imagen en base64 y retorna un objeto PIL.Image.
    """
    if image_data.startswith("data:image"):
        _, image_data = image_data.split(",", 1)
    decoded = base64.b64decode(image_data)
    return Image.open(BytesIO(decoded))

def generate_image(prompt, steps, guidance_scale, width, height):
    """
    Envía el prompt y parámetros a la API de Stable Diffusion Web UI para generar la imagen.
    """
    api_url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
    payload = {
        "prompt": prompt,
        "steps": steps,
        "cfg_scale": guidance_scale,
        "width": width,
        "height": height
    }
    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        st.error(f"Error al conectar con la API: {e}")
        return None

    data = response.json()
    if "images" in data and len(data["images"]) > 0:
        return decode_image(data["images"][0])
    else:
        st.error("La API no devolvió ninguna imagen.")
        return None

def build_prompt():
    """
    Construye el prompt en inglés a partir de las selecciones del usuario.
    """
    # Selección del tipo de escena
    scene_type = st.sidebar.selectbox(
        "Tipo de Escena",
        ["Retrato", "Paisaje", "Urbano", "Natural", "Nocturno"]
    )
    
    # Selección del estado de ánimo
    mood = st.sidebar.selectbox(
        "Estado de ánimo",
        ["sereno", "vibrante", "melancólico", "dinámico", "misterioso"]
    )
    mood_mapping = {
        "sereno": "serene",
        "vibrante": "vibrant",
        "melancólico": "melancholic",
        "dinámico": "dynamic",
        "misterioso": "mysterious"
    }
    mood_en = mood_mapping.get(mood, mood)
    
    # Selección del fondo o ambientación
    background = st.sidebar.selectbox(
        "Fondo",
        ["ciudad", "naturaleza", "interior", "atardecer", "amanecer"]
    )
    background_mapping = {
        "ciudad": "city",
        "naturaleza": "nature",
        "interior": "indoor",
        "atardecer": "sunset",
        "amanecer": "sunrise"
    }
    background_en = background_mapping.get(background, background)
    
    # Control para el nivel de detalle
    detail_level = st.sidebar.slider("Nivel de detalle (%)", min_value=10, max_value=100, value=70, step=5)
    
    # Control para la vivacidad de los colores
    colorfulness = st.sidebar.slider("Nivel de colorido (%)", min_value=10, max_value=100, value=80, step=5)
    
    # Opciones adicionales
    additional_options = st.sidebar.multiselect(
        "Elementos adicionales",
        [
            "efectos de luz",
            "composición artística",
            "iluminación dramática",
            "alta resolución",
            "detalles intrincados"
        ]
    )
    additional_options_mapping = {
        "efectos de luz": "light effects",
        "composición artística": "artistic composition",
        "iluminación dramática": "dramatic lighting",
        "alta resolución": "high resolution",
        "detalles intrincados": "intricate details"
    }
    additional_options_en = [additional_options_mapping.get(option, option) for option in additional_options]
    
    # Construcción del prompt en inglés
    prompt = (
        f"{scene_type} scene in a realistic style, {mood_en} mood, set in a {background_en} environment, "
        f"highly detailed ({detail_level}% detail), colorful ({colorfulness}% saturation)"
    )
    if additional_options_en:
        prompt += ", " + ", ".join(additional_options_en)
    prompt += ", ultra detailed, digital art"
    return prompt

# ===============================
# Interfaz de la Aplicación
# ===============================

# Título y descripción
st.markdown('<h1 class="title">RealGEN</h1>', unsafe_allow_html=True)
st.markdown("""
RealGEN es una aplicación que genera imágenes **realistas** basándose en parámetros predefinidos.
Utiliza los controles en la barra lateral para configurar tu imagen. El prompt final se genera automáticamente en inglés y se envía a la API de Stable Diffusion.
""")

# Parámetros generales de generación
steps = st.sidebar.slider("Número de pasos", min_value=10, max_value=100, value=20, step=5)
guidance_scale = st.sidebar.slider("Guidance Scale", min_value=1.0, max_value=20.0, value=7.5, step=0.5)
width = st.sidebar.selectbox("Ancho (px)", [256, 384, 512, 640, 768, 1024], index=2)
height = st.sidebar.selectbox("Alto (px)", [256, 384, 512, 640, 768, 1024], index=2)

# Construir y mostrar el prompt generado (dentro de un expander para no saturar la vista)
prompt = build_prompt()
with st.expander("Ver prompt generado"):
    st.markdown(f'<div class="prompt-display">{prompt}</div>', unsafe_allow_html=True)

# Botón para generar la imagen
if st.button("Generar Imagen"):
    st.info("Generando imagen, por favor espere...")
    generated_image = generate_image(prompt, steps, guidance_scale, width, height)
    if generated_image:
        st.image(generated_image, caption="Imagen generada", use_column_width=True)
