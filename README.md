# 🎨 Advanced AI Image Studio (Gemini 2.5 & GPT-Image)

Una estación de trabajo de vanguardia para la generación y edición de imágenes mediante Inteligencia Artificial. Este proyecto utiliza los modelos más recientes y experimentales de **Google** y **OpenAI**, optimizados para ofrecer alta fidelidad y capacidades multimodales.

## ✨ Características Principales

- **🚀 Google Gemini 2.5 Flash Image**: Procesa y genera imágenes/texto de forma nativa en la misma respuesta.
- **🖼️ GPT-Image Engine**: Generación de alta resolución mediante modelos **gpt-image-2** y **gpt-image-1** con sistema de *fallback* automático.
- **✏️ Edición Multimodal**: Modifica imágenes enviándolas directamente al modelo con instrucciones naturales.
- **📸 Captura en Vivo**: Soporte nativo para cámara web y carga de archivos locales.
- **📱 Social Integration**: Footer dinámico con enlaces a redes sociales integrados.
- **💾 Gestión de Galería**: Sistema de persistencia local para todas las imágenes generadas.

## 🛠️ Tecnologías y Librerías

- **[Streamlit](https://streamlit.io/)**: Core de la interfaz de usuario.
- **[Google GenAI SDK](https://github.com/google-gemini/generative-ai-python)**: Implementación de la nueva clase `genai.Client`.
- **[OpenAI SDK](https://github.com/openai/openai-python)**: Integración con los motores GPT-Image.
- **[Pillow](https://pillow.readthedocs.io/)**: Procesamiento de imágenes y conversión de bytes.
- **[St-Social-Media-Links](https://pypi.org/project/st-social-media-links/)**: Componente para conectividad social.

## 🏗️ Estructura y Arquitectura del Proyecto

El proyecto sigue una arquitectura modular donde cada motor de IA opera de forma independiente:

```
Text_Image_OPENAI/
├── app_gemini.py           # Engine de Google: Maneja visión y generación multimodal.
├── app_openai.py           # Engine de OpenAI: Especializado en generación por prompts.
├── env.example             # Plantilla de configuración de variables de entorno.
├── .env                    # Archivo de configuración real (ignorado por Git).
├── requirements.txt        # Lista completa de dependencias de última versión.
├── README.md               # Documentación técnica del sistema.
└── images/
    └── output/             # Repositorio de persistencia: donde vive tu arte generado.
```

## 🚀 Configuración Inicial

1. **Instalar Dependencias**
```bash
pip install -r requirements.txt
```

2. **Configurar Credenciales**
Copia el archivo de ejemplo y rellena tus llaves:
```bash
cp env.example .env
```
*Edita el `.env` con tus claves de Google AI Studio y OpenAI Dashboard.*

## 📖 Guía de Uso

### Opción A: Motor Gemini (Multimodal)
Ideal para ediciones complejas ("cambia el color de la ropa") o generación rápida.
```bash
streamlit run app_gemini.py
```

### Opción B: Motor OpenAI (Fidelidad)
Ideal para creaciones artísticas desde cero con control total de tamaño y calidad.
```bash
streamlit run app_openai.py
```

## 👨‍💻 Autor

**Edwin Quintero**
- Email: egqa1975@gmail.com
- [Facebook](https://www.facebook.com/edwin.quinteroalzate) | [LinkedIn](https://www.linkedin.com/in/edwinquintero0329/) | [GitHub](https://github.com/Edwin1719)






