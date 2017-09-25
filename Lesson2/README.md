# Lesson 2:

**By the end of this lesson, students will**:

* Have an understanding of variables, functions, and control flow statements in Python and how they work in Python as opposed to other languages.
* Be able to construct basic programs in Python and run them.

Before I start this lesson, let me make sure you know that as I write this lesson, I'm assuming that you have already done a fair share of basic programming. This means that I may go through a couple of concepts fairly quickly without slowing down to explain them.  

## Some Python Basics

Before we start doing any coding, I want you to look at the following block of Python code:

	a = 0
	while a < 20:
		a = a + 2
		if a == 12:
			print "I'm skipping this number because I don't like it."
		else:
			print a

You might have seen this code already if you were reading the course requirements of this class, but let's take a closer look at it. Now, if you've programmed a decent amount before, you should be able to have a rough idea of what the code is doing and what it will print out. Feel free to paste all this code into the helloworld.py file from the last lesson and run the file again in the terminal (using `python helloworld.py`) to see for sure what prints from it.  

Now, even though you might have been able to tell what was going to print out, you might have also noticed that there are some weird differences between this code and other languages you may have used in the past. 

Let's look at a couple of them.

### Variables

If you've coded in most other languages besides python, this line probably looks pretty weird to you.

	a = 0
	
No, this isn't the middle of the program where `a` has already been defined earlier. This is actually just how you define variables in Python. Shouldn't it look something like this?:

	int a = 0
	
You might ask. Well, yes, if we're using Java or most other languages, but Python is what people call **dynamically typed**. Pretty much, this means that Python is able to figure out what type of variable each variable is you ever having to say so in the code. In fact, if I wanted to, I could even do something like this:

	a = 0
	a = "yolo swag"
	a = False

*and the code would still work*. Pretty cool, huh?

### Control Flow

> If you haven't heard the term, "control flow" before, it's pretty much a general term for understanding while loops, if/else statements, for loops, and how they all fit together to determine the order that the code will run in.
 
#### Conditionals

Looking at these lines of code:

	while a < 20:
	...
		if a == 12:
	
You'll probably notice something very quickly. *No parentheses!* Yes, in Python, we don't need parentheses for our if or while loops. We just need the **condition** (the part of the statement that's either true or false) and a colon.

#### Indentation

The other thing you might notice is the lack of brackets for our while, if, and else statements. If you've used other languages, you'd probably be used to seeing something more like this:

	a = 0
	while a < 20:{
		a = a + 2
		if a == 12:{
			print "I'm skipping this number because I don't like it."
		} else: {
			print a
		}
	}
	
> (this code doesn't work, by the way).
 
The reason for the lack of brackets is that **Python relies on indentation instead of brackets** to figure out what code belongs to which statement.  

For example, 

	a = 0
	while a < 20:
	
the above lines of code are not indented at all because they are not inside of any statements. On the other hand, these lines:

		a = a + 2
		if a == 12:
		
are indented once since they are inside of the while loop, but not any other statements. Since they are inside of **1** statement, they are indented **1** time. On the other hand, this line of code:

			print "I'm skipping this number because I don't like it."

is indented **2** times since it is inside both the while loop and if statement. The extra indentation kind of serves as a replacement for the opening bracket that would have come after the if statement. Likewise, the following line:

		else:

is indented only **1** time, meaning that it is only inside the while loop, not the if statement, and it, in a similar way, serves as a replacement for the closing bracket that would have come before the else statement. **Therefore, it signifies the end of the if statement**.

The next line:

			print a

if you haven't guessed already, is indented 2 times since it is inside both the while loop and the else statement.

#### For Loops

I saved introducing for loops until now since they're much different than for loops in other languages. Here's an example of code you can try running:

	for i in range(10):
		print i
		
Now this looks a fair bit different from for loops in most other languages. Here's the Java equivalent of the above statement:

	for(int i = 0; i < 10; i++){
		System.out.println(i);
	}
	
When you run the code, you'll see that, like the Java code above, it will print the numbers 0-9. This is because the `range(10)` function defines that the for loop will go up to **but not including** the number 10, running pretty much the same way a regular for loop runs.

### Readability

One of the biggest differences in Python compared to other languages is its *readability* - pretty much, it looks more similar to English than any other coding language out there. Even looking at the above code for the for a Python for loop versus a Java one, you can tell that someone who has never coded before would be much more likely to understand the Python one. That was very intentional and a big reason why Python is growing so much. It's also a big reason why we're using it in this class.