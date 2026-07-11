import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from config import Config

class ImageCaptioner:
    def __init__(self):
        print(f"Initializing model: {Config.MODEL_ID}...")
        # Automatically downloads weights from Hugging Face on first run
        self.processor = BlipProcessor.from_pretrained(Config.MODEL_ID)
        self.model = BlipForConditionalGeneration.from_pretrained(Config.MODEL_ID)
        
        # Hardware acceleration
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)
        print(f"Model loaded successfully on {self.device}")

    def generate_caption(self, image_path):
        try:
            raw_image = Image.open(image_path).convert('RGB')
            
            # Preprocessing
            inputs = self.processor(raw_image, return_tensors="pt").to(self.device)
            
            # Inference
            with torch.no_grad():
                out = self.model.generate(**inputs, max_new_tokens=50)
            
            # Post-processing
            caption = self.processor.decode(out[0], skip_special_tokens=True)
            return caption.capitalize()
        except Exception as e:
            return f"Error generating caption: {str(e)}"