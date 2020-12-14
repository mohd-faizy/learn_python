# Code_2

# Algorithm
'''
1. Develop the interface
2. Predefined list
3. instruction
4. Check the words
    - if right then enter in the empty list & ask for next guess
    - if not in the list then print interface  
5. Reduce the turn's on each iteration for every worng guess
6. Genrate the interface
'''
import random


def hangman():

    word_list = random.choice(
        ["cat", "dog", "lion", "tiger", "apple", "banana", "rat", "sheep", "firefox", "tree"])
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ' '  # Empty string in the begining

    while len(word_list) > 0:

        random_word = ""

        for letter in word_list:
            if letter in guessmade:
                random_word = random_word + letter
            else:
                random_word = random_word + "_" + "  "

        if random_word == word_list:
            print(random_word)
            print("You win!")
            break

        print("Guess the word:          ", random_word)
        guess = input()

        if guess in valid_letters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word_list:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("   +------+   ")
                print("          |   ")
                print("          |   ")
                print("          |   ")
                print("         ===  ")
            if turns == 8:
                print("8 turns left")
                print("   +------+   ")
                print("   O      |   ")
                print("          |   ")
                print("          |   ")
                print("          |   ")
                print("         ===  ")
            if turns == 7:
                print("7 turns left")
                print("   +------+   ")
                print("   O      |   ")
                print("   |      |   ")
                print("          |   ")
                print("         ===  ")
            if turns == 6:
                print("6 turns left")
                print("   +------+   ")
                print("   O      |   ")
                print("   |      |   ")
                print("  /       |   ")
                print("         ===  ")
            if turns == 5:
                print("5 turns left")
                print("   +------+   ")
                print("   O      |   ")
                print("   |      |   ")
                print("  / \     |   ")
                print("         ===  ")
            if turns == 4:
                print("4 turns left")
                print("   +------+   ")
                print(" \ O      |   ")
                print("   |      |   ")
                print("  / \     |   ")
                print("         ===  ")
            if turns == 3:
                print("3 turns left")
                print("   +------+   ")
                print(" \ O /    |   ")
                print("   |      |   ")
                print("  / \     |   ")
                print("         ===  ")
            if turns == 2:
                print("2 turns left")
                print("   +------+   ")
                print(" \ O /|   |   ")
                print("   |      |   ")
                print("  / \     |   ")
                print("         ===  ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("   +------+   ")
                print(" \ O_|/   |   ")
                print("   |      |   ")
                print("  / \     |   ")
                print("         ===  ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("   +------+   ")
                print("   O _|   |   ")
                print("  /|\     |   ")
                print("  / \     |   ")
                print("         ===  ")
                break


name = input("Enter your name: ")
print("Welcome", name)
print("----------------------")
print("try to guess the word in less than 10 attempts")
hangman()
print()
