import whisper
from utils.config import MODEL_SIZE

_model = None

def load_model():
    global _model
    if _model is None:
        _model = whisper.load_model(MODEL_SIZE)
    return _model
