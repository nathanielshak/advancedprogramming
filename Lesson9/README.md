# Lesson 9: What's Recursion?

**To start this lesson, students should**:


**By completing this lesson, students will**:

## Zombies and Cats

To start with, I'm going to direct you to [this page](https://inventwithpython.com/blog/2011/08/11/recursion-explained-with-the-flood-fill-algorithm-and-zombies-and-cats/), which has a great illustration of recursion using zombies and cats. Read up to the **"The Basics: Recursive Calls and Base Cases"** part, then **come back here**. (Feel free to read further if you're curious, but we may end up double explaining some parts.)

## Alright...so what's recursion?

![](https://inventwithpython.com/blogstatic/floodfill/zombie1.gif)

Cool, so we just got...a weird example involving zombies and cats that somehow has to do with recursion. *How?*, you might ask? We'll get to that in a bit, but first, let's define some things.

### What is recursion?

Simply put, recursion is when a **function calls itself**. One example they gave later on the website was:

	def foo():
		foo()
		
**So what does this do?** 

Feel free to copy this code and try running it to see what happens. If you read further in the earlier link or tried that, you should know that you'll get something that says something like:

	RuntimeError: maximum recursion depth exceeded
	
Which pretty much means we got in an **infinite loop** and the `foo` function never stopped calling itself, causing the error you saw.

> An [infinite loop](https://en.wikipedia.org/wiki/Infinite_loop) is a common thing in computer science where you program ends up hypothetically getting stuck where it will run **forever** if we don't stop it. Normally, this will either cause a crash or we'll have to exit out of the program when this happens.
 
What do you think would happen if we did something like this?

	 def foo():
	 	print "hi." 
	 	foo()
	 	
If you guessed that it would print out "hi" forever, you're right. If you try running this code, you'll actually get this bug again:

	RuntimeError: maximum recursion depth exceeded

> If you can't see the "hi's", they're there - you just have to scroll up a while because the error message will have a long trail of listing what function it crashed in, which in this case involves calls of the same function.

That's because the program crashes from the infinite loop after printing "hi" many times.

Okay, howabout this one?

	def count(num):
		print num
		count(num + 1)
		
Similar story here. It prints out numbers starting from wherever you started, then going up and up until it crashes.

## Getting unstuck.

About now, you might be wondering how recursion is useful if all we'll ever do is get stuck in an infinite loop. That's where the **base case** comes in.

To illustrate this let's think back to the cat from the zombie example:

![](cat_transparent.png)

If there were no cats and infinite humans, what would happen? Zombies would keep spreading forever.

**The base case is condition that causes the function to stop making recursive calls**.

To illustrate this, let's look at some more examples:

	def count_to_100(num):
		if num > 100:
			print "all done!"
		else:
			print num
			count_to_100(num + 1)
			
This code is actually very similar to the last snippet we looked at. the main difference is the fact that we have a **base case**. If you run the code like this:

	count_to_100(1)
	
If you didn't already guess, we'd get an output like this:

	1
	2
	3
	4
	5
	6
	7
	8
	9
	10
	
	...
	
	90
	91
	92
	93
	94
	95
	96
	97
	98
	99
	100
	all done!

In this case, that base case is `num` being greater than 100, which is what allows the code to stop once it hits 100 instead of getting stuck in another infinite loop.

If we think back to the zombie example, we could see `num` being greater than 100 as an infected zombie running into cat, while any `num` being anything less 100 is like an infected zombie running into another uninfected human instead.

## Let's try it.

Let's try a similar version of this. Go ahead and find this function in exercises.py.
	
	#recursively count down from num to 0
	def count_down(num):
		#TODO: implement this!
		pass
		
Here, we're going to want to write a recursive function to count down from whatever number we supply down to 1, then print: "all done!"

For example:

	count_down(10)
	
should output:

	10
	9
	8
	7
	6
	5
	4
	3
	2
	1
	we done!

and
	
	count_down(4)

should output

	4
	3
	2
	1
	we done!
	
**I know it's really easy to do this using a while loop or for loop**. For the sake of this problem, see if you can do it with recursion.

> Hint: the code will be actually pretty similar to the previous coding problem we showed.

## We have to go deeper.

![](lego.gif)

After all of this, you might still be wondering why recursion is actually useful. Broadly speaking, recursion is a powerful tool for us to use whenever problems are structured where each level of the problem can be broken into a smaller version of the original problem.

That might be a bit confusing on first listen. 

To illustrate this, let's think of if we wanted to find the sum of the sequence of numbers counting up to 10.

So:

	sum_to_10(5) = 5 + 6 + 7 + 8 + 9 + 10 = 45
	
or

	sum_to_10(6) = 6 + 7 + 8 + 9 + 10 = 40
	
or

	sum_to_10(10) = 10
	
If we looked at this, we could see a pattern emerging where:

	sum_to_10(5) = 5 + sum_to_10(6)
	
or in general:

	sum_to_10(n) = n + sum_to_10(n + 1)
	
Here, we can see the repeating pattern of each step of this equation having another smaller version of the same equation inside of it.

If we were to code this up using recursion, it would look something like this:

	def sum_to_10(num):
		if num is 10:
			return 10
		else:
			return num + sum_to_10(num + 1)
			
It might be a bit confusing how this is working on first glance.
