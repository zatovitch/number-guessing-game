import random

def get_user_guess():
    """Function to get the user's guess."""
    return int(input("Enter your guess: "))

def guessing_game(get_guess_function):
    """Main function to run the number guessing game."""
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = get_guess_function()
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

# Start the game
if __name__ == "__main__":
    guessing_game(get_user_guess)