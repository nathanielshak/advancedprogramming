# Lesson 11: Object-oriented programming

**To start this lesson, students should**:

* Understand basic Python data structures (lists, dicts).
* Understand how functions are defined and called, and when to use them.

**By completing this lesson, students will**:

* Learn what classes are and when to use them.
* Know the difference between classes and objects.
* Be introduced to inheritance and abstract classes.
* Practice implementing classes.

## Thinking abstractly

Until now, we've been mainly organizing our code using *functions*. When we wanted to use the same code in multiple places, we would put it in a function, and just call the function in multiple places. What if we wanted to store data along with that code?

One useful example of this is the `maze` variable that we used in lesson 10. (You might want to go back and look at [lesson 10](../Lesson10) if you don't remember this.) The `maze` variable contained all of the data and code that you needed to deal with a two-dimensional grid. When you wrote your maze-solving algorithm, you didn't have to think about how all the data for the maze was stored, or deal with the data directly - all you had to do was tell the maze variable what you wanted it to do, and it took care of the rest.

This is a really powerful concept: **abstraction**. When working on large projects, it's always a good idea to break them down into small, manageable parts, and try to make each part know *as little about the other parts as possible*. Ideally, each part of the code should only care about *what the other parts of the code do*, but not *specifically how they do it*. If you design your project like this, then you can easily switch out parts of the code that you want to change, and if you don't touch the rest, it will all still work!

## Enter the Class

To allow us to organize code like this, we'll learn a new concept: **classes** and **instance objects** (commonly just called objects). An object is a collection of data (variables), along with functions (methods) that do things with those variables. A class is essentially a **blueprint for creating instance objects** - it defines which variables and methods exist on each object, *but not the values of the variables*. When you define a class, you're telling Python how to create objects of that type. When you **instantiate** it, you actually create an object of that type, and Python uses the class definition to fill it in.

This can be pretty confusing at first. Let's build up a simple class and talk about each part of it as we go.

The simplest possible class has *nothing in it*. It looks like this:

    class Car(object):
        pass

This class is called Car, and it *inherits* from `object`. We'll talk about inheritance later. For now, most classes should inherit from `object`, which is a built-in class in Python.

So what is this thing, then? Just defining the Car class doesn't actually create any variables - instead, it tells Python *how to create Car objects in general*. Now, in addition to numbers, strings, lists, dicts, and the like, we can also use Cars as values for variables! To make a Car, we call the Car class as if it were a function:

    c = Car()  # this creates a new Car object
    print(c)  # this prints something like '<Car object at 0x10a1b0a50>'

    d = Car()  # this is a different Car object
    print(d)  # this prints something like '<Car object at 0x10a1b0b10>'

    print(type(c) == type(d))  # this prints True: c and d are both Cars
    print(c == d)  # this prints False: c and d are different objects

Great! Now what?

## Adding variables

To make Car objects actually useful, we have to give them some variables and functions. We can do that like this:

    class Car(object):

        def __init__(self, wheels, miles, make, model, year, date_sold):
            self.wheels = wheels
            self.miles = miles
            self.make = make
            self.model = model
            self.year = year
            self.date_sold = date_sold

        def sale_price(self):
            # Returns how much we should sell the car for.
            return 5000.0 * self.wheels

        def purchase_price(self):
            # Returns how much we would buy the car back for.
            return 8000 - (0.10 * self.miles)

This code tells Python how to make a Car, but it doesn't actually create any Cars just yet. Like before, we can create Cars by calling the class as if it were a function, but now we have to pass some parameters:

    c = Car(4, 20000, None)  # 4 wheels, 20000 miles, not sold (date_sold is None)
    print(c.sale_price())  # prints 20000
    print(c.purchase_price())  # prints 6000

    d = Car(6, 10000, None)  # 6 wheels, 10000 miles, not sold (date_sold is None)
    print(d.sale_price())  # prints 30000
    print(d.purchase_price())  # prints 7000

To understand what's happening here, let's break down the Car class definition a bit. We defined a few functions, called `__init__`, `sale_price`, and `purchase_price`, *inside* the class.

Notice that all of these functions take `self` as the first parameter - when you call them, that's the *object* itself. When you call these functions, you don't need to provide `self` - Python will do that for you! This is why we could call `sale_price` and `purchase_price` without giving any parameters at all.

> When we defined `sale_price`, for example, we told Python *instructions for how to compute the sale price for some abstract car*. When we called `c.sale_price()`, we told Python to *follow those instructions using the car `c`*.

`__init__` is special - this is the function that Python calls automatically when you create a new Car object. So when we did `c = Car(4, 20000, None)`, Python created an empty Car object and called `__init__(c, 4, 20000, None)`. `__init__` is responsible for creating all of the variables within the class, which we call *attributes*. (Notice that all our `__init__` function does is assign the values from its parameters to attributes on `self`.) Then when we call other functions on the object `c`, like `c.sale_price()` and `c.purchase_price()`, they can access those same attributes.

> Note: You can access these attributes from outside the class definition too. For example, we can do something like `c = Car(...)`, then later we can use `c.wheels`. We don't have to only use the attributes inside functions defined inside the class.

> Note: We call variables *"attributes"* when they're inside a class, and we call functions *"methods"* when they're inside a class. From now on, when we say "function" or "variable", we're talking about functions and variables *outside of classes*.

## Practice time!

### 1. Writing a class

Find this class at the top of exercises.py:

    class Square(object):
        # TODO: write an __init__ method that sets the side_length attribute.
        pass

In this class, write an `__init__` method that sets the side_length attribute.

> Hint: don't forget that `__init__` should take both `self` and `side_length` as parameters.

### 2. Writing an instance method

Find this class at the top of exercises.py:

    class Rectangle(object):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def render(self):
            # TODO: write this method!
            print("not yet implemented")

This class represents an abstract rectangle with some width and height. We provided `__init__` for you. Fill in the method `render` so that it prints a rectangle of '@' characters to the terminal with the width and height from `self`.

### Doing more with instance methods

`__init__` can do more than just assign attributes. Consider this class:

    class CountUp(object):
        def __init__(self):
            self.count = 0

        def count(self):
            self.count = self.count + 3
            print(self.count)

Now that you've read the class definition, what do you think this code will print?

    c = CountUp()
    c.count()
    c.count()
    c.count()

If you guessed that it would print 3, 6, and 9, you're right! Remember that **only `__init__` should create new attributes**, but **any method can change their values**.

### 3. Writing an entire class

Now, let's put together all that we've learned about classes so far. Find this class in exercises.py:

    class CookieJar(object):
        def __init__(self, num_cookies):
            # TODO: write this method to make it set the num_cookies attribute
            pass

        def take_cookie(self):
            # TODO: write this method to make it decrease the number of cookies in
            # the jar by one. if there are no cookies in the jar, it should do
            # nothing.
            pass

        def add_cookie(self):
            # TODO: write this method to make it increase the number of cookies in
            # the jar by one.
            pass

Write all three functions to make the class keep track of the number of cookies in the jar.

## Inheritance

Let's say that in addition to cars, we also want to buy and sell trucks, but we don't want to buy them for the same price as cars. We could define another class to deal with trucks:

    class Truck(object):

        def __init__(self, wheels, miles, make, model, year, date_sold):
            self.wheels = wheels
            self.miles = miles
            self.make = make
            self.model = model
            self.year = year
            self.date_sold = date_sold

        def sale_price(self):
            # Returns how much we should sell the truck for.
            return 5000.0 * self.wheels

        def purchase_price(self):
            # Returns how much we would buy the truck back for.
            return 10000 - (0.10 * self.miles)

Notice that this class looks *almost exactly the same* as the Car class - the only thing that's different is a number in `purchase_price`! What if we wanted to start tracking the color of the cars and trucks? If we used this in a big project, it would get pretty annoying to have to change both classes whenever we wanted to add some information to our database. And we'd be more likely to make a mistake by forgetting to update one of the classes. What if we started selling go-karts as well? Then we'd have a third class to keep up to date along with Car and Truck! When will the madness end?!

When working on a big project, we try to **repeat ourselves as little as possible**. When we were using only functions, this means we would find places where we wrote the same code multiple times and move those out into separate functions. Now we can use **inheritance** to avoid repeating the same code in classes.

Put simply, inheritance means that one class can *implicitly* have all the same methods and attributes as another class.

Let's look at a concrete example to better understand this. We could say that Cars and Trucks are both Vehicles, so we would actually define three classes:

    class Vehicle(object):

        def __init__(self, wheels, miles, make, model, year, date_sold):
            self.wheels = wheels
            self.miles = miles
            self.make = make
            self.model = model
            self.year = year
            self.date_sold = date_sold

        def sale_price(self):
            # Returns how much we should sell the truck for.
            return 5000.0 * self.wheels

        def purchase_price(self):
            # Returns how much we would buy the truck back for.
            return 8000 - (0.10 * self.miles)

    class Car(Vehicle):  # NOTE: we use (Vehicle) here, not (object)
        pass

    class Truck(Vehicle):  # NOTE: we use (Vehicle) here, not (object)
        def purchase_price(self):
            # Returns how much we would buy the truck back for.
            return 10000 - (0.10 * self.miles)

When we use `(Vehicle)` in the class definition instead of `(object)`, that tells Python that the class we're creating should have *all the same methods as the parent class*, which is the one in parenthesis. We say that Car and Truck are **subclasses** of Vehicle, which is their **parent class** (also called the **superclass** or **base class**).

In this case, even though we didn't define anything at all in the Car class, it *inherits* the functions `__init__`, `sale_price`, and `purchase_price` from the Vehicle class. It's as if we defined those functions again in Car, with exactly the same code as in Vehicle, but we didn't have to write them again. Nice!

The Truck class also inherits from Vehicle, but we defined `purchase_price` in Truck also. When you create a Truck object and call `purchase_price()` on it, which function does it call? The one defined in Truck or the one defined in Vehicle?

The answer is that it *always calls the one defined latest*. So when you call `purchase_price` on a Car object, it will do the same thing as `purchase_price` on a Vehicle object. But if you call `purchase_price` on a Truck object, it will do something different, since the method definition in the Truck class **overrides** the method definition in the Vehicle class.

If we define another class that inherits from Truck, like MonsterTruck, and call `purchase_price` on a MonsterTruck object, it would do the same thing as it would for a Truck object, unless we defined *another* `purchase_price` function in the MonsterTruck class.

Note that we didn't override `sale_price` in any of the subclasses. So if we call `sale_price` on a Car object, then on a Truck object, then on a MonsterTruck object, it will use the same function all three times.

We say that Vehicle is an **abstract class** because it doesn't represent anything real - we're not supposed to use the class directly. Instead, we created subclasses of Vehicle, which we intend to use directly.

## Review

This was a lot of new stuff! Here's a quick summary of all the new terms we just learned:

* **abstraction**: Separating out the logical parts of a program into separate units, so that each one *knows what other parts do* but *doesn't care how they do it*.
* **instance object** (or just **object**): A logical collection of variables (*attributes*) and functions (*methods*) that operate on those variables.
* **class definition** (or just **class**): A blueprint for creating *objects*. This blueprint defines which *methods* and *attributes* exist on each object of this type, but doesn't define the values for the attributes.
* **instantiate**: To create an *object* using a *class definition*.
* **attribute**: A variable stored inside an *instance object*.
* **method**: A function defined inside a *class definition*.
* **`__init__`**: A special function that's called when an *object* is first created.
* **inheritance**: A method for classes to share *methods* without defining them multiple times.
* **subclass**: A class that *inherits* its method definitions from its *parent class*. All of the methods that are defined in the parent class are automatically part of the subclass as well.
* **parent class** (or **superclass**, or **base class**): A class that has *subclasses*.
* **override**: A method definition in a *class* with the same name as a method inherited from the parent class. The parent class' method doesn't exist in the subclass; instead, the override method takes its place.
* **abstract class**: A class that we only intend to *inherit* from, but never to *instantiate*. Usually we'll use abstract classes to define functions that all subclasses would need to inherit.

### 4. Putting it all together

Find this code in exercises.py:

    class Shape(object):
        def area(self):
            # This method should be overridden by all subclasses.
            return -1

        def print_area(self):
            # TODO: write this function
            pass

    class Triangle(Shape):
        def __init__(self, base, height):
            self.base = base
            self.height = height

        def area(self):
            # TODO: write this function
            return -1

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            # TODO: write this function
            return -1

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            # TODO: write this function
            return -1

    class Square(Rectangle):
        def __init__(self, side_length):
            # TODO: write this function
            pass

Here we define five classes at once! Shape is an abstract class that all the others inherit from. Triangle, Circle, and Rectangle inherit directly from Shape. Square inherits from Rectangle, since a square is just a rectangle whose width is equal to its height.

Your tasks:
* Fill in the `print_area` function in the base class (Shape).
* Fill in the `area` function in the Triangle, Circle, and Rectangle classes.
* Fill in the `__init__` function in the Square class. (Hint: it should set the `width` and `height` attributes.)
* Test your code by creating objects and calling methods on them.

> Hint: Remember that you can create an object by calling a class as if it were a function (like `r = Rectangle(10, 20)`). Then you can call methods on it like `r.area()`.

Area formulas:
* For a rectangle with width `w` and height `h`, the area is `w * h`.
* For a triangle with base `b` and height `h`, the area is `b * h / 2.0`.
* For a circle with radius `r`, the area is `math.PI * r * r`.

## More reading

If you want to learn more about classes, objects and inheritance, take a look at these tutorials:
* [Jeff Knupp's explanation of Python objects](https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/)
* [Object Oriented Programming from A Byte of Python](https://python.swaroopch.com/oop.html)

That's all for now - what a workout! On to [lesson 12](../Lesson12)!
