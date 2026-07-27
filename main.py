    
from Speak import *
from Voice import take_command
from assistance import process_command
from core import speak

while True:

    command=take_command()
    query = command.lower()

    if command =="exit":
        speak("Goodbye Sir")
        break

    process_command(command, query)




    