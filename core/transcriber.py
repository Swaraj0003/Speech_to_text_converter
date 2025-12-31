import os
import numpy as np
from scipy.io import wavfile
from core.model_loader import load_model

def transcribe_audio(wav_path: str) -> str:
    if not os.path.exists(wav_path):
        raise FileNotFoundError("Audio file not found")

    if os.path.getsize(wav_path) < 1000:
        raise RuntimeError("Audio file is empty or corrupted")

  
    sample_rate, audio = wavfile.read(wav_path)

    if audio.ndim > 1:
        audio = audio[:, 0]  

   
    audio = audio.astype(np.float32) / 32768.0

    model = load_model()

 
    result = model.transcribe(audio, fp16=False)

    return result["text"]
