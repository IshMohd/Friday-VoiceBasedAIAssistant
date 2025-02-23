import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import responses
from client import aiprocess
from openai import OpenAI
from gtts import gTTS
import os
import pygame
from weather import get_weather

r = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "09346fa657f04c4e91c6350c39639f30"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def handle_unknown_command():
    response = responses.get_response()
    speak(response)
    print(response)  

def processCommand(c):
    print(c)
    
    if "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")
    elif "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com/")        
    
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    elif "weather" in c.lower():
        city = c.split("in")[-1].strip()
        weather_info = get_weather(city)
        speak(weather_info)
        print(weather_info)            

    else:
        
        #This is default Google Gemini Model
        output = aiprocess(c)
        speak(output)
        print(output)
        
        #Generate random response incase AI model is not working
        # handle_unknown_command()        

if __name__ == "__main__":
    speak("Launching Friday.")
    while True:    
        #Listen for the launch word "Friday"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("Recognizing...")       
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "friday"):
                speak("Yes boss.")
                #Listen for command
                with sr.Microphone() as source:
                    print("Friday is active!")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        
        except Exception as e:
            print("Error; {0}".format(e))
                