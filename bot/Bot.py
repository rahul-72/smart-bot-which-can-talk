# Importing useful libraries

import smtplib  # To send email.
import pyttsx3  # For speak engine
import speech_recognition as sr  # For speeh recognition
import datetime
import os
import random


"""*************************************************************************************************************************************"""
def speak(audio):
    engine = pyttsx3.init('sapi5')  # Creating engine for speak.
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    #print(voices[0].id)
    engine.say(audio)
    engine.runAndWait()
	
"""*************************************************************************************************************************************"""

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Dhruva sir. Please tell me how may I help you")

"""*************************************************************************************************************************************"""


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:  # Getting from Microphone
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)  # Listening the input from Microphone
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-in")
        # Jarvis is Recognizing what is said by User.
        print(f"User said:\t {query} \n")
    except Exception as e:
        print("Say that again please.....")
        return "None"
    return query

"""*************************************************************************************************************************************"""


	



def sendEmail(to, content):
	
	server = smtplib.SMTP('smtp.gmail.com', port=587)
	server.ehlo()
	server.starttls()
	
	with open('data/password.txt' ,'r') as file:
		password = file.read()

	with open('data/username.txt' ,'r') as file:
		username = file.read()
	
	
	server.login(username, password)  # Read password from file.
	server.sendmail('charan7rahul@gmail.com', to, content)
	server.close()
	
	
		
"""*************************************************************************************************************************************"""

	

