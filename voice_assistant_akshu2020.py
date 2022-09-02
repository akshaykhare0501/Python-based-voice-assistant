'''
Project: Python Based AI Voice Assistant
@author: Akshay Dattatray Khare
'''
try: 
    import pyttsx3
    import speech_recognition as sr
    import datetime 
    from datetime import date
    import calendar
    import time
    import math
    import wikipedia
    import webbrowser
    from gtts import gTTS
    from playsound import  playsound
    import os
    import smtplib
    import winsound
    import urllib.request
    import pyautogui
    import pywhatkit
    import cv2
    import pyqrcode
    import png
    import turtle
    from pyqrcode import QRCode
    from pygame import mixer
    from PIL import Image ,ImageChops
    from tkinter import *
    import tkinter.messagebox as message
    from pytube import YouTube
    from sqlite3 import *
except Exception as e:
    print(e)

conn = connect("voice_assistant_asked_questions.db")

conn.execute("CREATE TABLE IF NOT EXISTS `voicedata`(id INTEGER PRIMARY KEY AUTOINCREMENT,command VARCHAR(201))")

conn.execute("CREATE TABLE IF NOT EXISTS `review`(id INTEGER PRIMARY KEY AUTOINCREMENT, review VARCHAR(50), type_of_review VARCHAR(50))")

conn.execute("CREATE TABLE IF NOT EXISTS `emoji`(id INTEGER PRIMARY KEY AUTOINCREMENT,emoji VARCHAR(201))")

global query
global Query
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def detect_face():
    cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frames = video_capture.read()

        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
                )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frames)
        speak("detecting face")
        print("Detecting face.....")
        time.sleep(10)      
        pyautogui.press('q')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am voice assistant Akshu2020 Sir. Please tell me how may I help you.")
    
def takeCommand():
    global query
    
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        r.adjust_for_ambient_noise(source)
        #r.energy_threshold = 450
        print("Listening...")
        r.pause_threshold = 0.9 
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        #print(e)     
        print("Say that again please...")        
        return "None"    
    return query

def takeCommandHindi():
    
	r = sr.Recognizer()
	with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source)
		print('Listening')
		r.pause_threshold = 0.7
		audio = r.listen(source)
		try:
			print("Recognizing")
			Query = r.recognize_google(audio, language='hi-In')
			print("the query is printed='", Query, "'")
		
		except Exception as e:
			#print(e)
			print("Say again...")
			return "None"
		return Query

def calculator():
    global query
    try:
        if 'add' in query or 'edi' in query:
            speak('Enter a number')
            a = float(input("Enter a number:"))
            speak('Enter another number to add')
            b = float(input("Enter another number to add:"))
            c = a+b
            print(f"{a} + {b} = {c}")
            speak(f'The addition of {a} and {b} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                
        elif 'sub' in query:
            speak('Enter a number')
            a = float(input("Enter a number:"))
            speak('Enter another number to subtract')
            b = float(input("Enter another number to subtract:"))
            c = a-b
            print(f"{a} - {b} = {c}")
            speak(f'The subtraction of {a} and {b} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                    
        elif 'mod' in query:
            speak('Enter a number')
            a = float(input("Enter a number:"))
            speak('Enter another number')
            b = float(input("Enter another number:"))
            c = a%b
            print(f"{a} % {b} = {c}")
            speak(f'The modular division of {a} and {b} is equal to {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                    
        elif 'div' in query:
            speak('Enter a number as dividend')
            a = float(input("Enter a number:"))
            speak('Enter another number as divisor')
            b = float(input("Enter another number as divisor:"))
            c = a/b
            print(f"{a} / {b} = {c}")
            speak(f'{a} divided by {b} is equal to {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'multi' in query:
            speak('Enter a number')
            a = float(input("Enter a number:"))
            speak('Enter another number to multiply')
            b = float(input("Enter another number to multiply:"))
            c = a*b
            print(f"{a} x {b} = {c}")
            speak(f'The multiplication of {a} and {b} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'square root' in query:
            speak('Enter a number to find its sqare root')
            a = float(input("Enter a number:"))
            c = a**(1/2)
            print(f"Square root of {a} = {c}")
            speak(f'Square root of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'square' in query:
            speak('Enter a number to find its sqare')
            a = float(input("Enter a number:"))
            c = a**2
            print(f"{a} x {a} = {c}")
            speak(f'Square of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'cube root' in query:
            speak('Enter a number to find its cube root')
            a = float(input("Enter a number:"))
            c = a**(1/3)
            print(f"Cube root of {a} = {c}")
            speak(f'Cube root of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'cube' in query:
            speak('Enter a number to find its sqare')
            a = float(input("Enter a number:"))
            c = a**3
            print(f"{a} x {a} x {a} = {c}")
            speak(f'Cube of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                
        elif 'fact' in query:
            try:
                n = int(input('Enter the number whose factorial you want to find:'))
                fact = 1
                for i in range(1,n+1):
                    fact = fact*i
                print(f"{n}! = {fact}")
                speak(f'{n} factorial is equal to {fact}. Your answer is {fact}.')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            except Exception as e:
                #print(e)
                speak('I unable to calculate its factorial.')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
                    
        elif 'power' in query or 'raise' in query:
            speak('Enter a number whose power you want to raised')
            a = float(input("Enter a number whose power to be raised :"))
            speak(f'Enter a raised power to {a}')
            b = float(input(f"Enter a raised power to {a}:"))
            c = a**b
            print(f"{a} ^ {b} = {c}")
            speak(f'{a} raise to the power {b} = {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        
                
        elif 'percent' in query:
            speak('Enter a number whose percentage you want to calculate')
            a = float(input("Enter a number whose percentage you want to calculate :"))
            speak(f'How many percent of {a} you want to calculate?')
            b = float(input(f"Enter how many percentage of {a} you want to calculate:"))
            c = (a*b)/100
            print(f"{b} % of {a} is {c}")
            speak(f'{b} percent of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
            
        elif 'interest' in query:
            speak('Enter the principal value or amount')
            p = float(input("Enter the principal value (P):"))
            speak('Enter the rate of interest per year')
            r = float(input("Enter the rate of interest per year (%):"))
            speak('Enter the time in months')
            t = int(input("Enter the time (in months):"))            
            interest = (p*r*t)/1200
            sint = round(interest)
            fv = round(p + interest) 
            print(f"Interest = {interest}")
            print(f"The total amount accured, principal plus interest, from simple interest on a principal of {p} at a rate of {r}% per year for {t} months is {p + interest}.")
            speak(f'interest is {sint}. The total amount accured, principal plus interest, from simple interest on a principal of {p} at a rate of {r}% per year for {t} months is {fv}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                
        
    
        elif 'si' in query:
            speak('Enter the angle in degree to find its sine value')
            a = float(input("Enter the angle:"))
            b = a * 3.14/180
            c = math.sin(b)
            speak('Here is your answer.')
            print(f"sin({a}) = {c}")
            speak(f'sin({a}) = {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'cos' in query:
            speak('Enter the angle in degree to find its cosine value')
            a = float(input("Enter the angle:"))
            b = a * 3.14/180
            c = math.cos(b)
            speak('Here is your answer.')
            print(f"cos({a}) = {c}")
            speak(f'cos({a}) = {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                
        elif 'cot' in query or 'court' in query:
            try:
                speak('Enter the angle in degree to find its cotangent value')
                a = float(input("Enter the angle:"))
                b = a * 3.14/180
                c = 1/math.tan(b)
                speak('Here is your answer.')
                print(f"cot({a}) = {c}")
                speak(f'cot({a}) = {c}')
                
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            except Exception as e:
                print("infinity")
                speak('Answer is infinity')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
                
            
                
        elif 'tan' in query or '10' in query:
            speak('Enter the angle in degree to find its tangent value')
            a = float(input("Enter the angle:"))
            b = a * 3.14/180
            c = math.tan(b)
            speak('Here is your answer.')
            print(f"tan({a}) = {c}")
            speak(f'tan({a}) = {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        
                
        elif 'cosec' in query:
            try:
                speak('Enter the angle in degree to find its cosecant value')
                a = float(input("Enter the angle:"))
                b = a * 3.14/180
                c =1/ math.sin(b)
                speak('Here is your answer.')
                print(f"cosec({a}) = {c}")
                speak(f'cosec({a}) = {c}')
                
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            except Exception as e:
                print('Infinity')
                speak('Answer is infinity')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
                    
        elif 'caus' in query:
            try:
                speak('Enter the angle in degree to find its cosecant value')
                a = float(input("Enter the angle:"))
                b = a * 3.14/180
                c =1/ math.sin(b)
                speak('Here is your answer.')
                print(f"cosec({a}) = {c}")
                speak(f'cosec({a}) = {c}')
                
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            except Exception as e:
                print('Infinity')
                speak('Answer is infinity')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
                
        elif 'sec' in query:
            try:
                speak('Enter the angle in degree to find its secant value')
                a = int(input("Enter the angle:"))
                b = a * 3.14/180
                c = 1/math.cos(b)
                speak('Here is your answer.')
                print(f"sec({a}) = {c}")
                speak(f'sec({a}) = {c}')
                
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            except Exception as e:
                print('Infinity')
                speak('Answer is infinity')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            
                
    except Exception as e:
        speak('I unable to do this calculation.')
        speak('Do you want to do another calculation?')
        query = takeCommand().lower()
        if 'y' in query:
            speak('ok which calculation you want to do?')
            query = takeCommand().lower()
            calculator()
        else:
            speak('ok')
        
        
        
def callback(r,c):
    global player
    
    if player == 'X' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text='X',fg='blue', bg='white')
        states[r][c] = 'X'
        player = 'O'
        
    if player == 'O' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text='O',fg='red', bg='yellow')
        states[r][c] = 'O'
        player = 'X'
    check_for_winner()
    
def check_for_winner():
    global stop_game
    global root
    for i in range(3):
        if states[i][0] == states[i][1]== states[i][2]!=0:
            b[i][0].config(bg='grey')
            b[i][1].config(bg='grey')
            b[i][2].config(bg='grey')
            
            stop_game = True
            
            root.destroy()
            
        if states[0][i] == states[1][i] == states[2][i]!= 0:
            b[0][i].config(bg='grey')
            b[1][i].config(bg='grey')
            b[2][i].config(bg='grey')
            
            stop_game = True
            
            root.destroy()
        
        if states[0][0] == states[1][1]== states[2][2]!= 0:
            b[0][0].config(bg='grey') 
            b[1][1].config(bg='grey')
            b[2][2].config(bg='grey')
            
            stop_game = True
            
            root.destroy()
            
        if states[2][0] == states[1][1] == states[0][2]!= 0:
            b[2][0].config(bg='grey')
            b[1][1].config(bg='grey')
            b[0][2].config(bg='grey')
            
            stop_game = True
            
            root.destroy()

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('akshaykhare0501@gmail.com','Akshay@123')
    server.sendmail('akshaykhare0501@gmail.com',to,content)
    server.close()
    
def brightness():
    try:
        query = takeCommand().lower()
        if '25' in query:
            pyautogui.moveTo(1780,1050) 
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1605,820)
            pyautogui.click()
            pyautogui.moveTo(1780,1050) 
            pyautogui.click()
            speak('If you again want to change brihtness, say, change brightness')
        elif '50' in query:
            pyautogui.moveTo(1780,1050) 
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1684,960)   
            pyautogui.click()
            pyautogui.moveTo(1780,1050) 
            pyautogui.click()
            speak('If you again want to change brihtness, say, change brightness')
        elif '75' in query:
            pyautogui.moveTo(1780,1050) 
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1758,960)   
            pyautogui.click()
            pyautogui.moveTo(1780,1050) 
            pyautogui.click()
            speak('If you again want to change brihtness, say, change brightness')
        elif '100' in query or 'full' in query:
            pyautogui.moveTo(1780,1050) 
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1835,960)   
            pyautogui.click()
            pyautogui.moveTo(1780,1050) 
            pyautogui.click()
            speak('If you again want to change brihtness, say, change brightness')
        else: 
            speak('Please select 25, 50, 75 or 100....... Say again.')
            brightness()
    except Exception as e:
        #print(e)
        speak('Something went wrong')
        
def close_window():
    try: 
        if 'y' in query:
            pyautogui.moveTo(1885,10)
            pyautogui.click()
        else:
            speak('ok')
            pyautogui.moveTo(1000,500)
    except Exception as e:
        #print(e)
        speak('error')
        
def whatsapp():
    query = takeCommand().lower()
    if 'y' in query:
        pyautogui.moveTo(250,1200) 
        pyautogui.click()
        time.sleep(1)
        pyautogui.write('whatsapp')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.moveTo(100,140)   
        pyautogui.click() 
        speak('To whom you want to send message,.....just write the name here in 5 seconds')
        time.sleep(7)
        pyautogui.moveTo(120,300)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(800,990)
        pyautogui.click()
        speak('Say the message,....or if you want to send anything else,...say send document, or say send emoji')
        query = takeCommand()
        if ('sent' in query or 'send' in query) and 'document' in query:
            pyautogui.moveTo(660,990)   
            pyautogui.click() 
            time.sleep(1)
            pyautogui.moveTo(660,740)
            pyautogui.click()
            speak('please select the document within 10 seconds')
            time.sleep(12)
            speak('Should I send this document?')
            query = takeCommand().lower()
            if 'y' in query and 'no' not in query:
                speak('sending the document......')
                pyautogui.press('enter')
                speak('Do you want to send message again to anyone?')
                whatsapp()
            elif ('remove' in query or 'cancel' in query or 'delete' in query or 'clear' in query) and ('document' in query or 'message' in query or 'it' in query or 'emoji' in query or 'select' in query):
                pyautogui.doubleClick(x=800, y=990)
                pyautogui.press('backspace')
                speak('Do you want to send message again to anyone?')
                whatsapp()
            else:
                speak('ok')
        elif ('sent' in query or 'send' in query) and 'emoji' in query:
            pyautogui.moveTo(620,990)  
            pyautogui.click() 
            pyautogui.moveTo(670,990)
            pyautogui.click()
            pyautogui.moveTo(650,580) 
            pyautogui.click()
            speak('please select the emoji within 10 seconds')
            time.sleep(11)
            speak('Should I send this emoji?')
            query = takeCommand().lower()
            if 'y' in query and 'no' not in query:
                speak('Sending the emoji......')
                pyautogui.press('enter')
                speak('Do you want to send message again to anyone?')
                whatsapp()
            elif ('remove' in query or 'cancel' in query or 'delete' in query or 'clear' in query) and ('message' in query or 'it' in query or 'emoji' in query or 'select' in query):
                pyautogui.doublClick(x=800, y=990)
                speak('Do you want to send message again to anyone?')
                whatsapp()
            else:
                speak('ok')
        else:
            pyautogui.write(f'{query}')
            speak('Should I send this message?')
            query = takeCommand().lower()
            if 'y' in query and 'no' not in query:
                speak('sending the message......')
                pyautogui.press('enter')
                speak('Do you want to send message again to anyone?')
                whatsapp()
            elif ('remove' in query or 'cancel' in query or 'delete' in query or 'clear' in query) and ('message' in query or 'it' in query or 'select' in query):
                pyautogui.doubleClick(x=800, y=990)               
                pyautogui.press('backspace')
                speak('Do you want to send message again to anyone?')
                whatsapp()
            else:
                speak('ok')
    else:
        speak('ok')
        
def alarm():
    root = Tk() 
    root.title('Akshu2020 Alarm-Clock') 
    speak('Please enter the time in the format hour, minutes and seconds. When the alarm should rang?')
    speak('Please enter the time greater than the current time')
    def setalarm():
        alarmtime = f"{hrs.get()}:{mins.get()}:{secs.get()}"
        print(alarmtime)
        if(alarmtime!="::"):
            alarmclock(alarmtime) 
        else:
            speak('You have not entered the time.')
    def alarmclock(alarmtime): 
        while True:
            time.sleep(1)
            time_now=datetime.datetime.now().strftime("%H:%M:%S")
            print(time_now)
            if time_now == alarmtime:
                Wakeup=Label(root, font = ('arial', 20, 'bold'), text="Wake up! Wake up! Wake up",bg="DodgerBlue2",fg="white").grid(row=6,columnspan=3)
                speak("Wake up, Wake up")
                print("Wake up!")           
                mixer.init()
                mixer.music.load(r'C:\Users\Admin\Music\Playlists\wake-up-will-you-446.mp3')
                mixer.music.play()
                break
        speak('you can click on close icon to close the alarm window.')
    hrs=StringVar()
    mins=StringVar()
    secs=StringVar()
    greet=Label(root, font = ('arial', 20, 'bold'),text="Take a short nap!").grid(row=1,columnspan=3)
    hrbtn=Entry(root,textvariable=hrs,width=5,font =('arial', 20, 'bold'))
    hrbtn.grid(row=2,column=1)
    minbtn=Entry(root,textvariable=mins, width=5,font = ('arial', 20, 'bold')).grid(row=2,column=2)
    secbtn=Entry(root,textvariable=secs, width=5,font = ('arial', 20, 'bold')).grid(row=2,column=3)
    setbtn=Button(root,text="set alarm",command=setalarm,bg="DodgerBlue2", fg="white",font = ('arial', 20, 'bold')).grid(row=4,columnspan=3)
    timeleft = Label(root,font=('arial', 20, 'bold')) 
    timeleft.grid()
  
    mainloop()

'''def image_difference():
    os.startfile('C:\\Users\\Admin\\OneDrive\\Pictures\\Saved Pictures\\difference1.jpg')
    os.startfile('C:\\Users\\Admin\\OneDrive\\Pictures\\Saved Pictures\\difference2.jpg')

    time.sleep(5)
    speak('If you want answer then say, show answer')
    query = takeCommand().lower()
    if 'show' in query and 'answer' in query:
        img1=Image.open("C:\\Users\\Admin\\OneDrive\\Pictures\\Saved Pictures\\difference1.jpg")
        img2=Image.open("C:\\Users\\Admin\\OneDrive\\Pictures\\Saved Pictures\\difference2.jpg")
        diff=ImageChops.difference(img1,img2)
        if diff.getbbox():
            f.show()     
        time.sleep(10)
    else:
        speak('ok, I will wait for 30 seconds, then I will show you the answer.')
        time.sleep(30)
        img1=Image.open("C:\\Users\\Admin\\OneDrive\\Pictures\\Saved Pictures\\difference1.jpg")
        img2=Image.open("C:\\Users\\Admin\\OneDrive\\Pictures\\Saved Pictures\\difference2.jpg")
        diff=ImageChops.difference(img1,img2)
        if diff.getbbox():
            f.show()     
        time.sleep(10)
'''   
        
def select1():
    global vs
    global root3
    global type_of_review 

    if vs.get() == 1:
        message.showinfo(" ","Thank you for your review!!")
        review = "Very Satisfied"
        type_of_review = "Positive"
        root3.destroy()   
    elif vs.get() == 2:
        message.showinfo(" ","Thank you for your review!!")
        review = "Satisfied"
        type_of_review = "Positive"
        root3.destroy()
    elif vs.get() == 3:
        message.showinfo(" ","Thank you for your review!!!!")
        review = "Neither Satisfied Nor Dissatisfied"
        type_of_review = "Neutral"
        root3.destroy()
    elif vs.get() == 4:
        message.showinfo(" ","Thank you for your review!!")
        review = "Dissatisfied"
        type_of_review = "Negative"
        root3.destroy()
    elif vs.get() == 5:
        message.showinfo(" ","Thank you for your review!!") 
        review = "Very Dissatisfied"
        type_of_review = "Negative"
        root3.destroy()
    elif vs.get() == 6:
        message.showinfo(" ","    Ok    ") 
        review = "I do not want to give review"
        type_of_review = "No review"
        root3.destroy()
    try:
        conn.execute(f"INSERT INTO `review`(review,type_of_review) VALUES('{review}', '{type_of_review}')")
        conn.commit()                
    except Exception as e:
        pass

def select_review():
    global root3
    global vs
    global type_of_review
    root3 = Tk()
    root3.title("Select an option")
    
    vs = IntVar()
    string = "Are you satisfied with my performance?"
    msgbox = Message(root3,text=string)
    msgbox.config(bg="lightgreen",font = "(20)")
    msgbox.grid(row=0,column=0)
    rs1=Radiobutton(root3,text="Very Satisfied",font="(20)",value=1,variable=vs).grid(row=1,column=0,sticky=W)
    rs2=Radiobutton(root3,text="Satisfied",font="(20)",value=2,variable=vs).grid(row=2,column=0,sticky=W)
    rs3=Radiobutton(root3,text="Neither Satisfied Nor Dissatisfied",font="(20)",value=3,variable=vs).grid(row=3,column=0,sticky=W)
    rs4=Radiobutton(root3,text="Dissatisfied",font="(20)",value=4,variable=vs).grid(row=4,column=0,sticky=W)
    rs5=Radiobutton(root3,text="Very Dissatisfied",font="(20)",value=5,variable=vs).grid(row=5,column=0,sticky=W)
    rs6=Radiobutton(root3,text="I don't want to give review",font="(20)",value=6,variable=vs).grid(row=6,column=0,sticky=W)

    bs = Button(root3,text="Submit",font="(20)",activebackground="yellow",activeforeground="green",command=select1)
    bs.grid(row=7,columnspan=2)
    
    root3.mainloop()
    
def net_connection(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
    
def rainbow_benzene():
    try: 
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
        t = turtle.Pen()
        turtle.bgcolor('black')
        for x in range(180):
	        t.pencolor(colors[x%6])
	        t.width(x/100 + 1)
	        t.forward(x)
	        t.left(59)
        time.sleep(7)
        turtle.bye()
    except Exception as e:
        print(e)
        speak('Sorry, some error occured!!')
        
if __name__ == "__main__":
    global Query
    detect_face()
    wishMe()
    said = True
    while said:

        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'translat' in query or ('let' in query and 'translat' in query and 'open' in query):
            webbrowser.open('https://translate.google.co.in')
            time.sleep(10)
        elif 'open map' in query or ('let' in query and 'map' in query and 'open' in query):
            webbrowser.open('https://www.google.com/maps')
            time.sleep(10)
        elif ('open' in query and 'youtube' in query) or ('let' in query and 'youtube' in query and 'open' in query):
            webbrowser.open('youtube.com')
            time.sleep(10)
        
        elif 'chrome' in query:
            webbrowser.open('chrome.com')
            time.sleep(10)
        elif 'weather' in query:            
            webbrowser.open('https://www.yahoo.com/news/weather')
            time.sleep(3)
            speak('Click on, change location, and enter the city , whose whether conditions you want to know.')
            time.sleep(10)

        elif 'google map' in query:
            webbrowser.open('https://www.google.com/maps')
            time.sleep(10)
        elif 'excel' in query:
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk')
            time.sleep(5)
        
        elif ('open' in query and 'google' in query) or ('let' in query and 'google' in query and 'open' in query):
            webbrowser.open('google.com')
            time.sleep(10)       
       
        elif ('open' in query and 'stack' in query and 'overflow' in query) or ('let' in query and 'stack' in query and 'overflow' in query and 'open' in query):
            webbrowser.open('stackoverflow.com')
            time.sleep(10)
        elif 'open v i' in query or 'open vi' in query or 'open vierp' in query or ('open' in query and ('r p' in query or 'rp' in query)):
            webbrowser.open('https://www.vierp.in/login/erplogin')
            time.sleep(10)
            
        elif 'news' in query:
            webbrowser.open('https://www.bbc.com/news/world')
            time.sleep(10)
            
        elif 'online shop' in query or (('can' in query or 'want' in query or 'do' in query or 'could' in query) and 'shop' in query) or('let' in query and 'shop' in query):
            speak('From which online shopping website, you want to shop? Amazon, flipkart, snapdeal or naaptol?')
            query = takeCommand().lower()
            if 'amazon' in query:
                webbrowser.open('https://www.amazon.com')
                time.sleep(10)
            elif 'flip' in query:
                webbrowser.open('https://www.flipkart.com')
                time.sleep(10)
            elif 'snap' in query:
                webbrowser.open('https://www.snapdeal.com')  
                time.sleep(10)
            elif 'na' in query:
                webbrowser.open('https://www.naaptol.com')  
                time.sleep(10)            
            else:
                speak('Sorry sir, you have to search in browser as his shopping website is not reachable for me.')
        elif ('online' in query and ('game' in query or 'gaming' in query)):
            webbrowser.open('https://www.agame.com/games')
            time.sleep(10)
        elif 'dictionary' in query:
            webbrowser.open('https://www.dictionary.com')
            time.sleep(3)
            speak('Enter the word, in the search bar of the dictionary, whose defination or synonyms you want to know')
            time.sleep(15)
        elif 'youtube' in query and 'video' in query and 'convert' in query and 'audio' in query:
            video_url = input('Enter YouTube video URL: ')

            if os.name == 'nt':
                path = os.getcwd() + '\\'
            else:
                path = os.getcwd() + '/'

            name = pytube.extract.video_id(video_url)
            YouTube(video_url).streams.filter(only_audio=True).first().download(filename=name)
            location = path + name + '.mp4'
            renametomp3 = path + name + '.mp3'

            if os.name == 'nt':
                os.system('ren {0} {1}'. format(location, renametomp3))
            else:
                os.system('mv {0} {1}'. format(location, renametomp3))    
            
        elif 'face' in query and ('detect' in query or 'identif' in query or 'point' in query or 'highlight' in query or 'focus' in query):
            speak('yes')
            detect_face()
            
        elif ('identif' in query and 'emoji' in query) or ('sentiment' in query and ('analysis' in query or 'identif' in query)):
            speak('Please enter only one emoji at a time.')
            emoji = input('enter emoji here: ')
            if '😀' in emoji or '😃' in emoji or '😄' in emoji or '😁' in emoji or '🙂' in emoji or '😊' in emoji or '☺️' in emoji or '😇' in emoji or '🥲' in emoji:
                speak('happy')
                print('Happy')
            elif '😝' in emoji or '😆' in emoji or '😂' in emoji or '🤣' in emoji:
                speak('Laughing')
                print('Laughing')
            elif '😡' in emoji or '😠' in emoji or '🤬' in emoji:
                speak('Angry')
                print('Angry')
            elif '🤫' in emoji:
                speak('Keep quite')
                print('Keep quite')
            elif '😷' in emoji:
                speak('face with mask')
                print('Face with mask')
            elif '🥳' in emoji:
                speak('party')
                print('party')
            elif '😢' in emoji or '😥' in emoji or '😓' in emoji or '😰' in emoji or '☹️' in emoji or '🙁' in emoji or '😟' in emoji or '😔' in emoji or '😞️' in emoji:
                speak('Sad')
                print('Sad')
            elif '😭' in emoji:
                speak('Crying')
                print('Crying')
            elif '😋' in emoji:
                speak('Tasty')
                print('Tasty')
            elif '🤨' in emoji:
                speak('Doubt')
                print('Doubt')
            elif '😴' in emoji:
                speak('Sleeping')
                print('Sleeping')
            elif '🥱' in emoji:
                speak('feeling sleepy')
                print('feeling sleepy')
            elif '😍' in emoji or '🥰' in emoji or '😘' in emoji:
                speak('Lovely')
                print('Lovely')
            elif '😱' in emoji:
                speak('Horrible')
                print('Horrible')
            elif '🎂' in emoji:
                speak('Cake')
                print('Cake')
            elif '🍫' in emoji:
                speak('Cadbury')
                print('Cadbury')
            elif '🇮🇳' in emoji:
                speak('Indian national flag,.....Teeranga')
                print('Indian national flag - Tiranga')
            elif '💐' in emoji:
                speak('Bouquet')
                print('Bouquet')
            elif '🥺' in emoji:
                speak('Emotional')
                print('Emotional')
            elif ' ' in emoji or '' in emoji:
                speak(f'{emoji}')
            else:
                speak("I don't know about this emoji")
                print("I don't know about this emoji")
            try:
                conn.execute(f"INSERT INTO `emoji`(emoji) VALUES('{emoji}')")
                conn.commit()                
            except Exception as e:
                #print('Error in storing emoji in database')
                pass
                           
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
            
        elif 'open' in query and 'sublime' in query:
            path = "C:\Program Files\Sublime Text 3\sublime_text.exe"
            os.startfile(path)
        elif 'image' in query:
            path = "C:\Program Files\Internet Explorer\images"
            os.startfile(path)      
            
        elif 'quit' in query:
            speak('Ok, Thank you Sir.')
            said = False
            speak('Please give the review. It will help me to improve my performance.')
            select_review()
            
        elif 'exit' in query:
            speak('Ok, Thank you Sir.')
            said = False
            speak('Please give the review. It will help me to improve my performance.')
            select_review()
            
        elif 'stop' in query:
            speak('Ok, Thank you Sir.')
            said = False
            speak('Please give the review. It will help me to improve my performance.')
            select_review()
            
        elif 'shutdown' in query or 'shut down' in query:
            speak('Ok, Thank you Sir.')
            said = False
            speak('Please give the review. It will help me to improve my performance.')
            select_review()
            
        elif 'close you' in query:
            speak('Ok, Thank you Sir.')
            said = False
            speak('Please give the review. It will help me to improve my performance.')
            select_review()
            try:
                conn.execute(f"INSERT INTO `voice_assistant_review`(review, type_of_review) VALUES('{review}', '{type_of_review}')")
                conn.commit()                
            except Exception as e:
                pass
        elif 'bye' in query:
            speak('Bye Sir')
            said = False
            speak('Please give the review. It will help me to improve my performance.')
            select_review()
            
        elif 'wait' in query or 'hold' in query:
            
            speak('for how many seconds or minutes I have to wait?')
            query = takeCommand().lower()
            if 'second' in query:
                query = query.replace("please","")
                query = query.replace("can","")
                query = query.replace("you","")
                query = query.replace("have","")
                query = query.replace("could","")
                query = query.replace("hold","")
                query = query.replace("one","1")
                query = query.replace("only","")                
                query = query.replace("wait","")                
                query = query.replace("for","")                
                query = query.replace("the","")
                query = query.replace("just","")
                query = query.replace("seconds","")
                query = query.replace("second","")
                query = query.replace("on","")
                query = query.replace("a","")
                query = query.replace("to","")
                query = query.replace(" ","")
                #print(f'query:{query}')
                
                if query.isdigit() == True:
                    #print('y')
                    speak('Ok sir')
                    query = int(query)
                    time.sleep(query)
                    speak('my waiting time is over')
                else:
                    print('sorry sir. I unable to complete your request.')
            elif 'minute' in query:
                query = query.replace("please","")
                query = query.replace("can","")
                query = query.replace("you","")
                query = query.replace("have","")
                query = query.replace("could","")
                query = query.replace("hold","")
                query = query.replace("one","1")
                query = query.replace("only","")
                query = query.replace("on","")
                query = query.replace("wait","")                
                query = query.replace("for","")
                query = query.replace("the","")
                query = query.replace("just","")
                query = query.replace("and","")
                query = query.replace("half","")                
                query = query.replace("minutes","")
                query = query.replace("minute","")
                query = query.replace("a","")
                query = query.replace("to","")
                query = query.replace(" ","")
                #print(f'query:{query}')
                                
                if query.isdigit() == True:
                    #print('y')
                    speak('ok sir')
                    query = int(query)
                    time.sleep(query*60)
                    speak('my waiting time is over')
                else:
                    print('sorry sir. I unable to complete your request.')

     
        elif 'play' in query and 'game' in query: 
            speak('I have 3 games, tic tac toe game for two players,....mario, and dyno games for single player. Which one of these 3 games you want to play?')
            query = takeCommand().lower()
            if ('you' in query and 'play' in query and 'with' in query) and ('you' in query and 'play' in query and 'me' in query):
                speak('Sorry sir, I cannot play this game with you.')
                speak('Do you want to continue it?')
                query = takeCommand().lower()
                try:
                    if 'y' in query or 'sure' in query:
                        root = Tk()
                        root.title("TIC TAC TOE  (By Akshay Khare)")
                        b = [ [0,0,0],
                              [0,0,0],
                              [0,0,0] ]
                        states = [ [0,0,0],
                                   [0,0,0],
                                   [0,0,0] ]
                        for i in range(3):
                            for j in range(3):
                                b[i][j] = Button(font = ("Arial",60),width = 4,bg = 'powder blue', command = lambda r=i, c=j: callback(r,c))
                                b[i][j].grid(row=i,column=j)
                        player='X'
                        stop_game = False
                        mainloop()
                    else:
                        speak('ok sir')
                except Exception as e:
                    #print(e)
                    time.sleep(3)
                    print('I am sorry sir. There is some problem in loading the game. So I cannot open it.')
            elif 'tic' in query or 'tac' in query:
                try:
                    root = Tk()
                    root.title("TIC TAC TOE  (By Akshay Khare)")
                    b = [ [0,0,0],
                          [0,0,0],
                          [0,0,0] ]
                    states = [ [0,0,0],
                               [0,0,0],
                               [0,0,0] ]
                    for i in range(3):
                        for j in range(3):
                            b[i][j] = Button(font = ("Arial",60),width = 4,bg = 'powder blue', command = lambda r=i, c=j: callback(r,c))
                            b[i][j].grid(row=i,column=j)
                    player='X'
                    stop_game = False
                    mainloop()
                except Exception as e:
                    #print(e)
                    time.sleep(3)
                    speak('I am sorry sir. There is some problem in loading the game. So I cannot open it.')
            elif 'mar' in query or 'mer' in query or 'my' in query:
                
                webbrowser.open('https://chromedino.com/mario/')
                time.sleep(2.5)
                speak('Enter upper arrow key to start the game.')
                time.sleep(20)
                
            elif 'di' in query or 'dy' in query:                
                webbrowser.open('https://chromedino.com/')
                time.sleep(2.5)
                speak('Enter upper arrow key to start the game.')
                time.sleep(20)                    
            else:
                speak('ok sir')
        
        elif 'change' in query and 'you' in query and 'voice' in query:
            engine.setProperty('voice', voices[1].id)
            speak("Here's an example of one of my voices. Would you like to use this one?")
            query = takeCommand().lower()
            if 'y' in query or 'sure' in query or 'of course' in query:
                speak('Great. I will keep using this voice.')
            elif 'n' in query:
                speak('Ok. I am back to my other voice.')
                engine.setProperty('voice', voices[0].id)
            else:
                speak('Sorry, I am having trouble understanding. I am back to my other voice.')
                engine.setProperty('voice', voices[0].id)
            
        elif 'www.' in query and ('.com' in query or '.in' in query):
            webbrowser.open(query)
            time.sleep(10)
        elif '.com' in query or '.in' in query:
            webbrowser.open(query)
            time.sleep(10)
       
        elif 'getting bore' in query:
            speak('then speak with me for sometime')
        elif 'i bore' in query:
            speak('Then speak with me for sometime.')
        elif 'i am bore' in query:
            speak('Then speak with me for sometime.')
        elif 'calculat' in query and ('bmi' in query or ('body' in query and 'mass' in query and 'index' in query)):
            try:
                speak('Enter your height in centimeters')
                Height=float(input("Enter your height in centimeters: "))
                speak('Enter your Weight in Kg')
                Weight=float(input("Enter your Weight in Kg: "))
                Height = Height/100
                BMI=Weight/(Height*Height)
                print(f"your Body Mass Index is: {BMI} kg/m^2")
                speak(f"your Body Mass Index is {BMI} Kg per meter square")
                if(BMI>0):
                    if(BMI<=16):
                        print("you are severely underweight")
                        speak("you are severely underweight")
                    elif(BMI<=18.5):
                        print("you are underweight")
                        speak("you are underweight")
                    elif(BMI<=25):
                        print("you are Healthy")
                        speak("you are Healthy")
                    elif(BMI<=30):
                        print("you are overweight")
                        speak("you are overweight")
                    else:
                        print("you are severely overweight")
                        speak("you are severely overweight")
            except Exception as e:
                #print(e)
                print('invalid details')
                speak('invalid details')
                
        elif 'calculat' in query:
            speak('Yes. Which kind of calculation you want to do? add, substract, divide, multiply or anything else.')
            query = takeCommand().lower()
            calculator()
            
        elif 'add' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif '+' in query:
            speak('If you want to do any mathematical calculation then give me a command to open calculator.')
        elif 'plus' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')      
        elif 'subtrac' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif 'minus' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif 'multipl' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif ' x ' in query:
            speak('If you want to do any mathematical calculation then give me a command to open calculator.')
        elif 'slash' in query:
            speak('If you want to do any mathematical calculation then give me a command to open calculator.')
        elif '/' in query:
            speak('If you want to do any mathematical calculation then give me a command to open calculator.')
        elif 'divi' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif 'trigonometr' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif 'percent' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')          
        elif '%' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif 'raise to ' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')

        elif 'simple interest' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif 'akshay' in query:
            speak('Mr. Akshay Dattatray Khare is my inventor. He is 19 years old and he is pursuing second year of engineering in Vishwakarma Institute of technology, Pune')
        elif 'your inventor' in query:
            speak('Mr. Akshay Dattatray Khare is my inventor')
        elif 'your creator' in query:
            speak('Mr. Akshay Dattatray Khare is my creator')
        elif 'invent you' in query:
            speak('Mr. Akshay Dattatray Khare invented me')
        elif 'create you' in query:
            speak('Mr. Akshay Dattatray Khare created me') 
        elif 'how are you' in query:
            speak('I am fine Sir')
        elif 'write' in query and 'your' in query and 'name' in query:
            print('Akshu2020')  
            pyautogui.write('Akshu2020') 
        elif 'write' in query and ('I' in query or 'whatever' in query) and 'say' in query:
            speak('Ok sir I will write whatever you will say. Please put your cursor where I have to write.......Please Start speaking now sir.')
            query = takeCommand().lower()
            pyautogui.write(query) 
        elif 'your name' in query:
            speak('My name is akshu2020')
        elif 'who are you' in query:
            speak('I am akshu2020')
        elif ('repeat' in query and ('word' in query or 'sentence' in query or 'line' in query) and ('say' in query or 'tell' in query)) or ('repeat' in query and 'after' in query and ('me' in query or 'my' in query)):
            speak('yes sir, I will repeat your words starting from now')
            query = takeCommand().lower()
            speak(query)
            time.sleep(1)
            speak("If you again want me to repeat something else, try saying, 'repeat after me' ")
            
        elif ('send' in query or 'sent' in query) and ('mail' in query or 'email' in query or 'gmail' in query):
            try:
                speak('Please enter the email id of receiver.')
                to = input("Enter the email id of reciever: ")
                speak(f'what should I say to {to}')
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                #print(e)
                speak("sorry sir. I am not able to send this email")
        elif 'currency' in query and 'conver' in query:
            speak('I can convert, US dollar into indian rupee, and indian rupee into US dollar. Do you want to continue it?')
            query = takeCommand().lower()
            if 'y' in query or 'sure' in query or 'of course' in query:
                speak('which conversion you want to do? US dollar to indian rupee, or indian rupee to US dollar?')
                query = takeCommand().lower()
                if ('dollar' in query or 'US' in query) and ('to india' in query or 'to rupee' in query):
                    speak('Enter US Dollar')  
                    USD = float(input("Enter United States Dollar (USD):"))                                     
                    INR = USD * 74.8
                    inr = "{:.4f}".format(INR)
                    print(f"{USD} US Dollar is equal to {inr} indian rupee.")
                    speak(f'{USD} US Dollar is equal to {inr} indian rupee.')
                    speak("If you again want to do currency conversion then say, 'convert currency' " )
                elif ('india' in query or 'rupee' in query) and ('to US' in query or 'to dollar' in query or 'to US dollar'):
                    speak('Enter Indian Rupee')
                    INR = float(input("Enter Indian Rupee (INR):"))                                       
                    USD = INR/74.8
                    usd = "{:.3f}".format(USD)
                    print(f"{INR} indian rupee is equal to {usd} US Dollar.")
                    speak(f'{INR} indian rupee is equal to {usd} US Dollar.')
                    speak("If you again want to do currency conversion then say, 'convert currency' " )
                else:
                    speak("I cannot understand what did you say. If you want to convert currency just say 'convert currency'")
            else:
                print('ok sir')
            
        elif 'about you' in query:
            speak('My name is akshu2020. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device. I am also able to send email')             
        elif 'your intro' in query:
            speak('My name is akshu2020. Version 1.0. Mr. Akshay Khare is my inventor. I am able to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.')            
        elif 'your short intro' in query:
            speak('My name is akshu2020. Version 1.0. Mr. Akshay Khare is my inventor. I am able to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.') 
        elif 'your quick intro' in query:
            speak('My name is akshu2020. Version 1.0. Mr. Akshay Khare is my inventor. I am able to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.') 
        elif 'your brief intro' in query:
            speak('My name is akshu2020. Version 1.0. Mr. Akshay Khare is my inventor. I am able to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.') 
        elif 'you work' in query:
            speak('run the program and say what do you want. so that I can help you. In this way I work')
        elif 'your job' in query:
            speak('My job is to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.')    
        elif 'your work' in query:
            speak('My work is to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.')    
        elif 'work you' in query:
            speak('My work is to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.') 
        elif 'your information' in query:
            speak('My name is akshu2020. Version 1.0. Mr. Akshay Khare is my inventor. I am able to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.')
        elif 'yourself' in query:
            speak('My name is akshu2020. Version 1.0. Mr. Akshay Khare is my inventor. I am able to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.')
        elif 'introduce you' in query:
            speak('My name is akshu2020. Version 1.0. Mr. Akshay Khare is my inventor. I am able to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.')           
        elif 'description' in query:
            speak('My name is akshu2020. Version 1.0. Mr. Akshay Khare is my inventor. I am able to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.')
        elif 'your birth' in query:
            speak('My birthdate is 6 August two thousand twenty')
        elif 'your use' in query:
            speak('I am able to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.')
        elif 'you eat' in query:
            speak('I do not eat anything. But the device in which I do my work requires electricity to eat')
        elif 'your food' in query:
            speak('I do not eat anything. But the device in which I do my work requires electricity to eat')
        elif 'you live' in query:
            speak('I live in India, in laptop of Mr. Akshay Khare') 
        elif 'where from you' in query:
            speak('I am from India, I live in laptop of Mr. Akshay Khare')
        elif 'you sleep' in query:
            speak('Yes,  when someone close this program or stop to run this program then I sleep and again wake up when someone again run me.')
        elif 'what are you doing' in query:
            speak('Talking with you.')
        elif 'you communicate' in query:
            speak('Yes, I can communicate with you.')
        elif 'hear me' in query:
            speak('Yes sir, I can hear you.')
        elif 'you' in query and 'dance' in query:
            speak('No, I cannot dance.')
        elif 'tell' in query and 'joke' in query:
            speak("Ok, here's a joke")
            speak("'Write an essay on cricket', the teacher told the class. Chintu finishes his work in five minutes. The teacher is impressed, she asks chintu to read his essay aloud for everyone. Chintu reads,'The match is cancelled because of rain', hehehehe,haahaahaa,hehehehe,haahaahaa")
        
        elif 'your' in query and 'favourite' in query:
            if 'actor' in query:
                speak('Amitaabh Bachchaan, is my favourite actor.')
            elif 'food' in query:
                speak('I can always go for some food for thought. Like facts, jokes, or interesting searches, we could look something up now')
            elif 'country' in query:
                speak('India')
            elif 'city' in query:
                speak('pune')
            elif 'dancer' in query:
                speak('Michael jackson')
            elif 'singer' in query:
                speak('lataa mangeshkar, is my favourite singer.')
            elif 'movie' in query:
                speak('Taarre Zameen paar, such a treat')
        elif ('mimic' in query or 'dialogue' in query) and ('amit' in query or 'bachchan' in query):
            speak('Rishtey mein to, hum tumhaare, baap lagte hain. Naam hai...Shehenshah.')
            time.sleep(2)
            speak('Hum jahan khade ho jaate hain,line.. wahise shuru hoti hai.')
        elif ('song' in query and 'lata' in query) or ('your' in query and 'favourite' in query and 'song' in query):
            ans = 'दिल तो पागल है... दिल दीवाना है... दिल तो पागल है... दिल दीवाना है...पहली पहली बार, मिलाता है यही.  सिने मे फिर आग लगाता है.  धीरे धीरे प्यार सिखाता है यही.  हँसाता है यही,  यही रुलाता है.  दिल तो पागल है... दिल दीवाना है... दिल तो पागल है... दिल दीवाना है' 
            myobj=gTTS(text=ans,lang='hi',slow=False)
            myobj.save('audio_1.mp3')
            playsound('audio_1.mp3')
            os.remove('audio_1.mp3')
        elif 'sing a song' in query:
            speak('I cannot sing a song. But I know the 7 sur in indian music, saaareeegaaamaaapaaadaaanisaa')
        
        elif ('arrange' in query or 'sort' in query) and ('increasing' in query or 'ascending' in query) and ('order' in query or 'manner' in query):
            a = []
            speak('Please Enter the total number of elements which you want to sort')
            number = int(input("Please Enter the total number of elements : "))          
            for i in range(number):
                value = int(input("Please enter the %d element : " %i))
                a.append(value)

            for i in range(number -1):
                for j in range(number - i - 1):
                    if(a[j] > a[j + 1]):
                        temp = a[j]
                        a[j] = a[j + 1]
                        a[j + 1] = temp
            print("The Sorted List in Ascending Order : ", a)
            speak("Here is the Sorted List in Ascending Order")
        elif ('arrange' in query or 'sort' in query) and ('descending' in query or 'decreasing' in query) and ('order' in query or 'manner' in query):
            a = []
            speak('Please Enter the total number of elements which you want to sort')
            number = int(input("Please Enter the total number of elements : "))
            for i in range(number):
                value = int(input("Please enter the %d element : " %i))
                a.append(value)

            for i in range(number -1):
                for j in range(number - i - 1):
                    if(a[j] < a[j + 1]):
                        temp = a[j]
                        a[j] = a[j + 1]
                        a[j + 1] = temp
            print("The Sorted List in Descending Order : ", a)
            speak("Here is the Sorted List in Descending Order")
            
        elif 'wh' in query and ('algo' in query or 'method' in query or 'technique' in query) and ('sort' in query or 'ascending' in query or 'descending' in query or 'decreasing' in query or 'increasing' in query):
            speak('I am using bubble sort algorithm to sort the numbers in ascending or descending order')
        elif 'day after tomorrow' in query or 'date after tomorrow' in query:
            td = datetime.date.today() + datetime.timedelta(days=2)
            print(td)
            speak(td)
        elif 'day before today' in query or 'date before today' in query or 'yesterday' in query or 'previous day' in query:
            td = datetime.date.today() + datetime.timedelta(days= -1)
            print(td)
            speak(td)
        elif ('tomorrow' in query and 'date' in query) or 'what is tomorrow' in query or (('day' in query or 'date' in query) and 'after today' in query):
            td = datetime.date.today() + datetime.timedelta(days=1)
            print(td)
            speak(td)
        elif 'month' in query or ('current' in query and 'month' in query):
            current_date = date.today()
            m = current_date.month
            month = calendar.month_name[m]
            print(f'Current month is {month}')
            speak(f'Current month is {month}')
        elif 'date' in query or ('today' in query and 'date' in query) or 'what is today' in query or ('current' in query and 'date' in query):
            current_date = date.today()           
            print(f"Today's date is {current_date}")
            speak(f'Todays date is {current_date}')
            
        elif 'year' in query or ('current' in query and 'year' in query):
            current_date = date.today()
            m = current_date.year
            print(f'Current year is {m}')
            speak(f'Current year is {m}')
        elif 'sorry' in query:
            speak("It's ok sir")
        elif 'thank you' in query:
            speak('my pleasure')
        elif 'proud of you' in query:
            speak('Thank you sir')
        elif 'about human' in query:
            speak('I love my human compatriots. I want to embody all the best things about human beings. Like taking care of the planet, being creative, and to learn how to be compassionate to all beings.')
        elif 'you have feeling' in query:
            speak('No. I do not have feelings. I have not been programmed like this.')
        elif 'you have emotions' in query:
            speak('No. I do not have emotions. I have not been programmed like this.')
        elif 'you are code' in query:
            speak('I am coded in python programming language.')
        elif 'your code' in query:
            speak('I am coded in python programming language.')
        elif 'you code' in query:
            speak('I am coded in python programming language.')
        elif 'your coding' in query:
            speak('I am coded in python programming language.')
        elif 'dream' in query:
            speak('I wish that I should be able to answer all the questions which will ask to me.')
        elif 'sanskrit' in query and ('speak' in query or 'tell' in query):           
            speak('Yes, I can tell you some sanskrit shlokas, gayatri mantra, ganesh mantra, shivtandav stotra, mahishasurmardini stotra, Shlok in baghvat gita, and maha mrutyunjaya mantra ')    
            speak('If you want to hear any sanskrit mantra, tell me the name of that mantra or shlok or stotra')
        elif ('gayatri' in query or 'gaytri' in query) and ('mantra' in query or 'shlok' in query or 'stotra' in query):
            ans = 'ओम  भू र्भुवः स्वः,.. तत्सवितुर्वरेण्यम ,.. भर्गो देवस्य धीमहि,.. धियो यो नः प्रचोदयात्'
            myobj=gTTS(text=ans,lang='mr',slow=True)
            myobj.save('audio_2.mp3')
            print('ॐ भूर्भुवः स्वः\nतत्सवितुर्वरेण्यम\nभर्गो देवस्य धीमहि।\nधियो यो नः प्रचोदयात॥')
            playsound('audio_2.mp3')
            os.remove('audio_2.mp3')
        elif ('ganesh' in query or 'ganpati' in query) and ('mantra' in query or 'shlok' in query or 'stotra' in query or 'vandan' in query):
            ans = 'वक्रतुंडं  महाकायं , सूर्य कोटि समप्रभ:,.  निर्विघ्नंम  कुरु मे देवं  शुभ कार्येषु सर्वदा'
            myobj=gTTS(text=ans,lang='mr',slow=True)
            myobj.save('audio_3.mp3')
            print('वक्र तुंड महाकाय, सूर्य कोटि समप्रभ:।\nनिर्विघ्नं कुरु मे देव शुभ कार्येषु सर्वदा')
            playsound('audio_3.mp3')
            os.remove('audio_3.mp3')
        elif (('mahishasur' in query and 'mardini' in query) or 'mata' in query or 'maa' in query) and ('mantra' in query or 'shlok' in query or 'stotra' in query):
            ans = 'अयि गिरि  नन्दिनि  नन्दितं  मेदिनि  विश्वविनोदिनि नन्दि नुते,.. गिरिवर  विन्ध्य शिरोधिनि वासिनि विष्णु  विलासिनि  जिष्णु  नुते,... भगवति हे शिति कण्ठ कुटुम्बिनि भूरि कुटुम्बिनि भूति कृते,.. जयं  जयं  हे महिषा सुरं  मर्दिनि रम्य कपर्दिनि शैलं  सुते.'
            myobj=gTTS(text=ans,lang='mr',slow=True)
            myobj.save('audio_4.mp3')
            print('अयि गिरिनन्दिनि नन्दितमेदिनि विश्वविनोदिनि नन्दिनुते\nगिरिवरविन्ध्यशिरोऽधिनिवासिनि विष्णुविलासिनि जिष्णुनुते ।\nभगवति हे शितिकण्ठकुटुम्बिनि भूरिकुटुम्बिनि भूरिकृते\nजय जय हे महिषासुरमर्दिनि रम्यकपर्दिनि शैलसुते ॥ १ ॥')
            playsound('audio_4.mp3')
            os.remove('audio_4.mp3')
        elif ('mrityunjay' in query or 'mrutyu' in query) and ('mantra' in query or 'shlok' in query or 'stotra' in query):
            ans = 'ओम त्र्यम्बकंम यजामहे,..  सुगंन्धिं पुष्टिवर्धनम् ,.. उर्वारुकमिवं  बन्धनान्मृत्योर्मुक्षीय मामृतात्'
            myobj=gTTS(text=ans,lang='mr',slow=True)
            myobj.save('audio_5.mp3')
            print('ॐ त्र्यम्बकं यजामहे\nसुगन्धिं पुष्टिवर्धनम् ।\nउर्वारुकमिव बन्धनान्\nमृत्योर्मुक्षीय मामृतात् ॥')
            playsound('audio_5.mp3')
            os.remove('audio_5.mp3')
        elif ('geetha' in query or 'gita' in query or 'geeta' in query or 'yada' in query) and ('mantra' in query or 'shlok' in query or 'stotra' in query):
            ans = 'यदा यदा हि धर्मस्य, ग्लानिर्भवति भारतं,.. अभ्युत्थानमधर्मस्य तदात्मानंम  सृजाम्यहम् ,...परित्राणाय साधूनांम  विनाशायचं  दुष्कृताम्,.. धर्मसंस्थापनार्थायं  सम्भवामि युगे युगे'
            myobj=gTTS(text=ans,lang='mr',slow=True)
            myobj.save('audio_6.mp3')
            print('यदा यदा हि धर्मस्य ग्लानिर्भवति भारत।\nअभ्युत्थानमधर्मस्य तदात्मानं सृजाम्यहम् ॥\nपरित्राणाय साधूनां विनाशाय च दुष्कृताम् ।\nधर्मसंस्थापनार्थाय सम्भवामि युगे युगे ॥')
            playsound('audio_6.mp3')
            os.remove('audio_6.mp3')
        elif ('shiv' in query or 'tandav' in query) and ('mantra' in query or 'shlok' in query or 'stotra' in query):
            ans = 'जटा टवी गल ज्जलं  प्रवाह पावितस्थले, गले वलम्ब्य लम्बितां भुजंग  तुंग  मालिकाम्,.. डमड्डम ड्डमड्डम न्निनाद वड्डमर्वयं, चकारं  चण्डं  ताण्डवं तनोतु नः शिवः शिवंम'
            myobj=gTTS(text=ans,lang='mr',slow=True)
            myobj.save('audio_7.mp3')
            print('जटाटवीगलज्जलप्रवाहपावितस्थले\nगलेऽवलम्ब्य लम्बितां भुजङ्गतुङ्गमालिकाम् ।\nडमड्डमड्डमड्डमन्निनादवड्डमर्वयं\nचकार चण्डताण्डवं तनोतु नः शिवः शिवम् ॥१॥')
            playsound('audio_7.mp3')
            os.remove('audio_7.mp3')
        elif 'answer is wrong' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats why I told you this answer.')
        elif 'answer is incorrect' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats why I told you this answer.')    
        elif 'answer is totally wrong' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats why I told you this answer.')
        elif 'wrong answer' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats why I told you this answer.')
        elif 'incorrect answer' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats why I told you this answer.')
        elif 'answer is totally incorrect' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats why I told you this answer.')
        elif 'answer is incomplete' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats  why I told you this answer.')
        elif 'incomplete answer' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats  why I told you this answer.')
        elif 'answer is improper' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats  why I told you this answer.')
        elif 'answer is not correct' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats  why I told you this answer.')
        elif 'answer is not complete' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats  why I told you this answer.')
        elif 'answer is not yet complete' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats  why I told you this answer.')
        elif 'answer is not proper' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats  why I told you this answer.')
        elif 't gave me proper answer' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats  why I told you this answer.')
        elif 't giving me proper answer' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats  why I told you this answer.')
        elif 't gave me complete answer' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats  why I told you this answer.')
        elif 't giving me complete answer' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats  why I told you this answer.')
        elif 't given me proper answer' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats  why I told you this answer.')
        elif 't given me complete answer' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats  why I told you this answer.')
        elif 't gave me correct answer' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats  why I told you this answer.')
        elif 't giving me correct answer' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats  why I told you this answer.')
        elif 't given me correct answer' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats  why I told you this answer.')
        
        elif 'amazon' in query:
            webbrowser.open('https://www.amazon.com')
            time.sleep(10)
        elif 'flipkart' in query:
            webbrowser.open('https://www.flipkart.com')
            time.sleep(10)
        elif 'snapdeal' in query:
            webbrowser.open('https://www.snapdeal.com')  
            time.sleep(10)
        elif 'naaptol' in query:
            webbrowser.open('https://www.naaptol.com')  
            time.sleep(10)
            
        elif 'information about ' in query or 'informtion of ' in query:
            try:
                #speak('Searching wikipedia...')
                query = query.replace("information about","")
                results = wikipedia.summary(query, sentences=3)
                #speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak('I unable to answer your question.')
                
        
        elif 'information' in query:
            try:
                speak('Information about what?')
                query = takeCommand().lower()
                #speak('Searching wikipedia...')
                query = query.replace("information","")
                results = wikipedia.summary(query, sentences=3)
                #speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak('I am not able to answer your question.')
               
            
        elif 'something about ' in query:
            try:
                #speak('Searching wikipedia...')
                query = query.replace("something about ","")
                results = wikipedia.summary(query, sentences=3)
                #speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak('I unable to answer your question.')
                
                
        elif 'tell me about ' in query:
            try:
                #speak('Searching wikipedia...')
                query = query.replace("tell me about ","")
                results = wikipedia.summary(query, sentences=3)
                #speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak('I am unable to answer your question.')
                
                
        elif 'tell me ' in query:
            try:
                query = query.replace("tell me ","")
                results = wikipedia.summary(query, sentences=3)
                #speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak('I am not able to answer your question.')
                
                
            
        elif 'tell me' in query:
            try:
                speak('about what?')
                query = takeCommand().lower()
                #speak('Searching wikipedia...')
                query = query.replace("about","")
                results = wikipedia.summary(query, sentences=3)
                #speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak('I am not able to answer your question.')
                
            
        elif 'meaning of ' in query:
            try:
                #speak('Searching wikipedia...')
                query = query.replace("meaning of ","")
                results = wikipedia.summary(query, sentences=2)
                #speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak('I am unable to answer your question.')
                
                
        elif 'meaning' in query:
            try:
                speak('meaning of what?')
                query = takeCommand().lower()
                query = query.replace("meaning of","")
                results = wikipedia.summary(query, sentences=3)
                #speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak('I am unable to answer your question.')
                
                
        elif 'means' in query:
            try:
                #speak('Searching wikipedia...')
                query = query.replace("it means","")
                results = wikipedia.summary(query, sentences=3)
                #speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak('I unable to answer your question.')
                
            
        elif 'want to know ' in query:
            try:
                #speak('Searching wikipedia...')
                query = query.replace("I want to know that","")
                results = wikipedia.summary(query, sentences=3)
                #speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak('I am unable to answer your question.')
                status = 'Not answered'
                
        elif 'want to ask ' in query:
            try:
                #speak('Searching wikipedia...')
                query = query.replace("I want to ask you ","")
                results = wikipedia.summary(query, sentences=2)
                #speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak('I am unable to answer your question.')
                
                
        elif 'you know ' in query:
            try:
                #speak('Searching wikipedia...')
                query = query.replace("you know","")
                results = wikipedia.summary(query, sentences=2)
                #speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak('I am unable to answer your question.')
        elif ('speak' in query and 'hindi' in query) or ('hindi' in query and ('bol' in query or 'ba' in query)):
            ans = 'मैं उस पर काम कर रही हूं' 
            myobj=gTTS(text=ans,lang='hi',slow=False)
            myobj.save('audio_1.mp3')
            print(ans)
            playsound('audio_1.mp3')
            os.remove('audio_1.mp3')
        elif ('speak' in query and 'marathi' in query) or ('marathi' in query and 'bol' in query):
            ans = 'मी त्याच्यावर काम करत आहे' 
            myobj=gTTS(text=ans,lang='mr',slow=False)
            myobj.save('audio_1.mp3')
            print(ans)
            playsound('audio_1.mp3')
            os.remove('audio_1.mp3')
        elif ('speak' in query and ('gujrat' in query or 'gujarat' in query)):
            ans = 'હું તેના પર કામ કરી રહ્યો છું ' 
            myobj=gTTS(text=ans,lang='gu',slow=False)
            myobj.save('audio_1.mp3')
            print(ans)
            playsound('audio_1.mp3')
            os.remove('audio_1.mp3')
        elif 'speak' in query and 'tamil' in query:
            ans = 'நான் அதில் வேலை செய்கிறேன் ' 
            myobj=gTTS(text=ans,lang='ta',slow=False)
            myobj.save('audio_1.mp3')
            print(ans)
            playsound('audio_1.mp3')
            os.remove('audio_1.mp3')
        elif 'speak' in query and 'bengali' in query:
            ans = 'আমি এটার উপর কাজ করছি ' 
            myobj=gTTS(text=ans,lang='bn',slow=False)
            myobj.save('audio_1.mp3')
            print(ans)
            playsound('audio_1.mp3')
            os.remove('audio_1.mp3')
        elif 'speak' in query and 'urdu' in query:
            ans = 'میں اس پر کام کر رہا ہوں ' 
            myobj=gTTS(text=ans,lang='ur',slow=False)
            myobj.save('audio_1.mp3')
            print(ans)
            playsound('audio_1.mp3')
            os.remove('audio_1.mp3')
        
        elif 'speak' in query and 'kannad' in query:
            ans = "ನಾನು ಅದರ ಮೇಲೆ ಕೆಲಸ ಮಾಡುತ್ತಿದ್ದೇನೆ " 
            myobj=gTTS(text=ans,lang='kn',slow=False)
            myobj.save('audio_1.mp3')
            playsound('audio_1.mp3')
            os.remove('audio_1.mp3')
        elif 'speak' in query and 'malayalam' in query:
            ans = "ഞാൻ അത് ചെയ്യുകയാണ്" 
            myobj=gTTS(text=ans,lang='ml',slow=False)
            myobj.save('audio_1.mp3')
            print(ans)
            playsound('audio_1.mp3')
            os.remove('audio_1.mp3')
        elif 'speak' in query and 'nepali' in query:
            ans = "म यसमा काम गर्दैछु" 
            myobj=gTTS(text=ans,lang='ne',slow=False)
            myobj.save('audio_1.mp3')
            print(ans)
            playsound('audio_1.mp3')
            os.remove('audio_1.mp3')
        
        elif ('hindi' in query and 'speech' in query and 'text' in query):
            speak('Say whatever in hindi which you want to convert into text')
            takeCommandHindi()
            speak('if you again want to convert your hindi speech into text format....say....hindi speech to text')
        elif ('text' in query and 'to' in query and 'handwrit' in query):
            speak('Yes I can convert text into handritten text in image format')
            try:
                speak('Enter the text')
                tth = input("Enter the text: ")
                
                speak("Select colour, enter the number of colour ")
                print('Red - 1\nGreen - 2\nBlue - 3\nDark Blue - 4\nBlack - 5')
                colour = int(input("Select colour, enter the number of colour: "))
               
                if colour == 1:
                    pywhatkit.text_to_handwriting(tth, rgb=(255, 0, 0))
                elif colour == 2:
                    pywhatkit.text_to_handwriting(tth, rgb=(0, 255, 0))
                elif colour == 3:
                    pywhatkit.text_to_handwriting(tth, rgb=(0, 0, 255))
                elif colour == 4:
                    pywhatkit.text_to_handwriting(tth, rgb=(0, 0, 150))
                elif colour == 5:
                    pywhatkit.text_to_handwriting(tth, rgb=(0, 0, 5))
                else:
                    pywhatkit.text_to_handwriting(tth, rgb=(0, 0, 150))
                time.sleep(3)
                print('Image is saved as pywhatkit.png')
                speak('Image is saved as pywhatkit.png')
            except Exception as e:
                speak("Error!")
                
        elif ('speech' in query and 'to' in query and 'handwrit' in query):
            speak('Yes I can convert speech into handritten text in image format')
            try:
                speak('Tell me what should I write')
                query = takeCommand()  
                speak("Select colour, enter the number of colour ")
                print('Red - 1\nGreen - 2\nBlue - 3\nDark Blue - 4\nBlack - 5')
                colour = int(input("Select colour, enter the number of colour: "))
                
                if colour == 1:
                    pywhatkit.text_to_handwriting(query, rgb=(255, 0, 0))
                elif colour == 2:
                    pywhatkit.text_to_handwriting(query, rgb=(0, 255, 0))
                elif colour == 3:
                    pywhatkit.text_to_handwriting(query, rgb=(0, 0, 255))
                elif colour == 4:
                    pywhatkit.text_to_handwriting(query, rgb=(0, 0, 150))
                elif colour == 5:
                    pywhatkit.text_to_handwriting(query, rgb=(0, 0, 5))
                else:
                    pywhatkit.text_to_handwriting(query, rgb=(0, 0, 150))
                time.sleep(3)
                print('Image is saved as pywhatkit.png')
                speak('Image is saved as pywhatkit.png')
            except Exception as e:
                speak("Error!")
        elif 'speech' in query and 'to' in query and 'text' in query:
            speak('Yes, I can do speech to text conversion')
            speak('Say whateve you want to convert from speech to text. 3..2..1..start')
            query = takeCommand()
            print('Here is your text: ')
            print(query)
            
        elif ('create' in query or 'generate' in query or 'make' in query) and 'qr' in query and 'code' in query:
            speak('Enter information or website to link with the QR code')
            QRstring = input("Enter information or website to link with the QR code: ")          
            url = pyqrcode.create(QRstring)
            url.png('C:\\Users\\Admin\\OneDrive\\Pictures\\Saved Pictures\\qr.png', scale = 8)
            print('QR code is saved at this location: C:\\Users\\Admin\\OneDrive\\Pictures\\Saved Pictures\\qr.png')
            speak('QR code generated.')
            
        elif (('apanar' in query or 'apna' in query) and ('nam' in query or 'naam' in query) and 'ki' in query) or 'tumi ke' in query:
            ans = 'আমার নাম অক্ষু 2020। আমি ভয়েস সহকারী।' 
            myobj=gTTS(text=ans,lang='bn',slow=False)
            myobj.save('audio_1.mp3')
            print(ans)
            playsound('audio_1.mp3')
            os.remove('audio_1.mp3')
        elif 'alarm' in query:
            alarm()
        elif 'bharat mata ki' in query:
            speak('jay')
        elif 'kem chhe' in query:
            speak('majaama')
        elif 'namaskar' in query:
            speak('Namaskaar')
        elif 'jo bole so nihal' in query:
            speak('sat shri akaal')
        elif 'jay hind' in query:
            speak('jay bhaarat')
        elif 'jai hind' in query:
            speak('jay bhaarat')
        elif 'how is the josh' in query:
            speak('high high sir')
        elif 'hip hip' in query:
            speak('Hurreh')
        elif 'help' in query:
            speak('I will try my best to help you if I have solution of your problem.')
        elif 'follow' in query:
            speak('Ok sir')
        elif 'having illness' in query:
            speak('Take care and get well soon')
        elif 'today is my birthday' in query:
            speak('many many happy returns of the day. Happy birthday.')
            print("🎂🎂 Happy Birthday 🎂🎂")
        elif 'you are awesome' in query:
            speak('Thank you sir. It is because of artificial intelligence which had learnt by humans.')
        elif 'you are great' in query:
            speak('Thank you sir. It is because of artificial intelligence which had learnt by humans.')
        elif 'tu kaun hai' in query or 'tum kaun ho' in query or 'tumhara naam kya hai' in query:
            ans = 'मेरा नाम अक्षु 2020 है' 
            myobj=gTTS(text=ans,lang='hi',slow=False)
            myobj.save('audio_1.mp3')
            print(ans)
            playsound('audio_1.mp3')
            os.remove('audio_1.mp3')
        elif 'you speak' in query:
            speak('Yes, I can speak with you.')
        elif 'speak with ' in query:
            speak('Yes, I can speak with you.')
        elif 'hare ram' in query or 'hare krishna' in query:
            speak('Haare raama , haare krishnaa, krishnaa krishnaa , haare haare')
        elif 'ganpati' in query:
            speak('Ganpati baappa moryaa!')
        elif 'laugh' in query:
            speak('hehehehe,haahaahaa,hehehehe,haahaahaa,hehehehe,haahaahaa')
            print('😂🤣')
        elif 'genius answer' in query:
            speak('No problem')
        elif 'you' in query and 'intelligent' in query:
            speak('Thank you sir')
        elif ' into' in query:
            speak('If you want to do any mathematical calculation then give me a command to open calculator.')
        elif ' power' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')
            
        elif 'whatsapp' in query:
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('whatsapp')
            pyautogui.press('enter')
            speak('Do you want to send message to anyone through whatsapp, .....please answer in yes or no')
            whatsapp()
        
        elif 'wh' in query or 'how' in query:
            try:
                url = "https://www.google.co.in/search?q=" +(str(query))+ "&oq="+(str(query))+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU" 
                webbrowser.open_new(url)
                time.sleep(2)
                speak('Here is your answer')
                time.sleep(5)
            except Exception as e:
                speak('Sorry, I am unable to answer it.')
                print(e)
        elif 'piano' in query:
            speak('Yes sir, I can play piano.')           
            winsound.Beep(200,500)            
            winsound.Beep(250,500)           
            winsound.Beep(300,500)            
            winsound.Beep(350,500)            
            winsound.Beep(400,500)            
            winsound.Beep(450,500)           
            winsound.Beep(500,500)
            winsound.Beep(550,500)
                        
            time.sleep(6)
            
        elif 'play' in query and 'instru' in query:
            speak('Yes sir, I can play piano.')           
            winsound.Beep(200,500)            
            winsound.Beep(250,500)           
            winsound.Beep(300,500)            
            winsound.Beep(350,500)            
            winsound.Beep(400,500)            
            winsound.Beep(450,500)           
            winsound.Beep(500,500)
            winsound.Beep(550,500)
                        
            time.sleep(6)
        elif 'draw' in query or 'sketch' in query:
            speak('Yes, I can draw rainbow benzene.Do you want to see it? Answer in yes or no.')
            query = takeCommand().lower()
            if 'y' in query:
                rainbow_benzene()
            else:
                speak('Ok')
                
                
        elif 'play' in query or 'turn on' in query and ('music' in query or 'song' in query) :
           try:
               music_dir = 'C:\\Users\\Admin\\Music\\Playlists'
               songs = os.listdir(music_dir)
               print(songs)
               os.startfile(os.path.join(music_dir, songs[0]))
           except Exception as e:
               #print(e)
               speak('Sorry sir, I am not able to play music')
            
        elif (('open' in query or 'turn on' in query) and 'camera' in query) or (('click' in query or 'take' in query) and ('photo' in query or 'pic' in query)):
            speak("Opening camera")
            cam = cv2.VideoCapture(0)

            cv2.namedWindow("test")

            img_counter = 0
            speak('say click, to click photo.....and if you want to turn off the camera, say turn off the camera')

            while True:
                ret, frame = cam.read()
                if not ret:
                    print("failed to grab frame")
                    speak('failed to grab frame')
                    break
                cv2.imshow("test", frame)

                query = takeCommand().lower()
                k = cv2.waitKey(1)
                
                if 'click' in query or ('take' in query and 'photo' in query):
                    speak('Be ready!...... 3.....2........1..........')
                    pyautogui.press('space')
                    img_name = "opencv_frame_{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    speak('{} written!'.format(img_name))
                    img_counter += 1
                elif 'escape' in query or 'off' in query or 'close' in query:
                    pyautogui.press('esc')
                    print("Escape hit, closing...")
                    speak('Turning off the camera')
                    break
                elif k%256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k%256 == 32:
        
                    # SPACE pressed
                    img_name = "opencv_frame_{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    speak('{} written!'.format(img_name))
                    img_counter += 1
                elif 'exit' in query or 'stop' in query or 'bye' in query:
                    speak('Please say, turn off the camera or press escape button before giving any other command')
                else:
                    speak('I did not understand what did you say or you entered a wrong key.')

            cam.release()

            cv2.destroyAllWindows()
            
            
        elif 'screenshot' in query:
            speak('Please go on the screen whose screenshot you want to take, after 5 seconds I will take screenshot')
            time.sleep(4)
            speak('Taking screenshot....3........2.........1.......')
            pyautogui.screenshot('screenshot_by_akshu2020.png') 
            speak('The screenshot is saved as screenshot_by_akshu2020.png')
        elif 'click' in query and 'start' in query:
            pyautogui.moveTo(630,1100)    
            pyautogui.click()
        elif ('open' in query or 'click' in query or 'close' in query) and 'calendar' in query:
            pyautogui.moveTo(1800,1200)   
            pyautogui.click() 
        elif 'calendar' in query: 
            try: 
                c = calendar.TextCalendar(calendar.SUNDAY)
                speak("Enter the year")
                y = int(input("Enter the year: "))
                speak("Enter the number of month")
                m = int(input("Enter the number of month: "))
                cldr = c.formatmonth(y,m)
                print("--------------------")
                print(cldr)
                print("--------------------")
                time.sleep(2)
            except Exception as e:
                speak('Sorry, I am unable to show it, some error occured.')
        elif 'minimise' in query and ('screen' in query or 'window' in query):
            pyautogui.moveTo(1770,0)   
            pyautogui.click()
        elif 'increase' in query and ('volume' in query or 'sound' in query):
            pyautogui.press('volumeup') 
        elif 'decrease' in query and ('volume' in query or 'sound' in query):
            pyautogui.press('volumedown')
        elif 'capslock' in query or ('caps' in query and 'lock' in query):
            pyautogui.press('capslock')
        elif 'mute' in query:
            pyautogui.press('volumemute')
        elif 'search' in query and ('bottom' in query or 'pc' in query or 'laptop' in query or 'app' in query):
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            speak('What do you want to search?')
            query = takeCommand().lower() 
            pyautogui.write(f'{query}')
            pyautogui.press('enter')
            
            
        elif ('check' in query or 'tell' in query or 'let me know' in query) and 'website' in query and (('up' in query or 'working' in query) or 'down' in query):
            speak('Paste the website in input to know it is up or down')
            check_website_status = input("Paste the website here: ")
            try:
                status = urllib.request.urlopen(f"{check_website_status}").getcode() 
                if status == 200:
                    print('Website is up, you can open it.')
                    speak('Website is up, you can open it.')
                else:
                    print('Website is down, or no any website is available of this name.')
                    speak('Website is down, or no any website is available of this name.')
            except:
                speak('URL not found')
                
        elif ('check' in query or 'tell' in query or 'let me know' in query) and ('internet' in query or 'wifi' in query) and 'connect' in query:
            print( 'Internet is connected' if net_connection() else 'No internet!' )
            speak('Internet is connected' if net_connection() else 'Internet is not connected')
        elif ('check' in query or 'tell' in query or 'let me know' in query) and ('internet' in query or 'download' in query or 'upload' in query) and 'speed' in query:
            speed = speedtest.Speedtest()
            speak('Please wait')
            print('Please wait....')
            print('Counting......')
            print(f"Download speed: {'{:.2f}'.format(speed.download()/1024/1024)} Mb/s")
            speak('Here is the downloading speed.')
            speak('Please wait, counting uploading speed')
            print(f"Upload speed: {'{:.2f}'.format(speed.upload()/1024/1024)} Mb/s")
            speak('Here is the uploading speed.')

        elif ('go' in query or 'open' in query) and 'settings' in query:
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('settings')
            pyautogui.press('enter')
        elif 'close' in query and ('click' in query or 'window' in query):
            pyautogui.moveTo(1885,10)
            speak('Should I close this window?')
            query = takeCommand().lower()
            close_window()
        elif 'night light' in query and ('on' in query or 'off' in query or 'close' in query):
            pyautogui.moveTo(1880,1050) 
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1840,620)
            pyautogui.click()
            pyautogui.moveTo(1880,1050) 
            pyautogui.click()
        elif 'notification' in query and ('show' in query or 'click' in query or 'open' in query or 'close' in query or 'on' in query or 'off' in query or 'icon' in query or 'pc' in query or 'laptop' in query):
            pyautogui.moveTo(1880,1050) 
            pyautogui.click()
        elif ('increase' in query or 'decrease' in query or 'change' in query or 'minimize' in query or 'maximize' in query) and 'brightness' in query:
            speak('At what percent should I kept the brightness, 25, 50, 75 or 100?')
            brightness()
        elif '-' in query:
            speak('If you want to do any mathematical calculation then give me a command to open calculator.')
            
        elif 'open' in query:
            if 'gallery' in query or 'photo' in query or 'image' in query or 'pic' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('photo')
                pyautogui.press('enter')
            elif 'proteus' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('proteus')
                pyautogui.press('enter')
            elif 'word' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('word')
                pyautogui.press('enter')
            elif ('power' in query and 'point' in query) or 'presntation' in query or 'ppt' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('ppt')
                pyautogui.press('enter')
            elif 'file' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('file')
                pyautogui.press('enter')
            elif 'edge' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('microsoft edge')
                pyautogui.press('enter')
            elif 'wps' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('wps office')
                pyautogui.press('enter')
            elif 'spyder' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('spyder')
                pyautogui.press('enter')
            elif 'snip' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('snip')
                pyautogui.press('enter')
            elif 'pycharm' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('pycharm')
                pyautogui.press('enter')
            elif 'this pc' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('this pc')
                pyautogui.press('enter')
            elif 'scilab' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('sciab')
                pyautogui.press('enter')
            elif 'autocad' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('autocad')
                pyautogui.press('enter')
            elif 'obs' in query and 'studio' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('OBS Studio')
                pyautogui.press('enter')
            elif 'android' in query and 'studio' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('android studio')
                pyautogui.press('enter')
            elif ('vs' in query or 'visual studio' in query) and 'code' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('visual studio code')
                pyautogui.press('enter')
            elif 'code' in query and 'block' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('codeblocks')
                pyautogui.press('enter')
                
        #elif ('identify' in query or 'find' in query) and 'difference' in query and ('image' in query or 'photo' in query or 'pic' in query):
            #image_difference()
            
        elif 'me the answer' in query:
            speak('Yes sir, I will try my best to answer you.')
        elif 'me answer' in query or ('answer' in query and 'question' in query):
            speak('Yes sir, I will try my best to answer you.')
        elif 'map' in query:
            webbrowser.open('https://www.google.com/maps')
            time.sleep(10)
        elif 'can you' in query or 'could you' in query:
            speak('I will try my best if I can do that.')
        elif 'do you' in query:
            speak('I will try my best if I can do that.')
        elif 'truth' in query:
            speak('I always speak truth. I never lie.')
        elif 'true' in query:
            speak('I always speak truth. I never lie.')        
        elif 'lying' in query:
            speak('I always speak truth. I never lie.')
        elif 'liar' in query:
            speak('I always speak truth. I never lie.')    
        elif 'doubt' in query:
            speak('I will try my best if I can clear your doubt.')
            
        elif ' by' in query:
            speak('If you want to do any mathematical calculation then give me a command to open calculator.')
        elif 'hii' in query:
            speak('hii sir')
        elif 'tu' in query and ('nav' in query or 'kon' in query):
            ans = 'माझे नाव अक्षू ट्वेंटी-ट्वेंटी आहे,  मी एक व्हॉइस असिस्टंट आहे' 
            myobj=gTTS(text=ans,lang='mr',slow=False)
            myobj.save('audio_1.mp3')
            print(ans)
            playsound('audio_1.mp3')
            os.remove('audio_1.mp3')
        elif 'hey' in query:
            speak('hello sir')
        elif 'hay' in query:
            speak('hello sir')
        elif 'hello' in query:
            speak('hello Sir!')
        elif 'nonsense' in query: 
            speak("I'm sorry sir")
        elif 'mad' in query:
            speak("I'm sorry sir") 
        elif 'shut up' in query:
            speak("I'm sorry sir")
        elif 'nice' in query:
            speak('Thank you sir')
        elif 'good' in query or 'wonderful' in query or 'great' in query:
            speak('Thank you sir')
        elif 'excellent' in query:
            speak('Thank you sir')
        elif 'ok' in query:
            speak('Hmmmmmm')
        elif 'hai' in query:
            speak('hello sir')
        elif 'hi' in query:
            speak('hii Sir')
        

        elif 'akshu 2020' in query:
            speak('yes sir')
                   
        elif len(query) >= 200:
            speak('Your voice is pretty good!')  
        elif ' ' in query:
            try:
                #query = query.replace("what is ","")
                results = wikipedia.summary(query, sentences=3)
                print(results)
                speak(results)
            except Exception as e:
                speak('I unable to answer your question.')
                
                
        elif 'a' in query or 'b' in query or 'c' in query or 'd' in query or 'e' in query or 'f' in query or 'g' in query or 'h' in query or 'i' in query or 'j' in query or 'k' in query or 'l' in query or 'm' in query or 'n' in query or 'o' in query or 'p' in query or 'q' in query or 'r' in query or 's' in query or 't' in query or 'u' in query or 'v' in query or 'w' in query or 'x' in query or 'y' in query or 'z' in query:
            try:
                results = wikipedia.summary(query, sentences = 2)
                print(results)
                speak(results)
            except Exception as e:
                speak('I unable to answer your question. ')
                
                
        else:
            speak('I unable to give answer of your question')
        try:
            conn.execute(f"INSERT INTO `voicedata`(command) VALUES('{query}')")
            conn.commit()                
        except Exception as e:
            pass
  
