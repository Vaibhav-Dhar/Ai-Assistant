import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
from selenium import webdriver
import os
import pyautogui
import psutil
import pywhatkit as kit
from selenium.webdriver.common.keys import Keys

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate=170
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    speak("Welcome master!")
    speak("This is Tokyo your AI assistant")
   
    hour=int(datetime.datetime.now().hour)
    if hour>=6 and hour<=12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon sir!")
    elif hour>=18 and hour<=24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")   

    speak("Tokyo at your service. How may i help you?")               

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        print(query)
        
    except Exception as e:
        print(e)
        speak("Please repeat that one more time...")
        return"None"
    return query

def command():
    command=[' *Search Wikipedia',' *Play something',' *Open Youtube',' *Open Google',' *Open Gmail',' *Open Linkedin',' *Open Github',' *Open Spotify',' *Open Instagram',' *Take Screenshot',' *Remeber',' *Cpu and Battery update',' *Date',' *Time',' *Exit']
    for i in command:
        print(i)
        
def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Jarvis_img\\js.png")

    
def cpu():

    cpu=str(psutil.cpu_percent())
    print(cpu)
    speak(f"You have used {cpu} of cpu")
    battery=psutil.sensors_battery().percent
    print(battery)
    speak(f"Your current battery in the system is {battery}")

if __name__=="__main__":

    wishme()
    
    while True:
        query=takecommand().lower()
        webbrowser = wb

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query=query.replace("Wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia...")
            print(results)
            speak(results)

        elif 'play something' in query:
            
            speak("What you want to play")
            query = takecommand().lower()            
            if 'song in youtube' in query:
                speak('Song name please')
                song_name = takecommand()
                browser = webdriver.Chrome('chromedriver.exe')
                browser.get('https://www.youtube.com')
                browser.find_element_by_xpath('//*[@id="search"]').send_keys(song_name)
                browser.find_element_by_xpath('//*[@id="search"]').send_keys(Keys.ENTER)
            
            if 'open youtube' in query:
                speak("opening youtube")
                browser = webdriver.Chrome('chromedriver.exe')
                browser.get('https://www.youtube.com')

       
        elif "open google" in query:
            speak("opening google")
            browser = webdriver.Chrome('chromedriver.exe')
            browser.get('https://www.google.com')
            
        
        elif "open gmail" in query:
            speak("opening gmail")
            browser = webdriver.Chrome('chromedriver.exe')
            browser.get('https://www.gmail.com')


        elif "open linkedin" in query:
            speak("opening linkedin")
            browser = webdriver.Chrome('chromedriver.exe')
            browser.get('https://www.linkedin.com/in/vaibhav-dhar3321/')

            
        elif "open instagram" in query:
            speak("opening instagram")
            browser = webdriver.Chrome('chromedriver.exe')
            browser.get('https://www.instagram.com')
            

        elif 'the time' in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S") 
            print(Time)   
            speak(Time)

        elif 'date today' in query:
            year=int(datetime.datetime.now().year)
            month=int(datetime.datetime.now().month)
            date=int(datetime.datetime.now().day)
            speak("Today's date is...")
            speak(date)
            speak(month)
            speak(year)    

        elif 'open github' in query:
            codePath="C:\\Users\\Vaibhav Dhar\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
            os.startfile(codePath)


        elif 'play spotify' in query:
            os.system("Spotify.lnk")   
    

        elif 'remember that' in query:
            speak("What should i remember sir?")
            data=takecommand()
            speak("You told me to remember that"+data)
            remember=open("data.txt", "w")
            remember.write(data) 
            remember.close()

    
        elif "screenshot" in query:
            screenshot()
            speak("screenshot taken sir!")

        elif "battery" in query:
            cpu()
        
        elif "show commands" in query:
            print(" Please see the above commands to use my services: ")
            speak("Please see the above commands to use my services: ")
            command()

        elif 'exit' in query:
            quit()
