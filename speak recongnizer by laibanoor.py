import pyttsx3
import speech_recognition as sr
import pywhatkit as kit
import datetime
import wikipedia
import webbrowser
import openai
import os
import sys


engine = pyttsx3.init()

def speak(text):
    """Function to make the assistant speak."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Function to listen to user's command."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that.")
        return None
    return query.lower()

def wish_user():
    """Function to wish the user based on time of the day."""
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Asslam u Alaikum!")
    elif 12 <= hour < 18:
        speak("good afternoon!")
    else:
        speak("Asslam u Alaikum!")

    speak("How can i help you?")

def handle_query(query):
    """Function to handle different user queries."""
    if 'play' in query:
        song = query.replace('play', '')
        speak(f'Playing {song}')
        kit.playonyt(song)
        
    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {time}")
        
    elif 'open' in query:
        app = query.replace('open', '')
        speak(f"Opening {app}")
        os.system(f"start {app}")

    elif 'wikipedia' in query:
        query = query.replace('wikipedia', '')
        speak(f"Searching Wikipedia for {query}")
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("There were multiple results, please be more specific.")
        except wikipedia.exceptions.HTTPTimeoutError:
            speak("Sorry, there was a timeout error while fetching results.")
            
    elif 'exit' in query or 'quit' in query:
        speak("Goodbye!")
        sys.exit()

    else:
        speak("Sorry, I am not sure how to respond to that.")

def main():
    wish_user()
    
    while True:
        query = take_command()
        if query:
            handle_query(query)

if __name__ == "__main__":
    main()
