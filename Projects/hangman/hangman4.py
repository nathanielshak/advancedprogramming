def start_hangman():
    print("Let's Start playing Hangman!")


def start_hangman():
    print("Let's Start playing Hangman!\n")

    man1 = """
       ____
      |    |
      |
      |
      |
     _|_
    |   |_____
    |         |
    |_________|
    """
    man2 = """
       ____
      |    |
      |    o
      |
      |
     _|_
    |   |_____
    |         |
    |_________|
    """
    man3 = """
       ____
      |    |
      |    o
      |    |
      |
     _|_
    |   |_____
    |         |
    |_________|
    """
    man4 = """
       ____
      |    |
      |    o
      |   /|
      |
     _|_
    |   |_____
    |         |
    |_________|
    """
    man5 = """
       ____
      |    |
      |    o
      |   /|\\
      |
     _|_
    |   |_____
    |         |
    |_________|
    """
    man6 = """
       ____
      |    |
      |    o
      |   /|\\
      |   /
     _|_
    |   |_____
    |         |
    |_________|
    """
    man7 = """
           ____
          |    |
          |    o
          |   /|\\
          |   / \\
         _|_
        |   |_____
        |         |
        |_________|
        """

    # The number of guesses our players get depends on the
    # number of total hangmen you design, hence I call this list guesses
    guesses = [man1, man2, man3, man4, man5, man6, man7]

    secret_word = "MINI"
    dashes = ["_", "_", "_", "_"]

    # Welcome message
    print("Welcome to Hangman!")
    # This selects the first man in the list and removes it.
    print(guesses.pop(0))

    # When the game is either won or lost, we change this to true
    game_over = False

    while not game_over:

        print("Guess the letter :")
        print(dashes)
        guessed_letter = raw_input()

        if guessed_letter in secret_word:

            # Update dashes
            for position in range(len(secret_word)):
                if secret_word[position] == guessed_letter:
                    dashes[position] = guessed_letter
            print("Good Job!")
            # Printing a blank line to make our terminal look more organized
            print

            # Check if game has been won
            if "_" not in dashes:
                # The moment you set this to True, you won't re-enter the while loop
                # indicating your game is over
                game_over = True
                print("------------------------------")
                print("Congratulations! You have won!")
                print("------------------------------")
        else:

            # If there are guesses left
            if len(guesses) > 0:
                print(guesses.pop(0))
                print("Oh no, wrong letter!")

            # If the player is out of guesses, he has lost
            else:
                # The moment you set this to True, you won't re-enter the while loop
                # indicating your game is over
                game_over = True
                print("Sorry! You lost!")
                print


start_hangman()