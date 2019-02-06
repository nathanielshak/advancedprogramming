import math


# 1. Writing a class

class Square(object):
    # TODO: write an __init__ method that sets the side_length attribute.
    pass


# 2. Writing an instance method

class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def render(self):
        # TODO: write this method
        print("not yet implemented")


# 3. Writing an entire class

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


# 4. Putting it all together

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
        # TODO: write this function.
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
