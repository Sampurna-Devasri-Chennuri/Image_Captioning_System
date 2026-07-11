import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from config import Config
from caption_generator import ImageCaptioner
from utils.helper import allowed_file, create_directories

app = Flask(__name__)
app.config.from_object(Config)

# Initialize project structure
create_directories([
    app.config['UPLOAD_FOLDER'], 
    'static/css', 
    'static/js', 
    'templates',
    'models',
    'utils'
])

# Initialize the Captioning Engine
# This downloads the ~900MB model on the very first execution
engine = ImageCaptioner()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        caption = engine.generate_caption(filepath)
        
        return jsonify({
            'success': True,
            'caption': caption,
            'image_url': f'/static/uploads/{filename}'
        })
        
    return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    app.run(debug=False, port=5000)