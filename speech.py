# import speech_recognition as sr

# recognizer = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Listening...")
#     audio = recognizer.listen(source)

# def listen():
#     with sr.Microphone(device_index=1) as source:
#         print("Bol bhai...")
#         recognizer.adjust_for_ambient_noise(source, duration=1)
#         print("Ab bol!")
#         audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
#     try:
#         command = recognizer.recognize_google(audio, language="en-IN")
#         print("Tune bola:", command)
#         return command.lower()
#     except sr.UnknownValueError:
#         print("Samjha nahi, dobara bol!")
#         return ""
#     except sr.RequestError:
#         print("Internet check kar!")
#         return ""
import speech_recognition as sr
import webbrowser
import os

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Bol bhai...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language="en-IN")
        print("Tune bola:", command)
        return command.lower()
    except:
        return ""

def execute(command):
    if "youtube" in command:
        webbrowser.open("youtube.com")
        print("YouTube khul raha hai!")
    
    elif "google" in command:
        webbrowser.open("google.com")
        print("Google khul raha hai!")
    
    elif "time" in command:
        from datetime import datetime
        print("Time hai:", datetime.now().strftime("%H:%M"))
    
    elif "band kar" in command or "exit" in command:
        print("Bye bhai!")
        exit()
    elif "Chrome open" in command:
        webbrowser.open("chrome")
        print("Chrome khul raha hai!")
    else:
        print("Samjha nahi, dobara bol!")

# Main loop
print("Voice Assistant Ready! Bol kuch bhi...")
while True:
    command = listen()
    if command:
        execute(command)