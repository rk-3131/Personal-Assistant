import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

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
        # print(query)
        # speak(query)
    
    except Exception as e:
        print(e)
        print("Say it again.....\n")
        return "None"
        
    return query


if __name__ == '__main__':
    brave_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
    webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))

    # wish_me()
    while True:
        query = get_command()
        print(query)
        query = query.lower()
        if 'jarvis quit' in query:
            speak("Yes I am shutting down")
            break
        # test case for the wikipedia case
        if 'wikipedia' in query: 
            print("Searching on wikipedia")
            query = query.replace('wikipedia', '')
            query = query.replace('on', '')
            result = wikipedia.summary(query, sentences=2)
            try:
                print(result.encode('utf-8'))
            except UnicodeEncodeError:
                pass
            speak(result)
        
        elif 'open youtube' in query:
            webbrowser.get('brave').open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.get('brave').open('google.com')
        
        elif 'open chatgpt' in query or 'open chat gpt' in query:
            webbrowser.get('brave').open('chat.openai.com')
        
        elif 'open gfg' in query or 'open geeks for geeks' in query or 'open geeksforgeeks' in query:
            webbrowser.get('brave').open('geeksforgeeks.org')

        elif 'open mails' in query or 'open mail' in query:
            webbrowser.get('brave').open('https://mail.google.com/mail/u/0/#inbox')
            webbrowser.get('brave').open('https://mail.google.com/mail/u/1/#inbox')
        
        elif 'open vs code' in query or 'open code' in query:
            code_path = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        
        elif 'open idea' in query:
            idea_path = "C:\\Program Files\\JetBrains\IntelliJ IDEA Community Edition 2021.3.1\\bin\\idea64.exe"
            os.startfile(idea_path)

        elif 'i want to compose email' in query or 'i want to send email' in query:
            webbrowser.get('brave').open('mail.google.com/mail/u/0/?ogbl#inbox?compose=new')
