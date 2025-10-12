import random

LOW, HIGH = 1, 100

def read_int(prompt: str) -> int:
    """Ask until user enters a valid number."""
    while True:
        raw = input(prompt).strip()
        if raw.lstrip("-+").isdigit():
            return int(raw)
        print("Please enter a valid number.")

def play_once(low: int = LOW, high: int = HIGH) -> int:
    """Play one round of the guessing game."""
    secret = random.randint(low, high)
    print(f"I'm thinking of a number between {low} and {high}.")
    tries = 0

    while True:
        guess = read_int("Your guess: ")
        tries += 1
        if guess < low or guess > high:
            print(f"Out of range! Guess between {low} and {high}.")
            continue
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {tries} tries.")
            return tries

def main():
    """Main game loop."""
    while True:
        play_once(LOW, HIGH)
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()