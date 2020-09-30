import pyttsx3
import random
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import re
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def there_exists(terms):
    for term in terms:
        if term in query:
            return True
#taking audio string
def speak(audio_string):
    engine.say(audio_string)
    engine.runAndWait()
#Greet me command
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Elena: Good Morning Human")
        speak("Good Morning Human")
    elif hour >=12 and hour < 16:
        print("Elena: Good Afternoon Human")
        speak("Good Afternoon Human")
    else:
        print("Elena: Good Evening Human")
        speak("Good Evening Human")
    print("Elena: I am Elena")
    speak("I am Elena,")
#Recognizing commands
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print(e)
        print("Elena: Say that again please, I didn't recognize....")
        return "None"
    return query

#mailing function
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your email id','your password')
    server.sendmail('Your email id', to, content)
    server.close()

def remove(string): 
    pattern = re.compile(r'\s+') 
    return re.sub(pattern, '', string)

def respond(query):
    if there_exists(['hey','hi','hello','hai','hi there']):
        greetings = ["hey, how can I help you", "hey, what's up?", "I'm listening", "how can I help you?","hello"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)
        return

    if there_exists(["how are you","how are you doing"]):
        speak("I'm very well, thanks for asking")
        return

    if there_exists(["what is your name","what's your name","tell me your name"]):
        print("Elena: My name is Elena")
        speak("my name is Elena")
        return

    if there_exists(["who made you","created you"]): 
        say = "I have been created by Rishabh Kumar."
        speak(say) 
        return

    if there_exists(['who are you','define yourself']):
        print("Hello, I am Elena. Your personal Assistant. I am here to make your life easier. You can command me to perform various tasks such as searching or opening applications etcetra")
        speak("Hello, I am Elena. Your personal Assistant. I am here to make your life easier. You can command me to perform various tasks such as searching or opening applications etcetra")
        return

    if there_exists(['what are you doing']):
        speak("I am listening to you.")
        return

    if there_exists(['wikipedia','wiki']):
        speak('Searching in wikipedia....')
        query=query.replace("wikipedia", "")
        results=wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        return

    if there_exists(['open youtube']):
        speak("opening youtube")
        webbrowser.open("www.youtube.com")
        return

    if there_exists(['open google']):
        speak("opening google")
        webbrowser.open("www.google.co.in")
        return

    if there_exists(['open gmail']):
        speak("opening gmail")
        webbrowser.open("mail.google.com")
        return

    if there_exists(['open facebook']):
        speak("opening facebook")
        webbrowser.open("www.fb.com")
        return

    if there_exists(['open github']):
        speak("opening github")
        webbrowser.open("www.github.com")
        return

    if there_exists(['play music','music','songs','song','play songs']):
        music_dir='E:\\music'
        songs = os.listdir(music_dir)
        music = songs[random.randint(0,len(songs)-1)]
        speak(f"playing {music}")
        print(music)
        os.startfile(os.path.join(music_dir,music))
        exit()

    if there_exists(['the time','what\'s the time' ]):
        time=datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Elena: the time is {time}")
        speak(f"the time is {time}") 
        return   

    if there_exists(['email','send an email']):
        try:
            speak("What should i send")
            content = takeCommand()
            speak("To whom I have to send this e mail")
            to = takeCommand().lower()
            t = remove(to)
            print(t)
            sendEmail(t, content)
            speak(f"Your email has been sent to {t} successfully")
            return
        except Exception as e:
            print(e)
            print("\nElena: Sorry, I am unable to send this email. Please try again")
            speak("Sorry, I am unable to send this email. Please try again")
            return

    if there_exists(['open vs code','open visual studio code','visual studio code','vs code']):
        code_path="C:\\Users\\risha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak('opening visual studio code')
        os.startfile(code_path)
        return
    if there_exists(['word','ms word']): 
        speak("Opening Microsoft Word") 
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word') 
        return

    if there_exists(['excel','ms excel']): 
        speak("Opening Microsoft Excel") 
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel') 
        return

    if there_exists(['google chrome','chrome']): 
        speak("Opening Google Chrome") 
        os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe') 
        return
    
    if there_exists(['search on google']):
        print("Elena: What do you want to search ?")
        speak("What do you want to search ?")
        search_g=takeCommand()
        url_g='https://google.com/search?q='+search_g
        print('Elena: Here is what I found')
        speak('Here is what I found')
        webbrowser.get().open(url_g)
        exit()

    if there_exists(['search on youtube']):
        print("Elena: What do you want to search ?")
        speak("What do you want to search ?")
        search_y=takeCommand()
        url_y = f"https://www.youtube.com/results?search_query={search_y}"
        print(f"Elena: here is what I found for{search_y} on youtube")
        speak(f'Here is what I found for {search_y} on youtube')
        webbrowser.get().open(url_y)
        exit()

    if there_exists(['find location','location','open map','open google map','google map','map']):
        print("Elena: Where do you want to go ?")
        speak("Where do you want to go ?")
        location=takeCommand()
        url='https://google.nl/maps/place/'+location+'/&amp;'
        webbrowser.get().open(url)
        print('Elena: Here is what I found')
        speak('Here is what I found')
        return


    if there_exists(['bye','good bye','goodbye','bye bye','exit','quit','no thank you','no','no thanks','bye elena','thanks','get lost','nothing']):
        speak("Have a nice day, Good Bye")
        exit()
    else:
        speak("I don't know that. I will inform my developers to make me familier with this, thank you.")

time.sleep(1)
wishMe()
c=0
while(1):
    if c==0:
        print("Elena: How may I help you\n")
        speak("How may i help you")
    else:
        print("Elena: Is there anything I can do for you\n")
        speak("Is there anything I can do for you")
    c+=1
    query = takeCommand().lower()
    respond(query)
