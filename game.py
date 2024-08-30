import random
import sys

words = [
    "air",
    "boo",
    "cat",
    "cow",
    "dad",
    "dog",
    "elf",
    "fox",
    "hey",
    "mom",
    "oil",
    "pig",
    "rye",
    "act",
"ask",
"arm",
"age",
"ago",
"air",
"ate",
"all",
"but",
"bye",
"bad",
"big",
"bed",
"bat",
"boy",
"bus",
"bag",
"box",
"bit",
"bee",
"buy",
"bun",
"cub",
"cat",
"car",
"cut",
"cow",
"cry",
"cab",
"can",
"dad",
"dab",
"dam",
"did",
"dug",
"den",
"dot",
"dip",
"day",
"ear",
"eye",
"eat",
"end",
"elf",
"egg",
"far",
"fat",
"few",
"fan",
"fun",
"fit",
"fin",
"fox",
"got",
"get",
"god",
"gel",
"gas",
"hat",
"hit",
"has",
"had",
"how",
"her",
"his",
"hen",
"ink",
"ice",
"ill",
"jab",
"jug",
"jet",
"jam",
"jar",
"job",
"jog",
"kit",
"key",
"lot",
"lit",
"let",
"lay",
"mat",
"man",
"mad",
"mug",
"mix",
"map",
"mum",
"mud",
"mom",
"may",
"met",
"net",
"new",
"nap",
"now",
"nod",
"net",
"not",
"nut",
"oar",
"one",
"out",
"owl",
"old",
"pat",
"peg",
"paw",
"pup",
"pit",
"put",
"pot",
"pop",
"pin",
"rat",
"rag",
"rub",
"row",
"rug",
"run",
"rap",
"ram",
"sow",
"see",
"saw",
"set",
"sit",
"sir",
"sat",
"sob",
"tap",
"tip",
"top",
"tug",
"tow",
"toe",
"tan",
"ten",
"two",
"use",
"van",
"vet",
"was",
"wet",
"win",
"won",
"wig",
"war",
"why",
"who",
"way",
"wow",
"you",
"yes",
"yak",
"yet",
"zip",
"zap"
]


def main():
    # guesses remaining (start with 6)
    guesses = 6
    # letters that have been revealed (all empty at first)
    revealed = ["_", "_", "_"]
    # keep track of letters already guessed
    guessed = set()

    # pick a word at random
    word = random.choice(words)
   # word = words[0]  # temporarily just use the first word 

    # play the game until they win or run out of guesses
    while guesses > 0:
        print("\n-----------------------------")
        print("Word:", " ".join(revealed))
        print("Guessed:", ", ".join(sorted(guessed)))
        print("Guesses Remaining:", guesses)
        print()

        # each round, ask for a letter, then check if it is in the word
        letter = input("Pick a letter: ")

        if letter in guessed:
            # if the letter is already guessed, we tell them that
            # (and let them guess again with no penalty)
            print(f"\nAlready guessed {letter}!")
        else:
            # update guesses and which letters have been seen
            guessed.add(letter)
            guesses -= 1

            # check word one letter at a time
            for index, word_letter in enumerate(word):
                if letter == word_letter:
                    revealed[index] = letter

            # if revealed is only letters, the player has won!
            if "_" not in revealed:
                print(f"{word}! You Win!")
                exit()
    print(f"\nSorry! The word was {word}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        random.seed(sys.argv[1])
    main()
