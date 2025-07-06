from win10toast import ToastNotifier
import pyttsx3 as pyt

text = "Time to Drink Water Buddy"
if text.lower() == 'quit' or text.lower() == 'exit':
    print("Exiting the TTS program.")
    exit()
engine = pyt.init()
engine.say(text)
engine.runAndWait()

toaster = ToastNotifier()
toaster.show_toast("DRINK WATER!!",
    "Time to drink water buddy!",
    duration=5)
    