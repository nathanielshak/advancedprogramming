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

    secret_word = "MINI"
    dashes = ["_", "_", "_", "_"]

    # Welcome message
    print("Welcome to Hangman!")
    print(man1)

    print("Guess the letter :")
    print(dashes)

    guessed_letter = input()

    if guessed_letter in secret_word:
        for position in [0, 1, 2, 3]:
            if secret_word[position] == guessed_letter:
                dashes[position] = guessed_letter
                print("Good Job, guess again!")
    else:
        print(man2)
        print("Oh no, wrong letter! Try again!")

    print(dashes)

start_hangman()