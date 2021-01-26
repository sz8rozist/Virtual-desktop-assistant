import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

MASTER = "Harry"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(text):
    engine.say(text) 
    engine.runAndWait()

def welcome():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour <12:
        speak("Good Morning" + MASTER)
    elif hour >= 12 and hour <18:
        speak("Good Afternoon"+ MASTER)
    else:
        speak("Good Evening" + MASTER)
    speak("I am jarvis. How may I help you?")
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)    
        print("Say that again please...")   
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smt.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password')
    server.sendmail("harry@codewithharry.com",to,content)
    server.close()
def main():
    speak("Initializing Jarvis.... ")
    welcome()
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak('Searching Wikipedia..')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        url = "youtube.com"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)
    elif 'open google' in query:
        url = "google.com"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)
    elif 'email to harry' in query.lower():
        try:
            speak("What sould I send?")
            content = takeCommand()
            speak("Kinek?")
            to = takeCommand()
            sendEmail(to,content)
            speak("Email has been sent successfully")
        except: Exception as e:
            print(e)
main()