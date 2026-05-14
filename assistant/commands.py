import webbrowser
from assistant.voice import speak


def execute_command(command):

    if 'youtube' in command:

        webbrowser.open('https://youtube.com')

        speak('Opening YouTube')


    elif 'google' in command:

        webbrowser.open('https://google.com')

        speak('Opening Google')


    elif 'how are you' in command or 'how r u' in command:

        speak('I am fine. How can I help you?')


    else:

        speak('Sorry, I did not understand')