import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate=175
engine.setProperty('rate',newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    speak("Welcome master!")
    speak("This is Tokyo your AI assistant")
    # speak("Today's date is")
    
    # year=int(datetime.datetime.now().year)
    # month=int(datetime.datetime.now().month)
    # date=int(datetime.datetime.now().day)
    # speak(date)
    # speak(month)
    # speak(year)
    # speak("The current time in my watch is")

    hour=int(datetime.datetime.now().hour)
    if hour>=6 and hour<=12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon sir!")
    elif hour>=18 and hour<=24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")   

    speak("I am at your service. How may i help you?")               

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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()    
    
if __name__=="__main__":
    wishme()
    
    while True:
        query=takecommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query=query.replace("Wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia...")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(Time)

        elif 'play spotify' in query:
            webbrowser.open("spotify.com")    

        elif 'email to Vaibhav' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "vaibhavdhar01@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email")        




                






        


        

























