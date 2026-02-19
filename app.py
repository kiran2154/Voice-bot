import pyautogui
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import sys
import datetime
import subprocess
from urllib.parse import quote
from openai import OpenAI
import time


class VoiceBot:
    def __init__(self):
        self.name = "Jarvis"

        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

        self.engine.setProperty('rate', 135)
        self.engine.setProperty('volume', 1.0)
        self.client = OpenAI(api_key=os.getenv("o8PGmNTl-VjlXIKktPRxX4IGEmB5ZAtiiF1bSNqLpHy4WJUO2_tt8peQeDLkiEq4Ih1LQYHG_1T3BlbkFJvVxCp3PRyB6KdeeH9P_2nCp9v2eoIqiWIN11MwbplZZE8REmBZmRt_jHQYHSLXF1NdMvgucEwA"))
        self.websites = {
            'youtube': 'https://www.youtube.com',
            'google': 'https://www.google.com',
            'facebook': 'https://www.facebook.com',
            'twitter': 'https://www.twitter.com',
            'instagram': 'https://www.instagram.com',
            'github': 'https://www.github.com',
            'reddit': 'https://www.reddit.com',
            'wikipedia': 'https://www.wikipedia.com',
            'gmail': 'https://www.gmail.com'
        }

        # Application paths
        self.apps = {
            'tlauncher': r"C:\Users\kiran\AppData\Roaming\.minecraft\TLauncher.exe"
        }

    # ---------------- SPEAK ----------------
    def speak(self, text):
        print(f"{self.name}: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
        # -------- SYSTEM CONTROLS --------

    def volume_up(self):
        pyautogui.press("volumeup")
        self.speak("Increasing volume.")

    def volume_down(self):
        pyautogui.press("volumedown")
        self.speak("Decreasing volume.")

    def mute_volume(self):
        pyautogui.press("volumemute")
        self.speak("Volume muted.")

    def take_screenshot(self):
        screenshot = pyautogui.screenshot()
        file_name = f"screenshot_{int(time.time())}.png"
        screenshot.save(file_name)
        self.speak("Screenshot captured.")

    def lock_screen(self):
        os.system("rundll32.exe user32.dll,LockWorkStation")
        self.speak("Locking the system.")

    # ---------------- LISTEN ----------------
    def listen(self):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=6)

            text = self.recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text.lower()

        except sr.UnknownValueError:
            self.speak("I did not catch that.")
        except sr.RequestError:
            self.speak("Speech recognition service is unavailable.")
        except Exception:
            self.speak("An unexpected error occurred.")
        return None

    # ---------------- WEBSITE ----------------
    def open_website(self, website, query=None):
        if website in self.websites:
            url = self.websites[website]

            if query:
                if website == 'youtube':
                    url += f"/results?search_query={quote(query)}"
                elif website == 'google':
                    url += f"/search?q={quote(query)}"

            webbrowser.open(url)
            self.speak(f"Opening {website}")
        else:
            self.speak("Website not found.")

    # ---------------- APPLICATION ----------------
    def open_application(self, app):
        try:
            if app == 'notepad':
                os.system('notepad')
                self.speak("Opening Notepad")

            elif app == 'calculator':
                os.system('calc')
                self.speak("Opening Calculator")

            elif app == 'command prompt':
                os.system('start cmd')
                self.speak("Opening Command Prompt")

            elif app == 'tlauncher':
                subprocess.Popen(self.apps['tlauncher'])
                self.speak("Launching TLauncher. Enjoy your game, sir.")

            else:
                self.speak("Application not supported.")

        except Exception:
            self.speak("Unable to open the application.")

    # ---------------- TIME & DATE ----------------
    def get_time(self):
        now = datetime.datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {now}")

    def get_date(self):
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        self.speak(f"Today is {today}")
        
    def ask_ai(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are Jarvis, a calm and intelligent AI assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200
            )

            answer = response.choices[0].message.content
            self.speak(answer)

        except Exception as e:
            self.speak("I am unable to connect to my intelligence core.")


    def process_command(self, command):
        if command is None:
            return

        # Wake word
        if "jarvis" not in command:
            return

        command = command.replace("jarvis", "").strip()

        if 'hello' in command or 'hi' in command:
            self.speak("At your service, sir.")

        elif 'time' in command:
            self.get_time()

        elif 'date' in command:
            self.get_date()
        
        elif 'volume up' in command:
            self.volume_up()

        elif 'volume down' in command:
            self.volume_down()

        elif 'mute' in command:
            self.mute_volume()

        elif 'screenshot' in command:
            self.take_screenshot()

        elif 'lock' in command:
            self.lock_screen()


        elif 'google' in command:
            query = command.replace('google', '').replace('search', '').replace('for', '').strip()
            if query:
                self.speak(f"Searching Google for {query}")
                self.open_website('google', query)
            else:
                self.open_website('google')

        elif 'youtube' in command:
            query = command.replace('youtube', '').replace('search', '').replace('play', '').strip()
            if query:
                self.speak(f"Searching YouTube for {query}")
                self.open_website('youtube', query)
            else:
                self.open_website('youtube')

        elif 'open' in command:
            if 'notepad' in command:
                self.open_application('notepad')
            elif 'calculator' in command:
                self.open_application('calculator')
            elif 'command prompt' in command or 'cmd' in command:
                self.open_application('command prompt')
            elif 'tlauncher' in command or 'minecraft' in command:
                self.open_application('tlauncher')
            elif 'open' in command:
                for site in self.websites.keys():
                    if site in command:
                        self.open_website(site)
                        return

            else:
                self.speak("I cannot open that yet.")

        elif 'exit' in command or 'quit' in command or 'bye' in command:
            self.speak("Turning off. Goodbye, sir.")
            time.sleep(0.5)
            self.engine.stop()
            sys.exit()

        else:
            self.ask_ai(command)

    # ---------------- RUN ----------------
    def run(self):
        self.speak("Jarvis online")
        while True:
            command = self.listen()
            if command:
                self.process_command(command)

def main():
    try:
        bot = VoiceBot()
        bot.run()
    except KeyboardInterrupt:
        print("\nJarvis stopped.")


if __name__ == "__main__":
    main()