# Lesson 5: Let's get some practice.

**To start this lesson, students should:**

* Have a basic understanding of lists and dictionaries in Python.
* Have a solid grasp of control flow and designing logical solutions to coding problems.
* Understand variables, operations, and booleans.

**By completing this lesson, students will:**

* Gain a soldified understanding of variables, control flow, lists, and dictionaries.
* Get experience putting together more complex programs and designing solutions to more difficult coding problems.

## Getting Started

In the last several lessons we introduced a decent amount of material. Getting familiar with Python and learning about things like lists and dictionaries can be intimidating at first, but as you get more experience, it starts to become routine. However, to get there, you need *practice*. In this lesson, we're going to focus on putting everything we've learned so far together through some coding.

> Remember, if there's something in Python that you want to do, but you either forgot how to or haven't done it before, **Google it!** In fact, there may be several problems in here that are very difficult to solve without Googling how to do certain things in Python. Remember, the best programmers aren't the people who know the most - it's the people that are the best at **figuring out what they don't know**. Learning how to be good at Googling is part of learning to be a good programmer.

Some exercises were pulled from Shrey's [next level programming](https://github.com/ShreyGupta19/streetcode-next-level/blob/master/labs/lab1.md). 

Go ahead and open up exercises.py and we'll get started.

### Square if odd

At the top of the code, you'll see the `square_if_odd` function:

    # Returns the square of a number if it's odd; otherwise, returns the original number.
    def square_if_odd(num): 
        # TODO: implement this!
        return -1

For this function, we will write code that will make the function return the square of `num` if it is odd, or just the original number if it is even.

    square_if_odd(2) -> 2
    square_if_odd(3) -> 9
    square_if_odd(-8) -> -8
    square_if_odd(-9) -> 81

> Hint: Remember that the `%` operator gives the remainder of a division problem. So `6 % 2 == 0`, `7 % 2 == 1`.

### In Range    

For the `in_range` function, we will write code that will return `True` or `False` depending on whether the number supplied in the parameter, `num` is between `lower` and `upper`, inclusive.

    in_range(1, 3, 2) -> True
    in_range(-2, 80, 80) -> True
    in_range(-3, 5, 6) -> False

### Even Elements

For the `even_elements` function, we will write code that will take in a list of numbers, supplied in `nums`, then return a list containing only the even numbers in nums in the same order.

    even_elements([1, 2, 5, 7, 2, 6, 7, 9]) -> [2, 2, 6]
    even_elements([-8, 2, 4]) -> [-8, 2, 4]
    even_elements([1, 3, 5, 7]) -> []

### Most Common Letter

For the `most_common_letter` function, we will write code that will return the most common occuring letter in the parameter, `str`. If there is a tie, you can return any of the top occuring letters.

    most_common_letter("abcb") -> 'b'
    most_common_letter("popular") -> 'p'
    most_common_letter("andskfjngrkejnhkjjfjfjnfnkzzjj") -> 'j'

> **Hint:** think about how a dictionary could be useful here. Also, you can iterate through letters in a string in Python like this:

    # this will print each individual letter in the string s
    for letter in s:
        print(letter)

### Maximum Difference

In the `max_diff` function, we will write code that will return the maximum difference between any two numbers in the list of numbers, `nums`. You can assume that everything in the list, `nums` is a number and that there are at least 2 numbers in list.

    max_diff([1, 4, -9, 2, 3, 20]) -> 29
    max_diff([1, 3, 5]) -> 4
    max_diff([-2, 0]) -> 2

### Hourglass

For the `hourglass` function, write code that prints an hourglass shape of a given size `size` (i.e. the base of the hourglass has `2 * size` stars).

For example, the following is an hourglass of size 3 :

    hourglass(3) 
    ******
     ****
      **
     ****
    ******

And the following is an hourglass of size 5:

    hourglass(5)
    **********
     ********
      ******
       ****
        **
       ****
      ******
     ********
    **********

**Hint:** In Python, you can multiply strings! For example, the code `"a" * 7` would result in `"aaaaaaa"`. You can also add strings by doing things like `"aaa" + "b" * 2`, which would result in `"aaabb"`.
**Hint:** If you're having trouble writing this function, try writing a function that just prints the top-left part of the hourglass first. Then add on the bottom-left part, and the right parts after that.

We're done! [On to lesson 6](../Lesson6)
