from transformers import BlipProcessor, BlipForConditionalGeneration
from config import Config

def load_ai_model():
    """
    Utility function to explicitly pre-download or fetch the model.
    """
    processor = BlipProcessor.from_pretrained(Config.MODEL_ID)
    model = BlipForConditionalGeneration.from_pretrained(Config.MODEL_ID)
    return processor, model

from caption_generator import ImageCaptioner

def get_engine():
    return ImageCaptioner()