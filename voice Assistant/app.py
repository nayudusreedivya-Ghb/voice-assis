import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Text-to-speech setup
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I could not understand you.")
        return ""

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return ""


print("================================")
print("       VOICE ASSISTANT")
print("================================")

speak("Hello! I am your voice assistant.")

while True:

    command = listen()

    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    elif "your name" in command:
        speak("I am your Python voice assistant.")

    elif "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye!")
        break

    else:
        speak("Sorry, I don't know that command.")