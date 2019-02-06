# Lesson 4: Scope.

**To start this lesson, students should:**

* Have a basic understanding of functions in Python.
* Have a solid grasp of control flow.

**By completing this lesson, students will:**

* Gain a deeper understanding of variable scope and control flow.

## Getting Started

As you'll create bigger and more complex programs understanding scope will make your life much easier. "Scope" is a way for us to create variables that are only visible to a certain section of your code. For example in a for loop we create a varible that ceases to exist once the loop is over.

    # this will print each individual letter in the string s by creating a new variable letter
    s = "Hello World!"
    for letter in s:
        print(letter)
    # this next line will crash your program! Because the variable 'letter' doesn't exist
    # outside the 'scope' of your for loop.
    print(letter)
    # but this line would pass just fine since its a "global" variable
    print(s)

### Global variables vs Local variables

If a variable is defined at the very top of a python program it can be accessed by any block of code in the file. We call those global variables because everything in our "world" can access it.
In Python anytime we use the ':' character we're creating local scope and anything created under and tabbed in is a local variable. It can only be accessed in the same "block" of code its defined in.

    name = "April Smith" # global variable
    age = 18 # another global
    if age > 17:
      message = "You are over 17 years old!" # local variable
      print(message)
    print(message) # this is an error since we are now "outside" of the block where message was defined.
    print(name) # this is fine since it was defined "globally" and outside of any blocks.

A quick way to tell if a variable is a local variable or not is to ask yourself these questions:
> * Was this variable created inside of a function?
> * Was it created under a ':' and is it more tabbed in then the rest of your code?

If you answered yes to any, or all, of those questions then that variable is a local variable!

We're done! [On to lesson 5](../Lesson5)
