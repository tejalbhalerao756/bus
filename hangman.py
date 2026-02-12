import random

# Predefined list of 5 words
words = ["python", "apple", "tiger", "chair", "robot"]

# Randomly choose one word
secret_word = random.choice(words)

# Create empty display word ( _ _ _ _ )
guessed_letters = []
display_word = ["_"] * len(secret_word)

# Maximum incorrect guesses
max_attempts = 6
incorrect_guesses = 0

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

# Game loop
while incorrect_guesses < max_attempts and "_" in display_word:
    
    print("Word:", " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print("Correct guess! ✅\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print("Wrong guess! ❌")
        print("Remaining attempts:", max_attempts - incorrect_guesses, "\n")

# Final Result
if "_" not in display_word:
    print("🎉 Congratulations! You won!")
    print("The word was:", secret_word)
else:
    print("💀 Game Over!")
    print("The correct word was:", secret_word)