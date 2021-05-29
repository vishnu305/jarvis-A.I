import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import cv2 #pip install opencv-python
import random
import requests
import pywhatkit as kit #pip install pywhatkit
import sys
import pyjokes
import pyautogui
import time
import instaloader
from PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtCore import QTimer, QTime, QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JarvisGui import Ui_MainWindow
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager





engine = pyttsx3.init('sapi5')#to get the inbuilt voice stored in microsoft you can search about sapi5 more on wikipedia
voices = engine.getProperty('voices')#to get that voice to a variable
engine.setProperty('voice',voices[0].id)# there are two voices we are selecting the first voice of male voice
#print(voices[1].id)#to print the voice name


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self.TaskExecution()
    
    
    def TaskExecution(self):
        def takeCommand():
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                r.pause_threshold = 1#seconds of non-speaking audio before a phrase is considered complete
                r.energy_threshold = 700 
                audio = r.listen(source,timeout=10,phrase_time_limit=5)
            try:
                print("Recognizing...")
                self.query=r.recognize_google(audio,language='en-in')
                print(f"User said: {self.query}\n")
            except Exception as e:
            #print(e)
                print("say that again please...")
                return "None"
            return self.query
        def speak(audio):
            print(audio)
            print("\n")
            engine.say(audio)
            engine.runAndWait()
        def wishMe():
            hour = int(datetime.datetime.now().hour)
            time = datetime.datetime.now().strftime("%I %M ")
            if hour >= 0 and  hour<12:
                speak("Good Morning sir!") 
                speak(f"it's {time} AM")
            elif hour>=12 and hour<18:
                speak("Good Afternoon sir!")
                speak(f"it's {time} PM")
            else:
                speak("Good Evening sir!")
                speak(f"it's {time} PM")
            
           
            speak("I am Jarvis Sir.  Please tell me how may I help you")

        def sendEmail(to,content):
            server = smtplib.SMTP('smtp.gmail.com',587)#search about smtp in google
            server.ehlo()
            server.starttls()
            server.login('divvelavishnusai','9390182229')
            server.sendmail('divvelavishnusai',to,content)
            server.close()
        def news():
            main_url='https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=7113e657f0554f3ea267bf41637e3d0c'
            main_page = requests.get(main_url).json()
            articles=main_page["articles"]
            head=[]
            day=['first','second','third','fourth','fifth']
            for ar in articles:
                head.append(ar["title"])
            for i in range(len(day)):
                speak(f"today's {day[i]} news is : {head[i]}")
        def pdf_reader():
            book = open('dbms.pdf','rb')
            import PyPDF2
            pdfReader = PyPDF2.PdfFileReader(book)#pip install PyPDF2
            pages = pdfReader.numPages
            speak(f"Total numbers of pages in this book {pages} ")
            speak("sir please enter the page number i have to read ")
            pg = int(input("Please enter the page number: "))
            page = pdfReader.getPage(pg)
            text=page.extractText()
            speak(text)
        j=0
        def opendetails():
            spacek("you want to only see the user deties or i should speack")

            s=takecommend()

            if(s=="see"):
                with open("user.text","r" ) as e:
                    e.readlines()
                    print(e)
                    e.close()
            else:
                with open("data of user.text","r") as e:
                    s = e.readlines()
                    print(s)
                    speak(s)
                    e.close()
        def jarvis():
            j=0
            if j==0:
                speak("")
                
            else:
                speak("jarvis in a sleep mode sir")
                
            try:

                s = takeCommand()
                print(s)
                if 'sleep' in s:
                    speak("ok sir")
                    jarvis()
                    j+=1
                elif'wake up'in s:
                    speak("ok sir it will take some time to get connection to network")
                    speak('     Ok sir now i am in alert mode.  Do you have any other work sir?')
                    startExecution.start()
                else:
                    jarvis()
            except Exception as e1:
                jarvis()
        original_name = "Vishnu Sai Kumar Divvela"
        wishMe()
        while True:
            self.query = takeCommand().lower()
            #logic for executing tasks based on query
            if 'wikipedia' in self.query:
                speak(' Searching wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query,sentences=2)
                speak("According to wikipedia")
                speak(results)  
                speak("sir, do you have any other work")
            elif 'how are you' in self.query:
                speak('I am doing good sir')
                speak('I am fine, glad you me that sir')
                speak('How are you sir ?')
                takeCommand().lower()
                speak('Ok sir')
                speak("sir, do you have any other work")
            elif 'about'in self.query or 'who are you' in self.query:
                speak("My name is Jarvis, I am an prototype of Artificial Intelligence, i am here to assist you and i am created by Vishnu Sai Kumar Divvela")
            elif 'thankyou' in self.query or 'thank you' in self.query:
                speak("it's my pleasure sir")
                speak("sir, do you have any other work?")
            elif 'open youtube' in self.query:
                speak('opening youtube sir')
                speak('sir, what i have to search in Youtube?')
                k=takeCommand()
                webbrowser.open("www.youtube.com/results?search_query=" + k + "")
                speak("sir, do you have any other work")
            elif 'open google' in self.query:
                speak('opening google sir')
                webbrowser.open("google.com")
                speak("sir, do you have any other work")
            elif 'open stackoverflow' in self.query:
                speak('opening stack over flow sir')
                webbrowser.open("stackoverflow.com")
                speak("sir, do you have any other work")

            elif 'play music' in self.query:
                music_dir='C:\\Users\\DIVVELA VISHNU\\Downloads\\songs'

                songs = os.listdir(music_dir)
                rd=random.choice(songs)
                if rd.endswith('.mp3'):
                    speak('playing the music sir')
                    os.startfile(os.path.join(music_dir,rd))
            elif 'time' in self.query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
                speak("sir, do you have any other work")

            elif 'sleep mode' in self.query:
                speak("Ok sir,   Bye sir   have a nice day")
                break
            elif 'quit' in self.query:
                speak("Ok sir,   Bye sir   have a nice day")
                break
            elif 'nothing' in self.query:
                speak('Ok sir, Bye sir have a nice day')
                break
            elif 'bye' in self.query:
                speak("Ok sir,   Bye sir   have a nice day")
                exit()
            elif 'day' in self.query:
                day = datetime.datetime.now().strftime("%A")
                speak(f"Sir, today is {day}")
                speak("sir, do you have any other work")

            elif 'date' in self.query:
                date =  datetime.datetime.now()
                speak('sir, todays date is ')
                speak(date)
                speak("sir, do you have any other work")

            elif 'code' in self.query:
                path = "C:\\Microsoft VS Code\\Code.exe"
                speak('opening vs code editor sir')
                os.startfile(path)
                speak("sir, do you have any other work")

            elif 'send email' in self.query:
                try:
                    #speak("To whom i have to send the email sir ?")
                    #em=takeCommand().lower
                    speak("what should i send sir ?")
                    content=takeCommand().lower()
                    to = 'arunadivvela88@gmail.com'
                    sendEmail(to,content)
                    speak("Email has been send sir!")
                except Exception as e:
                    print(e)
                    speak("Soryy sir i am unable to send this email at this moment")
            elif 'open notepad' in self.query:
                path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
                speak('opening notepad sir')
                os.startfile(path)
                speak("sir, do you have any other work")

            elif 'open command prompt' in self.query:
                speak('opening command prompt sir')
                os.system('start cmd')
                speak("sir, do you have any other work")

            elif 'open camera' in self.query:
                speak('opening camera sir')
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam',img)
                    k=cv2.waitKey(50)
                    if k==27:
                        break
                cap.release()
                cv2.destroyAllWindows()
                speak("sir, do you have any other work")

            elif 'ip address' in self.query:
                from requests import get
                ip = get('https://api.ipify.org').text
                print(ip)
                speak(f"Sir, Your IP address is {ip}")
                speak("sir, do you have any other work")

            elif 'open facebook' in self.query:
                speak('opening facebook sir')
                webbrowser.open('www.facebook.com')
                speak("sir, do you have any other work")

            elif 'open google search' in self.query:
                speak("sir, what should i search on google ?")
                self.query=takeCommand().lower()
                webbrowser.open(f"{self.query}")
                speak("sir, do you have any other work")

            elif 'send message' in self.query:
                kit.sendwhatmsg("+919849521890","This is testing protocol",4,13)
                speak('Message has been sent sir')
                speak("sir, do you have any other work")

            elif 'my favourite video in youtube' in self.query:
                speak('opening your favourate video on youtube sir')
                kit.playonyt("fast and furious 9 trailer")
                speak("sir, do you have any other work")


            elif 'my favourite video on youtube' in self.query:
                speak('opening your favorate video on youtube sir')
                kit.playonyt("fast and furious 9 trailer")
                

            elif 'favourite music' in self.query:
                speak('playing your favourate music sir')
                music_dir='C:\\Users\\DIVVELA VISHNU\\Downloads\\songs'

                songs = os.listdir(music_dir)
                if rd.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir,songs[0]))

            #elif 'no' in self.query:
            #    speak("thanks for using me sir, have a good day!")
            #    sys.exit()
            elif 'close notepad' in self.query:
                speak('Ok sir, closing notepad')
                os.system("taskkill /f /im notepad.exe")
                speak("sir, do you have any other work")

            elif 'set alarm' in self.query:
                n=int(datetime.datetime.now().hour)
                if n == 22:
                    music_dir='C:\\Users\\DIVVELA VISHNU\\Downloads\\songs'

                    songs = os.listdir(music_dir)
                    rd=random.choice(songs)
                    if rd.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir,rd))
            elif 'joke' in self.query:
                joke = pyjokes.get_joke()
                speak('sir, todays joke is ')
                speak(joke)
                speak("sir, do you have any other work")

            elif 'shut down' in self.query:
                speak('shutting down your system sir ')
                os.system('shutdown /s /t 5')
            elif 'restart' in self.query:
                os.system('shutdown /r /t 5')
            elif 'sleep' in self.query:
                os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
            elif 'open ms teams' in self.query:
                speak('opening microsoft teams sir')
                path = "C:\\Users\\DIVVELA VISHNU\\Desktop\\All Desktop Apps\\Microsoft Teams" 
                os.startfile(path)
                speak("sir, do you have any other work")

            elif 'close ms teams' in self.query:
                speak('closing microsoft teams sir')
                os.system("taskkill /f /im Microsoft Teams.exe")
                speak("sir, do you have any other work")
            
            elif 'switch the window' in self.query:
                speak('switching the window sir')
                pyautogui.keyDown("alt")
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.keyUp('alt')
            elif  'news' in self.query:
                speak('please wait sir, fetching the latest news today')
                news()
            elif 'where i am' in self.query or 'where are we' in self.query or 'where am i' in self.query :
                speak("wait sir, let me check")
                from requests import get
                try:
                    
                    ipAddress = get('https://api.ipify.org').text
                    print(ipAddress)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAddress+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city=geo_data['city']
                    country = geo_data['country']
                    speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    speak("sorry sir, Due to network issue i am unable to find where we are..")
                    pass
            elif 'instagram profile' in self.query or 'profile on instagram' in self.query:
                speak("sir please enter the user name correctly ... ")
                name=input('Enter User name Here = ')
                webbrowser.open(f"www.instagram.com/{name}/")
                speak(f"Sir here is the profile of the user {name}")
                time.sleep(5)
                speak('sir would you like to download profile picture of this account ?(yes or no)')
                condition = takeCommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader() #pip install instadownloader
                    mod.download_profile(name,profile_pic_only=True)
                    speak('I am done sir, profile picture is sved in our main folder. now i am ready for next command')
                else:
                    speak('ok sir, sir do you have any other work?')
                    pass
            elif 'screenshot' in self.query or 'screen shot' in self.query:
                speak('sir, please tell me the name for this screen shot file')
                name = takeCommand().lower()
                speak('sir please hold the screen for few seconds, i am taking screenshot')
                time.sleep(3)
                img=pyautogui.screenshot()
                img.save(f"{name}.png")
                speak('i am done sir, the screen shot is saved in our main folder. now i am ready for next command')
            elif 'prime' in self.query:
                speak('what i have to search in Amazon Prime Video Sir ?')
                take = takeCommand()
                speak('opening Amazon prime video sir')
                webbrowser.open(f"https://www.primevideo.com/search/ref=atv_nb_sr?phrase={take}&ie=UTF8")
                speak("sir, do you have any other work")
            elif 'what is my name' in self.query:
                speak(f"sir, your name is {original_name}")
            elif 'pdf' in self.query:
                pdf_reader()
            elif 'hi' in self.query:
                speak('Hi sir, what can i do for you?')
            elif 'what is your name' in self.query:
                speak('sir my name is Jarvis, i am a prototype of personal assist using Aritificial Intelligence')
                speak('sir , do you have any other work?')
            elif 'i am very happy with your service' in self.query:
                speak('Thanks a lot sir,      sir do you have any other work?')
            elif 'whatsapp' in self.query or 'whats app' in self.query:
                
                driver = webdriver.Chrome(ChromeDriverManager().install())
                #driver = webdriver.Chrome("C:/Users/michael/Downloads/chromedriver_win32/chromedriver.exe")
                driver.get("http://web.whatsapp.com")
                driver.maximize_window()
                speak('sir, enter the name to which you have to send message;')
                name = input("Enter name :")
                speak('sir, enter the message you have to send')
                msg = input("Enter Message :")
                speak('sir , enter the occurance of the message;')
                count = int(input("Enter the occurance of your message have to be delivered"))
                input("Enter any thing after scaning your Qr Code")
                user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
                user.click()
                msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
                for index in range(count):
                    msg_box.send_keys(msg)
                    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
                speak('Message sended successfully')
                speak('sir, do you have any other work?')
            elif 'who is' in self.query:
                webbrowser.open(self.query)
            elif 'hello' in self.query:
                speak('hello sir how are you')
            elif 'good' in self.query or 'well' in self.query:
                speak('great to that you are well sir')
                speak('sir, do you have any other work?')
            


            elif "i love you" in self.query:
                speak("It's hard to understand sir")
                speak('sir, do you have any other work?')
            elif "dont listen" in self.query or "stop listening" in self.query:
                speak("ok sir")
                jarvis()

            elif 'change my name' in self.query or 'change name' in self.query:
                speak('what is your new name sir ?')
                s = takeCommand()
                original_name = s
                speak('Ok sir')
                speak("Now your name is ")
                speak(s)
                speak('sir, do you have any other work?')

            elif 'user details' in self.query:
                opendetails()

            elif 'about me' in self.query or 'do you know me'in self.query:
                speak("what is your name")
                s = takecommend().lower()
                if 'vishnu' in s:
                    speak('Yes, sir i know your data')
                else:
                    speak("i dont have your data")
                speak('do you have any other work sir?')
            elif "who made you" in self.query or "who created you" in self.query:
                speak("I have been created by Vishnu")
                speak('sir do you have any other work?')
            elif  'where is the location of' in self.query:
                
                self.query = self.query.replace("where is the location of","")
                location = self.query
                speak("User asked to Locate")
                speak(location)
                
                webbrowser.open("https://www.google.com/maps/place/" + location + "")
                speak('sir, do you have any other work?')
            elif "weather" in self.query or 'climate' in self.query:
                speak(" Can you enter your City name sir?")
                city_name = input('enter your city name = ')
                webbrowser.open("https://www.accuweather.com/en/in/" + city_name + "/189231/weather-forecast/189231")
                speak("opening wether for")
                speak(city_name)
                speak('sir , do you have any other work?')
            
            elif 'help me' in self.query:
                speak("ofcourse sir ! how can i help you sir? ")
                speak('can you say your problem sir?')
                s = takeCommand()
                print(s)
                speak(
                    "There are 3 thing that i can do for you sir i can search for it on google or youtube or wikipedia")
                speak("where i should to serach sir")
                s1 = takeCommand().lower()
                if s1 == 'google':
                    speak("opening  google sir!")
                    webbrowser.open(
                        "www.bing.com/search?q=" + s + "=9d02b0a92caa4bc895c28ea9269d27e6&FORM=ANAB01&PC=ASTS")

                elif s1 == 'youtube' :
                    speak(f"opening youtube{sex}!")
                    webbrowser.open("www.youtube.com/results?search_query=" + s + "")

                elif s1 == 'wikipedia' :
                    speak("Accroding to wikipedia")
                    result = wikipedia.summary(s, sentences=2)
                speak('sir, do you have any other work?')
            
            elif "know about vishnu" in self.query:
                speak(
                    "yes sir i know him becuase of him im able to talk to you he is a very nice person would you like to know more about mister Vishnu Sai Kumar Divvela")
                s = takeCommand().lower()
                if s == "yes":
                    opendetails()
                else:
                    speak("ok !sir thank you for give me time sir")
                speak('sir, do you have any other work?')
            elif 'open calculator'in self.query:
                speak("opening the calculator sir")
                path = "C:\\Users\\DIVVELA VISHNU\\Desktop\\python projects\\Scientific aluculator by python"
                os.startfile(path)
                speak("sir, do you have any other work")
            elif 'open chrome' in self.query:

                speak("opening broswer sir")
                p = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(p)
                time.sleep(6)
                speak('sir, do you have any other work?')
            elif 'google maps' in self.query:
                speak('sir, enter the name of the city which you want the location!')
                location = input('Enter the city = ')
                speak("User asked to Locate")
                speak(location)
                
                webbrowser.open("https://www.google.com/maps/place/" + location + "")
                speak('sir, do you have any other work?')
            elif 'gaana' in self.query:
                speak('sir, what songs do you want to search?')
                speak('Please enter that song sir!')
                song = input('Enter the song = ')
                speak(f"sir you are searching for the songs for {song}")
                speak('opening gaana sir')
                webbrowser.open(f"https://gaana.com/search/{song}")
                speak('sir, do you want any other work ?')
            elif 'train tickets' in self.query:
                speak('opening IRCTC website sir')
                webbrowser.open('https://www.irctc.co.in/nget/train-search')
                speak('sir do you have any other work ?')
            elif 'aeroplane tickets' in self.query:
                speak('opening sir')
                webbrowser.open('https://www.air.irctc.co.in/')
                speak('sir, do you have any other work?')
            elif 'bus tickets' in self.query:
                speak('opening sir')
                webbrowser.open('https://www.redbus.in/?gclid=CjwKCAiApNSABhAlEiwANuR9YDZQrxY4fqm33Beenf-Q4D8t34aCOzgx4TPavaBgzfT1evr_1PPn0hoC9JMQAvD_BwE')
                speak('sir, do you have any other work?')
            elif 'movie tickets' in self.query:
                speak('opening sir')
                webbrowser.open('https://in.bookmyshow.com/')
                speak('sir, do you have any other work?')
            elif 'open amazon shopping' in self.query:
                speak('what i want to search in amazon sir?')
                hi = takeCommand()
                speak('ok sir, opening amazon shopping sir')
                webbrowser.open(f"https://www.amazon.in/s?k={hi}&ref=nb_sb_noss")
                speak('sir, do you have any other work?')
            elif 'open filpkart shopping' in self.query:
                speak('what i want to search in flipkart sir?')
                hi = takeCommand()
                speak('ok sir, opening flipkart shopping sir')
                webbrowser.open(f"https://www.flipkart.com/search?q={hi}=AS_Query_HistoryAutoSuggest_2_0&otracker1=AS_Query_HistoryAutoSuggest_2_0&marketplace=FLIPKART&as-show=on&as=off&as-pos=2&as-type=HISTORY")
                speak('sir, do you have any other work?')
            elif 'book an appointment for hospital' in self.query or 'hospital' in self.query: 
                speak('opening  Appolo website sir ')
                webbrowser.open('https://www.askapollo.com/')
                speak('sir, do you have any other work?')
            elif 'book an appointment for homeocare' in self.query or 'homeocare' in self.query:
                speak('opening homeocare sir')
                webbrowser.open('https://www.onlinehomeocare.com/')
                speak('sir, do you have any other work?')
            elif 'gas cylinder' in self.query:
                speak('opening sir')
                webbrowser.open('https://cx.indianoil.in/webcenter/portal/LPG/pages_bookyourcylinder')
                speak('sir, do you have any other work?')
            elif 'recharge' in self.query:
                speak('please enter your mobile network sir')
                recharge = input('Enter your mobile network = ').lower()
                if recharge == 'jio':
                    speak('opening jio website sir')
                    webbrowser.open('https://www.jio.com/selfcare/recharge/mobility/plans/?serviceId=3c88378636c215296aed3e7c5a94def7&partyId=5042838705&serviceType=mobility&next=PREPAID&billingType=PREPAID&maskedServiceId=93*****106')
                elif recharge == 'airtel':
                    speak('opening airtel website sir')
                    webbrowser.open('https://www.airtel.in/')
                elif recharge == 'bsnl':
                    speak('opening bsnl website sir')
                    webbrowser.open('https://www.bsnl.co.in/')
                else :
                    speak('opening recharge website sir')
                    webbrowser.open('https://www.freecharge.in/prepaid')
                speak('sir, do you have any other work?')
            
            






            
               
            

            
                
            

            

startExecution = MainThread()  


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    def startTask(self):
        
        
        self.ui.movie = QtGui.QMovie("../../Downloads/jarvis1.gif")
        self.ui.JarvisGui.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Downloads/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        #startExecution.TaskExecution()
        startExecution.start()
        
        

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)



app = QApplication(sys.argv)
advjarvis = Main()
advjarvis.show()
exit(app.exec_())










        


        
        
       






        

       




        
        
            


        
        

        


        

