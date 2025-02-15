import streamlit as st
import requests
import base64
from io import BytesIO
from PIL import Image

# ===============================
# Control de Acceso por Contraseña utilizando session_state y contenedor dinámico
# ===============================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    password_container = st.empty()
    password = password_container.text_input("Ingrese la contraseña para acceder", type="password")
    
    if password:
        if password == "AlanTuring2025":
            st.session_state.authenticated = True
            password_container.empty()
        else:
            st.error("Contraseña incorrecta. Acceso denegado.")
            st.stop()
    else:
        st.warning("Por favor, ingrese la contraseña para continuar.")
        st.stop()

# ===============================
# CSS personalizado para mejorar el estilo
# ===============================
st.markdown("""
    <style>
    body {
        background: linear-gradient(45deg, #f0f2f6, #ffffff);
    }
    .title {
        font-size: 2.8em;
        font-weight: bold;
        color: #333333;
        text-align: center;
        margin-bottom: 20px;
    }
    .prompt-display {
        background-color: #ffffff;
        border-left: 5px solid #4b4b4b;
        padding: 10px 15px;
        margin: 10px 0;
        font-size: 1.1em;
        color: #333333;
    }
    .image-container {
        text-align: center;
        margin-top: 20px;
    }
    button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 10px 20px;
        margin: 10px;
        cursor: pointer;
        font-size: 1em;
    }
    button:hover {
        background-color: #45a049;
    }
    .download-button {
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ===============================
# Bandera para bloquear interacciones mientras se genera la imagen
# ===============================
if "is_generating" not in st.session_state:
    st.session_state.is_generating = False

# Variable para controlar si los widgets deben estar deshabilitados
is_generating = st.session_state.is_generating

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
    disabled_flag = st.session_state.get("is_generating", False)
    
    scene_type = st.sidebar.selectbox(
        "Tipo de Escena",
        ["Retrato", "Paisaje", "Urbano", "Natural", "Nocturno"],
        disabled=disabled_flag
    )
    
    mood = st.sidebar.selectbox(
        "Estado de ánimo",
        ["sereno", "vibrante", "melancólico", "dinámico", "misterioso"],
        disabled=disabled_flag
    )
    mood_mapping = {
        "sereno": "serene",
        "vibrante": "vibrant",
        "melancólico": "melancholic",
        "dinámico": "dynamic",
        "misterioso": "mysterious"
    }
    mood_en = mood_mapping.get(mood, mood)
    
    background = st.sidebar.selectbox(
        "Fondo",
        ["ciudad", "naturaleza", "interior", "atardecer", "amanecer"],
        disabled=disabled_flag
    )
    background_mapping = {
        "ciudad": "city",
        "naturaleza": "nature",
        "interior": "indoor",
        "atardecer": "sunset",
        "amanecer": "sunrise"
    }
    background_en = background_mapping.get(background, background)
    
    detail_level = st.sidebar.slider(
        "Nivel de detalle (%)",
        min_value=10, max_value=100, value=70, step=5,
        disabled=disabled_flag
    )
    
    colorfulness = st.sidebar.slider(
        "Nivel de colorido (%)",
        min_value=10, max_value=100, value=80, step=5,
        disabled=disabled_flag
    )
    
    additional_options = st.sidebar.multiselect(
        "Elementos adicionales",
        ["efectos de luz", "composición artística", "iluminación dramática", "alta resolución", "detalles intrincados"],
        disabled=disabled_flag
    )
    additional_options_mapping = {
        "efectos de luz": "light effects",
        "composición artística": "artistic composition",
        "iluminación dramática": "dramatic lighting",
        "alta resolución": "high resolution",
        "detalles intrincados": "intricate details"
    }
    additional_options_en = [additional_options_mapping.get(option, option) for option in additional_options]
    
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
st.markdown('<h1 class="title">RealGEN</h1>', unsafe_allow_html=True)
st.markdown("""
RealGEN es una aplicación que genera imágenes **realistas** basándose en parámetros predefinidos.
Utiliza los controles en la barra lateral para configurar tu imagen. El prompt final se genera automáticamente en inglés y se envía a la API de Stable Diffusion.
""")

# ===============================
# Parámetros generales de generación con ajustes de baja potencia
# ===============================
st.sidebar.info("Parámetros de baja potencia (para generación en 1 minuto y 30 segundos): 5 pasos y resolución 512x512. Puedes modificarlos si lo deseas.")
steps = st.sidebar.slider("Número de pasos", min_value=1, max_value=30, value=5, step=1, disabled=is_generating)
guidance_scale = st.sidebar.slider("Guidance Scale", min_value=1.0, max_value=20.0, value=7.5, step=0.5, disabled=is_generating)
width = st.sidebar.selectbox("Ancho (px)", [256, 384, 512, 640, 768, 1024], index=2, disabled=is_generating)
height = st.sidebar.selectbox("Alto (px)", [256, 384, 512, 640, 768, 1024], index=2, disabled=is_generating)

# Construir y mostrar el prompt generado (dentro de un expander para no saturar la vista)
prompt = build_prompt()
with st.expander("Ver prompt generado"):
    st.markdown(f'<div class="prompt-display">{prompt}</div>', unsafe_allow_html=True)

# Botón para generar la imagen (deshabilitado mientras se está generando)
if st.button("Generar Imagen", disabled=is_generating):
    st.session_state.is_generating = True  # Bloquea nuevas peticiones
    with st.spinner("Generando imagen, por favor espere..."):
        generated_image = generate_image(prompt, steps, guidance_scale, width, height)
    st.session_state.is_generating = False  # Permite nuevas peticiones una vez finalizada la generación
    if generated_image:
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image(generated_image, caption="Imagen generada", use_container_width=True)
        buffer = BytesIO()
        generated_image.save(buffer, format="PNG")
        byte_data = buffer.getvalue()
        st.download_button(
            label="Descargar Imagen",
            data=byte_data,
            file_name="RealGEN.png",
            mime="image/png",
            key="download-btn"
        )
        st.markdown('</div>', unsafe_allow_html=True)
