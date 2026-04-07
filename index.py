import random

# Predefined word list
words = ["apple", "tiger", "chair", "robot", "plant"]

# Choose a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Create blank display
display = ["_"] * len(word)

print("Welcome to Hangman Game!")

# Game loop
while wrong_guesses < max_wrong and "_" in display:
    print("\nWord:", " ".join(display))
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong guess! Attempts left:", max_wrong - wrong_guesses)

# Result
if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)