# Import the text-to-speech library
import pyttsx3

# Create a text-to-speech engine
engine = pyttsx3.init()

# Ask the user to type some text
text = input("Type something to speak: ")

# Use the engine to say the text
engine.say(text)

# Run the speech engine
engine.runAndWait()
