import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import random
import webbrowser
import os

# Functionality of this project
# speak and operate
# wishMe()  will wish according to time ie. good morng good afternoon
# Search anything in wikipidea, print and speak about that upto 1 or any number od sentences
# intro() will introduce about digital assistant
# open google and search anything
# open youtube and play any video
# open stackoverFlow and search content
# play music offline, will randomly play songs from device
# open notepad
# open VS code
# open commond Propmt
# tell date and time
# send Email  (working)
# skype call to some person(working)

# want to add
# auto refresh in windows




engine =pyttsx3.init('sapi5') #microsoft ech api
voices = engine.getProperty('voices')
#print(voices[0].id)  #voices[0].id for male voice
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.setProperty('rate',120)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir..")
    elif hour >=12 and hour<18:
        speak("Good Aftenoon sir")
    else:
        speak("Good Evening Sir")
        
    speak(" ")
    
def takeCommond():
    #it takes microphone input from user
    rm = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        rm.pause_thresold=0.5 #after 1 second of no audio terminate
        audio = rm.listen(source) 

    try:
        print("Recognizing .....")
        query = rm.recognize_google(audio,language='en-IN') #hi-IN
        print(f"User said :{query}\n")

    except Exception:
        #print(e)
        print("Please say it again ...")
        #speak("Sorry Sir Your internet is too week. I can not help you sir")
        return "NONE"
    return query


def intro():
    speak("Sir I'm zoya,I'm 35978621 alfa beta  your digital assistant. i will help you")
    
    

if __name__ == "__main__":

   
    wishMe()
    engine.setProperty('rate',110)
    speak("I am Zoya  sir, How may I help you ")
    #print(datetime.datetime.now())

try:
    while True:
        query=takeCommond().lower()
        if 'wikipedia' in query:
            speak("Sir searching wikipedia")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("Sir According to wikipedia")
            print(result)
            speak(result)
        elif input()=='c':
            quit()

        elif 'open notepad' in query:
            path='C:\\Users\\arpit\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk'
            os.startfile(path)
        
        elif 'command' in query:
            path='C:\\Users\\arpit\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk'
            os.startfile(path)
        
        elif 'vs code' in query:
            path='C:\\Users\\arpit\\AppData\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk'
            os.startfile(path)



        elif 'open youtube' in query:
            speak("Sir what do you want to listen ")
            quest=takeCommond().lower()
            while quest=='none':
                speak("Sir I did not get you please say it again")
                quest=takeCommond().lower()
            quest=quest.replace(" ","+")
            webbrowser.open(f"youtube.com/search?q={quest}")

        elif 'open google' in query:
            speak('what do you want to search ')
            quest = takeCommond().lower()
            while quest=='none':
                speak("Sorry sir, please say it again")
                quest = takeCommond().lower()
                
            webbrowser.open(f"google.com/search?q={quest}")
        
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open stack over flow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'play songs' in query:
            music='C:\\Users\\arpit\\Desktop\\mp3'
            
            songs=os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music,random.choice(songs)))
            #quit()
            
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(strTime)
            speak(f"Sir the time is {strTime}") 

        
        elif 'intro' in query:
            intro()

        elif 'Stop' in query or 'close' in query:
           speak("Okey Sir, I'm going..")
           quit()
            
        elif 'shutdown' in query:
            speak('okay, shutting down')
            os.system('shutdown -s')
except KeyboardInterrupt:
    raise
except:
    print("closed")    






    
    

             
            
        























