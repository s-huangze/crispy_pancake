import random

LOW, HIGH = 1, 100
MAX_TRIES = 7               # Attempt limit
ENABLE_COLOR = True         # Toggle colors on/off

def c(text: str, code: str) -> str:
    """Return ANSI-colored text if enabled; otherwise plain text."""
    if not ENABLE_COLOR:
        return text
    return f"\033[{code}m{text}\033[0m"

def read_int(prompt: str):
    """Ask until user enters a valid number, or return None if user quits."""
    while True:
        raw = input(prompt).strip()
        if raw.lower() in ("q", "quit"):
            return None
        if raw.lstrip("-+").isdigit():
            return int(raw)
        print(c("Please enter a valid number (or 'q' to quit this round).", "91"))  # red

def play_once(low: int = LOW, high: int = HIGH) -> int:
    """Play one round of the guessing game. Returns number of tries this round."""
    secret = random.randint(low, high)
    print(c(f"I'm thinking of a number between {low} and {high}. You have {MAX_TRIES} attempts. (Type 'q' to give up)", "96"))  # cyan
    tries = 0

    while tries < MAX_TRIES:
        result = read_int("Your guess: ")
        if result is None:
            print(c(f"You gave up! The correct number was {secret}.", "95"))  # magenta
            return tries  # count tries so far (doesn't add an extra)
        guess = result
        tries += 1

        if guess < low or guess > high:
            print(c(f"Out of range! Guess between {low} and {high}.", "95"))  # magenta
            continue

        # Closeness feedback
        diff = abs(guess - secret)
        if diff <= 3:
            print(c("🔥 Very close!", "92"))
        elif diff <= 10:
            print(c("🙂 Close!", "94"))
        else:
            print(c("❄️ Way off!", "90"))

        # High/low hints
        if guess < secret:
            print(c("Too low!", "93"))
        elif guess > secret:
            print(c("Too high!", "93"))
        else:
            print(c(f"Correct! You got it in {tries} tries.", "92"))
            return tries

    print(c(f"Out of attempts! The correct number was {secret}.", "91"))
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
    """Main game loop with difficulty selection, summaries, high score, and quit support."""
    total_games = 0
    total_tries = 0
    best_score = None
    while True:
        low, high = choose_difficulty()
        tries = play_once(low, high)
        total_games += 1
        total_tries += tries
        avg = total_tries / total_games if total_games else 0.0

        if best_score is None or (tries > 0 and tries < best_score):
            best_score = tries
            if tries > 0:
                print(c(f"🎉 New best score: {best_score} tries!", "92"))
        else:
            if best_score is not None:
                print(c(f"Best score so far: {best_score} tries.", "96"))

        print(c(f"Game summary: You took {tries} tries this round. Total games: {total_games}.", "96"))
        print(c(f"Average tries per game: {avg:.1f}", "96"))

        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            if best_score is not None:
                print(c(f"Thanks for playing! Final average: {avg:.1f} tries, best score: {best_score} tries.", "96"))
            else:
                print(c(f"Thanks for playing! Final average: {avg:.1f} tries.", "96"))
            break

if __name__ == "__main__":
    main()
