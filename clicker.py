import time, random, threading
from pynput.mouse import Controller, Button
from pynput.keyboard import KeyCode, Listener

hotkey = KeyCode(char='r')
press_key = Button.left
max_delay = 0.1
min_delay = 0.11

class Clicker(threading.Thread): 
    def __init__(self, max_delay, min_delay, press_key): 
        super(Clicker, self).__init__() 
        self.max_delay = max_delay
        self.min_delay = min_delay 
        self.press_key = press_key 
        self.running = False

    def start_click(self): 
        self.running = True

    def stop_click(self): 
        self.running = False

    def run(self):
        while True:
            while self.running: 
                mouse.click(self.press_key)
                time.sleep(round(random.uniform(self.max_delay, self.min_delay), 4))

def on_press(key):
    if key == hotkey:
        if clicker.running:
            clicker.stop_click()
        else:
            clicker.start_click()

mouse = Controller()
clicker = Clicker(max_delay, min_delay, press_key)
clicker.start()

with Listener(on_press=on_press) as listener:
    listener.join()
