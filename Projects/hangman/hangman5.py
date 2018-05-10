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

    guesses = [man1, man2, man3, man4, man5, man6, man7]

    print("Welcome to Hangman!")
    print


    # Customizing our input
    print("Please enter the secret word")
    secret_word = raw_input()
    secret_word = list(secret_word)
    dashes = ["_" for _ in secret_word]

    print("Thank you! - Lets start the game")

    print(guesses.pop(0))
    game_over = False

    while not game_over:

        print("Guess the letter :")
        print(dashes)
        guessed_letter = raw_input()

        if guessed_letter in secret_word:
            for position in range(len(secret_word)):
                if secret_word[position] == guessed_letter:
                    dashes[position] = guessed_letter
            print("Good Job!")
            print

            if "_" not in dashes:
                game_over = True
                print("------------------------------")
                print("Congratulations! You have won!")
                print("------------------------------")
        else:

            if len(guesses) > 0:
                print(guesses.pop(0))
                print("Oh no, wrong letter!")

            else:
                game_over = True
                print("Sorry! You lost!")
                print

        if game_over:
            break


start_hangman()