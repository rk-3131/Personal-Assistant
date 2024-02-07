import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# voices are the inbuild voices that are present in the system and hence they can be used to get the voice of the jarvis

# print(voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour <= 2:
        speak("I think you should rest a bit as we know to be healthy you need to sleep")

    elif hour >= 5 and hour < 12:
        speak("Good Morning, have a good day")

    elif hour >= 12 and hour < 6:
        speak("Good evening and I wish you had productive day")

    elif hour >= 6 and hour <=12:
        speak("Have a good productive time")

    speak("Tell me how can I assist you")


def get_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....\n")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....\n")
        query = r.recognize_google(audio_data=audio)
        print(query)
        speak(query)
    
    except Exception as e:
        print(e)
        print("Say it again.....\n")
        return "None"
        
    return query


if __name__ == '__main__':
    # wish_me()
    while True:
        query = get_command()
        print(query)
        # test case for the wikipedia case
        if query.__contains__('wikipedia'):
            print("Searching on wikipedia")
            query = query.replace('wikipedia', '')
            print(query)
            result = wikipedia.summary(query, sentence=2)
            print(result)
            speak(result)
        else:
            speak("If is not executing")