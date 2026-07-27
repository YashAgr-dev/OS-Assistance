import subprocess
import os
import pygetwindow as gw
import pyautogui
import ctypes
import time


# ==============================
# Windows System Applications
# ==============================

def open_settings():
    subprocess.Popen("start ms-settings:", shell=True)

def open_control_panel():
    subprocess.Popen("control")

def open_task_manager():
    subprocess.Popen("taskmgr")

def open_cmd():
    subprocess.Popen("cmd")

def open_powershell():
    subprocess.Popen("powershell")

def open_terminal():
    subprocess.Popen("wt")

def open_registry():
    subprocess.Popen("regedit")

def open_device_manager():
    subprocess.Popen("devmgmt.msc")

def open_disk_management():
    subprocess.Popen("diskmgmt.msc")

def open_services():
    subprocess.Popen("services.msc")

def open_event_viewer():
    subprocess.Popen("eventvwr.msc")

def open_system_information():
    subprocess.Popen("msinfo32")

def open_resource_monitor():
    subprocess.Popen("resmon")

def open_performance_monitor():
    subprocess.Popen("perfmon")

def open_character_map():
    subprocess.Popen("charmap")

def open_snipping_tool():
    subprocess.Popen("snippingtool")

# ==============================
# User Folders
# ==============================

def open_downloads():
    os.startfile(os.path.join(os.path.expanduser("~"), "Downloads"))

def open_documents():
    os.startfile(os.path.join(os.path.expanduser("~"), "Documents"))

def open_desktop():
    os.startfile(os.path.join(os.path.expanduser("~"), "Desktop"))

def open_pictures():
    os.startfile(os.path.join(os.path.expanduser("~"), "Pictures"))

def open_videos():
    os.startfile(os.path.join(os.path.expanduser("~"), "Videos"))

def open_music():
    os.startfile(os.path.join(os.path.expanduser("~"), "Music"))

def open_startup():
    subprocess.Popen("shell:startup", shell=True)

def open_temp():
    os.startfile(os.environ["TEMP"])



# ==========================================
# WINDOW CONTROL FUNCTIONS
# ==========================================

# Show Active Window
def active_window():

    window = gw.getActiveWindow()

    if window:

        print("Active Window :", window.title)

    else:

        print("No Active Window")


# List All Windows
def list_windows():

    windows = gw.getAllTitles()

    print("\nOpen Windows\n")

    for window in windows:

        if window.strip():

            print(window)


# Find Window
def find_window(title):

    windows = gw.getWindowsWithTitle(title)

    if windows:

        print("Window Found :", windows[0].title)

    else:

        print("Window Not Found")


# Maximize Window
def maximize_window(title):

    windows = gw.getWindowsWithTitle(title)

    if windows:

        windows[0].maximize()

        print("Window Maximized")

    else:

        print("Window Not Found")


# Minimize Window
def minimize_window(title):

    windows = gw.getWindowsWithTitle(title)

    if windows:

        windows[0].minimize()

        print("Window Minimized")

    else:

        print("Window Not Found")


# Restore Window
def restore_window(title):

    windows = gw.getWindowsWithTitle(title)

    if windows:

        windows[0].restore()

        print("Window Restored")

    else:

        print("Window Not Found")


# Close Window
def close_window(title):

    windows = gw.getWindowsWithTitle(title)

    if windows:

        windows[0].close()

        print("Window Closed")

    else:

        print("Window Not Found")


# Activate Window
def activate_window(title):

    windows = gw.getWindowsWithTitle(title)

    if windows:

        windows[0].activate()

        print("Window Activated")

    else:

        print("Window Not Found")


# Move Window
def move_window(title, x, y):

    windows = gw.getWindowsWithTitle(title)

    if windows:

        windows[0].moveTo(x, y)

        print("Window Moved")

    else:

        print("Window Not Found")


# Resize Window
def resize_window(title, width, height):

    windows = gw.getWindowsWithTitle(title)

    if windows:

        windows[0].resizeTo(width, height)

        print("Window Resized")

    else:

        print("Window Not Found")


# Show Desktop
def show_desktop():

    pyautogui.hotkey("win", "d")

    print("Desktop Displayed")


# Lock Windows
def lock_windows():

    ctypes.windll.user32.LockWorkStation()

    print("Windows Locked")


# Switch Window
def switch_window():

    pyautogui.hotkey("alt", "tab")

    print("Window Switched")


# Screenshot Active Window
def active_window_screenshot(filename):

    image = pyautogui.screenshot()

    image.save(filename)

    print("Screenshot Saved")    