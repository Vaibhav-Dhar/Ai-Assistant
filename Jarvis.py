import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
from selenium import webdriver
import os
import subprocess

import pyautogui
import psutil
import pywhatkit as kit
from selenium.webdriver.common.keys import Keys
import cv2
import time
import random
import json

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 170
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    speak("Welcome master!")
    speak("This is Tokyo your AI assistant")

    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour <= 12:
        speak("Good Morning sir!")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon sir!")
    elif hour >= 18 and hour <= 24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

    speak("Tokyo at your service. How may i help you?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)

    except Exception as e:
        print(e)
        speak("Please repeat that one more time...")
        return "None"
    return query


def command():
    command = [' *Search Wikipedia', ' *Play something', ' *Open Youtube', ' *Open Google', ' *Open Gmail',
               ' *Open Linkedin', ' *Open Github', ' *Open Spotify', ' *Open Instagram', ' *Take Screenshot',
               ' *Remeber', ' *Cpu and Battery update', ' *Date', ' *Time', ' *Exit']
    for i in command:
        print(i)


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Jarvis_img\\js.png")


def cpu():
    cpu = str(psutil.cpu_percent())
    print(cpu)
    speak(f"You have used {cpu} of cpu")
    battery = psutil.sensors_battery().percent
    print(battery)
    speak(f"Your current battery in the system is {battery}")


def RockPaperScissors():
    # create a list of play options
    t = ["Rock", "Paper", "Scissors"]

    # assign a random play to the computer
    computer = t[randint(0, 2)]

    # set player to False
    player = False

    while player == False:
        # set player to True
        speak("Choose rock, paper or scissors")
        playerChoice = takecommand()
        if 'rock' in playerChoice:
            player = "Rock"

        elif 'paper' in playerChoice:
            player = "Paper"

        elif 'scissors' in playerChoice:
            player = "Scissors"

        else:
            speak("That's not a valid play. Check your spelling!")

        if player == computer:
            speak("It's a tie, you chose" + player + "and Computer chose" + computer)

        elif player == "Rock":
            if computer == "Paper":
                speak("You lose!" + computer + "covers" + player)
            else:
                speak("You win!" + player + "smashes" + computer)
        elif player == "Paper":
            if computer == "Scissors":
                speak("You lose!" + computer + computer + "cut" + player)
            else:
                speak("You win!" + player + "covers" + computer)
        elif player == "Scissors":
            if computer == "Rock":
                speak("You lose..." + computer + "smashes" + player)
            else:
                speak("You win!" + player + "cut" + computer)

        # player was set to True, but we want it to be False so the loop continues
        speak("Do you wanna play again")
        ChoicePlayAgain = takecommand()
        if 'yes' in ChoicePlayAgain or 'ya' in ChoicePlayAgain:
            ChoicePlayAgain = False

        else:
            ChoicePlayAgain = True
            speak("Exited Rock Paper scissors")
        player = ChoicePlayAgain
        computer = t[randint(0, 2)]


if __name__ == "__main__":

    wishme()

    while True:
        query = takecommand().lower()
        webbrowser = wb

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
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

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Address is {ip}")

        elif 'set an alarm' in query:
            speak("Enter The Time")
            alarm_time = input("Enter the Time:")
            speak("Alarm Set for " + alarm_time)
            while True:
                Time_AC = datetime.datetime.now()
                now = Time_AC.strftime("%H:%M:%S")

                if now == alarm_time:
                    speak("Alarm Over")
                    playsound('alarm.mp3')

                elif now > alarm_time:
                    break

        elif "open google" in query:
            speak("opening google")
            browser = webdriver.Chrome('chromedriver.exe')
            browser.get('https://www.google.com')

        elif "shutdown system" in query:
            speak("Shutting down system")
            os.system("shutdown /s /t 5")

        elif "restart system" in query:
            speak("Restarting system")
            os.system("shutdown /r /t 5")

        elif "sleep" in query and 'system' in query:
            speak("Going to sleep")
            os.system("rundll32.exe powrprof.dll , SetSuspendState 0,1,0")

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

        elif "capture" in query or "photo" in query or "pic" in query or 'picture' in query:
            speak("Press 'P' to take a photo, esc to exit")
            cam = cv2.VideoCapture(0)
            while True:
                _, frame = cam.read()  # We don't want ret in this
                cv2.imshow("Image Preview", frame)  # Show the current frame
                key = cv2.waitKey(1)
                if key == 27:  # If you press Esc then the frame window will close (and the program also)
                    speak("Exited Photo window")
                    break
                elif key == ord('p'):  # If you press p/P key on your keyboard
                    cv2.imwrite("pic.png",
                                frame)  # Save current frame as picture with name pic.jpg
                    time.sleep(0.7)
                    speak("Opening your picture now")
                    os.startfile("pic.png")

            cam.release()
            cv2.destroyAllWindows()

        elif 'jokes' in query:
            with open("text_files/jokes.json", "r", encoding="utf-8") as f:
                jokes_json = json.load(f)
                i = random.randint(1, 386)
                data = jokes_json[i]
                print(f"{data['setup']}\n")
                speak(data['setup'])
                time.sleep(2)
                print(f"{data['punchline']}\n")
                speak(data['punchline'])

        elif 'the time' in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            print(Time)
            speak(Time)

        elif 'date today' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("Today's date is...")
            speak(date)
            speak(month)
            speak(year)

        elif 'play' in query and ('rock' in query or 'paper' in query or 'scissors' in query):
            RockPaperScissors()


        elif 'open github' in query:
            codePath = "C:\\Users\\Vaibhav Dhar\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
            os.startfile(codePath)


        elif 'play spotify' in query:
            os.system("Spotify.lnk")


        elif 'remember that' in query:
            speak("What should i remember sir?")
            data = takecommand()
            speak("You told me to remember that" + data)
            remember = open("data.txt", "w")
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
