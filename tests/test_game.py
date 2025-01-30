# Description: Number Guessing Game Logic
import random

def guessing_game(get_guess):
    print("🎲 Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 100)  # Generates a number between 1 and 100
    attempts = 0  

    while True:
        try:
            guess = get_guess()
            attempts += 1  

            if guess < secret_number:
                if secret_number - guess <= 10:
                    print("🔼 Too low! But you're close.")
                else:
                    print("🔼 Too low! Try again.")
            elif guess > secret_number:
                if guess - secret_number <= 10:
                    print("🔽 Too high! But you're close.")
                else:
                    print("🔽 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break  # Exit the loop once the number is found

        except ValueError:
            print("⚠️ Error: Please enter a valid number!")

def get_user_guess():
    return int(input("Guess the number (between 1 and 100): "))

# Start the game
guessing_game(get_user_guess)
