# Lesson 12: Exceptions

**To start this lesson, students should**:

* Understand common control flow patterns like if/else blocks, while loops, and for loops.
* Have some experience writing and using classes.

**By completing this lesson, students will**:

* Learn what exceptions are.
* Learn when to use exceptions, and how to structure code around them.

## Dealing with errors

Imagine you were dealing with this code:

    def some_calculation(x, y, z):
        print 'doing some calculations...'
        ret = (x + y) / z
        print 'done with some calculations!'
        return ret

    def do_something(x, y, z):
        print 'doing something...'
        ret = some_calculation(z, y, x)
        print 'done with something!'
        return ret

    def another_function(x, y):
        print 'running another function...'
        ret = do_something(x, y, y)
        print 'done runnning another function!'
        return ret

We already know that we can't divide by zero - there's no reasonable value that could come out of that division, so the program will crash. So we have to avoid calling `some_calculation` when `z` is zero. But we might call these functions in lots of different places - how can we make sure we avoid crashing?

One way could be to always check if `z` is zero before calling `some_calculation`. But we'd have to repeat the same code in a lot of places, since we would have to manually check if `z` was zero every time we called `some_calculation`! In addition, we have to check `x` when we call `do_something` or `another_function`, and our code will get ugly really quickly since we're checking for zeroes all over the place.

In some languages, like C, this is what you're supposed to do. But Python provides a better way to handle potential errors: using **exceptions**.

## Exceptions

You're already familiar with if/else blocks, while loops, and for loops, and how each of them makes the program run in a different way. **Exceptions** are another way to change how the program runs: they allow you to *interrupt* the program when an error occurs, and *handle* it somewhere else.

In this example, the basic idea is that you *don't check if `z` is zero*, you just *assume it's not and proceed anyway*. If `z` is zero, then `some_calculation` raises an **exception**, and the rest of the code doesn't run.

When an exception is raised, Python will *skip the rest of the code* until an appropriate `except` block is found. Maybe this is best illustrated by example... we can write code like this:

    try:
        print 'about to divide y by z...'
        ret = y / z
        print 'y / z is', ret
    except ZeroDivisionError:
        print 'could not divide because z was zero'
    print 'all done!'

What exactly are we saying here? Let's break it down.

We put code that we think might raise an exception in the `try` block. In this case, the `y / z` line is the important part.

The second part, `except ZeroDivisionError`, specifies a *type of exception* that we think might happen during the `try` block. If that exception does happen at any point during the `try` block, then Python stops running the code in the `try` block, and it starts running the code in the `except` block immediately. If Python reaches the end of the `try` block and there were no exceptions, then it *skips the `except` block* and continues running the code after it.

If you run the code above when `z` is not zero, then the code in the `except` block will never run. The example code will print something like this:

    about to divide x by y...
    x / y is 3
    all done!

But if you run it when `z` is zero, then the `y / z` line will raise an exception, so the `try` block will stop running at that point and the `except` block will run instead. The example code will print this:

    about to divide x by y...
    could not divide because y was zero
    all done!

We skipped the second print statement in the `try` block, because the line right before it raised a ZeroDivisionError exception, and went right away to the `except` block.

### 1. Safe divide

In exercises.py, write the function `safe_divide` so that it returns the value of `x / y` if `y` isn't zero, and returns zero if `y` is zero.

You could do this by just checking if `y` is zero before dividing, but for this exercise, use a `try` block instead.

### 2. Dictionary get

In exercises.py, write the function `dict_get` so that it returns the value for the given key, or `None` if the key doesn't exist in the dictionary.

## Raising exceptions

So far, we've seen that exceptions can come from parts of the code where unexpected things can happen, like dividing by zero. But you can also raise exceptions yourself - for this, use the `raise` statement.

It's pretty easy to use:

    raise ZeroDivisionError()  # this line always raises an exception

So far we've used ZeroDivisionError as an example, but there are lots of different types of exceptions. Here are some of the more common types:

* `KeyError`: happens when you try to get a key from a dictionary that doesn't exist.
* `IndexError`: happens when you try to access a list item that doesn't exist.
* `ValueError`: happens when you give an invalid value, like trying to convert a string like `'hi'` to a number.
* `AttributeError`: happens when you try to get an attribute from an object, but the attribute doesn't exist.
* `NameError` or `UnboundLocalError`: happens when you try to use a variable before giving it a value.

Python has many more built-in exception types. You can read about them all [here](https://docs.python.org/2/library/exceptions.html).

> Note: You can even define your own types of exceptions! All you have to do is define a subclass of Python's built-in `Exception` class, and then you can use your own class as an exception.

### 3. Strict factorial

You remember the factorial function from lesson 8, right? It went something like this:

    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

This function works fine for positive numbers and zero. But what if `n` is negative? It doesn't make sense to compute the factorial of a negative number, so let's make our factorial function raise an exception if someone tries to use it to compute a negative factorial.

In exercises.py, write a version of `factorial` that raises ValueError if `n` is negative.

## Exception objects

Notice how in the `raise` statement, we used parenthesis?

    raise ZeroDivisionError()

This looks just like creating a new object of a class - that's because that's exactly what it is! We're actually creating an *object* of the class ZeroDivisionError, and *raising* that object. You could even do it like this:

    z = ZeroDivisionError()
    raise z

You can pass arguments to most types of exceptions:

    raise KeyError('this key does not exist')
    raise ValueError(14)
    raise Exception('you can put as many parameters as you want here', 42, 56.3, None, True)

If you want to get the actual exception object that was raised, you can catch it using the `as` keyword:

    try:
        raise KeyError('lolz', 42)

    except KeyError as e:
        # now e is the exception object itself. the arguments that were passed
        # to it are in e.args.
        print e.args[0]  # prints 'lolz'
        print e.args[1]  # prints '42'

<!-- %%
TODO: write an exercise here
-->

## Catching more exceptions

Now that you know about some more types of exceptions, you can also catch multiple types of exceptions at once. Imagine that instead of dividing by `z` in our example above, we're instead dividing by a value from a dictionary, `d[k]`. If `d[k]` is zero, we can still get ZeroDivisionError, like before. But if `d[k]` doesn't exist, then we could also get KeyError. Here's how we can deal with that:

    try:
        print 'about to divide y by d[k]...'
        ret = y / d[k]
        print 'y / d[k] is', ret
    except ZeroDivisionError:
        print 'could not divide because d[k] was zero'
    except KeyError:
        print 'could not divide because d[k] did not exist'
    print 'all done!'

The order of the `except` blocks doesn't matter in this case. If there's no exception, then none of them will ever be run, but if there is an exception, **only one** of them will ever be run - the one corresponding to the type of exception that happened. (If the `except ZeroDivisionError` block runs, then it will skip the `except KeyError` block when it's done.)

<!-- %%
TODO: write an exercise here
-->

## Exceptions and functions

You may be wondering: what happens if my code raises an exception, but doesn't catch it with an `except` block? What part of the program do we skip to?

The answer is that we *unwind the call stack*. This means that whatever function we're in "returns" immediately, and then we look for an `except` block in the function that called it.

We could rearrange the previous example like this:

    def divide(a, b):
        print 'about to divide a by b...'
        ret = a / b
        print 'a / b is', ret
        return ret

    try:
        ret = divide(y, d[k])
    except ZeroDivisionError:
        print 'could not divide because d[k] was zero'
    except KeyError:
        print 'could not divide because d[k] did not exist'
    print 'all done!'

In this example, ZeroDivisionError can happen when we're inside the `divide` function. Since it's not inside a `try` block at all in that function, the exception **propagates** to the caller - it's as if the exception was raised by the `divide(y, d[k])` line instead. Exceptions can propagate through any number of functions.

In fact, all of the following functions can raise ZeroDivisionError:

    # this function raises ZeroDivisionError if y is zero
    def f1(x, y):
        return x / y

    # this function also raises ZeroDivisionError if y is zero
    def f2(x, y):
        if y == 0:
            raise ZeroDivisionError()
        return x / y

    # this function always raises ZeroDivisionError
    def f3(x, y):
        raise ZeroDivisionError()

    # this function raises ZeroDivisionError if y is zero (since there is no
    # except block to catch it), but returns 0 if d[k] doesn't exist (since the
    # KeyError is caught by the except block)
    def f4(x, d, k):
        try:
            return x / d[k]
        except KeyError:
            return 0

<!-- %%
TODO: write an exercise here
-->

## Exceptions and inheritance

When you catch a specific type of exception, you're actually catching that exception type *and all subclasses of that exception type*. This might be a little confusing at first, so here's another example:

    try:
        print 'about to divide y by d[k]...'
        ret = y / d[k]
        print 'y / d[k] is', ret
    except Exception:
        print 'could not divide'
    print 'all done!'

When we run this code, we would see `could not divide` in the output in both error cases (where `d[k]` is zero, and where `d[k]` doesn't exist). This is because ZeroDivisionError and KeyError are both subclasses of Exception, so the `except` block catches both of them. See [the Python documentation](https://docs.python.org/2/library/exceptions.html#exception-hierarchy) for a full description of which exceptions inherit from which others.

<!-- %%
TODO: write an exercise here
-->

## Finally

By now, you've seen a lot of examples of `try` and `except` blocks. There are actually two more blocks that you should know about: `else` and `finally`. `else` isn't useful very often (we'll describe it at the end, but won't do any exercises for it). But you should probably know about `finally`.

Put simply, if Python reaches the `try` block at all, then the code in a `finally` block will **always** run. And it runs after everything else in the other blocks (`try`, `except`, and `else`). Specifically:

* If an exception happens in the `try` block and is caught in an `except` block, the `finally` block runs after the `except` block.
* If an exception happens in the `try` block and is not caught, the `finally` block runs *before* the exception propagates.
* If no exception happens in the `try` block, the `finally` block runs immediately after the `try` block is done.
* If the function returns during the `try` block, the `finally` block runs immediately before the function returns.

So when should you use a `finally` block? Usually, you would use a `finally` block when you need to *clean something up* regardless of whether an error occurred or not. For example, we might open a file and do something with it, but we need to make sure to close it when we're done even if there's an exception. We could do that like this:

    file = open(...)
    try:
        # do something with the file here
        ...
    finally:
        file.close()

<!-- %%
TODO: write an exercise here
-->

## Else

We mentioned the `else` block above, but we said it's not useful very often. But for completeness, we'll describe how it works.

If there's an `else` block after a `try` block, it only runs if *no exception happened* during the `try` block, but it's *not covered by the `except` blocks*. Maybe it's easier to understand in code:

    try:
        # if a KeyError happens in here, we run the except block and NOT the
        # else block. if any other exception happens in here, we don't run the
        # except block or the else block - the exception propagates. but if no
        # exception happens in here, then we run the else block after the try
        # block is done.
        ...
    except KeyError:
        ...
    else:
        # if any exception (including KeyError) happens in here, it propagates.
        # it does NOT run the except block above.
        ...

So what's the point of `else`? What's the difference between this:

    try:
        # do something risky
    except KeyError:
        # handle the KeyError
    # do something else

and this:

    try:
        # do something risky
    except KeyError:
        # handle the KeyError
    else:
        # do something else

In the first case, the `# do something else` part runs if there was a KeyError, and also runs if there was no exception. In the second case, the `# do something else` part only runs if there was no exception - it doesn't run if there was a KeyError.

## More reading

If you want to learn more about exceptions and error handling, take a look at these pages:
* [Official Python documentation about exceptions](https://docs.python.org/2/tutorial/errors.html)
* [Programiz tutorial on Python exceptions](https://www.programiz.com/python-programming/exception-handling)
