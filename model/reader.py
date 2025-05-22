import pyttsx3

def read_text(text: str):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # kecepatan bicara
    engine.setProperty('volume', 0.9)  # volume (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()
