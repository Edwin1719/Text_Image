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

# Cabecera UI
st.image(
    'https://img.freepik.com/vector-gratis/diseno-plantilla-ai-degradado_23-2150380008.jpg',
    use_container_width=True
)
st.title('🖌️ Editor / Generador de Imágenes')
mode = st.sidebar.selectbox('¿Qué quieres hacer?', ['Editar', 'Crear'])

# Función para mostrar y descargar imágenes
def mostrar_y_descargar(parts, label):
    for part in parts:
        if part.inline_data:
            img = Image.open(BytesIO(part.inline_data.data))
            st.image(img, caption=label, use_container_width=True)
            buf = BytesIO()
            img.save(buf, format='PNG')
            st.download_button('⬇️ Descargar', buf.getvalue(), f'{label.lower()}.png', 'image/png')

if mode == 'Editar':
    st.write('Sube una imagen (JPG/PNG) o usa la cámara:')
    col1, col2 = st.columns([3, 1])
    with col1:
        file = st.file_uploader('', type=['jpg', 'jpeg', 'png'])
    with col2:
        use_camera = st.checkbox('Usar cámara')
    camera_file = None
    if use_camera:
        camera_file = st.camera_input('Capturar imagen')
    selected = file or camera_file
    if selected:
        st.image(selected, caption='Original', use_container_width=True)
        prompt = st.text_input('¿Qué edición quieres?', 'Agrega una chaqueta gris.')
        if st.button('🖼️ Generar edición'):
            with st.spinner('Procesando…'):
                resp = client.models.generate_content(
                    model='gemini-2.0-flash-exp-image-generation',
                    contents=[prompt, Image.open(selected)],
                    config=types.GenerateContentConfig(response_modalities=['TEXT', 'IMAGE'])
                )
            mostrar_y_descargar(resp.candidates[0].content.parts, 'Editada')

else:  # Crear
    prompt = st.text_area('Prompt', 'Un paisaje surrealista.')
    if st.button('🖼️ Generar imagen'):
        with st.spinner('Generando…'):
            resp = client.models.generate_content(
                model='gemini-2.0-flash-exp-image-generation',
                contents=prompt,
                config=types.GenerateContentConfig(response_modalities=['TEXT', 'IMAGE'])
            )
        mostrar_y_descargar(resp.candidates[0].content.parts, 'Generada')

# Footer con redes sociales
st.markdown('---')
st.markdown(
    "<div style='text-align:center;'>"
    "<strong>Desarrollador:</strong> Edwin Quintero | "
    "<strong>Email:</strong> egqa1975@gmail.com"
    "</div>",
    unsafe_allow_html=True
)
social_links = [
    'https://www.facebook.com/edwin.quinteroalzate',
    'https://www.linkedin.com/in/edwinquintero0329/',
    'https://github.com/Edwin1719'
]
SocialMediaIcons(social_links).render()