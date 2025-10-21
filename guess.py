import random

# Example constants (replace with your actual values)
LOW, HIGH = 1, 100
MAX_TRIES = 7

# Helper function for colored printing
def color_print(msg: str, color: str):
    """Prints a message in color if the 'c()' function exists."""
    try:
        print(c(msg, color))
    except NameError:
        print(msg)

# Example read_int function
def read_int(prompt: str):
    """Prompts user for input and returns an integer, or None if 'q' is entered."""
    user_input = input(prompt)
    if user_input.lower() == "q":
        return None
    try:
        return int(user_input)
    except ValueError:
        print("Invalid input! Enter a number or 'q' to quit.")
        return read_int(prompt)

def play_once(low: int = LOW, high: int = HIGH) -> int:
    """Play one round of the guessing game. Returns number of tries this round."""
    secret = random.randint(low, high)

    # Game intro
    color_print(f"I'm thinking of a number between {low} and {high}. You have {MAX_TRIES} attempts. (Type 'q' to give up)", "96")

    tries = 0
    while tries < MAX_TRIES:
        result = read_int("Your guess: ")  # may be int or None if user typed 'q'

        if result is None:
            color_print(f"You gave up! The correct number was {secret}.", "95")
            return tries

        guess = result
        tries += 1

        if guess < low or guess > high:
            color_print(f"Out of range! Guess between {low} and {high}.", "95")
            continue

        # Feedback on guess
        diff = abs(guess - secret)
        if diff <= 3:
            color_print("🔥 Very close!", "92")
        elif diff <= 10:
            color_print("🙂 Close!", "94")
        else:
            color_print("❄️ Way off!", "90")

        # High/low hints
        if guess < secret:
            color_print("Too low!", "93")
        elif guess > secret:
            color_print("Too high!", "93")
        else:
            color_print(f"Correct! You got it in {tries} tries.", "92")
            return tries

    color_print(f"Out of attempts! The correct number was {secret}.", "91")
    return tries
