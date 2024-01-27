import time, random
from pynput import keyboard
from pynput.mouse import Controller, Button

hotkey = "r"
press_key = Button.left
max_delay = 0.1
min_delay = 0.11

mouse = Controller()
click = 0

def on_release(key):
    global click
    if key.char == hotkey:
        click == ~click
        while True:
            mouse.press(press_key)
            mouse.release(press_key)
            time.sleep(round(random.uniform(max_delay, min_delay), 4))


with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
