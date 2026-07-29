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

    difference = abs(guess - generated_number)

    if difference <= 10:
        print("You are very close! Guess slightly lower.")
        print()
    elif difference <= 20:
        print("You are getting closer. Try a lower number!")
        print()
    else:
        print("Your guess is too high! Try a lower number.")
        print()

def guess_higher_hint(guess, generated_number):

    difference = abs(guess - generated_number)

    if difference <= 10:
        print("You are very close! Guess slightly higher.")
        print()
    elif difference <= 20:
        print("You are getting closer. Try a higher number!")
        print()
    else:
        print("Your guess is too low! Try a higher number.")
        print()

# Provide feedback to the player

def display_win_message(guess, generated_number):
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

def play_game():

    print("I am thinking of a number ...")
    print()

     # Generate number
    generated_number = generate_random_number()

    attempts = 0
    attempt_limit = 10
    guess_history = []

    while attempts < attempt_limit:

        # Get initial guess
        guess = get_player_guess()

        print("=" * 45)

        attempts += 1

        record_guess_history(guess=guess, guess_history=guess_history)

        if guess == generated_number:

            display_win_message(guess = guess, generated_number=generated_number)
            print(f"You guessed the number in  {attempts} attempts")
            break
        elif attempts >= attempt_limit:

            limit_attempts(attempts, attempt_limit, generated_number=generated_number)
            break
        else:
            give_hint(guess, generated_number)

    print("Guess History: ", guess_history)

    print()

    
#### Main game loop

# Main game function

# Display Welcome
display_welcome()

play_again_response = True

while play_again_response:

    # Play 1 complete game
    play_game()

    # Ask to repeat

    play_again_response = play_again()

    print("=" * 45)
