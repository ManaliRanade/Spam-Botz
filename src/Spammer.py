from pynput.keyboard import *

keyboard = Controller()
def spammer(message):
    for unit in message:
        keyboard.press(unit)
        keyboard.release(unit)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)