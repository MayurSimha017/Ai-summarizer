from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from transformers import pipeline
from newspaper import Article
from PIL import Image
import pytesseract

app = Flask(__name__)
CORS(app)
summarizer = pipeline("summarization")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.form
    text = data.get('text', '')
    url = data.get('url', '')
    length = data.get('length', 'medium')

    if url:
        article = Article(url)
        article.download()
        article.parse()
        text = article.text

    if 'file' in request.files:
        image = Image.open(request.files['file'].stream)
        text = pytesseract.image_to_string(image)

    if not text.strip():
        return jsonify({'summary': 'No valid input provided.'})

    max_len = {'short': 50, 'medium': 100, 'long': 200}.get(length, 100)
    summary = summarizer(text, max_length=max_len, min_length=30, do_sample=False)[0]['summary_text']

    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
