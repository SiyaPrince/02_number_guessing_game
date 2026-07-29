import random

# Function to welcome player

def display_welcome():

    print("=" * 45)
    print()
    print("Welcome to the Number Guessing Game!")
    print()
    print("=" * 45)
    print()

# Generate a random number

MIN_NUMBER = 1
MAX_NUMBER = 100

def generate_random_number():
    return random.randint(MIN_NUMBER, MAX_NUMBER)

# Ask for guesses

def get_player_guess():
    while True:
        try:
            print("I am thinking of a number ...")
            print()
            guess = int(input(f"Enter your guess (between {MIN_NUMBER} and {MAX_NUMBER}): "))
            print()
            if validate_guess(guess):
                return guess
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Validate the guess

def validate_guess(guess):
    if MIN_NUMBER <= guess <= MAX_NUMBER:
        return True
    
    print(f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")
    print()
    return False
# Give hints to the player based on their guess

def give_hint(guess, generated_number): # 80, 100
    if guess > generated_number:
        guess_lower_hint(guess, generated_number)
    else:
        guess_higher_hint(guess, generated_number)

# Give hints to the player

def guess_lower_hint(guess, generated_number):

    difference = guess - generated_number

    if abs(difference) <= 10:
        print("You are very close! Guess slightly lower.")
        print()
    elif abs(difference) <= 20:
        print("You are getting closer. Try a lower number!")
        print()
    else:
        print("Your guess is too high! Try a lower number.")
        print()

def guess_higher_hint(guess, generated_number):

    difference = guess - generated_number

    if abs(difference) <= 10:
        print("You are very close! Guess slightly higher.")
        print()
    elif abs(difference) <= 20:
        print("You are geting closer. Try a higher number!")
        print()
    else:
        print("Your guess is too low! Try a higher number.")
        print()

# Provide feedback to the player

def provide_feedback(guess, generated_number):
    if guess == generated_number:
        print("Congratulations! You've guessed the correct number!")
        print()

# Ask the player if they want to play again

def play_again():
    while True:
        response = input("Do you want to play again? (yes/no): ").strip().lower()
        print()

        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes'(y) or 'no'(n).")
            print()

# Function that records the history of the guesses

def record_guess_history(guess, guess_history):
    guess_history.append(guess)

# Function to add limit to the number of attempts

def limit_attempts(attempts, max_attempts, generated_number):
    if attempts >= max_attempts:
        print("Out of attempts! The game is over.")
        print()
        print(f"The number was: {generated_number}")
        print()
        return True
    return False


# Function to play game

def play_game(guess, generated_number):

    attempts = 0
    attempt_limit = 10
    guess_history = []

    while (guess != generated_number) and (attempts != attempt_limit):

        # Give hint
        give_hint(guess, generated_number)

        # Ask player's guess
        guess = get_player_guess()

        record_guess_history(guess=guess, guess_history=guess_history)

        attempts += 1
        limit_attempts(attempts, attempt_limit, generated_number=generated_number)

    print(guess_history)

    print()

    provide_feedback(guess = guess, generated_number=generated_number)
    
#### Main game loop

# Main game function

# Display Welcome
display_welcome()

# Generate number
generated_number = generate_random_number()

# Ask player's guess
guess = get_player_guess()

# Play 1 complete game
play_game(guess, generated_number)

# Ask to repeat

play_again()
