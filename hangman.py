import random

# List of predefined words
words = ["python", "laptop", "coding", "internship", "developer", "hangman", "programming", "challenge", "algorithm", "function"]

# Randomly choose a word
chosen_word = random.choice(words)

# Create empty spaces
guessed_word = ["_"] * len(chosen_word)

# Store guessed letters
guessed_letters = []

# Number of attempts
attempts = 6

print(" Welcome to Hangman Game!")

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Attempts Left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check guessed letter
    if guess in chosen_word:
        print(" Correct Guess!")

        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                guessed_word[index] = guess

    else:
        print(" Wrong Guess!")
        attempts -= 1

# Final Result
if "_" not in guessed_word:
    print("\n Congratulations! You guessed the word:")
    print(chosen_word)
else:
    print("\n Game Over!")
    print("The correct word was:", chosen_word)