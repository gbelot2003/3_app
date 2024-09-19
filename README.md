# Proyecto de Integración con ChatGPT

Este proyecto es una aplicación web desarrollada con Flask que integra el modelo GPT-3.5 Turbo de OpenAI para crear un asistente de inteligencia artificial conversacional. El asistente puede manejar **intents** como consultar datos desde ChromaDB y llamar a APIs externas.

## Tabla de Contenidos

- [Prerequisitos](#prerequisitos)
- [Instalación](#instalación)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso](#uso)
- [Configuración](#configuración)
- [Notas](#notas)
- [Licencia](#licencia)

## Prerequisitos

- Python 3.8 o superior
- Clave de API de OpenAI
- pip (administrador de paquetes de Python)

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tuusuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. **Crea y activa un entorno virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. **Instala los paquetes requeridos:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configura tu Clave de API de OpenAI:**

   ```bash
   export OPENAI_API_KEY='tu-clave-de-api'  # En Windows usa `set`
   ```

## Estructura del Proyecto

```
├── app.py
├── conversation
│   ├── __init__.py
│   └── conversation.py
├── services
│   ├── __init__.py
│   ├── api_service.py
│   ├── chroma_service.py
│   └── file_processing_service.py
├── intents
│   ├── __init__.py
│   ├── api_intent.py
│   └── chroma_query_intent.py
├── utils
│   ├── __init__.py
│   └── dependency_injector.py
├── file_processing
│   ├── __init__.py
│   ├── excel_processor.py
│   └── pdf_processor.py
├── data
│   ├── documento1.pdf
│   └── datos.xlsx
├── templates
│   └── chat.html
├── requirements.txt
└── README.md
```

- **app.py**: Archivo principal de la aplicación Flask.
- **conversation**: Paquete que contiene la lógica de la conversación.
  - **conversation.py**: Contiene la clase `Conversation` que gestiona el chat.
- **services**: Contiene clases de servicio para diversas funcionalidades.
  - **api_service.py**: Servicio para interactuar con APIs externas.
  - **chroma_service.py**: Servicio para interactuar con ChromaDB.
  - **file_processing_service.py**: Servicio para procesar archivos iniciales.
- **intents**: Contiene clases de intent para manejar acciones específicas.
  - **api_intent.py**: Intent para manejar llamadas a APIs.
  - **chroma_query_intent.py**: Intent para manejar consultas a ChromaDB.
- **utils**: Funciones utilitarias y de inyección de dependencias.
  - **dependency_injector.py**: Maneja la inyección de dependencias y la inicialización de servicios.
- **file_processing**: Contiene módulos para procesar archivos.
  - **pdf_processor.py**: Módulo para extraer texto de PDFs.
  - **excel_processor.py**: Módulo para extraer texto de archivos Excel.
- **data**: Directorio que contiene los archivos de datos iniciales (PDFs y archivos Excel).
- **templates**: Contiene plantillas HTML para la aplicación Flask.
  - **chat.html**: Plantilla para la interfaz de chat.
- **requirements.txt**: Lista las dependencias de Python del proyecto.
- **README.md**: Documentación del proyecto.

## Uso

1. **Ejecuta la aplicación Flask:**

   ```bash
   python app.py
   ```

2. **Accede a la aplicación:**

   Abre tu navegador web y navega a `http://localhost:5000`.

3. **Interactúa con el Chatbot:**

   - Ingresa tu mensaje en el campo de entrada y envíalo.
   - El asistente responderá basándose en los intents implementados o utilizará la API de OpenAI para respuestas generales.

## Configuración

- **Clave de API de OpenAI:**

  Asegúrate de configurar tu clave de API de OpenAI como una variable de entorno:

  ```bash
  export OPENAI_API_KEY='tu-clave-de-api'
  ```

- **Archivos de Datos Iniciales:**

  Coloca tus archivos PDF y Excel en el directorio `data`. Actualiza las rutas de los archivos en `file_processing_service.py` si es necesario.

## Notas

- **Dependencias:**

  - El proyecto utiliza `langchain`, `openai`, `PyPDF2`, `pandas` y otras librerías listadas en `requirements.txt`.
  - Asegúrate de que todas las dependencias estén instaladas y actualizadas.

- **Versiones de API:**

  - Ten en cuenta las versiones de la API de OpenAI y de `langchain` que estás utilizando, ya que pueden existir cambios importantes entre versiones.
  - Ajusta tu código según la documentación más reciente si actualizas los paquetes.

- **Manejo de Errores:**

  - Actualmente, la aplicación puede no manejar todas las excepciones. Considera agregar manejo de errores para un uso en producción.

- **Extensibilidad:**

  - El proyecto está diseñado para ser modular y extensible. Puedes agregar nuevos intents y servicios según sea necesario.

## Licencia

[Licencia MIT](LICENSE)