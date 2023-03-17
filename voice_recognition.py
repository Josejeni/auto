import speech_recognition as abi
import pyttsx3

engine=pyttsx3.init()
listener=abi.Recognizer()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
with abi.Microphone() as source:
    print("Listening......")
    voice=listener.listen(source)
    command=listener.recognize_google(voice)
    engine.say('command')
    engine.runAndWait()
    print(command)
# except:
#     pass
