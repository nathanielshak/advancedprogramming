# Lesson 7: An Introduction to Sorting

**To start this lesson, students should:**

**By completing this lesson, students will:**

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

Now, we're going to try our hand at implementing this algorithm. Go ahead and open up sublime and a write functinon like this


	def selection_sort(nums):
		...
		return nums
		
That takes in an unsorted list of numbers, `nums`, and returns it sorted.

Feel free to run that code to confirm that it works. Make sure to spend some time thinking out the algorithm and really understanding it before you write the code.

### Big O

You already know what I'm going to ask next. **What's the Big O runtime of this?** Take some time and come up with your best answer. Once you think you have something, you can click [here](selectionbigo.md) to see if you were right. 

## Bucket Sort

Next, we're going to learn about a sorting algorithms that *could actually use* Selection Sort as part of it. However, in general, it will run much faster, especially with large input sizes.

[Here](https://mathspace.co/learn/world-of-maths/coding-and-algorithms/sorting-algorithms-58142/sorting-algorithms-2104/) is a detailed description of bucket sort (you'll have to scroll down a bit until you hit bucket sort). Feel free to check out some of the other sorting algorithms while you're there!

> When the page says: "Use the **insertion sort** algorithm to sort elements in bins that have multiple elements", you could actually use any sorting algorithm, including **selection sort**!

And [here](https://www.youtube.com/watch?v=VuXbEb5ywrU) is a video that demonstrates one example of how bucket sort could work.

> When the video says "Now sort each bucket individually using **insertion sort**", once again, you could use any sorting algorithm. 
 
### Big O

This one is a bit less straightforward to figure out. This is because the Big O runtime depends on what sorting algorithm we use for each bucket. 

For the sake of this example, see if you can figure out what the Big O runtime would be if we used **selection sort** on each bucket.

Once you think you have a good guess, click [here](bucketbigo.md) to see if you were right.


 