import webbrowser
import pyautogui
import subprocess
import urllib.parse

# ==========================================
# BROWSER AUTOMATION
# ==========================================

# Open Browsers

def open_chrome():
    subprocess.Popen("start chrome", shell=True)

def open_edge():
    subprocess.Popen("start msedge", shell=True)

def open_firefox():
    subprocess.Popen("start firefox", shell=True)

# Browser Controls

def new_tab():
    pyautogui.hotkey("ctrl", "t")

def close_tab():
    pyautogui.hotkey("ctrl", "w")

def reopen_closed_tab():
    pyautogui.hotkey("ctrl", "shift", "t")

def next_tab():
    pyautogui.hotkey("ctrl", "tab")

def previous_tab():
    pyautogui.hotkey("ctrl", "shift", "tab")

def new_window():
    pyautogui.hotkey("ctrl", "n")

def incognito_mode():
    pyautogui.hotkey("ctrl", "shift", "n")

def refresh_page():
    pyautogui.press("f5")

def hard_refresh():
    pyautogui.hotkey("ctrl", "shift", "r")

def bookmark_page():
    pyautogui.hotkey("ctrl", "d")

def open_history():
    pyautogui.hotkey("ctrl", "h")

def open_downloads():
    pyautogui.hotkey("ctrl", "j")

# Websites

def open_google():
    webbrowser.open("https://www.google.com")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_github():
    webbrowser.open("https://github.com")

def open_chatgpt():
    webbrowser.open("https://chat.openai.com")

def open_stackoverflow():
    webbrowser.open("https://stackoverflow.com")

def open_leetcode():
    webbrowser.open("https://leetcode.com")

def open_gmail():
    webbrowser.open("https://mail.google.com")

def open_google_drive():
    webbrowser.open("https://drive.google.com")

def open_google_maps():
    webbrowser.open("https://maps.google.com")

# Search Functions

def search_google(query):
    webbrowser.open(
        "https://www.google.com/search?q=" +
        urllib.parse.quote(query)
    )

def search_youtube(query):
    webbrowser.open(
        "https://www.youtube.com/results?search_query=" +
        urllib.parse.quote(query)
    )

def search_github(query):
    webbrowser.open(
        "https://github.com/search?q=" +
        urllib.parse.quote(query)
    )

def search_stackoverflow(query):
    webbrowser.open(
        "https://stackoverflow.com/search?q=" +
        urllib.parse.quote(query)
    )

def search_leetcode(query):
    webbrowser.open(
        "https://leetcode.com/problemset/?search=" +
        urllib.parse.quote(query)
    )

# Zoom

def zoom_in():
    pyautogui.hotkey("ctrl", "+")

def zoom_out():
    pyautogui.hotkey("ctrl", "-")

def reset_zoom():
    pyautogui.hotkey("ctrl", "0")

# Navigation

def go_back():
    pyautogui.hotkey("alt", "left")

def go_forward():
    pyautogui.hotkey("alt", "right")

# Scroll

def scroll_up():
    pyautogui.scroll(600)

def scroll_down():
    pyautogui.scroll(-600)