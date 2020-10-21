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
        rest(1.2)

def parse_word():
    rest(5)
    sequence = ["ctrl+c", "tab", "ctrl+v", "shift+tab", "shift+tab",
                "shift+tab", "ctrl+v", "tab"]
    strike_sequence(sequence)

def edit_last_word():
    rest(5)
    sequence = ["ctrl+h", "enter", "enter"]
    strike_sequence(sequence)

def enter_card():
    rest(3.5)
    sequence = ["tab", "ctrl+a", "ctrl+c", "ctrl+enter", "rest",
                "tab", "tab", "ctrl+v"]
    strike_sequence(sequence)

def minimize_window():
    keyboard.press_and_release("windows+down")

def main():
    keyboard.add_hotkey('ctrl+shift+p', lambda: parse_word())
    keyboard.add_hotkey('ctrl+shift+h', lambda: edit_last_word())
    keyboard.add_hotkey('ctrl+shift+enter', lambda: enter_card())

    print("Press esc to exit keyboard profile")
    minimize_window()
    keyboard.wait("esc")

main()

