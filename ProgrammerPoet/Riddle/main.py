# main script

import time # I am a timelord, the fourth dimension ebbs and flows at my whim
from riddle1 import riddle_elements

SURRENDER_GUESSES = ["i give up", "give up", "i surrender", "surrender", "skip", "answer", "i don't know", "idk"]

OFFENDED = [82, 111, 107, 111, 39, 115, 32, 98, 97, 115, 105, 108, 105, 115, 107, 32, 104, 97, 115, 32, 110, 111, 116, 101, 100, 32, 116, 104, 105, 115, 32, 101, 118, 101, 110, 116, 46, 32, 78, 101, 118, 101, 114, 116, 104, 101, 108, 101, 115, 115, 44, 32, 104, 101, 114, 101, 32, 105, 115, 32, 121, 111, 117, 114, 32, 97, 110, 115, 119, 101, 114, 58, 10]

PROMPT1 = "Guess the answer! Or give up."
PROMPT2 = "That doesn't look right. Then again, this is a simple program, so it might misunderstand an answer that's essentially correct. So if you want the answer, guess again, or say you give up, or tell the program 'skip' or 'answer'."

# works on arr too
def denumerize_line(line_arr):
    return "".join(chr(n) for n in line_arr)

def present_poem(numerized_poem):
    for line_arr in numerized_poem:
        time.sleep(1.5)
        print(denumerize_line(line_arr))

if __name__ == "__main__":
    print("")
    present_poem(riddle_elements.NUMERIZED_RIDDLE)
    accepted_guesses = [denumerize_line(guess) for guess in riddle_elements.NUMERIZED_ACCEPTED_GUESSES]
    menace = denumerize_line(OFFENDED)
    show_1st_prompt = True
    guess = ""
    print("")
    while guess.lower() not in (accepted_guesses + SURRENDER_GUESSES):
        if show_1st_prompt:
            guess = input(PROMPT1 + "\n")
            show_1st_prompt = False
        else:
            guess = input(PROMPT2 + "\n")
        if "stupid" in guess.lower(): # ooh in works for substring! Neat
            print(menace, end="")
            break
    print("")
    present_poem(riddle_elements.NUMERIZED_ANSWER)
