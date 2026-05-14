import os
import speech_recognition as sr


def speak(text):

    print("Assistant:", text)

    os.system(
        f'powershell -Command "Add-Type -AssemblyName System.Speech; '
        f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\');"'
    )



def take_command():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        audio = r.listen(
            source,
            timeout=5,
            phrase_time_limit=5
        )

    try:

        command = r.recognize_google(audio)

        print("You said:", command)

        return command.lower()

    except Exception as e:

        print(e)

        return ""