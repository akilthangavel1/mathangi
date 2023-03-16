import pickle
import urllib.request
import http
import speech_recognition as sr
import cv2
from textblob import  TextBlob
filename = 'knn.sav'
loaded_model = pickle.load(open(filename, 'rb'))
r = sr.Recognizer()
speech = sr.Microphone(device_index=1)
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
det=['itching',
'skin rash',
'nodal skin eruptions',
'continuous sneezing',
'shivering',
'chills',
'joint pain',
'stomach pain',
'acidity',
'ulcers on tongue',
'muscle wasting',
]

a=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
b=0
c=0
if True:
    for j in range(0,11):
        print(det[j])
        fti="Do you have "+str(det[j])
        speaker.Speak(fti)
        with speech as source:
            print("say something!…")
            audio = r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            recog = r.recognize_google(audio, language = 'en-US')
            print(recog)
            if recog in "yes":
                b=1
            elif recog in "no":
                b=0
        except:
            pass
        print(b)
        a[j]=float(b)
    
Current_reports = [a]
predicted = loaded_model.predict(Current_reports)
ty="Your Body Condition is"+str(predicted[0])
speaker.Speak(ty)
print(ty)

if predicted[0] not in "Normal":
    speaker.Speak("Do you want to book appointment ")
    with speech as source:
            print("say something!…")
            audio = r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
    try:
        recog = r.recognize_google(audio, language = 'en-US')
        print(recog)
        if recog in "yes":
            c=1
        elif recog in "no":
            c=0
    except:
        pass
    print(c)
    if c==1:
        ur= "https://api.thingspeak.com/update?api_key=C6TYSSCZS42F7QCI&field6=Person1_0987654321"
        urllib.request.urlopen(ur)

        
        
    
    

