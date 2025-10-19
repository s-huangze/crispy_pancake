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

def choose_difficulty():
    """Ask the user to choose a difficulty level."""
    print("Choose difficulty: Easy (E), Medium (M), or Hard (H)")
    choice = input("Your choice: ").strip().lower()

    if choice in ("e", "easy"):
        return 1, 10
    elif choice in ("m", "medium"):
        return 1, 50
    elif choice in ("h", "hard"):
        return 1, 100
    else:
        print("Invalid choice — defaulting to Medium.")
        return 1, 50

def main():
    """Main game loop with difficulty selection and summaries."""
    total_games = 0
    total_tries = 0
    while True:
        low, high = choose_difficulty()
        tries = play_once(low, high)
        total_games += 1
        total_tries += tries
        print(f"Game summary: You took {tries} tries this round. Total games played: {total_games}.")
        avg = total_tries / total_games
        print(f"Average tries per game: {avg:.1f}")

        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print(f"Thanks for playing! Final average: {avg:.1f} tries over {total_games} game(s).")
            break

if __name__ == "__main__":
    main()
