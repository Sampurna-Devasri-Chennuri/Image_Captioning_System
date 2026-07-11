from PIL import Image

def process_image(image_path):
    """
    Standardizes image format before model processing.
    """
    img = Image.open(image_path).convert('RGB')
    return img