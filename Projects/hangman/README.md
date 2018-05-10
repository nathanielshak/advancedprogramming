# Hangman - [WIP]

Creator: Bhavika Devnani

Firstly, if you don't know what hangman is, check this out 
[this](https://en.wikipedia.org/wiki/Hangman_(game)) and try playing it 
[here](https://www.ego4u.com/en/chill-out/games/hangman#form-top)!

Throughout the project, we will be using different data structures 
and algorithms that we've discussed throughout the lessons. 
Don't worry too much if you haven't done all the lessons, I will go through the essentials and link
you to the lessons as and when required. 

We will approach this project as a series of consecutive milestones, so 
it's totally okay if you don't want to do this in one sitting.

Now that we all are on the same page, let's start building! 

### Milestone 1 : Getting started

Let's first create the file that our hangman code will reside in. 
Go ahead and create a file called hangman.py in your desktop.
Open the file in the text editor of your choice.

Once you've done so, let's write the function that will house the logic of your hangman code.
Note that all the code below goes in `hangman.py`

    # This is the function that our logic will go into
    def start_hangman():
        print("Let's Start playing Hangman!")
    
    # This is the function call to kickstart the function. 
    # Note that the above function won't run until you call it usintg the line below    
    start_hangman()

After this is done, let's save our file.

Now we have our basic file ready to go. Lets see what happens when we run it!
        
To run this file, first open a new terminal window. 

In your terminal, type in `cd` and hit enter. This will take you to your root directory. (You don't 
need to worry about what that means right now, however you can read more [here](http://www.linfo.org/cd.html).)

Now type `cd/Desktop` and hit enter. This takes you to your desktop, where your `hangman.py` file is saved.

Finally, to run our file lets type in `python hangman.py` and this will run your file!

Hopefully, if everything goes right, you should have `Let's Start playing Hangman!` print in your terminal!
As a little experiment, see what happens when you comment 
out the last line of the file and try saving and running the file again.

Wonderful, now you have the basic workflow to run your file in place!! We will use `python hangman.py` to run 
your file every time we make a change to it.

To see how your file should like at the end of this chapter, see [hangman1](hangman1.py)

**Lessons used:**

* [Some Housekeeping and Getting Started with Python](Lesson1)


### Milestone 2 : Building our hangman's stages

Let's have some fun and finally build our hangman! I have a pretty basic hangman typed out, 
feel free to use it or get as creative as you want!!

       ____
      |    |
      |    o
      |   /|\\
      |   / \\
     _|_
    |   |_____
    |         |
    |_________|   

Now how can we get python to print out this hangman? It's as simple as putting it in a multi-line string.
How do we do that?

Whenever we want python to store multi line strings, we put those lines within 3 double quotes as such : 

    man = """
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

A small thing to notice is, I have put two backslashes `\\` instead of one for our hangman's right arm.
This is because python treats `\` as a special character, and we have to tell python we are indeed attempting
to print a `\`.(Optional : read more [here](https://docs.python.org/2.0/ref/strings.html))
Now lets try to print and see how our man look like!

First, go to your `hangman.py` file. Lets change the function to print our hangman:

    def start_hangman():
        print("Let's Start playing Hangman!\n")
        
        man = """
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
        print(man)
    
    start_hangman()

Run the file and see what happens!

Now that you can print one hangman to the terminal, let's build the different stages of the hangman we will use throughout the game!

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
        print(man1)
        print(man2)
        print(man3)
        print(man4)
        print(man5)
        print(man6)
        print(man7)
    
    start_hangman()

Run this file, and you should be able to see all the stages of the hangman!


This is what your file should look like after you're done with this section : [hangman2](hangman2.py)


### Milestone 3 : Getting hangman to work a word - First Letter

Now that we have our stages for hangman working, let's use it to turn it into a game!

Let our secret word be "MINI"

Let's try and figure out what our welcome screen should look like. 
In our welcome screen, let's welcome the player to hangman, and show them the first level of the 
hangman without any parts. We should also ask the player to enter a letter to guess, and show 4 
empty dashes indicating no guesses made so far.

We can do that by changing our earlier code to :

    def start_hangman():
        
        ...
         
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
        #Welcome message
        print("Welcome to Hangman!")
        print(man1)
        print("_ _ _ _") 
        print() #easy way to print an empty line
        print("Guess the letter :")
    
    start_hangman()

*Small note: The bit where I have written `...` , I refer to all the code that we earlier wrote between `def start_hangman():` and `man7 = """`. I will use this notation often to prevent re-writing long bits of code from previous sections.*

You should try running this bit of code in the terminal and see what happens!

If everything goes well, you should see:

    Welcome to Hangman!

       ____
      |    |
      |
      |
      |
     _|_
    |   |_____
    |         |
    |_________|
    
    _ _ _ _
    Guess the letter :
    
    Process finished with exit code 0


Now lets actually take a guess from the user and change our hangman accordingly.

To take in an input from the terminal, we will use a function called `raw_input()`. This function reads whatever the person
is typing in the terminal. Lets store that input in a variable called `guessed_letter`.

    def start_hangman():
        
        ...
         
        print("Guess the letter :")
        guessed_letter = raw_input()
    
    start_hangman()

Awesome, now the players guess should be stored in `guessed_letter`

We have to now figure out whether this letter is actually in the word "MINI" or not.

Python makes this super easy using the `in` keyword. All we will have to do is type:

    secret_word = "MINI"
    if guessed_letter in secret_word:
        # Turn the corresponding dash into letter
    else:
        # print the next hangman

What happens if the person guesses the wrong letter? 

We want to print the next hangman in line, and a message to try again.
That bit is nice and easy.

However, what happens when the person prints the right letter?

If the letter typed actually belongs to the word "MINI" then we want to convert the corresponding dash into the 
letter. For instance, if someone guesses the letter "N", I will want the 4 dashes to look like _ _ A _.

The easiest way to do that will be to store the 4 dashes in a `list` and then change the dash to a letter in the given position 
whenever someone guesses correctly.
(To remember what `lists` are look at Lesson3!)

We need to remember to do that for EVERY occurence of the letter. For instance, if someone
guesses "I", we need to change the 2nd and 4th letter to I. We will do that using a for loop
to go through every letter, check if it's equal to the `guessed_letter` and if it is,
we will change the same position in `dashes` to that letter.

Thus, lets add on to the code above :

    secret_word = "MINI"
    dashes = ["_", "_", "_", "_"]
    len_of_word = len(secret_word)
    positions = range(len_of_word)
    if guessed_letter in secret_word:
        for position in positions:
            if secret_word[position] == guessed_letter:
                dashes[position] = guessed_letter
    else:
        print(man2)

Let's examine what the code is doing line by line for a second.

`if guessed_letter in secret_word:` : This allows us to enter the next line of code if 
the guessed_letter is one of the letters in `secret_word` otherwise it sends us to the 
`else` line.

`len_of_word = len(secret_word)` : This line uses an inbuilt python function called `len()`. `len()` can
 be used in many ways, but here, it takes in our secret word and gives us the length of the word

`for position in range(len_of_word):` : This goes through all the positions in the word. Since
"MINI" has 4 letters, we will give it position numbers(also called indices) 
which are 0, 1, 2, 3. (Remember in programming languages we start counting at 0.) If you
don't remember loops, make sure to check out Lesson2!

`if secret_word[position] == guessed_letter:` : This will compare the letter at the position
with the `guessed_letter` and will go to the next line only if the `if` statement is true.

`dashes[position] = guessed_letter` : Finally, this will put in `guessed_letter` into the position 
where the dash was.

Whew, that was quite a bit.

Let's try running all of our code together. At this point it should look like :

    def start_hangman():
        
        ...
         
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
        
        guessed_letter = raw_input()
    
        if guessed_letter in secret_word:
        
            for position in range(len_of_word):
                if secret_word[position] == guessed_letter:
                    dashes[position] = guessed_letter
                    print("Good Job!")
        else:
        
            print(man2)
            print("Oh no, wrong letter!")
    
        print(dashes)
    
    start_hangman()

If everything goes well, you should be able to put in a guessed letter and see your code work!

To see how your file should like at the end of this chapter, see [hangman3](hangman3.py)

**Lessons used:**

* [Getting Familiar with Python](Lesson2)
* [Lists and Dictionaries](Lesson3)

### Milestone 4 : Getting hangman to work a word - Whole word

So far, we have accomplished the ability to guess one letter, and then update our hangman. 
Lets now attempt to do this for the full word.

We want to make sure the game goes on until the player has won the game or is out of guesses.
For each letter, based on whether the guess is correct or not, we have different actions.
Since we want to do the same action for each letter, we will be using a `loop`, specifically a `while loop`.
(If you don't remember what a `while loop` is, do a quick recap here)

If we were to write in simple english what we wanted our code to do it would be : 

    While the game hasn't been won or lost:
    
        Get a letter
    
        If the letter is correct :
        
            We update the letter in _dashes_
            We want to display the letter in correct dashes
            if all letters have been guessed:
                We tell the player they won the game, and we end the game.
            
        If the letter is incorrect:
        
            We want to print the hangman with another part.
            if all the guesses have been used:
                We tell the player they lost the game, and we end the game
        

Try to implement this yourself - for some inspiration, you can always see and try running [hangman4](hangman4.py)

**Lessons used:**

* [Searching and an Introduction to Algorithmic Analysis](Lesson5)

### Milestone 5 : Getting your hangman to work for any word!

Our algorithm should currently be quite easy to use for any word - 
all we have to make a code change. However, what we could do is make it even more fun
and allow someone to type in a secret word at the start of the game, and have other people 
guess the word.

We can re-use a lot of concepts from the previous milestones, specifically `raw_input()`.

Give it a shot before looking at [hangman5](hangman5.py)


### Milestone 6 : Celebrate!

You now have a fully functional hangman game that you can run in your terminal, Congratulations!

As a future exercise, you can think about how to add some cool features like:

* Have hangman not be sensitive about the case of the letter.
* Have the hangman game in place (not have a series of hangmen print out in the terminal, but instead the same one look like its updating)
* Have many more parts in the hangman
* Have hangman work for phrases in addition to words.
* Have timeouts for guesses.
* Have a competitive version(multiplayer)

..... and many more!