import streamlit as st
import os

from audio.recorder import record_audio
from audio.file_handler import save_uploaded_wav
from core.transcriber import transcribe_audio

st.set_page_config(
    page_title="Speech to Text Converter",
    layout="centered"
)

st.title("🎙️ Speech-to-Text Converter")
st.caption("Offline • Open Source • Whisper Powered")

tab1, tab2 = st.tabs(["🎤 Record Audio", "📁 Upload WAV"])

# ---------------- RECORD AUDIO ----------------
with tab1:
    duration = st.slider("Recording duration (seconds)", 2, 20, 5)

    if st.button("Start Recording"):
        wav_path = "recorded.wav"

        try:
            with st.spinner("Recording..."):
                record_audio(duration, wav_path)

            if not os.path.exists(wav_path):
                st.error("Recording failed. WAV file not created.")
            else:
                st.success("Recording complete")

                with st.spinner("Transcribing..."):
                    text = transcribe_audio(wav_path)

                st.text_area("Transcribed Text", text, height=250)

        except Exception as e:
            st.error(f"Error: {str(e)}")

# ---------------- UPLOAD WAV ----------------
with tab2:
    uploaded_file = st.file_uploader(
        "Upload WAV file (16kHz mono recommended)",
        type=["wav"]
    )

    if uploaded_file:
        wav_path = "uploaded.wav"

        try:
            save_uploaded_wav(uploaded_file, wav_path)

            with st.spinner("Transcribing..."):
                text = transcribe_audio(wav_path)

            st.text_area("Transcribed Text", text, height=250)

        except Exception as e:
            st.error(f"Error: {str(e)}")
