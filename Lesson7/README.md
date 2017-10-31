# Lesson 7: An Introduction to Sorting

**To start this lesson, students should:**

* Have a familiarity and basic understanding of Big O analysis.
* Understand lists in Python.
* Have a decent amount amount of experience analyzing and coding semi-complex algoirthms.

**By completing this lesson, students will:**

* Get practice implementing complex algorithms to solve coding problems.
* Be introduced to sorting algorithms, the variety of concerns that may come into play when choosing one.
* Gain a greater understanding of Big O analysis and the nuances of where it might not explain everything.
* Get introduced the concept of Space vs Time complexity.
* Get practice reading documentation.

## What is sorting?

Go ahead and take a look at this video:

[![Watch the video](youtube.png)](https://www.youtube.com/watch?v=kPRA0W1kECg)

Okay, *what was that?* What that was, was a bunch of different **sorting algorithms**.

#### What are sorting algorithms?

Sorting is one of the most classic problems in computer science. What is the best way to take an array, or list in our case, of unsorted numbers and rearrange them into sorted order? Each different way to solve this problem, we call a **sorting algorithm**.

There are at least 20 sorting algorithms I've heard of before, and probably hundreds in existance. Here we will introduce a couple of them, look at their advantages and disadvantages, and try to code some of them up.

Since there is a ton of explanations and research already out there around sorting algorithms, this lesson will involve a lot of us linking you to other pages that describe these. This lesson would be especially helpful to go through with a mentor if you're having trouble grasping any of the concepts. Some of these can be difficult to understand on the first read.

## Selection Sort

For an explanation of selection sort, go [here](https://www.tutorialspoint.com/data_structures_algorithms/selection_sort_algorithm.htm).

To see a video demonstration of it, go [here](https://www.youtube.com/watch?v=92BfuxHn2XE).

### Code it up!

Now, we're going to try our hand at implementing this algorithm. We've provided some starter code in `exercises.py`. Open this up and find this function:

	#sorts the nums array using selection sort
	def selection_sort(nums):
		result = nums[:]
		#TODO: write the code to sort the result array!
		return result
		
Here, we want to write a function that takes in an unsorted list of numbers, `nums`, and returns a sorted version of it using selection sort as the `result` array.

Feel free to run that code to confirm that it works. We've written a quick test that will print out the results of your algorithm on a random array - if this comes out sorted, your code works! 

Make sure to spend some time thinking out the algorithm and really understanding it before you write the code.

### Big O

You already know what I'm going to ask next. **What's the Big O runtime of this?** Take some time and come up with your best answer. Once you think you have something, you can click [here](selectionbigo.md) to see if you were right. 

## Bucket Sort

Next, we're going to learn about a sorting algorithm you can actually combine with Selection Sort. However, in general, it will run much faster, especially with large input sizes.

[Here](https://mathspace.co/learn/world-of-maths/coding-and-algorithms/sorting-algorithms-58142/sorting-algorithms-2104/) is a detailed description of bucket sort (you'll have to scroll down a bit until you hit bucket sort + potentially have to sign up). Feel free to check out some of the other sorting algorithms while you're there!

> When the page says: "Use the **insertion sort** algorithm to sort elements in bins that have multiple elements", you could actually use any sorting algorithm, including **selection sort**!

And [here](https://www.youtube.com/watch?v=VuXbEb5ywrU) is a video that demonstrates one example of how bucket sort could work.

> When the video says "Now sort each bucket individually using **insertion sort**", once again, you could use any sorting algorithm, such as Selection Sort.
 
### Big O

This one is a bit less straightforward to figure out. This is because the Big O runtime depends on what sorting algorithm we use for each bucket. 

For the sake of this example, see if you can figure out what the Big O runtime would be if we used **selection sort** on each bucket.

Once you think you have a good guess, click [here](bucketbigo.md) to see if you were right.

### Code it up!

Once you have a good understanding of how bucket sort works, let's code it up! Now, this one might be a bit tricky since there's many different steps. To help, we've already written some code to get you started:

	BUCKET_NUM = 10
	
	#sorts the nums array using bucket sort with selection sort. The number of buckets is declared in BUCKET_NUM.
	def bucket_sort(nums):
		#initializes a list of lists - each of these lists are a bucket!
		buckets = [[] for i in range(BUCKET_NUM)]
	
		#TODO: put the numbers each into their respective buckets
		for num in nums:
			pass
	
		#TODO: sort each bucket using the selection_sort function you wrote earlier
		for bucket in buckets:
			pass
	
		#TODO: put all the sorted buckets together into the results list
		result = []
		for bucket in buckets:
			pass
	
		return result

Okay, there's a lot of pieces to this. Before we get started, you should know we've put some constraints on our sorting algorithm. Importantly:

#### You will only be sorting numbers within the range of 0-99 using 10 buckets.

If you look at the first part of the code:

	buckets = [[] for i in range(BUCKET_NUM)]
	
Here, we already have set up the buckets for you. This is in the form of a list of 10 empty lists.

### Part 1: dividing numbers into buckets:

Our first step of the algorithm, we will write here:

	#TODO: put the numbers each into their respective buckets
	for num in nums:
		pass

Here, we will write code that puts each of the numbers in the nums array into one of the lists in `buckets`. 

Since we know that we have 10 buckets and the numbers go from 0-99, like the example on the [mathspace page](https://mathspace.co/learn/world-of-maths/coding-and-algorithms/sorting-algorithms-58142/sorting-algorithms-2104/), we know that we can partition the buckets as follows:

buckets[0] will have 0-9

buckets[1] will have 10-19

bucket[2] will have 20-29

and so on.

> Hint: the [python append](https://docs.python.org/2/tutorial/datastructures.html) function might be helpful here.
> 
> Also, it might be helpful to know that dividing in Python always rounds down. EX: 9/10 will be 0 and 21/10 will be 2.
 
### Part 2: sorting the buckets using selection sort

In the next part of the code:

	#TODO: sort each bucket using the selection_sort function you wrote earlier
	for bucket in buckets:
		pass
		
We want to go through each bucket in our `buckets` array and sort it using the `selection_sort` algorithm we wrote earlier. 

These should be in the same file, so you've already done most of the work! Just go through each bucket in the array and call the `selection_sort` function on it.

### Part 3: putting together the sorted arrays

In the last part of the code:

	#TODO: put all the sorted buckets together into the results list
	result = []
	for bucket in buckets:
		pass
	
	return result
	
We want to put together all the sorted arrays in `buckets` into our results array, then return in.

> Hint: [this](https://stackoverflow.com/questions/8177079/python-take-the-content-of-a-list-and-append-it-to-another-list) stack overflow post might be helpful if you're trying to figure out how to add lists together.
 
Once you're done with that, go ahead and run the code. The tests we've written should print out a sorted array if your code works. 

If you want to experiement, you can try comparing how fast selection_sort and bucket_sort take on the same random list. If you increase the number of elements in the list to about 10,000, you might start to notice a difference.

On to [lesson 8](../Lesson8)!



 