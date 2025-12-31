import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from utils.config import SAMPLE_RATE, AUDIO_CHANNELS

def record_audio(duration: int, output_path: str):
    """
    Records audio from microphone and saves as PCM 16-bit WAV
    """

    audio = sd.rec(
        frames=int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=AUDIO_CHANNELS,
        dtype=np.int16   # FORCE PCM 16-bit
    )
    sd.wait()

    if audio.size == 0:
        raise RuntimeError("Microphone returned empty audio")

    write(output_path, SAMPLE_RATE, audio)
