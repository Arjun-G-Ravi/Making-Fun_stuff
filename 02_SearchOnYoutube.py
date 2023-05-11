# Just tell the program what you want once "I am listening" appears on screen
# The program will search on youtube and play the first video on recomendation
import speech_recognition as sr
import pyttsx3
from time import sleep
import pywhatkit as pk

def talk(): #using pyttsx3
    words = input() 
    engine = pyttsx3.init() 
    engine.setProperty('rate',125)  
    engine.setProperty('volume',2.0)   
    voices = engine.getProperty('voices')       
    engine.setProperty('voice', voices[0].id) 
    engine.say(words)
    engine.runAndWait()
    engine.stop()
    
def talk(word):
    engine = pyttsx3.init() 
    engine.setProperty('rate',125)  
    engine.setProperty('volume',2.0)   
    voices = engine.getProperty('voices')     
    engine.setProperty('voice', voices[0].id) 
    engine.say(word)
    engine.runAndWait()
    engine.stop()

def myCommand(): 
    r = sr.Recognizer()                                                                                    
    with sr.Microphone() as source: 
        talk("Next command sir")  
        sleep(.25)                                                                     
        print("I am listening:") 
        r.pause_thresholdld =  1 
        audio = r.listen(source) 
        
    try:  
        query = r.recognize_google(audio, language='en-in') #result2 is being printed
        return query 
    
    except sr.UnknownValueError: 
        print("Sorry. I didn't get that")
        talk("Sorry. I didn't get that")
        sleep(1)
        return "rerun"
    
x = myCommand()
print("\n\n\n",x)
pk.playonyt(x)