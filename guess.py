def play_once(low: int = LOW, high: int = HIGH) -> int:
    """Play one round of the guessing game. Returns number of tries this round."""
    secret = random.randint(low, high)
    # Intro line (colored if c() exists)
    try:
        print(c(f"I'm thinking of a number between {low} and {high}. You have {MAX_TRIES} attempts. (Type 'q' to give up)", "96"))
    except NameError:
        print(f"I'm thinking of a number between {low} and {high}. You have {MAX_TRIES} attempts.")

    tries = 0
    while tries < MAX_TRIES:
        result = read_int("Your guess: ")   # may be int or None if user typed 'q'
        if result is None:
            try:
                print(c(f"You gave up! The correct number was {secret}.", "95"))
            except NameError:
                print(f"You gave up! The correct number was {secret}.")
            return tries

        guess = result
        tries += 1

        # Range check
        if guess < low or guess > high:
            try:
                print(c(f"Out of range! Guess between {low} and {high}.", "95"))
            except NameError:
                print(f"Out of range! Guess between {low} and {high}.")
            continue

        # Closeness feedback
        diff = abs(guess - secret)
        try:
            if diff <= 3:
                print(c("🔥 Very close!", "92"))      # green
            elif diff <= 10:
                print(c("🙂 Close!", "94"))           # blue
            else:
                print(c("❄️ Way off!", "90"))         # gray
        except NameError:
            if diff <= 3:
                print("Very close!")
            elif diff <= 10:
                print("Close!")
            else:
                print("Way off!")

        # High/low hints
        if guess < secret:
            try:
                print(c("Too low!", "93"))            # yellow
            except NameError:
                print("Too low!")
        elif guess > secret:
            try:
                print(c("Too high!", "93"))           # yellow
            except NameError:
                print("Too high!")
        else:
            try:
                print(c(f"Correct! You got it in {tries} tries.", "92"))  # green
            except NameError:
                print(f"Correct! You got it in {tries} tries.")
            return tries

    # Out of attempts
    try:
        print(c(f"Out of attempts! The correct number was {secret}.", "91"))  # red
    except NameError:
        print(f"Out of attempts! The correct number was {secret}.")
    return tries