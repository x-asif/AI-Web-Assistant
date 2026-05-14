from assistant.voice import speak
import wikipediaapi

wiki = wikipediaapi.Wikipedia(
    user_agent='AI Assistant',
    language='en'
)


def get_ai_response(message):

    message = message.lower().strip()

    try:

        if "hello" in message:

            answer = "Hello, nice to meet you."

        elif message.startswith("what is"):

            topic = message[8:].strip()

            page = wiki.page(topic)

            answer = page.summary[:500]

        elif message.startswith("who is"):

            topic = message[7:].strip()

            page = wiki.page(topic)

            answer = page.summary[:500]

        else:

            answer = (
                "I am still learning."
            )

    except Exception as e:

        print(e)

        answer = (
            "Sorry, I could not find information."
        )

    speak(answer)

    return answer