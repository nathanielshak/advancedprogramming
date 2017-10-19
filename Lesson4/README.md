# Lesson 4: Let's get some practice.

**To start this lesson, students should:**

* Have a basic understanding of Lists and Dictionaries in Python.
* Have a solid grasp of control flow and designing logical solutions to coding problems.
* Understand variables, operations, and booleans.

**By completing this lesson, students will:**

* Gain a soldified understanding of variables, control flow, lists, and dictionaries.
* Get experience putting together more complex programs and desigining solutions to difficult coding problems.

## Getting Started

Okay, in the last several lessons we introduced a decent amount of material. Getting familiar with Python and learning about things like lists and dictionaries can be scary and intimidating at first, but as you get further and further it starts to become routine. However, to get there, you need *practice*. In this lesson, we're going to focus on putting everything we've learned so far together through some coding.

> Remember, if there's something in Python that you want to do, but you either forgot how to or haven't done it before, **Google it!** In fact, there may be several problems in here that are very difficult to solve without Googling how to do certain things in Python. Remember, the best programmers aren't the people who know the most - it's the people that are the best at **figuring out what they don't know**. Learning how to be good at Googling is part of learning to be a good programmer.
 
Some exercises were pulled from Shrey's [next level programming](https://github.com/ShreyGupta19/streetcode-next-level/blob/master/labs/lab1.md).

Okay, go ahead and open up exercises.py.

### Square if odd

At the top of the code, you'll see this function:

	#returns the square of a number if it's odd, otherwise returns the original number
	def square_if_odd(num):	
		#TODO: implement this!
		return -1
		
For this function, we will write code that will make the function return the square of `num` if it is odd, or just the original number if it is even.

	square_if_odd(2) -> 2
	square_if_odd(3) -> 9
	square_if_odd(-8) -> -8
	square_if_odd(-9) -> 81
	
### In Range	

For this function:

	#returns whether the given number is within the range of lower and upper inclusive (True or False)
	def in_range(lower, upper, num):
		#TODO: implement this!
		return False

We will write code that will return `True` or `False` depending on whether the number supplied in the parameter, `num` is between `lower` and `upper`, inclusive.

	in_range(1,3,2) -> True
	in_range(-2,80,80) -> True
	in_range(-3,5,6) -> False
	

### Even Elements

For this function:

	#takes in a list of numbers and returns a list of only the even ones
	def even_elements(nums):
		#TODO: implement this!
		return []
		
We will write code that will take in a list of numbers, supplied in `nums`, then return a list containing only the even numbers in nums in the same order.

	even_elements([1,2,5,7,2,6,7,9]) -> [2,2,6]
	even_elements([-8,2,4]) -> [-8,2,4]
	even_elements([1,3,5,7]) -> []
	

### Most Common Letter

For this function: 

	#takes in a string and returns the most common letter occuring in the string - if there's a tie, you may return any of them
	def most_common_letter(str):
		#TODO: implement this!
		return 'a'
		
We will write code that will return the most common occuring letter in the parameter, `str`. If there is a tie, you can return any of the top occuring letters.

	most_common_letter("abcb") -> 'b'
	most_common_letter("popular") -> 'p'
	most_common_letter("andskfjngrkejnhkjjfjfjnfnkzzjj") -> 'j'
	
> **Hint:** think about how a dictionary could be useful here. Also, you can iterate through letters in a string in Python like this:
 
 	#will print each individual in the string, word
	for letter in word:
		print letter
		

### Maximum Difference

For this function:

	#takes in a list of numbers and returns the maximum difference between any two numbers in the list
	def max_diff(nums):
		#TODO: implement this!
		return -1
		
In this function, we will write code that will return the maximum difference between any two numbers in the list of number, `nums`. You can assume that everything in the list, `nums` is a number and that there are at least 2 numbers in list.

	max_diff([1,4,-9,2,3,20]) -> 29
	max_diff([1,3,5]) -> 4
	max_diff([-2,0]) -> 2
	
> **Hint**: to get positive and negative infinity, you can use float("inf") or -float("inf")


### Hourglass

For this function:

	#prints an hourglass made out of '*' characters with a base the size of the size supplied * 2
	def hourglass(size):
		#TODO: implement this!
		print "not implemented"

Write a function that prints an hourglass shape of a given size `size` (i.e. the base of the hourglass has `2 * size` stars).
	
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
	
**Hint:** In Python, you can multiply strings! For example, the code: 

	"a" * 7
	
would result in:

	"aaaaaaa"
	
You can also add strings like this:
	
	"aaa" + "3" * 2
	
which would result in

	"aaa33"

### Max Ascending Sublist Size

For this function:

	#returns the size of the maximum increasing sublist in the list of numbers supplied in the variable, nums
	def max_ascending_sublist_size(nums):
		#TODO: implement this!
		return -1
		
Write a function that takes an list of integers and returns the size of the largest ascending sublist. An ascending sublist is one where each element is greater than the previous number in the list. For example, for the list `[1, 5, 9, 9, 8, 7]`, `[1, 5, 9]` is an ascending sublist, but `[9, 9]` (not strictly greater), `[9, 8, 7]` (descending), and `[1, 5, 8]` (not consecutive) are not. 

	max_ascending([5, 10, 15, 20]) --> 4
	max_ascending([1, 3, 2, 4, 5, 6, 1]) --> 3
	max_ascending([4, 3, 2, 1]) --> 1
	
> This one is definitely the hardest of the lesson, so don't get discouraged if it takes a while.
