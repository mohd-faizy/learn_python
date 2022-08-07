# Code_1

import random

def draw_man(progress):
    if progress == 0:
        print("No hanged parts yet! :)")
        return

    for i in range(0, progress):
        if i == 0:
            print("+------+")
            print("       |")
            print("       |")
            print("       |")
            print("      === ")

        elif i == 1 and progress == 2:
            print("   +------+")
            print("   O      |")
            print("   |      |")
            print("          |")
            print("         ===")

        elif i == 2 and progress == 3:
            print("   +------+")
            print("   O      |")
            print("   |      |")
            print("  / \     |")
            print("         ===")

        elif i == 3 and progress == 4:
            print("   +------+")
            print(" \ O /    |")
            print("   |      |")
            print("  / \     |")
            print("         ===")

        elif i == 4 and progress == 5:
            print("Last breaths counting, Take care!")
            print("   +------+")
            print(" \ O_|/   |")
            print("   |      |")
            print("  / \     |")
            print("         ===")

        elif i == 5 and progress == 6:
            print("You loose")
            print("You let a kind man die")
            print("   +------+")
            print("   O _|   |")
            print("  /|\     |")
            print("  / \     |")
            print("         ===")

    return


category = random.choice(["Color", "Language", "Animal"])
print("Category: " + category)

if category == "Color":
    word = random.choice(["crimson", "tangerine", "lemon", "grass",
                          "teal", "cerulean", "indigo", "lavender", "magenta"])
elif category == "Language":
    word = random.choice(["Python", "Spanish", "Java",
                          "English", "HTML", "Chinese", "Swift", "Indonesian"])
else:  # category == "Animal"
    word = random.choice(["tiger", "beaver", "falcon",
                          "bass", "kangaroo", "thylacine"])

# player's guessing progress on the word
word_progress = ["-"] * len(word)

# keep track of which letters have already been guessed
guessed = []

# user can have 6 wrong guesses
incorrect = 0

while incorrect < 6 and "-" in word_progress:
    # display game progress
    print()
    draw_man(incorrect)
    print(" ".join(word_progress))
    print("Guessed letters: ")
    print(" ".join(guessed))
    print()

    # ask user for alphabetical guess, which will be forced lowercase
    guess = "0"
    if not guess.isalpha():
        guess = input("Guess a letter or the word: ").lower()

    if guess == word.lower():
        # oh snap you won let's go start the victory sequence
        break
    elif len(guess) > 1:  # if you guess a dupe word, shame on you
        print("Sorry, that's not the word.")
        incorrect += 1
    elif guess in guessed:
        print("You already guessed that letter.")
    elif guess not in word.lower():
        print(guess + " is not in the word.")
        incorrect += 1
        guessed.append(guess)
    else:  # guess (letter) is in word
        print(guess + " is in the word!")
        guessed.append(guess)
        for i in range(len(word)):
            if word_progress[i] == "-" and word[i].lower() == guess:
                word_progress[i] = word[i]  # to make original caps show up

print()
if incorrect == 6:
    print("You lost!")
    print("The word was: " + word)
else:  # we're out of the loop because we found or guessed the word
    if "-" in word_progress:
        print("You guessed the word! You win!")
        for i in range(len(word)):
            word_progress[i] = word[i]
    else:  # "-" not in word progress
        print("You found the word! You win!")
        
# either way, show their final progress
draw_man(incorrect)
print(" ".join(word))
print("Guessed letters: ")
print(" ".join(guessed))
print()
print("Thanks for playing!")
