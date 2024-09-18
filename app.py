from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pyttsx3
from io import BytesIO

app = Flask(__name__)
CORS(app) 

# Initialize pyttsx3 engine
engine = pyttsx3.init()

@app.route('/api/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Create a buffer for the audio file
    audio_buffer = BytesIO()

    # Set speech parameters (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

    # Save the speech to the buffer
    engine.save_to_file(text, audio_buffer)
    engine.runAndWait()

    # Seek to the beginning of the BytesIO buffer
    audio_buffer.seek(0)

    # Send the audio file as a response
    return send_file(audio_buffer, mimetype='audio/wav')

if __name__ == '__main__':
    app.run(port=5000)
