import streamlit as st
from PIL import Image
from io import BytesIO
from google import genai
from google.genai import types
from st_social_media_links import SocialMediaIcons

# ─── Configuración ─────────────────────────────────────────────────────────
API_KEY = st.secrets["GEMINI_API_KEY"]
if not API_KEY:
    st.error("No se encontró GEMINI_API_KEY en los Secrets.")
    st.stop()
client = genai.Client(api_key=API_KEY)

st.title("🖌️ Mixto: Crear y Editar Imágenes")
mode = st.sidebar.selectbox("Acción", ["Editar", "Crear"])

def mostrar_y_descargar(bytes_data, label):
    img = Image.open(BytesIO(bytes_data))
    st.image(img, caption=label, use_container_width=True)
    buf = BytesIO(); img.save(buf, format="PNG")
    st.download_button("⬇️ Descargar imagen", buf.getvalue(), f"{label}.png", "image/png")

# ─── Edición (Flash Experimental) ──────────────────────────────────────────
if mode == "Editar":
    file = st.file_uploader("Selecciona imagen", type=["png","jpg","jpeg"])
    prompt = st.text_input("Instrucción de edición", "Agrega una chaqueta gris.")
    if file and st.button("Generar edición"):
        with st.spinner("Procesando…"):
            resp = client.models.generate_content(
                model="gemini-2.0-flash-exp-image-generation",
                contents=[prompt, Image.open(file)],
                config=types.GenerateContentConfig(response_modalities=["TEXT","IMAGE"])
            )
        for part in resp.candidates[0].content.parts:
            if part.inline_data:
                mostrar_y_descargar(part.inline_data.data, "Editada")

# ─── Creación (Imagen 3) ───────────────────────────────────────────────────
else:
    prompt = st.text_area("Prompt de creación", "Un paisaje surrealista.")
    if st.button("Generar imagen"):
        with st.spinner("Generando…"):
            resp = client.models.generate_images(
                model="imagen-3.0-generate-002",
                prompt=prompt,
                config=types.GenerateImagesConfig(number_of_images=1, aspect_ratio="1:1")
            )
        for img_obj in resp.generated_images:
            mostrar_y_descargar(img_obj.image.image_bytes, "Generada")

# ─── Footer ────────────────────────────────────────────────────────────────
SocialMediaIcons([
    "https://facebook.com/edwin.quinteroalzate",
    "https://linkedin.com/in/edwinquintero0329",
    "https://github.com/Edwin1719"
]).render()
