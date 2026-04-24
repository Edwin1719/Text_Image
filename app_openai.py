import os
import base64
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
from PIL import Image
from io import BytesIO

# =========================
# CONFIG
# =========================
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

OUTPUT_DIR = "images/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================
# FUNCIONES
# =========================
def save_image(image_base64, filename):
    image_bytes = base64.b64decode(image_base64)
    path = os.path.join(OUTPUT_DIR, filename)

    with open(path, "wb") as f:
        f.write(image_bytes)

    return path


def generate_images(prompt, size, quality, n):
    try:
        return client.images.generate(
            model="gpt-image-2",
            prompt=prompt,
            size=size,
            quality=quality,
            n=n
        )
    except Exception:
        return client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size=size,
            quality=quality,
            n=n
        )

# =========================
# UI STREAMLIT
# =========================
st.set_page_config(page_title="Generador de Imágenes AI", layout="wide")

st.title("🎨 Generador de Imágenes con IA")
st.markdown("Crea imágenes usando el modelo más avanzado de OpenAI.")

# =========================
# INPUTS
# =========================
prompt = st.text_area(
    "Prompt",
    placeholder="Ej: Fotografía fotorrealista de un astronauta en Medellín tomando café, luz natural..."
)

col1, col2, col3 = st.columns(3)

with col1:
    size = st.selectbox(
        "Tamaño",
        ["1024x1024", "1024x1536", "1536x1024", "2560x1440"]
    )

with col2:
    quality = st.selectbox(
        "Calidad",
        ["low", "medium", "high"],
        index=1
    )

with col3:
    n = st.slider("Número de imágenes", 1, 4, 1)

generate_btn = st.button("🚀 Generar imágenes")

# =========================
# GENERACIÓN
# =========================
if generate_btn:
    if not prompt.strip():
        st.warning("⚠️ Debes ingresar un prompt.")
    else:
        with st.spinner("Generando imágenes..."):
            try:
                result = generate_images(prompt, size, quality, n)

                st.success("✅ Imágenes generadas")

                cols = st.columns(n)

                for i, item in enumerate(result.data):
                    image_base64 = item.b64_json
                    image_bytes = base64.b64decode(image_base64)

                    image = Image.open(BytesIO(image_bytes))

                    filename = f"image_{i+1}.png"
                    path = save_image(image_base64, filename)

                    with cols[i]:
                        st.image(image, caption=f"Imagen {i+1}")
                        st.download_button(
                            label="⬇️ Descargar",
                            data=image_bytes,
                            file_name=filename,
                            mime="image/png"
                        )

            except Exception as e:
                st.error(f"Error: {str(e)}")

# =========================
# HISTORIAL
# =========================
st.markdown("---")
st.subheader("📁 Imágenes generadas")

files = os.listdir(OUTPUT_DIR)

if files:
    cols = st.columns(4)
    for i, file in enumerate(files[::-1]):
        path = os.path.join(OUTPUT_DIR, file)
        image = Image.open(path)

        with cols[i % 4]:
            st.image(image, caption=file)
else:
    st.info("Aún no hay imágenes generadas.")