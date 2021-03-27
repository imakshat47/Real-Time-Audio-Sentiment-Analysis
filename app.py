# Importing libs
import speech_recognition as sr
from textblob import TextBlob as blob
# Check Devices
print(" Devices: ")
print(sr.Microphone.list_microphone_names())
# Initiating Instance
r = sr.Recognizer()
# Let's go for listening...
while(True):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
        print("Listening...")
        try:
            text = r.recognize_google(audio)
            print("Text => ",text)
            tb = blob(text)
            print("Polarity => ",tb.sentiment[0])
            print("Subjectivity => ",tb.sentiment[1])
        except:
            print('Sorry!! Something went wrong...')        
    print("Listening... ")
    