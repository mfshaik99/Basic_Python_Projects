# Import the necessary libraries
import speech_recognition as sr  # For recognizing speech
import pyautogui  # For typing the text automatically

# Create a Recognizer object
recognizer = sr.Recognizer()

# Use the microphone as the audio input
with sr.Microphone() as source:
    print("Please say something...")
    
    # Listen to the user's voice
    audio = recognizer.listen(source)

# Try to recognize the speech
try:
    # Use Google's speech recognition to convert audio to text
    text = recognizer.recognize_google(audio)
    
    # Print what the user said
    print("You said:", text)
    
    # Type the recognized text wherever the cursor is
    pyautogui.write(text)

# Handle errors if the speech is not clear
except sr.UnknownValueError:
    print("Sorry, I couldn't understand what you said.")

# Handle errors if there's a problem connecting to the recognition service
except sr.RequestError:
    print("There was a problem connecting to the speech recognition service.")
