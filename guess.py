def play_once(low: int = LOW, high: int = HIGH, difficulty: str = "normal") -> int:
    # ✅ Suggestion #2 — Add difficulty-based logic
    if difficulty == "easy":
        max_tries = MAX_TRIES + 3
    elif difficulty == "hard":
        max_tries = max(1, MAX_TRIES - 2)
    else:
        max_tries = MAX_TRIES
 
    if low > high:
        print("Sorry, the range between the low and high bars is invalid")
        return -1
 
    secret = random.randint(low, high)
    try:
        print(c(f"I'm thinking of a number between {low} and {high}. You have {max_tries} attempts. (Type 'q' to give up)", "96"))
    except NameError:
        print(f"I'm thinking of a number between {low} and {high}. You have {max_tries} attempts.")
 
    tries = 0
    while tries < max_tries:
        result = read_int("Your guess: ")
        if result is None or not isinstance(result, int):
            print("Invalid input! Please enter a number or 'q' to quit.")
            continue
 
        guess = result
 
        if guess < low or guess > high:
            try:
                print(c(f"Out of range! Guess between {low} and {high}.", "95"))
            except NameError:
                print(f"Out of range! Guess between {low} and {high}.")
            continue
 
        tries += 1
        diff = abs(guess - secret)
        try:
            if diff <= 3:
                print(c("🔥 Very close!", "92"))
            elif diff <= 10:
                print(c("🙂 Close!", "94"))
            else:
                print(c("❄️ Way off!", "90"))
        except NameError:
            if diff <= 3:
                print("Very close!")
            elif diff <= 10:
                print("Close!")
            else:
                print("Way off!")
 
        if guess < secret:
            try:
                print(c("Too low!", "93"))
            except NameError:
                print("Too low!")
        elif guess > secret:
            try:
                print(c("Too high!", "93"))
            except NameError:
                print("Too high!")
        else:
            try:
                print(c(f"Correct! You got it in {tries} tries.", "92"))
            except NameError:
                print(f"Correct! You got it in {tries} tries.")
            return tries
 
    try:
        print(c(f"Out of attempts! The correct number was {secret}.", "91"))
    except NameError:
        print(f"Out of attempts! The correct number was {secret}.")
    return tries
