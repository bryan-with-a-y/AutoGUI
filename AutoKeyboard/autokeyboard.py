import io, time

import keyboard

def rest(mult=1):
    time.sleep(0.1*mult)

def tab(num_tabs):
    for i in range(num_tabs):
        keyboard.press_and_release("tab")
        rest()

def shift_tab(num_tabs):
    for i in range(num_tabs):
        keyboard.press_and_release("shift+tab")
        rest()

def enter(lst):
    tab(5)
    keyboard.write(lst[1])
    rest()

    tab(1)
    keyboard.press_and_release("ctrl+a")
    rest()

    keyboard.write(lst[2])
    rest()

    tab(1)
    keyboard.write(lst[3])
    rest()

    shift_tab(7)
    keyboard.press_and_release("down arrow")
    rest()

def main():
    keyboard.press_and_release("alt+tab")
    rest(mult=10)

    with io.open("real_cloze_deck.txt", "r", encoding="utf-8") as deck_file:
        start_line = 4
        for i in range(start_line-1):
            deck_file.readline()

        for deck_string in deck_file.readlines():
            cloze_sentence = deck_string.split("\t\t")[1]
            
            korean_word = deck_string.split("\t\t")[0]
            highlight_text = cloze_sentence.split("::")[2].split("}}")[0]
            english_word = cloze_sentence.split("::")[1]
            dictionary_form = cloze_sentence.split("\t")[0]
            start = cloze_sentence.index("{")
            end = cloze_sentence.index("}")+2
            korean_sentence = (cloze_sentence[0:start] + 
                    korean_word + 
                    cloze_sentence[end:-1]).strip()
            
            enter([korean_word, english_word,
                   korean_sentence, highlight_text])
            #break

main()



