# Lesson 3: Lists and Dictionaries

**To start this lesson, students should:**

* Be familiar with Python and know how to run, save, and edit Python files.
* Understand variables and control flow in Python
* Be familiar with arrays or lists in some context.

**By completing this lesson, students will:**

* Gain an understanding of Lists and Dicts in Python as well as how to use them practically.
* Get experience thinking out and desiging solutions to coding problems.

## Getting Started

For this lesson, we'll be doing a decent amount of coding. To start, download the exercises.py file in this folder (or just copy and paste it into your own file). This file contains the code for several functions that we will work through in the course of this lesson.

## Lists

Before we get into the coding, let's introduce a data structure in Python: **lists**.

> If you haven't heard the term "data structure" before, it describes a sort of computer storage unit that we use in coding to hold data and information.

If you're familiar with arrays in other languages, the Python version of them is lists. Lists are a way of storing several pieces of data in order. If you need a bit of a review, think of arrays and lists as a cabinet with several shelves in order that each have a piece of data stored. We keep track of each "shelf" by labeling it with a number starting from 0 and increasing. The first "shelf" is numbered 0, then 1, then 2, etc.

In Python, we can initialize a list like this:

    items = ["yay", "words", "in", "a", "list"]

In memory, the data would look something like this:

|**Label**|items[0]|items[1]|items[2]|items[3]|items[4]|
|---------|--------|--------|--------|--------|--------|
|**Data** |"yay"   |"words" |"in"    |"a"     |"list"  |

Then we can access items in the list like this:

    print(items[0])  # this will print out "yay"

or change the values of the list around like this:

    items[3] = "weee"  # now "a" is replaced with "weee"

The list would now look like this:

|**Label**|items[0]|items[1]|items[2]|items[3]|items[4]|
|---------|--------|--------|--------|--------|--------|
|**Data** |"yay"   |"words" |"in"    |"weee"  |"list"  |

We can find how long the list is like this:

    print(len(items))  # will print 5

We can go through all items in a list in order and print them like this:

    for item in items:
        print(item)

One big difference between Python lists and arrays in other languages is how flexible Python lists are. You can tack on to the list on the fly:

    items.append("sup")  # now "sup" is the last element in the list
    
Making the list look like this:

|**Label**|items[0]|items[1]|items[2]|items[3]|items[4]|items[5]|
|---------|--------|--------|--------|--------|--------|--------|
|**Data** |"yay"   |"words" |"in"    |"weee"  |"list"  |"sup"   |

You can mix types in the list:

    items.append(32)  # this is completely fine

Which would make the list look like this:

|**Label**|items[0]|items[1]|items[2]|items[3]|items[4]|items[5]|items[6]|
|---------|--------|--------|--------|--------|--------|--------|-----   |
|**Data** |"yay"   |"words" |"in"    |"weee"  |"list"  |"sup"   |32      |

### List Exercises

That was a lot of information at once. Let's put some of it into practice with some coding exercises. Inside of excercises.py, you'll see functions named `list_print`, `list_sum`, and `find_list_max` at the top.

#### List Print

The first function, `list_print`, is already filled out for you. This function goes through every item in a list passed as a parameter (in the `lst` variable) and prints them in order. You can use this as an example as you work on the rest of the problems.

#### List Sum

The first function we're going to write our code in is `list_sum`. In this function, we will assume the parameter, `lst` is a list of numbers, and we will want the function to compute the sum of all of them, then return that sum. 

> **Hint**: Think of how using a variable could be helpful here.

Once you've written that function, go ahead and run exercises.py to see if your solution works. This will run the function you wrote on several predesigned tests and check if the answer matches what it should be - the output will be on the terminal. (It will say all your other solutions are wrong, but that's okay. You haven't written them yet.)

#### Find List Max

For the other function, `find_list_max`, we'll take in a list of positive numbers, and we will return the largest number in that list.

Once you're done writing that, go ahead and run exercises.py again to test your solution.

## Dictionaries

One of the other important data structures in Python is called a **dictionary** (or "dict" for short). If you're familiar with maps in other languages, such as Java, dictionaries in Python are very similar.

Like lists, dictionaries are a data structure that can hold several seperate pieces of data. The difference is that lists have these pieces of data *ordered*, so we can write things like "I want the first element of this list" and have a clear answer. Dictionaries are different because they are *unordered*, and instead have what we call **keys**.

Keys are a way of labeling each "data slot" of a dictionary so that we know how to refer to and access each piece of data. If think of a list as a cabinet with several shelves in a row that are all ordered by number, think of a dictionary as a cabinet where we label each shelf with not necessarily a number, but a specific label that says something like "books" or "cleaning supplies".

In Python, most kinds of things that you would normally store in a variable (a string, a number, a boolean) can be keys in dictionaries, but not everything can be. Dictionary keys need to be *hashable*. You don't really need to worry about what that means yet; for now, a general rule is that only more simple datatypes will work - think numbers, booleans, and strings - and not bigger things like lists or other dictionaries. On the other hand, the **values** contained in a dictionary could be any data type in Python, even another dictionary! Here's what initializing an empty dictionary looks like:

    empty_dict = {}

You can also initialize them with items already inside.

    food = {"ham": "yes", "egg": "idk", "spam": "no"}

The data in this dictionary would look something like this:

|**Label**|food["ham"]|food["egg"]|food["spam"]|
|---------|-----------|-----------|------------|
|**Data** |"yes"      |"idk"      |"no"        |

Then, you can access items in the dictionary like this:

    print(food["spam"])

which would print out: "no".

You can modify things in the dictionary like this:

    food["egg"] = 42

> Like lists, you can mix different value types in dictionaries.

Which would make it look like this:

|**Label**|food["ham"]|food["egg"]|food["spam"]|
|---------|-----------|-----------|------------|
|**Data** |"yes"      |42         |"no"        |

You can add new keys into the dictionaries like this:

    food[87] = True

> You can also mix different key types in dictionaries.

And then the dictionary would look like this:

|**Label**|food["ham"]|food["egg"]|food["spam"]|food[87]|
|---------|-----------|-----------|------------|--------|
|**Data** |"yes"      |42         |"no"        |True    |

Like lists, dictionaries also have a `len()` that gives the number of items in the dictionary:

    print(len(food))  # this prints 4

And you can write loops over the contents of a dictionary in multiple ways:

    for key in dictionary.keys():  # loop over the keys only
        ...

    for value in dictionary.values():  # loop over the values only
        ...

    for key, value in dictionary.items():  # loop over the keys along with their values
        ...

Anyway, that should be most of what you need to know on dictionaries. For more information, feel free to read up [here](https://www.python-course.eu/dictionaries.php).

### Dictionaries Exercises

Okay, back to coding. Take a look at the `dict_print`, `key_max_value`, and `count_items` functions in exercises.py. We've provided `dict_print` as an example of how to iterate through a dictionary's keys and print out the associated values.

#### Key Max Value

Go ahead and find the `key_max_value` function. In this function, we're going write code to iterate through the dictionary passed as a parameter in `d` and return the **key** that matches with the highest **value** stored in the dictionary (remember the difference between keys and values). We can assume all values in the dictionary will be positive numbers.

So if we passed in a dictionary like this:

|**Label**|d[999]|d["yolo"]|d[True]|d["heheheh"]|
|---------|------|---------|-------|------------|
|**Data** |1     |42       |18     |22          |

the function should return "yolo".

> **Hint**: both `print_dict` and `find_list_max` could be helpful here to use as examples.

#### Count Items

Next, you'll see the `count_items` function. In this function, we will iterate through a list, and return a dict that has each item in the list as a **key** mapped to the number of times that item appeared in the list as its associated **value**.

For example, calling the function like this:

    count_items(["yo", "yo", 1, 1, 1, 3, 2, 3, 8, 7])

should return a dict that looks like this:

|**Label**|d["yo"]|d[1]|d[2]|d[3]|d[8]|d[7]|
|---------|-------|----|----|----|----|----|
|**Data** |2      |3   |1   |2   |1   |1   |

After that, go ahead and run exercises.py to test your solutions - once you've got all the tests passing, you're done!

[On to lesson 4](../Lesson4)