from flask import Flask, request, jsonify, flash , redirect
from deepface import DeepFace
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()
app = Flask(__name__)
CORS(app)

@app.route('/api/upload', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file in request'})
    
    file = request.files['image']
    file.save('image.png')
    
    try:
        result = DeepFace.analyze('image.png', enforce_detection=False)
        dominant_emotion = result[0]['dominant_emotion']
        return jsonify({'mood': dominant_emotion})
    except ValueError as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    host = os.getenv('DOMAIN', 'localhost')
    port = int(os.getenv('PORT', 3001))
    app.run(host=host, port=port)