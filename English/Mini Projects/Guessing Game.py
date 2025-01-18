def guessing_game():
    # The secret word to guess
    secret_word = "Messi"

    # Hints to provide during the game
    hint = {
        1: "He has been playing as a professional since he is 16.",
        2: "He played with Thierry Henry.",
        3: "He won Champions League.",
        4: "He won La Liga.",
        5: "He is the Greatest of All Time."
    }

    # Initialize variables
    guess = ""
    guess_count = 0
    hint_word = "hint"  # Keyword to request a hint
    x = 0  # Tracks the number of hints given
    hint_requested = False  # Indicates if the user requested a hint
    guesses_maxed = False  # Indicates if the maximum guesses have been reached

    # Main game loop
    while guess != secret_word and not guesses_maxed:
        if guess_count < 3:  # Allow only 3 guesses
            if hint_requested and x < 5:
                x += 1
                print(hint.get(x, "No more hints available."))
                hint_requested = False

            # Get the user's guess
            guess = input("Guess (type 'hint' for a clue): ").capitalize()

            if guess == secret_word:
                print("You guessed the player!")  # Correct guess
                break
            elif guess.lower() == hint_word:
                if x < 5:
                    hint_requested = True  # Mark that a hint was requested
                else:
                    print("No more hints available.")  # No more hints to give
            else:
                print("Sorry, that's not correct!")  # Incorrect guess
                guess_count += 1  # Increment guess count
        else:
            print("You are out of guesses.")  # Maximum guesses reached
            guesses_maxed = True


# Run the game
guessing_game()
