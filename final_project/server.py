from flask import Flask, render_template, request
import json
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/englishToSpanish")
def englishToSpanish():
    text_to_translate = request.args.get('textToTranslate')
    return translator.english_to_french(text_to_translate)

@app.route("/spanishToEnglish")
def spanishToEnglish():
    text_to_translate = request.args.get('textToTranslate')
    return translator.french_to_english(text_to_translate)

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
