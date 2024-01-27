import time, random
from pynput import keyboard
from pynput.mouse import Controller, Button

click = 0
hotkey = "r"
press_key = Button.left
up_delay = 0.1
down_delay = 0.11

mouse = Controller()

def on_release(key):
    global click
    if key.char == hotkey:
        click == ~click
        while True:
            mouse.press(press_key)
            mouse.release(press_key)
            time.sleep(round(random.uniform(up_delay, down_delay), 4))


with keyboard.Listener(on_release=on_release) as listener:
    listener.join()