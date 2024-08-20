from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import PyPDF2

def translate_text(text, dest_lang='es'):
    try:
        translator = GoogleTranslator(target=dest_lang)
        translation = translator.translate(text)
        return translation
    except Exception as e:
        return f"Error en la traducción: {e}"


def speak_text(text, lang='es'):
    try:
        tts = gTTS(text, lang=lang)
        audio_file = "translated.mp3"
        tts.save(audio_file)
        os.system(f"afplay {audio_file}")  # Usa afplay en lugar de mpg321
    except Exception as e:
        print(f"Error al reproducir el texto: {e}")


def read_pdf(file_path):
    texts = []
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    texts.append(f"Página {i + 1}:\n{text}")
                else:
                    texts.append(f"Página {i + 1}: (No se pudo extraer texto)")
    except Exception as e:
        print(f"Error al leer el PDF: {e}")
    return texts


def main():
    print("Introduce la ruta del archivo PDF que deseas traducir:")
    pdf_path = input()
    pages_text = read_pdf(pdf_path)

    if not pages_text:
        print("No se pudo extraer texto del PDF.")
        return

    print(f"El PDF tiene {len(pages_text)} páginas.")
    print("Introduce el número de la página desde la cual deseas empezar a traducir (1 a {len(pages_text)}):")
    start_page = int(input())

    if start_page < 1 or start_page > len(pages_text):
        print("Número de página no válido.")
        return

    print("¿A qué idioma quieres traducirlo? (es para español, en para inglés, fr para francés, etc.)")
    dest_lang = input()

    # Validación simple del idioma
    if dest_lang not in ['es', 'en', 'fr', 'de', 'it']:
        print("Idioma no soportado.")
        return

    for page_number, text in enumerate(pages_text[start_page-1:], start=start_page):
        print(f"Traduciendo página {page_number}...")
        translated_text = translate_text(text, dest_lang)
        # print(f"Texto traducido de la página {page_number}: {translated_text}")

        # Reproducción de la traducción en voz
        speak_text(translated_text, lang=dest_lang)

if __name__ == "__main__":
    main()

