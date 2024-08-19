# Book_translate

Este proyecto permite traducir el texto de un archivo PDF a diferentes idiomas y reproducir la traducción en formato de audio.

## Requisitos

Asegúrate de tener Python 3 instalado en tu sistema. Además, necesitarás instalar las siguientes bibliotecas:

- deep-translator para realizar la traducción.
- gtts para convertir el texto traducido en audio.
- PyPDF2 para leer el contenido del PDF.

Puedes instalar estas bibliotecas utilizando pip. Aquí están los comandos para instalar las dependencias necesarias:

    pip install deep-translator gtts PyPDF2

## Cómo usar

1. **Prepara el archivo PDF:** Asegúrate de tener el archivo PDF que deseas traducir guardado en tu computadora.
2. **Ejecuta el script:** Corre el script Python desde tu terminal. El script te pedirá la ruta del archivo PDF y el idioma al que deseas traducir el texto. Elige un idioma de entre los siguientes: español (es), inglés (en), francés (fr), alemán (de), italiano (it).


    python path/to/your/script.py

Reemplaza path/to/your/script.py con la ruta real de tu script.

3. **Introduce la ruta del archivo PDF:** El script te pedirá que ingreses la ruta del archivo PDF que deseas traducir.
4. **Selecciona el idioma:** Introduce el código del idioma al que deseas traducir el texto (por ejemplo, es para español).
5. **Escucha la traducción:** El script traducirá el texto de cada página del PDF y reproducirá la traducción en formato de audio.

## Ejemplo de Ejecución

    python /path/to/your/script.py
Salida esperada:


    Introduce la ruta del archivo PDF que deseas traducir:
    /path/to/your/file.pdf
    ¿A qué idioma quieres traducirlo? (es para español, en para inglés, fr para francés, etc.)
    es
    Traduciendo página 1...
    Texto traducido de la página 1: (Texto traducido aquí)

## Notas

Asegúrate de que el entorno virtual esté activado si estás usando uno.
La reproducción de audio usa el comando afplay, que está disponible en macOS. Si estás en otra plataforma, es posible que necesites modificar el comando para reproducir archivos de audio.
Si el PDF contiene imágenes en lugar de texto, considera usar una herramienta de OCR para extraer el texto.
