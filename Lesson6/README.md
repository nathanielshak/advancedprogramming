# Lesson 6: Searching and an Introduction to Algorithmic Analysis

**To start this lesson, students should:**

* Understand lists in Python
* Be able to analyze code effectively
* Have a grasp on algebra level math

**By completing this lesson, students will:**

* Become familiar with the linear and binary search algorithms
* Gain an understanding of the concept of algorithmic efficiency
* Become familiar with Big O runtime analysis

## Searching through a phone book

Imagine you're trying to find someone's name in a phone book. For the sake of this example, let's imagine that there's no table of contents showing the page number of each letter section. Also for the sake of this example, let's pretend that we have no idea the numerical distribution of the starting letter of names are across the phone book - for all we know, there might be no names starting with the letters "A-P", making the first name in the phone book start with the letter "Q" or every name in the phone book might start with the letter "A". Who knows? All we know is that the names are sorted in alphabetical order.

There are a couple strategies we could use here.

### Linear Search

The most straightforward way to do this would be to start at the very beginning of the phone book, then flip page by page until you find the name. It's guaranteed to work - you know you'll find it *eventually*. It's just that it might take a very long time, especially if the name you're looking for happens to be near the end.

If drew a metaphor between this and coding, we could say the phone book is equivalent to a list of sorted numbers, and we're trying to find the index of the list a certain number is at. The code equivalent of looking through every page in the phone book until we found what we were looking for would be something like this:

    def linear_search(phonebook, desired_name):
        for page in range(len(phoneboook)):
            if phonebook[page] is desired_name:
                return page

That seems pretty simple. It's an elegant solution that really doesn't take that much code. This solution is actually a well-known algorithm called **linear search**.

However, let's imagine the phone book is a thousand pages. What about ten thousand pages? A million pages, even? How many pages are we going to end up going through? The only thing we can say for sure is that, *at worst*, we'd go through all the pages in the phone book. Now, we still know we'll find the name for sure, but **can we do better?**

### Binary Search

One thing that **linear search** never took advantage of was the fact that our phone book had all the names sorted. How could we take advantage of this information to speed up our search?

Well, for one, what if we started from the very middle of the phone book? If we got there and the names on that page were later (alphabetically) than our desired name, we could ignore the half of the phone book after the middle and repeat the process with the first half of the phone book. Now let's look at the middle of the first half of the phone book. If the names on that page are earlier (alphabetically) than the name we're looking for, we can ignore the top quarter of the phone book, and look only at the second quarter of the book. In fact, if we repeat this process over and over, we'll eventually get to our desired name likely much faster than we would have if we went page by page.

> [Click here to see a video demonstrating this.](https://www.youtube.com/watch?v=o2LqhHoAXxI)

How fast will we get there? In linear search, we knew that *at worst* we'd have to check every page. In binary search, we know that every time we check a page, we divide the number of possible pages the name could be on in half. That means, in the worst case, the number of pages we'd have to check would be how many times we'd have to divide the original number of pages in two before reaching one. Mathematically speaking, that would be: log<sub>2</sub>(N) where N is the number of pages in the phone book.

While it might be hard to see how much a difference this makes at first, for large numbers of pages, this makes a **huge** difference.

Here's a table to show us the difference in how many pages each algorithm would have to check at most:

|Pages        |Linear       |Binary|
|-------------|-------------|------|
|10           |10           |3     |
|100          |100          |7     |
|1000         |1000         |10    |
|1,000,000    |1,000,000    |20    |
|1,000,000,000|1,000,000,000|30    |

Wow, that's a big difference, and it shows an important concept in programming. Even if something works, *there could always be a way to do it better*.

### Let's code it up

Open up exercises.py and you'll see the following code:

    # Searches linearly through a sorted list of numbers (nums) for a number
    # (target) and returns whether or not the list contains the number.
    def linear_search(nums, target):
        for num in nums:
            if num == target:
                return True
        return False

    # Uses binary search to look through a sorted list of numbers (nums) for a
    # number (target) and returns whether or not the list contains the number.
    def binary_search(nums, target):
        # TODO: implement this!
        return False

We've already implemented linear search for you in the first function. In this case, we want to check *whether or not* a number exists in a sorted list, then return `True` or `False` depending on if it is or not. Your job is to implement the binary search portion based on what we described above.

Here is a diagram of what binary search would look like on a list of sorted numbers if you were looking for the number 76.

![](bsearch.jpg)

> The arrow represents which number you're checking at any given point and comparing to the number you're looking for before choosing which half to look into.

## Algorithmic Analysis

Through all of this, there's something that is hopefully becoming clear: **regardless of if the code works, some code will be inherently faster than other code that does the same thing depending on your approach**. In this section, we're going to talk about **algorithmic analysis**, the way you can formalize and measure the **efficiency** of one coding approach versus another.

To start with, let's take a look at one of the exercises we did in the last lesson. Do you remember the max difference question from [lesson 4](../Lesson4)? Just a as refresher, we were supposed to write a function that will return the maximum difference between any two numbers in the list of numbers `nums`. We assumed that everything in the list `nums` is a number and that there are at least 2 numbers in the list.

Here's one potential solution to that problem:

    def max_diff(nums):
        cur_max_diff = 0
        for num1 in nums:
            for num2 in nums:
                diff = abs(num1 - num2)
                if diff > cur_max_diff:
                    cur_max_diff = diff
        return cur_max_diff

### What's going on in this code? 

For every number in the array, we're checking the difference between that number and all the other numbers in the array and saving the greatest difference we see. You can copy the code and test it yourself if you're curious.

### How much work does this take?

It depends on how many numbers are in the list, `nums`. Every number in `nums` is checked against all the numbers in nums, so if there are 3 numbers in `nums`, that will be 3\*3=9 checks. If there are 20 numbers, there will be 20\*20=400 checks. As a general rule, it seems like we can safely say that there will be n<sup>2</sup> checks, where n is the length of the `nums` list.

### A Different Approach

Okay, now let's look at a different way we could have solved this problem.

    def max_diff(nums):
        cur_min = nums[0]
        cur_max = nums[0]
        for num in nums:
            if num > cur_max:
                cur_max = num
            if num < cur_min:
                cur_min = num
        return cur_max - cur_min

Depending on how you approached the problem from lesson 4, your code for `max_diff` could have either looked more like this or like the previous solution. *Both of these solutions work*. Feel free to copy this code and test it if you want.

### What's going on in this code?

In this solution, we keep track of the minimum and the maximum number in the list as we loop through every number stored in the list. After checking every number, we return the difference between the maximum and the minimum number as the max difference.

### How is this code different?

At first glance, this code might not look too different. It's just a slightly different way of solving the same problem. However, the biggest difference is in **how much work the code does**. 

In the previous solution, we came to the conclusion that the algorithm did n<sup>2</sup> checks of the list, where n is the number of elements in the list. How many checks does this algorithm do?

If we look at it carefully, there is only one loop through the list, therefore, **each element in the list is only checked once**. This means that, compared to the **n<sup>2</sup>** checks the first algorithm does, this algorithm only does **n** checks.

Now we can see that even though both of these algorithms work, the second one is objectively better because **it is always more efficent**.

## Big O

There's a way of measuring **algorithmic efficiency**, as we were talking about it above. The way we do that is through something called **Big O Notation**. This is essentially a way to measure how much work an algorithm does **in the worst case relative to its input size**, which we denote as **n**.

The Big O runtime of our first `max_diff` algorithm above is written like:

O(n<sup>2</sup>)

While the Big O runtime of the second `max_diff` algorithm above is written like:

O(n)

That seems easy enough, but there are some nuances we need to be aware of. What if we modified the first `max_diff` algorithm to look like this?

    def max_diff(nums):
        for i in range(1000):
            print("hi.")
        cur_max_diff = 0
        for num1 in nums:
            for num2 in nums:
                diff = abs(num1 - num2)
                if diff > cur_max_diff:
                    cur_max_diff = diff
        return cur_max_diff

How does this make the code different? All that really changes is that whenever you run the code, now it will annoyingly print out "hi" 1000 times before calculating the max difference in the array. Even though this doesn't affect whether or not we get the right answer, it obviously adds to how much work the code does. So, does that mean the Big O notation would now look like this?

O(n<sup>2</sup> + 1000)

That seems logical. In addition to the n<sup>2</sup> checks on the list, we also have to do the work of printing "hi." 1000 times. However, in Big O notation, we're only concerned with runtime with regards to the input, so we can ignore constants - therefore, the Big O runtime would still be:

O(n<sup>2</sup>)

What if the code looked like this?

    def max_diff(nums):
        for i in nums:
            print(i)
        cur_max_diff = 0
        for num1 in nums:
            for num2 in nums:
                diff = abs(num1 - num2)
                if diff > cur_max_diff:
                    cur_max_diff = diff
        return cur_max_diff

Now you might be wondering if the Big O runtime looks like this:

O(n<sup>2</sup> + n)

since we loop through the array an additional time in the beginning, adding **n** extra checks. In actuality, it would still be this:

O(n<sup>2</sup>)

When using Big O notation, we're only concerned with the biggest terms and can ignore smaller ones. Another example - what if we modified the code from the second `max_diff` algorithm to look like this?

    def max_diff(nums):
        cur_min = nums[0]
        cur_max = nums[0]
        for num in nums:
            print(num)
        for num in nums:
            if num > cur_max:
                cur_max = num
            if num < cur_min:
                cur_min = num
        return cur_max - cur_min
        
Now, we loop through the array twice. Would the Big O notation now be

O(2n)?

Actually, it would still be

O(n).

Another rule of Big O notation is that we ignore constant factors.

We'll talk more about Big O notation in the future, but as an exercise, see if you can figure out what the Big O runtime of binary and linear search are. Check with a mentor to see if you're right! Feel free to read up more about Big O [here](https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/) too.

See you in [lesson 7](../Lesson7)!
