import os

class Config:
    SECRET_KEY = 'vibe-coding-ai-secret-key'
    UPLOAD_FOLDER = os.path.join('static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB limit
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}
    # High-quality BLIP model from Salesforce
    MODEL_ID = "Salesforce/blip-image-captioning-base"