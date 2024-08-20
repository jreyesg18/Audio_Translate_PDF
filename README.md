# Audio Translate PDF

Este proyecto permite traducir el contenido de un archivo PDF a diferentes idiomas y reproducir la traducción en voz. Puedes seleccionar desde qué página deseas comenzar a traducir y leer el contenido del PDF.

## Requisitos

Antes de ejecutar el script, asegúrate de tener instaladas las siguientes bibliotecas de Python:

- `deep_translator`
- `gtts`
- `PyPDF2`
- `os` (módulo estándar de Python)

Puedes instalar estas bibliotecas utilizando pip. Aquí están los comandos para instalar las dependencias necesarias:

    pip install deep-translator gtts PyPDF2

## Uso

1. **Clona este repositorio** o descarga los archivos del proyecto.
2. **Ejecuta el script AudioTranslate.py:**

    python Main.py

3. **Introduce la ruta** del archivo PDF que deseas traducir.
4. **Selecciona la página de inicio** introduciendo el número de la página desde la cual deseas comenzar la traducción. Por ejemplo, si deseas comenzar desde la página 3, escribe 3.
5. **Elige el idioma** al que deseas traducir el contenido. Escribe el código del idioma:
- **'es'** para español
- **'en'** para inglés
- **'fr'** para francés
- **'de'** para alemán
- **'it'** para italiano 

6. El script **traducirá** y **leerá** en voz el contenido de las páginas seleccionadas.


## Notas

El script utiliza **GoogleTranslator** de la biblioteca **deep_translator** para realizar la traducción.
La reproducción de la traducción en voz se realiza utilizando la biblioteca **gTTS** y el comando **afplay** en macOS. Si estás usando un sistema operativo diferente, puede que necesites modificar el comando de reproducción de audio **(afplay)** para que funcione en tu entorno.