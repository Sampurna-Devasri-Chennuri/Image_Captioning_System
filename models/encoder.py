from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.models import Model

def get_encoder():
    """
    Returns the ResNet50 model pretrained on ImageNet, 
    with the top layer removed for feature extraction.
    """
    model = ResNet50(weights='imagenet')
    model = Model(inputs=model.input, outputs=model.get_layer('avg_pool').output)
    return model