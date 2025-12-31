# 🎙️ Speech-to-Text Converter (Offline, Open-Source)

An offline, open-source Speech-to-Text (STT) application built using OpenAI Whisper and Streamlit, designed with a modular, industry-grade architecture.  
The system converts spoken audio into accurate text without using paid APIs or internet connectivity.

---

## 📌 Project Overview

This project implements a speech recognition pipeline that allows users to:
- Record audio using a microphone, or
- Upload a WAV audio file

and converts the speech into text using a deep learning-based speech recognition model.

The application is fully offline, secure, and cross-platform, making it suitable for real-world deployment, academic projects, and research use.

---

## 🚀 Key Features

- Offline speech recognition (no internet required)
- 100% open-source (no paid APIs)
- High accuracy using Whisper AI model
- Clean, modular, and scalable architecture
- Streamlit-based web interface
- Windows-safe implementation (FFmpeg bypassed)
- Supports microphone input and WAV file uploads

---

## 🏗️ System Architecture

User Audio Input  
→ Audio Recording / Upload  
→ Audio Validation & Preprocessing  
→ Whisper Deep Learning Model  
→ Text Transcription Output

---

## 🧠 Technology Stack

- Programming Language: Python 3.10
- Speech Recognition Model: OpenAI Whisper (Open Source)
- Web Interface: Streamlit
- Audio Processing: sounddevice, SciPy
- Machine Learning Framework: PyTorch
- Deployment: Local / Cloud Ready

---

## 📁 Project Structure

speech_to_text_convertor/  
├── app.py                  # Streamlit UI entry point  
├── requirements.txt        # Project dependencies  
│  
├── core/                   # AI & transcription logic  
│   ├── model_loader.py  
│   └── transcriber.py  
│  
├── audio/                  # Audio handling  
│   ├── recorder.py  
│   └── file_handler.py  
│  
└── utils/                  # Configuration  
    └── config.py  

---

## ⚙️ Installation & Setup

### Step 1: Create Virtual Environment (Recommended)

conda create -n stt python=3.10 -y  
conda activate stt  

### Step 2: Install Dependencies

pip install -r requirements.txt  

---

## ▶️ Run the Application

streamlit run app.py  

Open your browser and navigate to:  
http://localhost:8501

---

## 🎤 How It Works

1. User records speech or uploads a WAV file  
2. Audio is saved in PCM 16-bit WAV format  
3. Audio is loaded directly as a NumPy array  
4. Whisper model processes the audio  
5. Transcribed text is displayed in the UI  

Note:  
The project bypasses FFmpeg decoding to ensure maximum stability on Windows systems.

---

## 📊 Applications

- Lecture transcription
- Accessibility tools for hearing-impaired users
- Voice notes and dictation
- Interview and meeting transcription
- Voice-controlled applications

---

## 🔮 Future Enhancements

- Real-time live transcription
- Multi-language translation
- Speaker diarization
- Cloud deployment using Docker
- Mobile application integration
- Voice command support

---



---

## 📜 License

This project uses open-source libraries and is intended for educational and research purposes.  
You are free to modify and extend it as needed.

---

## 🙌 Acknowledgements

- OpenAI Whisper (open-source speech recognition model)
- Streamlit community
- Open-source Python ecosystem

---



---




