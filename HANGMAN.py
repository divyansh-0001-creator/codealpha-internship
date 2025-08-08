import random

# List of predefined words
words = ["apple", "blueberry", "mango", "guava", "peach"]

# Select a random word
word_to_guess = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Create a hidden version of the word (e.g., "_ _ _ _ _")
hidden_word = ["_"] * len(word_to_guess)

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have", max_guesses, "incorrect guesses allowed.")

while incorrect_guesses < max_guesses and "_" in hidden_word:
    print("\nCurrent word:", " ".join(hidden_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                hidden_word[i] = guess
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Wrong guess! You have", max_guesses - incorrect_guesses, "guesses left.")

# Game over messages
if "_" not in hidden_word:
    print("\nCongratulations! You guessed the word:", word_to_guess)
else:
    print("\nGame Over! The word was:", word_to_guess)

