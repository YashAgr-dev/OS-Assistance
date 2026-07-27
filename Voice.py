import speech_recognition as sr

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone(1) as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print("You said:",command)
        return command
    except Exception :
        print("Sorry, I didn't understand that . Please try again.")  
        return ""
