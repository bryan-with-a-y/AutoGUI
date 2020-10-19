import time

import keyboard

def rest(mult=1):
    time.sleep(.1*mult)

def strike_sequence(lst):
    for key_stroke in lst:
        if key_stroke == "rest":
            rest(3)
            continue
        keyboard.press_and_release(key_stroke)
        rest()

def parse_word():
    rest(5)
    keyboard.press_and_release("ctrl+c")
    rest()
    keyboard.press_and_release("tab")
    rest()
    keyboard.press_and_release("ctrl+v")
    rest()
    keyboard.press_and_release("shift+tab")
    rest()
    keyboard.press_and_release("shift+tab")
    rest()
    keyboard.press_and_release("shift+tab")
    rest()
    keyboard.press_and_release("ctrl+v")
    rest()
    keyboard.press_and_release("tab")

def edit_last_word():
    rest(5)
    keyboard.press_and_release("ctrl+h")
    rest()
    keyboard.press_and_release("enter")
    rest()
    keyboard.press_and_release("enter")

def enter_card():
    rest(3.5)
    sequence = ["tab", "ctrl+a", "ctrl+c", "ctrl+enter", "rest",
                "tab", "tab", "ctrl+v"]
    strike_sequence(sequence)
    #keyboard.press_and_release("tab")
    #keyboard.press_and_release("ctrl+a")
    #keyboard.press_and_release("ctrl+c")
    #keyboard.press_and_release("ctrl+enter")
    #keyboard.press_and_release("tab")
    #keyboard.press_and_release("tab")
    #keyboard.press_and_release("ctrl+v")

keyboard.add_hotkey('ctrl+shift+p', lambda: parse_word())
keyboard.add_hotkey('ctrl+shift+h', lambda: edit_last_word())
keyboard.add_hotkey('ctrl+shift+enter', lambda: enter_card())

keyboard.wait("esc")

