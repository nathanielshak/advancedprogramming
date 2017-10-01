# Lesson 3:

**To start this lesson, students should:**

* Be familiar with Python and know how to run, save, and edit Python files.
* Understand variables and control flow in Python
* Be familiar with arrays or lists in some context.


**By completing this lesson, students will:**

* Gain an understanding of Lists and Dicts in Python as well as how to use them practically.
* Get experience thinking out and desiging solutions to coding problems.

## Getting Started

For this lesson, we'll be doing a decent amount of coding. To start, download the exercises.py file (or just copy and paste it into your own file if you're feeling lazy). This file contains the code for several functions that we will work through in the course of this lesson. 

## Lists

If you're familiar with arrays in other languages, the Python version of them is lists. Pretty much, they're a way of storing several ordered items. If you need a bit of a review, think of them as a cabinet with several cabinets in order that each have something stored. We keep track of each "shelf" by number starting from 0. The first "shelf" is numbered 0, then 1, then 2, etc.

We can initialize a list like this:

	items = ["yay", "words", "in", "a", "list"]
	
Then we can access items in the list like this.

	print items[0] # will print out "yay"
	a = items[2] # a now equals "in"

or change the values of the list around like this:

	items[3] = "weee" # now "a" is replaced with "weee"

	
or find how long the list is like this:

	print len(items) # will print 5
	
We can iterate through all items in a list and print them like this:

	for item in items:
		print item
		
One big difference between Python lists and arrays in other languages is how flexible Python lists are. You can tack on to the list on the fly:

	items.append("sup") #now "sup" is the last element in the list
	
You can mix types in the array:

	items.append(32) # this is completely fine
 