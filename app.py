import streamlit as st
import openai
import io
from PIL import Image
import requests
from st_social_media_links import SocialMediaIcons

# Cargar la imagen desde una URL
image_url = "https://media.licdn.com/dms/image/v2/C5612AQFVb6K_9Q6HSw/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1632878983190?e=2147483647&v=beta&t=YCtJyzQ2iEz1vDBKYQR9pqGUR70WilMcJioicVtViSY"  # Reemplaza con la URL de tu imagen
st.markdown(
    f"""
    <style>
    .center-img {{
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%;  # Ajusta el tamaño según sea necesario
    }}
    </style>
    <img src="{image_url}" class="center-img">
    """,
    unsafe_allow_html=True
)

st.title("Generador de Imágenes DALL-E 3")

# Solicitar la clave API al usuario
api_key = st.text_input("Introduce tu clave API de OpenAI", type="password")

if api_key:
    openai.api_key = api_key

    # Entrada de texto para el prompt
    prompt = st.text_input("Introduce un prompt para generar una imagen:")

    # Botón para generar la imagen
    if st.button("Generar Imagen"):
        with st.spinner("Generando imagen..."):
            try:
                response = openai.Image.create(
                    prompt=prompt,
                    n=1,
                    size="1024x1024"
                )
                image_url = response['data'][0]['url']
                st.image(image_url, caption=prompt, use_column_width=True)

                # Guardar la imagen en un buffer
                buf = io.BytesIO()
                image = Image.open(requests.get(image_url, stream=True).raw)
                image.save(buf, format="PNG")
                byte_im = buf.getvalue()

                # Botón para descargar la imagen
                st.download_button(
                    label="Descargar imagen",
                    data=byte_im,
                    file_name="generated_image.png",
                    mime="image/png"
                )
            except Exception as e:
                st.error(f"Error al generar imágenes: {e}")

# Pie de página con información del desarrollador y logos de redes sociales
st.markdown("""
---
**Desarrollador:** Edwin Quintero Alzate<br>
**Email:** egqa1975@gmail.com<br>
""")

social_media_links = [
    "https://www.facebook.com/edwin.quinteroalzate",
    "https://www.linkedin.com/in/edwinquintero0329/",
    "https://github.com/Edwin1719"]

social_media_icons = SocialMediaIcons(social_media_links)
social_media_icons.render()