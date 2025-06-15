import pyttsx3 as pyt
while True:
    text = input("Enter text to convert to speech: ")
    engine = pyt.init()
    engine.say(text)
    engine.runAndWait()
    if text.lower() == 'quit' or text.lower() == 'exit':
        print("Exiting the TTS program.")
        break