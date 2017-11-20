# Lesson 9: What's Recursion?

**To start this lesson, students should**:

* Have experience coding solutions to complex problems.
* Have a clear understanding of functions and control flow.
* Be familiar with 2D arrays/lists.

**By completing this lesson, students will**:

* Understand what recursion is.
* Gain some experience writing recursive functions.

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
	
	#recursively count down from num to 1
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
			
It might be a bit confusing how this is working on first glance. Try sketching out each function call if you're confused and go through it with a mentor until you have a good grasp on that.

## Factorials

Once you've done that, we're going to try to code another similar problem. If you've heard of factorials in math before, this is the way they work:

	5! = 5*4*3*2*1 = 120
	
or
	
	4! = 4*3*2*1 = 24
	
or 

	0! = 1! = 1
	
You might notice some similarities to the previous problem (hint hint). Go ahead and find this part of the code in `exercises.py`:

	#recursively compute a factorial
	def factorial(num):
		#TODO: implement this!
		return -1
		
and implement the **recursive** version of factorial. 

> Once again, I know this could be done with a for loop or a while loop, but for the sake of this exercises, let's do it with recursion.
> 
> **Hint**: similar to the previous problem, notice that factorial(n) = n * factorial(n-1)

## Back to the Zombies

About now you might still not be convinced that recursion is useful. The main reason being that every problem we've solved so far could've been solved **more easily** without even using recursion in the first place.

For example, we could have easily done this for count_down:

	def count_down(num):
		cur_num = num
		while cur_num > 0:
			print cur_num
			cur_num -= 1
		print "all done!

Or this for factorial:

	def factorial(num):
		result = 1
		for i in range(1, num + 1):
			result *= i
		return result

> range(1, num + 1) will go from 1 to num
 
If you thought that both of these solutions would have run just as quickly as the recursive solutions, and they would've been less confusing to code, you would've been right! The main purpose of us coding them recursively was just as a learning exercise.

But that begs the question, *when is recursion actually useful?*

### Zombie Algorithm with Recursion

Rather than try to answer that question with just an explanation, I'll try to give an example.

Let's go back to that zombie example we opened with. 

![](https://inventwithpython.com/blogstatic/floodfill/zombie1.gif)

And this time, let's imagine what the code would look like if we were to simulate this happening **using code**.

> As a warning, this part is pretty tricky, but very important - so do take the time to go through it with a mentor if possible until you really understand it.

Firstly, how would we represent the problem in the first place? How would we keep track of what spaces have zombies, humans, or cats? 

The easiest way would probably be a **2 Dimensional Array**. In other words, a **list of lists**. This means to access the top left person (that eventually turns into a zombie) in the above picture, we could do:

	world[0][0]
	
Where `world` is our 2D array that holds all the humans, zombies, and cats.

Likewise, to get the topmost left cat, we would do:

	world[2][1]
	
Just to make this example easier, let's pretend turning one of these spaces into a zombie could be done simply by saying:

	word[6][6] = ZOMBIE
	
Okay, so given that what would the code look like for this?

I guess there could be some conceivable way to use while loops and for loops in an **iterative** way to keep on checking if humans exist next to zombies and turning those humans into zombies, but recursion actually makes this much easier.

### The base case

To figure out what the recursive solution would look like, first, think: what is our base case? In other words, at what points does the recursion (in this case, the recursion being more humans turning into zombies) stop?

The answer to this would be when you run into another zombie (it's already a zombie) or when you run into a cat.

If we know this, then we can start our recursive function like this:

	def zombie_bite(x, y):
		if world[x][y] is ZOMBIE or world[x][y] is CAT:
			return
			
> Here we're assuming that x and y are the coordinates of the being that was just bitten.
 
### Turning the human into a zombie
 
Okay, what next?

Firstly, we know that if it reaches the next point in the code, it's a human, so we know that human will turn into a zombies since it just got bitten.

	def zombie_bite(x, y):
		if world[x][y] is ZOMBIE or world[x][y] is CAT:
			return
		world[x][y] = ZOMBIE
		
### Recursive zombie bites
		
Now, the hard part. How do we code in the recursion? How do we make sure that the zombies spread as far as they should?

Well, we know that the code we just wrote here will should run the same for any other creature that got bitten, right?

What would happen if I did this?

	def zombie_bite(x, y):
		if world[x][y] is ZOMBIE or world[x][y] is CAT:
			return
		world[x][y] = ZOMBIE
		zombie_bite(x, y + 1)
		
Try to take some time to think this out before reading on.

This would cause the zombie outbreak to spread vertically downwards from the original zombie until we reached another existing zombie or a cat.

This is because each time a human was turned into a zombie, a recursive call would be made, calling `zombie_bite` on the human below, and repeating until we reached another zombie or a cat.

> If you're not sure why this is, take some time to sketch it out and talk it over with a mentor until you get it - this part is really important to get before moving on.
 
But the zombies need to be spreading in other directions too, right? - not just down.

### Multidirectional zombie bites

You're right - what would happen if we modified the code to do this?

 	def zombie_bite(x, y):
		if world[x][y] is ZOMBIE or world[x][y] is CAT:
			return
		world[x][y] = ZOMBIE
		zombie_bite(x, y + 1)
		zombie_bite(x + 1, y)

Again, talk it over with a mentor until you understand what's going on here. 

### You try!

Once you get that, I'll let you go ahead and try to complete the rest of the missing code. **Hint:** we need two more lines similar to the ones we just wrote.

> For now, don't worry about going out of bounds on the `world` 2d array. We can pretend the code automatically stops when it goes off the end of the world.

Once, you get that and check it with a mentor, congrats! You made it! We've just successfully coded a full zombie outbreak :)

![](zombierabits.gif)

If you still don't feel like you understand recursion well, it's okay. We'll have plenty of time to practice in [Lesson 10](../Lesson10).