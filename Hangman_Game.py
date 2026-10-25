import random

words = ["apple", "tiger", "mango", "grapes", "python"]

word = random.choice(words)
blanks = ["_"] * len(word)

chances = 6

print("Welcome to Hangman!")
print("Guess the word:", " ".join(blanks))

while "_" in blanks and chances > 0:

    letter = input("Enter a letter: ").lower()

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                blanks[i] = letter

        print("Correct guess!")
    else:
        chances -= 1
        print("Wrong guess!")
        print("Chances left:", chances)

    print("Word:", " ".join(blanks))

if "_" not in blanks:
    print("You won!")
else:
    print("You lost!")
    print("The word was:", word)