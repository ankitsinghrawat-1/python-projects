import win32com.client as wincom
def speak_text(text):
        """
        Converts the given text to speech using SAPI.SpVoice.
        """
        speaker = wincom.Dispatch("SAPI.SpVoice")
        speaker.Speak(text)

if __name__ == "__main__":
        message = "Hello, this is a test of SAPI text-to-speech in Python."
        speak_text(message)

        while True:
                user_input = input("Enter text to speak (or '-1' to exit): ")
                if user_input == "-1":
                    break
                speak_text(user_input)