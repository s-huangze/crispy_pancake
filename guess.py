def safe_print(msg: str, color: str = None):
    try:
        print(c(msg, color))
    except NameError:
        print(msg)
 
 
def play_once(low: int = LOW, high: int = HIGH, difficulty: str = "normal") -> int:
    # Difficulty logic
    if difficulty == "easy":
        max_tries = MAX_TRIES + 3
    elif difficulty == "hard":
        max_tries = max(1, MAX_TRIES - 2)
    else:
        max_tries = MAX_TRIES
 
    if low > high:
        safe_print("Sorry, the range between the low and high bars is invalid", "91")
        return -1
 
    secret = random.randint(low, high)
    safe_print(f"I'm thinking of a number between {low} and {high}. You have {max_tries} attempts. (Type 'q' to give up)", "96")
 
    tries = 0
    while tries < max_tries:
        result = read_int("Your guess: ")
        if result is None or not isinstance(result, int):
            safe_print("Invalid input! Please enter a number or 'q' to quit.", "95")
            continue
 
        guess = result
        if guess < low or guess > high:
            safe_print(f"Out of range! Guess between {low} and {high}.", "95")
            continue
 
        tries += 1
        diff = abs(guess - secret)
 
        # Feedback
        if diff <= 3:
            safe_print("🔥 Very close!", "92")
        elif diff <= 10:
            safe_print("🙂 Close!", "94")
        else:
            safe_print("❄️ Way off!", "90")
 
        # High/low hints
        if guess < secret:
            safe_print("Too low!", "93")
        elif guess > secret:
            safe_print("Too high!", "93")
        else:
            safe_print(f"Correct! You got it in {tries} tries.", "92")
            return tries
 
    safe_print(f"Out of attempts! The correct number was {secret}.", "91")
    return tries
