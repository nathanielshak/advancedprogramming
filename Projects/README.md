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


### Milestone 3 : Getting hangman to work a word

Now that we have our stages for hangman working, let's use it to turn it into a game!

Let our secret word be "PLAY"

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
        print("Guess the letter :")
    
    start_hangman()

*Small note: The bit where I have written `...` , I refer to all the code that we earlier wrote between `def start_hangman():` and `man7 = """`. I will use this notation often to prevent re-writing long bits of code from previous sections.*

You should try running this bit of code in the terminal and see what happens!
 
Now lets actually take a guess from the user and change our hangman accordingly.

To take in an input from the terminal, we will use a function called `input()`. This function takes in whatever
the person playing the game types in the terminal, and stores it in a variable.

    def start_hangman():
        
        ...
         
        print("Guess the letter :")
        guessed_letter = input()
    
    start_hangman()

Awesome, now the players guess should be stored in `guessed_letter`

We have to now figure out whether this letter is actually in the word "PLAY" or not.

### Milestone 3.5 : Breaking things and fixing them - 1

<!---
TODO: Show how to find bugs with code and fix edge cases
-->

### Milestone 4 : Getting hangman to work with any word

<!---
TODO: Use loops to get it working with any word
-->

### Milestone 4.5 : Breaking things and fixing them - 2

<!---
TODO: Show how to find bugs with code and fix edge cases
-->

### Milestone 5.5 : Code organization and using classes(Optional)

<!---
TODO: Show how we can break up one long function into smaller working parts
-->


### Milestone 6 : Celebrate!

<!---
TODO: This section
-->
