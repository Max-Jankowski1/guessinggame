import random

def play_game():
    number_to_guess = random.randint(1, 50)
    guessed = False

    while not guessed:
        user_guess = input("Guess a number between 1 and 50 (or 'q' to quit): ")

        if user_guess.lower() == 'q':
            print("Thanks for playing! Goodbye.")
            return

        try:
            guess = int(user_guess)
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
            continue

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            guessed = True

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == 'y':
        play_game()
    else:
        print("Thanks for playing! Goodbye.")

play_game()