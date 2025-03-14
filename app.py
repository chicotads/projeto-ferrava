from flask import Flask, render_template, request, jsonify
import pytesseract
from PIL import Image
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nenhum arquivo selecionado'}), 400

    # Extrair texto usando OCR
    image = Image.open(file)
    extracted_text = pytesseract.image_to_string(image, lang=request.form['source_lang'])

    # Traduzir texto
    translator = Translator()
    translated = translator.translate(extracted_text, src=request.form['source_lang'], dest=request.form['target_lang'])

    # Retornar resultado
    return jsonify({
        'extracted_text': extracted_text,
        'translated_text': translated.text
    })

if __name__ == '__main__':
    app.run(debug=True)
    git add .
git commit -m "Design modernizado com Bootstrap, cores e imagens"
git push origin main