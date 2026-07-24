🖼️ Image Captioning AI

An AI-powered web application that automatically generates natural-language captions for uploaded images using BLIP (Bootstrapping Language-Image Pre-training) and Deep Learning.

🚀 Features
Upload an image and generate an AI-powered caption
Uses the Salesforce BLIP Image Captioning Model
Supports CPU and CUDA GPU acceleration
Clean and responsive web interface
Secure filename handling
Supports common image formats
Flask-based backend
Real-time caption generation
🛠️ Tech Stack
Python
Flask
PyTorch
Hugging Face Transformers
BLIP
Pillow
HTML
CSS
JavaScript
📂 Project Structure
Image-Captioning-AI/
│
├── app.py
├── caption_generator.py
├── config.py
├── image_preprocessing.py
├── model_loader.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── encoder.py
│   └── decoder.py
│
├── utils/
│   ├── helper.py
│   ├── predict.py
│   └── preprocessing.py
│
├── templates/
│   ├── index.html
│   └── about.html
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── uploads/
│
└── sample_images/
⚙️ Installation
1. Clone the Repository
git clone https://github.com/Sampurna-Devasri-Chennuri/Image_Captioning_System.git
cd Image_Captioning_System
2. Create a Virtual Environment
python -m venv venv
3. Activate the Virtual Environment

Windows:

venv\Scripts\activate

macOS/Linux:

source venv/bin/activate
4. Install Dependencies
pip install -r requirements.txt
▶️ Run the Application
python app.py

Open your browser and visit:

http://127.0.0.1:5000
🧠 How It Works
The user uploads an image.
The Flask backend receives the image.
The image is securely saved.
The BLIP processor preprocesses the image.
The BLIP model analyzes the visual content.
An AI-generated caption is created.
The caption is displayed on the web interface.
🤖 AI Model

This project uses the Salesforce BLIP image captioning model through Hugging Face Transformers.

The model automatically downloads the required weights during the first execution.

🌐 Deployment

The application can be deployed using platforms such as Render with the following start command:

gunicorn app:app
📸 Example

Upload an image such as:

A dog playing in a field

The AI model may generate:

"A dog is running through a grassy field."

🔮 Future Improvements
Multi-language caption generation
Voice output for generated captions
Caption history
Image-to-story generation
Mobile application
Improved GPU-based inference
Multiple caption generation options
👩‍💻 Author

Sampurna Devasri Chennuri

B.Tech Computer Science Engineering Student

⭐ If you found this project interesting, consider giving the repository a star!
