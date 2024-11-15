from random import randint
import art

# * Global Constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


print(art.logo)

# Step 4: Function to check user's guess against actual answer.
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of attempts remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:   # elif user_guess == answer:
        print(f"You got it! The answer was {actual_answer}.")


# Step 2: Function to set difficulty.
def set_difficulty():
    level = input("Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Invalid Input.")
        return None

def game():
    # Step 1: Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!\n"
            "I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")



    # Step 3: Let the user guess a number.
    attempts = set_difficulty()

    # Step 4.5: Check if attempts were set; exit if invalid input was provided.
    if attempts is None:
        return      # Exit the game

    # Step 5: Repeat guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Guess a number: "))
        # Step 6: Track the number of turns and reduce by 1 if they get it wrong.
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print("You ran out of guesses. You lose...")
            return
        elif guess != answer:
            print("Guess again.")

game()

