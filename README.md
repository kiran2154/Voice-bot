# 🎙️ SPEECH - Jarvis Voice Assistant

SPEECH is a Python-based voice assistant inspired by Jarvis.  
It can listen to voice commands, respond using text-to-speech, open applications, control system functions, and integrate AI responses using OpenAI.

---

## 🚀 Features

- 🎤 Speech Recognition (Voice Commands)
- 🔊 Text-to-Speech Responses
- 🌐 Open Websites (Google, YouTube, etc.)
- 🖥️ Open Applications (Notepad, Calculator, etc.)
- 🔒 System Controls (Volume, Screenshot, Lock Screen)
- 🤖 AI Answer System (OpenAI Integration)
- 🔐 Secure API Key Handling via Environment Variables

---

## 🛠️ Tech Stack

- Python 3.x
- speech_recognition
- pyttsx3
- pyautogui
- OpenAI API
- Git & GitHub

---

## 🔐 Environment Setup (IMPORTANT)

This project uses environment variables for security.

### 1️⃣ Set your OpenAI API Key (Windows PowerShell)


```powershell
setx OPENAI_API_KEY "your_api_key_here"
