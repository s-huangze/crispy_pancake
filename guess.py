import random

LOW, HIGH = 1, 100
MAX_TRIES = 7               # Attempt limit (from change #4)
ENABLE_COLOR = True         # Toggle colors on/off

def c(text: str, code: str) -> str:
    """Return ANSI-colored text if enabled; otherwise plain text."""
    if not ENABLE_COLOR:
        return text
    return f"\033[{code}m{text}\033[0m"

def read_int(prompt: str) -> int:
    """Ask until user enters a valid number."""
    while True:
        raw = input(prompt).strip()
        if raw.lstrip("-+").isdigit():
            return int(raw)
        print(c("Please enter a valid number.", "91"))  # red

def play_once(low: int = LOW, high: int = HIGH) -> int:
    """Play one round of the guessing game."""
    secret = random.randint(low, high)
    print(c(f"I'm thinking of a number between {low} and {high}. You have {MAX_TRIES} attempts.", "96"))  # cyan
    tries = 0

    while tries < MAX_TRIES:
        guess = read_int("Your guess: ")
        tries += 1

        if guess < low or guess > high:
            print(c(f"Out of range! Guess between {low} and {high}.", "95"))  # magenta
            continue

        # Closeness feedback
        diff = abs(guess - secret)
        if diff <= 3:
            print(c("🔥 Very close!", "92"))      # green
        elif diff <= 10:
            print(c("🙂 Close!", "94"))           # blue
        else:
            print(c("❄️ Way off!", "90"))         # gray

        # High/low hints
        if guess < secret:
            print(c("Too low!", "93"))            # yellow
        elif guess > secret:
            print(c("Too high!", "93"))           # yellow
        else:
            print(c(f"Correct! You got it in {tries} tries.", "92"))  # green
            return tries

    print(c(f"Out of attempts! The correct number was {secret}.", "91"))  # red
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
        print(c(f"Game summary: You took {tries} tries this round. Total games played: {total_games}.", "96"))  # cyan
        avg = total_tries / total_games
        print(c(f"Average tries per game: {avg:.1f}", "96"))  # cyan

        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print(c(f"Thanks for playing! Final average: {avg:.1f} tries over {total_games} game(s).", "96"))
            break

if __name__ == "__main__":
    main()
