import random
#from gtts import gTTS
#from playsound import playsound
#import os
import pyttsx3
i=0
par=True
engine = pyttsx3.init()

def train(question):
    dataset=open("dataset.txt","a+")
    ip="- - "+question+"\n"
    response=input("Suggestion: ")
    if response=="-":
        dataset.close
        chat()
    op="  - "+response+"\n"
    dataset.write(ip)
    dataset.write(op)
    chat()
    dataset.close

def voice(word):
    #global i
    #i+=1
    #txt=gTTS(text=word, lang='en-us')
    #file=str("voices/voice"+str(i)+".mp3")
    #txt.save(file)
    #playsound(file)
    #----------------
    engine.setProperty('rate', 145)
    engine.setProperty('volume', 1)
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(word)
    engine.runAndWait()

def chat():
    global par
    while(par):
        question=input("You: ")
        q=question.lower()
        if q=="bye":
            print("See you again!")
            voice("See you again!")
            par=False
            break
        ques="- - "+q+"\n"
        l=[]
        dataset=open("dataset.txt","r")
        for line in dataset:
            fileline=line.lower()
            if ques in fileline:
                readl=dataset.readline()
                l.append(readl.lower())
        try:
            r=random.choice(l)
            r1=r.strip("  - ")
            response=r1.strip("\n")
            print("ZenBot:",response)
            voice(response)
        except IndexError:
            print("------What shall i reply for this?------")
            voice("What shall i reply for this?")
            train(question)
        dataset.close()

chat()
