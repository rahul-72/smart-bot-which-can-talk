
import datetime
import wikipedia  # To search on wikipedia
import webbrowser  # To open website on Browser like youtube, LinkedIn, google etc.
# webbrowser.get('chrome')
import os
import random
from bot import Bot
from bot import Smart


"""***************************************************************************************************************************************"""


# MAIN BODY
if __name__ == '__main__':


    Bot.wishMe()
    while True:
        query = Bot.takeCommand().lower()
        # gettign a string here. Now we will perform our logics.
        # Our logics come here like wikipedia, time, music etc.
        # speak fucntion.
        if "wikipedia" in query:
            try:
                Bot.speak("Searching wikipedia......")
                query = query.replace('wikipedia', "")
                results = wikipedia.summary(query, sentences=2)
                print(results)
                Bot.speak(results)
            except Exception as e:
                Bot.speak("Do not find any result. Search again.....")
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir = "E:\\music"
            songs = os.listdir(music_dir)
            if songs:
                print(songs)
                play_song = random.choice(songs)
                os.startfile(os.path.join(music_dir, play_song))  # Use random module here to select random song.
            else:
                Bot.speak("Your Music Directory is empty...Add some songs in your Directory.")

        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            Bot.speak(f"Sir, the time is {time} ")
        elif "open slack" in query:
            try:
                path = "C:\\Users\\XYZ\\AppData\\Local\\slack\\slack.exe"
                os.startfile(path)
            except Exception as e:
                Bot.speak("Path of slack not found. Set it's path.")

        elif "email to rahul" in query:
            # Make dictionary of name with thier email address.
            try:
                Bot.speak("what should I say? ")
                content = Bot.takeCommand()
                to = "charan7rahul@gmail.com"
                Bot.sendEmail(to, content)
                Bot.speak("Sir, email has been sent!")
            except Exception as e:
                print(e)
                Bot.speak("Sorry Sir, I am not able to send this email. Add password and username in the username.txt and password.txt files")


        elif "quit" in query:
            Bot.speak("Bye Sir")
            break

        else:
            Smart.chat(query)


