import random

# Constants for setting up the game
LOW = 1         # Minimum number in guessing range
HIGH = 100      # Maximum number in guessing range
MAX_TRIES = 7   # Number of tries allowed for players
 
 
def c(msg: str, color: str = None):
    """
    Optional color wrapper for messages.
    Returns the message with a color tag if color is provided.
    """
    return msg if not color else f"[{color}] {msg}"
 
 
def safe_print(msg: str, color: str = None):
    """ 
    Prints message with color with c() function
    If no color, falls back to basic print function
    """
    try:
        print(c(msg, color))
    except NameError:
        print(msg)

# ===========================
# Analytics helpers (no extra imports)
# ===========================
def _optimal_attempts(low: int, high: int) -> int:
    """
    Computes ceil(log2(range_size)) without math import.
    Uses integer bit_length trick: ceil(log2(n)) = (n-1).bit_length()
    """
    n = max(1, (high - low + 1))
    return (n - 1).bit_length()

def _ascii_trajectory(guesses, secret):
    """
    Builds a tiny ASCII bar series showing how close each guess was.
    Taller bar = closer to the secret.
    """
    if not guesses:
        return ""
    diffs = [abs(g - secret) for g in guesses]
    mx = max(diffs)
    if mx == 0:
        return "▮" * 10
    bars = []
    for d in diffs:
        # Map diff to 1..10, where smaller diff => taller bar
        height = 10 - round(9 * d / mx)
        height = 1 if height < 1 else height
        bars.append("▮" * height)
    return " ".join(bars)

def _print_analytics(low, high, tries, secret, guesses, won: bool, quit_early: bool):
    """
    Prints post-game analytics: optimal attempts, efficiency, and guess trajectory.
    Keeps everything dependency-free and consistent with your color tags.
    """
    safe_print("— Analytics —", "96")
    opt = _optimal_attempts(low, high)
    safe_print(f"Optimal attempts (binary search): {opt}", "94")
    safe_print(f"Your attempts counted: {tries}", "94")

    if won and tries > 0:
        # Efficiency is how close you were to optimal in % (higher is better)
        efficiency = (opt * 100.0) / tries
        safe_print(f"Efficiency vs. optimal: {efficiency:.1f}%", "94")
    elif quit_early:
        safe_print("Efficiency vs. optimal: N/A (quit)", "94")
    else:
        # Out of attempts without success
        safe_print("Efficiency vs. optimal: 0.0% (did not guess)", "94")

    # Per-guess closeness summary
    if guesses:
        last_diff = abs(guesses[-1] - secret)
        best_diff = min(abs(g - secret) for g in guesses)
        safe_print(f"Best closeness (min |guess - secret|): {best_diff}", "94")
        safe_print(f"Last guess distance from secret: {last_diff}", "94")
        safe_print(f"Guess trajectory (closer = taller): { _ascii_trajectory(guesses, secret) }", "94")
    else:
        safe_print("No valid guesses to analyze.", "94")
# ===========================


def read_int(prompt: str, max_invalid: int = 3):
    """
    Reads an integer input from the user.
    Allows quitting with 'q' and limits invalid attempts.
    Returns an int or None if the user quits or exceeds invalid attempts.
    """
    invalid_attempts = 0
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'q':
            safe_print("You gave up. Better luck next time!", "95")
            return None
        try:
            return int(user_input)
        except ValueError:
            invalid_attempts += 1
            safe_print("Invalid input! Enter a number or 'q' to quit.", "95")
            if invalid_attempts >= max_invalid:
                safe_print("Too many invalid inputs. Game over!", "91")
                return None
 
 
def play_once(low: int = LOW, high: int = HIGH, difficulty: str = "normal") -> int:
    """
    Plays one round of the guessing game.
    Adjusts difficulty by modifying the number of allowed attempts.
    Returns the number of valid guesses made, or -1 if range is invalid.
    """
    # Adjusts difficulty level by adding attempts
    if difficulty == "easy":
        max_tries = MAX_TRIES + 3
    elif difficulty == "hard":
        max_tries = max(1, MAX_TRIES - 2)
    else:
        max_tries = MAX_TRIES

    # Validates range to prevent errors
    if low > high:
        safe_print("Invalid range between low and high values!", "91")
        return -1
     
    # Generates the secret number
    secret = random.randint(low, high)
    safe_print(f"I'm thinking of a number between {low} and {high}. You have {max_tries} attempts. (Type 'q' to quit)", "96")

    # Tracks valid guesses for post-game analytics
    tries = 0
    guesses = []  # <-- analytics: store each valid guess

    while tries < max_tries:
        guess = read_int("Your guess: ")
        if guess is None:
            # Player quit early: print analytics based on what we have
            _print_analytics(low, high, tries, secret, guesses, won=False, quit_early=True)
            return tries  # For if user quit
         
        # Validates guess range
        if guess < low or guess > high:
            safe_print(f"Out of range! Guess between {low} and {high}.", "95")
            continue
 
        tries += 1  # Counts all valid attempts after checking everything above
        guesses.append(guess)  # <-- analytics: record valid guess
        diff = abs(guess - secret)

        # Feedback on how close the guess was (the number after allows for colors)
        if diff <= 3:
            safe_print("Very close!", "92")
        elif diff <= 10:
            safe_print("Close!", "94")
        else:
            safe_print("Way off!", "90")

        # Hint on direction of guess
        if guess < secret:
            safe_print("Too low!", "93")
        elif guess > secret:
            safe_print("Too high!", "93")
        else:
            safe_print(f"Correct! You got it in {tries} tries.", "92")
            # Print analytics on win
            _print_analytics(low, high, tries, secret, guesses, won=True, quit_early=False)
            return tries  # Correct guess ends the round

    # If user ran out of attempts without success
    safe_print(f"Out of attempts! The correct number was {secret}.", "91")
    # Print analytics on loss
    _print_analytics(low, high, tries, secret, guesses, won=False, quit_early=False)
    return tries
 
 
def main():
    """
    Main game loop.
    Welcomes the player, tracks high score,  offers replay option.
    """
    safe_print("🎮 Welcome to the Number Guessing Game!", "96")
    high_score = None
 
    while True:
        result = play_once()
        if result > 0:
            # Update high score if it's the best so far
            if high_score is None or result < high_score:
                high_score = result
                safe_print(f"🏆 New High Score: {high_score} tries!", "93")
            else:
                safe_print(f"Your best so far: {high_score} tries.", "94")

        # Allows for player to replay
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            safe_print("Thanks for playing! 👋", "94")
            break
 
# Entry point for script
if __name__ == "__main__":
    main()
