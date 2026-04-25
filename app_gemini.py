import streamlit as st
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from st_social_media_links import SocialMediaIcons

# Cargar API Key
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
API_KEY = os.getenv('GEMINI_API_KEY')

if not API_KEY:
    st.error('❗ No se encontró GEMINI_API_KEY en .env')
    st.stop()

# Inicializar cliente de Gemini
client = genai.Client(api_key=API_KEY)

# Modelo (puedes cambiarlo si falla)
MODEL_ID = "gemini-2.5-flash-image"

# UI
st.image(
    'https://img.freepik.com/vector-gratis/diseno-plantilla-ai-degradado_23-2150380008.jpg',
    use_container_width=True
)

st.title('🖌️ Editor / Generador de Imágenes (Gemini)')
mode = st.sidebar.selectbox('¿Qué quieres hacer?', ['Editar', 'Crear'])

# -----------------------------
# FUNCIÓN CORREGIDA
# -----------------------------
def mostrar_y_descargar(response, label):

    # Compatibilidad con distintas versiones del SDK
    parts = []

    if hasattr(response, "candidates"):
        parts = response.candidates[0].content.parts
    elif hasattr(response, "parts"):
        parts = response.parts

    if not parts:
        st.error("⚠️ No se recibieron datos del modelo")
        return

    for part in parts:

        # Evitar pensamientos internos
        if hasattr(part, "thought") and part.thought:
            continue

        # 🖼️ IMAGEN (FORMA CORRECTA ACTUAL)
        if part.inline_data and part.inline_data.data:
            try:
                image_bytes = part.inline_data.data
                img = Image.open(BytesIO(image_bytes))

                st.image(img, caption=label, use_container_width=True)

                buf = BytesIO()
                img.save(buf, format='PNG')

                st.download_button(
                    label=f'⬇️ Descargar {label}',
                    data=buf.getvalue(),
                    file_name=f'{label.lower()}.png',
                    mime='image/png'
                )
            except Exception as e:
                st.error(f"Error procesando imagen: {e}")

        # 📝 TEXTO
        elif part.text:
            st.info(part.text)

# -----------------------------
# EDITAR
# -----------------------------
if mode == 'Editar':

    st.write('Sube una imagen o usa la cámara:')

    col1, col2 = st.columns([3, 1])

    with col1:
        file = st.file_uploader(
            'Sube imagen',
            type=['jpg', 'jpeg', 'png'],
            label_visibility="collapsed"
        )

    with col2:
        use_camera = st.checkbox('Usar cámara')

    camera_file = None
    if use_camera:
        camera_file = st.camera_input('Capturar imagen')

    selected = file or camera_file

    if selected:
        input_image = Image.open(selected)
        st.image(input_image, caption='Original', use_container_width=True)

        prompt = st.text_input(
            '¿Qué edición quieres?',
            'Agrega una chaqueta gris.'
        )

        if st.button('🖼️ Generar edición'):
            with st.spinner('Procesando edición...'):

                resp = client.models.generate_content(
                    model=MODEL_ID,
                    contents=[prompt, input_image],
                    config=types.GenerateContentConfig(
                        response_modalities=['TEXT', 'IMAGE']
                    )
                )

            mostrar_y_descargar(resp, 'Editada')

# -----------------------------
# CREAR
# -----------------------------
else:

    prompt = st.text_area(
        'Prompt',
        'Un paisaje surrealista de una ciudad flotando en una botella.'
    )

    if st.button('🖼️ Generar imagen'):
        with st.spinner('Generando nueva imagen...'):

            resp = client.models.generate_content(
                model=MODEL_ID,
                contents=[prompt],
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE']
                )
            )

        mostrar_y_descargar(resp, 'Generada')

# -----------------------------
# FOOTER
# -----------------------------
st.markdown('---')
st.markdown(
    "<div style='text-align:center;'>"
    "<strong>Desarrollador:</strong> Edwin Quintero | "
    "<strong>Modelo:</strong> Gemini Flash Image"
    "</div>",
    unsafe_allow_html=True
)

social_links = [
    'https://www.facebook.com/edwin.quinteroalzate',
    'https://www.linkedin.com/in/edwinquintero0329/',
    'https://github.com/Edwin1719'
]

SocialMediaIcons(social_links).render()