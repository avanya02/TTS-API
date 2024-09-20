
from flask import Flask, request, send_file
import pyttsx3
from io import BytesIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def text_to_speech(text):
    engine = pyttsx3.init()
    mp3_fp = BytesIO()  # In-memory file
    engine.save_to_file(text, mp3_fp)
    engine.runAndWait()
    mp3_fp.seek(0)  # Move to the start of the file for reading
    return mp3_fp

@app.route('/api/tts', methods=['POST'])
def tts():
    data = request.json
    text = data.get('text')

    if not text:
        return {"error": "No text provided"}, 400

    audio_data = text_to_speech(text)
    return send_file(audio_data, mimetype='audio/mpeg', as_attachment=True, download_name='speech.mp3')

if __name__ == '__main__':
    app.run(debug=True)
