# 🎙️ SPEECH - Jarvis Voice Assistant

SPEECH is a Python-based voice assistant inspired by Jarvis.  
It can understand voice/text commands, perform system operations, and automate everyday tasks.

---

## ✨ Features

- 🎤 Voice command recognition (with fallback to text input)
- 🔊 Text-to-speech responses (natural speaking)
- 🌐 Web automation (Google, YouTube, etc.)
- 🖥️ Open system applications (Notepad, Calculator, CMD)
- 🎛️ System controls:
  - Volume up/down/mute
  - Lock screen
  - Screenshot capture
- 🧠 Smart fallback:
  - Unknown commands → Google search
- ⚡ Works even without microphone (typing mode)

---

## 🛠️ Technologies Used

- Python
- SpeechRecognition
- Pyttsx3 (Text-to-Speech)
- PyAutoGUI
- Webbrowser
- PyAudio (optional for microphone)

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/voice-bot.git
cd voice-bot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

to run
python app.py
