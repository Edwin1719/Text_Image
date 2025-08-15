![texto del vínculo](https://img.freepik.com/fotos-premium/retrato-ai-generando-banner-concepto-tecnologia-futura-contenido_310913-1658.jpg)

# 🖌️ Text_Image_Gemini

Una aplicación web sencilla y potente para generar y editar imágenes usando Google Gemini 2.0 Flash, construida con Streamlit.

## ✨ Características

- **🎨 Generación de Imágenes**: Crea imágenes únicas a partir de descripciones de texto
- **✏️ Edición de Imágenes**: Modifica imágenes existentes con instrucciones en lenguaje natural
- **📷 Entrada Flexible**: Sube archivos o usa la cámara web directamente
- **💾 Descarga Fácil**: Descarga las imágenes generadas en formato PNG
- **🖥️ Interfaz Intuitiva**: Diseño limpio y responsivo con Streamlit

## 🚀 Demo

![Demo de la aplicación](https://img.freepik.com/vector-gratis/diseno-plantilla-ai-degradado_23-2150380008.jpg)

## 📋 Requisitos Previos

- Python 3.8 o superior
- Una clave API de Google Gemini
- Conexión a internet

## 🛠️ Instalación

1. **Clona el repositorio**
```bash
git clone https://github.com/tu-usuario/Text_Image_Gemini.git
cd Text_Image_Gemini
```

2. **Crea un entorno virtual** (recomendado)
```bash
python -m venv venv

# En Windows
venv\Scripts\activate

# En macOS/Linux
source venv/bin/activate
```

3. **Instala las dependencias**
```bash
pip install -r requirements.txt
```

4. **Configura tu API Key**
```bash
# Copia el archivo de ejemplo
cp .env.example .env

# Edita el archivo .env y agrega tu clave API
GEMINI_API_KEY=tu_clave_api_aqui
```

5. **Ejecuta la aplicación**
```bash
streamlit run app_gemini.py
```

## 🔑 Obtener API Key de Gemini

1. Visita [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Inicia sesión con tu cuenta de Google
3. Crea una nueva API Key
4. Copia la clave y agrégala a tu archivo `.env`

## 📖 Uso

### Modo Crear
1. Selecciona "Crear" en la barra lateral
2. Escribe una descripción detallada de la imagen que deseas generar
3. Haz clic en "🖼️ Generar imagen"
4. Descarga tu imagen generada

**Ejemplo de prompts:**
- "Un paisaje surrealista con montañas flotantes y cielo púrpura"
- "Un gato astronauta explorando un planeta de queso"
- "Una ciudad futurista con rascacielos de cristal al atardecer"

### Modo Editar
1. Selecciona "Editar" en la barra lateral
2. Sube una imagen o usa la cámara web
3. Describe la edición que quieres realizar
4. Haz clic en "🖼️ Generar edición"
5. Descarga tu imagen editada

**Ejemplo de ediciones:**
- "Agrega una chaqueta roja"
- "Cambia el fondo por una playa tropical"
- "Convierte la foto a estilo anime"

## 🏗️ Estructura del Proyecto

```
Text_Image_Gemini/
├── app_gemini.py           # Aplicación principal de Streamlit
├── requirements.txt        # Dependencias de Python
├── .env                   # Variables de entorno (no incluido en git)
├── .env.example          # Plantilla de variables de entorno
├── .gitignore            # Archivos a ignorar por git
├── LICENSE               # Licencia del proyecto
└── README.md             # Este archivo
```

## 🔧 Tecnologías Utilizadas

- **[Streamlit](https://streamlit.io/)**: Framework para aplicaciones web en Python
- **[Google Gemini 2.0 Flash](https://deepmind.google/technologies/gemini/)**: Modelo de IA para generación de imágenes
- **[Pillow (PIL)](https://pillow.readthedocs.io/)**: Biblioteca de procesamiento de imágenes
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: Gestión de variables de entorno

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si quieres mejorar este proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Roadmap

- [ ] Soporte para más formatos de imagen
- [ ] Historial de generaciones
- [ ] Batch processing para múltiples imágenes
- [ ] Integración con APIs de almacenamiento en la nube
- [ ] Modo oscuro para la interfaz

## ⚠️ Limitaciones

- Requiere conexión a internet para funcionar
- Limitado por los términos de uso de la API de Gemini
- La calidad de las imágenes depende del modelo utilizado
- Tiempo de generación puede variar según la complejidad

## 🐛 Reportar Problemas

Si encuentras algún problema, por favor [abre un issue](https://github.com/tu-usuario/Text_Image_Gemini/issues) con:

- Descripción detallada del problema
- Pasos para reproducir el error
- Capturas de pantalla (si aplica)
- Información del sistema operativo y versión de Python

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Edwin Quintero**
- Email: egqa1975@gmail.com
- LinkedIn: [edwinquintero0329](https://www.linkedin.com/in/edwinquintero0329/)
- GitHub: [Edwin1719](https://github.com/Edwin1719)
- Facebook: [edwin.quinteroalzate](https://www.facebook.com/edwin.quinteroalzate)

## 🙏 Agradecimientos

- Google por proporcionar la API de Gemini
- La comunidad de Streamlit por su excelente framework
- Todos los contribuidores y usuarios que hacen posible este proyecto

---

⭐ Si este proyecto te fue útil, ¡considera darle una estrella!






