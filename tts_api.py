from flask import Flask, request, jsonify, send_file
import pyttsx3
import os

# Initialize the Flask app
app = Flask(__name__)

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Route for the text-to-speech API
@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']

    # Set properties for the voice (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

    # Save the audio to a file
    output_filename = 'output.mp3'
    engine.save_to_file(text, output_filename)
    engine.runAndWait()

    if os.path.exists(output_filename):
        return send_file(output_filename, as_attachment=True)
    else:
        return jsonify({'error': 'Failed to generate speech'}), 500

    # Send the audio file as a response
    return send_file(output_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
