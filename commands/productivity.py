import os
import time
import datetime
import subprocess
import pyperclip
import sqlite3


# ==========================================
# Productivity Functions
# ==========================================

# Create Note
def create_note(note):

    with open("notes.txt", "a") as file:

        file.write(note + "\n")

    print("Note Saved Successfully")


# Show Notes
def show_notes():

    if os.path.exists("notes.txt"):

        with open("notes.txt", "r") as file:

            print(file.read())

    else:

        print("No Notes Found")


# Clear Notes
def clear_notes():

    open("notes.txt", "w").close()

    print("All Notes Cleared")


# Add Task
def add_task(task):

    with open("todo.txt", "a") as file:

        file.write(task + "\n")

    print("Task Added Successfully")


# Show Tasks
def show_tasks():

    if os.path.exists("todo.txt"):

        with open("todo.txt", "r") as file:

            print(file.read())

    else:

        print("No Tasks Found")


# Clear Tasks
def clear_tasks():

    open("todo.txt", "w").close()

    print("All Tasks Cleared")


# Show Date
def current_date():

    print(datetime.date.today())


# Show Time
def current_time():

    print(datetime.datetime.now().strftime("%I:%M:%S %p"))


# Stopwatch
def stopwatch():

    input("Press ENTER to Start Stopwatch")

    start = time.time()

    input("Press ENTER to Stop Stopwatch")

    end = time.time()

    print("Elapsed Time :", round(end - start, 2), "Seconds")


# Countdown Timer
def countdown(seconds):

    while seconds:

        mins, secs = divmod(seconds, 60)

        print(f"{mins:02}:{secs:02}", end="\r")

        time.sleep(1)

        seconds -= 1

    print("\nTime's Up!")


# Open Calculator
def open_calculator():

    subprocess.Popen("calc")


# Open Notepad
def open_notepad():

    subprocess.Popen("notepad")


# Open Clock
def open_clock():

    subprocess.Popen("start ms-clock:", shell=True)


# Open Calendar
def open_calendar():

    subprocess.Popen("start outlookcal:", shell=True)


# Open Paint
def open_paint():

    subprocess.Popen("mspaint")


# Create Folder Quickly
def quick_folder(folder):

    os.makedirs(folder, exist_ok=True)

    print("Folder Created Successfully")


# Open Downloads
def open_downloads():

    os.startfile(os.path.join(os.path.expanduser("~"), "Downloads"))