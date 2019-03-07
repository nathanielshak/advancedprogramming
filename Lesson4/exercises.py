# Returns the square of a number if it's odd; otherwise, returns the original number.
def square_if_odd(num): 
    # TODO: implement this!
    return -1


# Returns whether the given number is within the range of lower and upper inclusive (True or False).
def in_range(lower, upper, num):
    # TODO: implement this!
    return False


# Takes in a list of numbers and returns a list of only the even ones.
def even_elements(nums):
    # TODO: implement this!
    return []


# Takes in a string and returns the most common letter occuring in the string.
# If there's a tie, you may return any of them.
def most_common_letter(str):
    # TODO: implement this!
    return 'a'


# Takes in a list of numbers and returns the maximum difference between any two numbers in the list.
def max_diff(nums):
    # TODO: implement this!
    return -1


# Prints an hourglass made out of '*' characters with a base the size of the number supplied * 2.
def hourglass(size):
    # TODO: implement this!
    print("not implemented")









'''
The below code is just to test your code. You don't need to touch these.
'''

def test_function(fn, tests):
    print("Testing %s..." % fn.__name__)
    for i, (args, expected_result) in enumerate(tests):
        print("Running test %d (%r)..." % (i, args))
        if not isinstance(args, tuple):
            args = (args,)
        actual_result = fn(*args)
        if actual_result == expected_result:
            print("PASS!")
        else:
            print("FAIL!")
            print("result was %r, but it should have been %r" % (actual_result, expected_result))
            return False
    return True

fn_to_tests = [
    (square_if_odd, [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 9),
        (-8, -8),
        (-9, 81),
    ]),
    (in_range, [
        ((0, 0, 0), True),
        ((1, 3, 2), True),
        ((-2, 80, 80), True),
        ((-3, 5, 6), False),
    ]),
    (even_elements, [
        ([1, 2, 5, 7, 2, 6, 7, 9], [2, 2, 6]),
        ([-8, 2, 4], [-8, 2, 4]),
        ([1, 3, 5, 7], []),
    ]),
    (most_common_letter, [
        ("abcb", "b"),
        ("popular", "p"),
        ("andskfjngrkejnhkjjfjfjnfnkzzjj", "j"),
    ]),
    (max_diff, [
        ([1, 4, -9, 2, 3, 20], 29),
        ([1, 3, 5], 4),
        ([-2, 0], 2),
    ]),
]

if __name__ == "__main__":
    for fn, tests in fn_to_tests:
        test_function(fn, tests)
        print()
