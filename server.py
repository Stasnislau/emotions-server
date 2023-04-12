from flask import Flask, request, jsonify
from deepface import DeepFace
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def analyze():
    img = request.body['image']
    result = DeepFace.analyze(img, enforce_detection=False)
    dominant_emotion = result[0]['dominant_emotion']
    return jsonify({'dominant_emotion': dominant_emotion})

if __name__ == '__main__':
    host = os.getenv('DOMAIN', 'localhost')
    port = int(os.getenv('PORT', 3001))
    app.run(host=host, port=port)