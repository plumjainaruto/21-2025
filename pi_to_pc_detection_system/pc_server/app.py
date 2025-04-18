
from flask import Flask, render_template, request, jsonify
import base64
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'static/captures'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

detections = []

@app.route('/')
def index():
    return render_template('index.html', detections=detections)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    label = data['label']
    image_data = base64.b64decode(data['image'])

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    filename = f"{UPLOAD_FOLDER}/{timestamp}_{label}.jpg"
    
    with open(filename, 'wb') as f:
        f.write(image_data)

    detections.insert(0, {
        'date': now.strftime("%Y-%m-%d"),
        'time': now.strftime("%H:%M:%S"),
        'label': label,
        'image_path': filename
    })

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
