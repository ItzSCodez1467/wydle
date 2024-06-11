import random
from typing import List
from wonderwords import RandomWord
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

class wordSelector:
    def __init__(self):
        self.Slctr = RandomWord()

    def getRandomWord(self) -> str:
        return self.Slctr.word(word_max_length=5, word_min_length=5)

class wordVerifier(wordSelector):
    def __init__(self):
        super().__init__()
        TIMES = [0, 0, 0, 0, 0]
        WORDS = []

        for _ in TIMES:
            WORDS.append(self.getRandomWord())

        if len(WORDS) != 5:
            raise IndexError("`len` OF `words` MUST BE 5 !", len(WORDS))

        self.word = random.choice(WORDS)

    def glist(self, other: str) -> List[str]:
        slfLtr: List[str] = list(self.word)
        othLtr: List[str] = list(other)
        retVal: List[str] = [''] * 5

        # First pass to check for correct letters in the correct position (green)
        for i, ltr in enumerate(slfLtr):
            if othLtr[i] == ltr:
                retVal[i] = "green"
                othLtr[i] = None  # Mark as checked

        # Second pass to check for correct letters in the wrong position (yellow)
        for i, ltr in enumerate(slfLtr):
            if retVal[i] != "green":
                if othLtr[i] in slfLtr:
                    retVal[i] = "yellow"
                    slfLtr[slfLtr.index(othLtr[i])] = None  # Mark as used
                else:
                    retVal[i] = "grey"

        return retVal

def print_colored_output(word: str, colors: List[str]):
    color_map = {
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "grey": Fore.BLACK + Back.WHITE
    }

    for letter, color in zip(word, colors):
        print(color_map[color] + letter, end=" ")
    print(Style.RESET_ALL)

print("W.Y.D.L.E")
print("---------\n\n")
print("The word has been chosen".center(50))
print("\n\n\n")

tries = 32
ertyu
winner = False
wrdVerify = wordVerifier()

while tries:
    tries -= 1

    print("Please select the word")
    uWord = input("> ")
    if len(uWord) < 5 or len(uWord) > 5:
        print("\n\nThe word must be 5 letters long.")
        ws = wordSelector()
        uWord = ws.getRandomWord()
        print(f"Automatically selected {uWord}\n\n")

    ret = wrdVerify.glist(uWord)
    print_colored_output(uWord, ret)

    if ret == ["green", "green", "green", "green", "green"]:
        winner = True
        break

if winner:
    print("Congratulations! You've guessed the word correctly!")
else:
    print(f"Sorry, you've run out of tries. The correct word was: {wrdVerify.word}")
