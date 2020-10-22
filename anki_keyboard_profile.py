import os, sys
import time

import keyboard

from assets.objects.ProfileSelector import ProfileSelector as PS

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

def enter_english_input():
    keyboard.press_and_release("ctrl+shift+1")

def enter_korean_input():
    keyboard.press_and_release("ctrl+shift+2")

def enter_japanese_input():
    keyboard.press_and_release("ctrl+shift+3")

def main():
    profile = PS()
    keyboard.add_hotkey('ctrl+shift+p', lambda: parse_word())
    keyboard.add_hotkey('ctrl+shift+h', lambda: edit_last_word())
    keyboard.add_hotkey('ctrl+shift+enter', lambda: enter_card())


    if profile == "desktop":
        keyboard.add_hotkey('ctrl+shift+1', lambda: enter_english_input())
        keyboard.add_hotkey('ctrl+shift+2', lambda: enter_korean_input())
        keyboard.add_hotkey('ctrl+shift+3', lambda: enter_japanese_input())
    elif profile == "laptop":
        keyboard.add_hotkey('ctrl+shift+j', lambda: enter_english_input())
        keyboard.add_hotkey('ctrl+shift+k', lambda: enter_korean_input())
        keyboard.add_hotkey('ctrl+shift+l', lambda: enter_japanese_input())
 
    time.sleep(2)
    print("Profile in use: {}".format(profile))
    print("Press 'esc' to exit keyboard profile.")
    print("Automatically inimizing after 2 seconds")
    minimize_window()
    keyboard.wait("esc")

main()

