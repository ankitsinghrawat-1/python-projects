import pyttsx3 as pyt
text = input("Enter text to convert to speech: ")
engine = pyt.init()
engine.say(text)
engine.runAndWait()