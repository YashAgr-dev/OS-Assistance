import pyautogui
import subprocess
import screen_brightness_control as sbc

# ==========================================
# MEDIA CONTROL
# ==========================================

# Play / Pause
def play_pause():
    pyautogui.press("playpause")
    print("Play/Pause")

# Next Song
def next_song():
    pyautogui.press("nexttrack")
    print("Next Song")

# Previous Song
def previous_song():
    pyautogui.press("prevtrack")
    print("Previous Song")

# Stop Media
def stop_media():
    pyautogui.press("stop")
    print("Media Stopped")

# Volume Up
def volume_up():
    pyautogui.press("volumeup")
    print("Volume Increased")

# Volume Down
def volume_down():
    pyautogui.press("volumedown")
    print("Volume Decreased")

# Mute
def mute():
    pyautogui.press("volumemute")
    print("Muted")

# Unmute
def unmute():
    pyautogui.press("volumemute")
    print("Unmuted")

# Brightness Up
def brightness_up():

    current = sbc.get_brightness()[0]

    if current < 100:
        sbc.set_brightness(current + 10)

    print("Brightness Increased")

# Brightness Down
def brightness_down():

    current = sbc.get_brightness()[0]

    if current > 10:
        sbc.set_brightness(current - 10)

    print("Brightness Decreased")

# Set Brightness
def set_brightness(level):

    sbc.set_brightness(level)

    print("Brightness Set")

# Current Brightness
def current_brightness():

    print("Brightness :", sbc.get_brightness()[0], "%")

# Open Spotify
def open_spotify():
    subprocess.Popen("spotify")

# Open VLC
def open_vlc():
    subprocess.Popen("vlc")

# Open Windows Media Player
def open_media_player():
    subprocess.Popen("wmplayer")

# Open YouTube Music
def open_youtube_music():
    subprocess.Popen(
        "start https://music.youtube.com",
        shell=True
    )

# Open Spotify Web
def open_spotify_web():
    subprocess.Popen(
        "start https://open.spotify.com",
        shell=True
    )

# Increase Volume 10 Times
def volume_max():

    for i in range(10):
        pyautogui.press("volumeup")

    print("Volume Increased")

# Decrease Volume 10 Times
def volume_min():

    for i in range(10):
        pyautogui.press("volumedown")

    print("Volume Decreased")