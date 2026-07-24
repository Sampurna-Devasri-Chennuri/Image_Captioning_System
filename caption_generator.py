import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from config import Config


class ImageCaptioner:
    def __init__(self):
        print(f"Initializing model: {Config.MODEL_ID}...")

        self.processor = BlipProcessor.from_pretrained(
            Config.MODEL_ID
        )

        self.model = BlipForConditionalGeneration.from_pretrained(
            Config.MODEL_ID
        )

        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        self.model.to(self.device)

        print(
            f"Model loaded successfully on {self.device}"
        )

    def generate_caption(self, image_path):
        try:
            raw_image = Image.open(
                image_path
            ).convert("RGB")

            inputs = self.processor(
                images=raw_image,
                return_tensors="pt"
            )

            inputs = {
                key: value.to(self.device)
                for key, value in inputs.items()
            }

            with torch.no_grad():
                output = self.model.generate(
                    **inputs,
                    max_new_tokens=50
                )

            caption = self.processor.decode(
                output[0],
                skip_special_tokens=True
            )

            return caption.capitalize()

        except Exception as e:
            return f"Error generating caption: {str(e)}"