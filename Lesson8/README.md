# Lesson 8: More advanced algorithms

**To start this lesson, students should:**

* Understand the basics of lists and dicts in Python.
* Have a decent amount of experience analyzing and coding semi-complex algorithms.

**By completing this lesson, students will:**

* Gain more practice with using data structures.
* Practice decomposing complex functions into smaller, simpler functions.

Learning to code is like learning to play an instrument - It's all about practice and repetition. This lesson contains a few more practice problems to reinforce what you've learned.

## 1. round_sum

The first question is on CodingBat again. Do to the question [here](http://codingbat.com/prob/p179960), then
return here afterward for the other questions - they will all be in exercises.py.

## 2. Find last letters

The next exercise is in exercises.py. Copy the code to your own file, then find this code:

	# 2. Find last letters
	
	def find_last_letters(word):
	  result = {}
	  # TODO
	  return ret


Write a function that takes a word and returns a dictionary of the position of the last occurrence of each letter. 

For example, given the word 'challenge', it would return the dictionary `{'c': 0, 'h': 1, 'a': 2, 'l': 4, 'e': 8, 'n': 6, 'g': 7}` (remember, the first letter is at position 0).

## 3. Words by length

### Part 1:

Find this part of the code in part 3:

	def words_by_length(words):
	  result = {}
	  # TODO
	  return result

Write this function so that it takes a list of words and separates them into a dict that arranges them by length, mapping each length to a list of words that are that length.

For example, given the list `['cat', 'dog', 'bird', 'sheep', 'rat', 'horse', 'human', 'lion']`, your function should return:

	{
	  3: ['cat', 'dog', 'rat'],
	  4: ['bird', 'lion'],
	  5: ['sheep', 'horse', 'human'],
	}
	
### Part 2:

Now, in this part of the code:

	def word_appears(words_dict, word):
	  # TODO
	  return False

Write another function that takes this dictionary as the parameter, `word_dict` and a word and returns True if the word appears anywhere in the dictionary.

### Challenge:

What happens if a word appears more than once in the input list? 

In this part of the code:

	def words_by_length_challenge(words):
	  result = {}
	  # TODO
	  return result

Write a different version of your function so that each word appears only once in the returned dictionary.

## 4. Nested lists

This is a two-part question.

### Part A: Splitting lists

In this part of the code:

	def split_list(items, count):
	  result = []
	  # TODO
	  return result

Write a function that takes a list, `items`, and a number and breaks the list into a list of lists of the given size. 

The last sub-list can be shorter if there aren't enough items to fill it up. For example:

	split_list([1, 3, 5, 7], 2) -> [[1, 3], [5, 7]]
	split_list([1, 3, 5, 7, 9, 11, 13], 3) -> [[1, 3, 5], [7, 9, 11], [13]]
	split_list([1, 3, 5, 7], 10) -> [[1, 3, 5, 7]]
	split_list([], 3) -> []

(`split_list` always returns a list containing other lists, unless the input list is empty.)

> **Hint**: You can access items from the end of a list using negative numbers. For example, `some_list[-1]` is the last item in a list, `some_list[-2]` is the second-to-last, and so on. (You can solve this problem without using negative indices, but your code will probably be a bit longer.)

### Challenge: 

In this function:

	def split_list_challenge(items, count):
	  result = []
	  # TODO
	  return result

Try rewriting the function using slices instead. [This StackOverflow answer](https://stackoverflow.com/a/509295) explains what slices are and how to use them.

**Note**: It's possible to write this function in a single line using a *list comprehension*, a shorthand for loops that generate lists. It's not part of this lesson, but if you're curious, you can read about list comprehensions [here](http://www.pythonforbeginners.com/basics/list-comprehensions-in-python).

### Part B: Finding items in nested lists

In this function:

	def which_list(lists, item):
	  # TODO
	  return -1

Write a function that finds which sublist a given item is in. If the item is in multiple sublists, return the first one that it appears in. If the item isn't in any of the lists, return -1. For example:

	which_list([[1, 3, 5], [5, 7, 9], [9, 11]], 1) -> 0
	which_list([[1, 3, 5], [5, 7, 9], [9, 11]], 5) -> 0
	which_list([[1, 3, 5], [5, 7, 9], [9, 11]], 9) -> 1
	which_list([[1, 3, 5], [5, 7, 9], [9, 11]], 11) -> 2
	which_list([[1, 3, 5], [5, 7, 9], [9, 11]], 17) -> -1

> **Hint**: You can use `for item_index, item in enumerate(list)` to iterate over list items along with their indexes, so `item_index` would equal the list index, and `item` would be the actual item at that index.

### Runtime

What's the Big O runtime of the function in part A? What about part B? Check with a mentor to see if you're right.

Challenge: Can you make part B faster if you make part A return something else? (Don't worry if you can't figure out a way to do this - it's pretty difficult! Feel free to brainstorm ideas with people around you.)

We're all done here - on to Lesson 9!
