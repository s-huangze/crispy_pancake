import random
 
LOW = 1
HIGH = 100
MAX_TRIES = 7
 
 
def c(msg: str, color: str = None):

    return msg if not color else f"[{color}] {msg}"
 
 
def safe_print(msg: str, color: str = None):
    try:
        print(c(msg, color))
    except NameError:
        print(msg)
 
 
def read_int(prompt: str, max_invalid: int = 3):

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
    if difficulty == "easy":
        max_tries = MAX_TRIES + 3
    elif difficulty == "hard":
        max_tries = max(1, MAX_TRIES - 2)
    else:
        max_tries = MAX_TRIES
 
    if low > high:
        safe_print("Invalid range between low and high values!", "91")
        return -1
 
    secret = random.randint(low, high)
    safe_print(f"I'm thinking of a number between {low} and {high}. You have {max_tries} attempts. (Type 'q' to quit)", "96")
 
    tries = 0
    while tries < max_tries:
        guess = read_int("Your guess: ")
        if guess is None:
            return tries
 
        if guess < low or guess > high:
            safe_print(f"Out of range! Guess between {low} and {high}.", "95")
            continue
 
        tries += 1
        diff = abs(guess - secret)
 
        if diff <= 3:
            safe_print("🔥 Very close!", "92")
        elif diff <= 10:
            safe_print("🙂 Close!", "94")
        else:
            safe_print("❄️ Way off!", "90")
 
        if guess < secret:
            safe_print("Too low!", "93")
        elif guess > secret:
            safe_print("Too high!", "93")
        else:
            safe_print(f"✅ Correct! You got it in {tries} tries.", "92")
            return tries
 
    safe_print(f"Out of attempts! The correct number was {secret}.", "91")
    return tries
 
 
def main():
    safe_print("🎮 Welcome to the Number Guessing Game!", "96")
    while True:
        play_once()
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            safe_print("Thanks for playing! 👋", "94")
            break
 
 
if __name__ == "__main__":
    main()
