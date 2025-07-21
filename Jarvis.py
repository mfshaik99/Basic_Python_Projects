import speech_recognition as sr
import webbrowser
import pyttsx3
from gtts import gTTS
import pygame
import os
import time

# Initialize recognizer and pyttsx3 engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak using gTTS and pygame
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    pygame.mixer.quit()
    os.remove('temp.mp3')

# Function to process and handle user commands
def processCommand(command):
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")
    elif "open chat" in command:
        webbrowser.open("https://chatgpt.com")
    elif "pilot" in command:
        webbrowser.open("https://copilot.microsoft.com")
    elif "the best ever chatbot in the world" in command:
        webbrowser.open("https://x.ai")
    elif "are you ready" in command:
        speak("Yes, I am ready to assist you.")
    elif "gemini" in command:
        webbrowser.open("https://gemini.google.com")
    elif "open stack overflow" in command:
        webbrowser.open("https://stackoverflow.com")
    elif "open deadshot" in command:
        webbrowser.open("https://deadshot.io")
    elif "open github" in command:
        webbrowser.open("https://github.com")
    elif "open code" in command or "open visual studio code" in command:
        os.system("start code")
    elif "open terminal" in command or "open command prompt" in command:
        os.system("start cmd")
    elif "open notepad" in command:
        os.system("start notepad")
    elif "open calculator" in command:
        os.system("start calc")
    elif "open leetcode" in command:
        webbrowser.open("https://leetcode.com")
    elif "end the program" in command:
        speak("Goodbye, Farhan sir!")
        exit()
    else:
        speak("Searching...")
        webbrowser.open(f"https://www.google.com/search?q={command}")

# Main
if __name__ == "__main__":
    speak("Initializing Jarvis. Hello Farhan sir, I am Jarvis, your virtual assistant. How can I help you today?")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=3)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                wake_word = recognizer.recognize_google(audio)

            if wake_word.lower() == "jarvis":
                speak("Yeah")
                with sr.Microphone() as source:
                    print("Listening for your command...")
                    recognizer.adjust_for_ambient_noise(source, duration=3)
                    audio = recognizer.listen(source, timeout=10)
                    command = recognizer.recognize_google(audio)
                    print(f"You said: {command}")
                    processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.WaitTimeoutError:
            print("Listening timed out.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")
