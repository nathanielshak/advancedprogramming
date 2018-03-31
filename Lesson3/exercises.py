## LIST EXERCISES


# Prints out all the items in the list.
def list_print(lst):
    for item in lst:
        print(item)



# Sums up all the numbers in the list and returns the sum.
def list_sum(lst):
    # TODO: finish this!
    return -1



# Finds and returns the greatest number in the list.
# You can assume all numbers in the list are positive.
def find_list_max(lst):
    # TODO: finish this!
    return -1





## DICT EXERCISES


# Prints out each corresponding key/value pair in a dict.
def dict_print(d):
    for key, value in d.items():
        print("key: " + str(key) + " value: " + str(value))



# Returns the key that has the highest value in the dict.
# You can assume all values in the dict are positive numbers.
def key_max_value(d):
    # TODO: finish this!
    return -1



# Counts how many of each item are in the given list,
# Returns them as a dict of items mapping to the number of times they appeared.
def count_items(lst):
    # TODO: finish this!
    print("not implemented yet :(")




'''
The below code is just to test your code. You don't need to touch these.
'''

def test_list_sum(tests):
    print("Testing list_sum...")
    test_num = 1
    for test in tests:
        print("test " + str(test_num))
        if list_sum(test[0]) == test[1]:
            print("PASS!")
        else:
            print("FAIL!")
            print("failed on " + str(test[0]))
            print("answer was " + str(list_sum(test[0])) + ", but it should have been " + str(test[1]))
            return False
        test_num += 1
    return True

def test_list_max(tests):
    print("Testing list_max....")
    test_num = 1
    for test in tests:
        print("test " + str(test_num))
        if find_list_max(test[0]) == test[1]:
            print("PASS!")
        else:
            print("FAIL!")
            print("failed on " + str(test[0]))
            print("answer was " + str(find_list_max(test[0])) + ", but it should have been " + str(test[1]))
            return False
        test_num += 1
    return True

def test_key_max_value(tests):
    print("Testing key_max_value....")
    test_num = 1
    for test in tests:
        print("test " + str(test_num))
        if key_max_value(test[0]) == test[1]:
            print("PASS!")
        else:
            print("FAIL!")
            print("failed on " + str(test[0]))
            print("answer was " + str(key_max_value(test[0])) + ", but it should have been " + str(test[1]))
            return False
        test_num += 1
    return True

def test_count_items(tests):
    print("Testing count_items....")
    test_num = 1
    for test in tests:
        print("test " + str(test_num))
        if count_items(test[0]) == test[1]:
            print("PASS!")
        else:
            print("FAIL!")
            print("failed on " + str(test[0]))
            print("answer was " + str(count_items(test[0])) + ", but it should have been " + str(test[1]))
            return False
        test_num += 1
    return True

def test_all():
    all_passed = True
    if test_list_sum([([1,2,3], 6), ([], 0), ([-82, 4, 9 ,9 ,9 ,9], -42)]):
        print("list_sum works!")
    else:
        print("whoops, list sum doesn't work :(")
        all_passed = False
    print("____________________________________________________________________\n")

    if test_list_max([([2,2,2,8,4], 8), ([1], 1), ([4, 9 ,9 ,7 ,9], 9)]):
        print("list_max works!")
    else:
        print("whoops, list max doesn't work :(")
        all_passed = False
    print("____________________________________________________________________\n")

    if test_key_max_value([({1:2,2:3,4:1,9:2}, 2), ({"dog":20, "cat":10, "meep":1000}, "meep")]):
        print("key_max_value works!")
    else:
        print("whoops, key_max_value doesn't work :(")
        all_passed = False
    print("____________________________________________________________________\n")


    if test_count_items([([1,2,3,2,3,4,8], {1:1,2:2,3:2,4:1,8:1}), ([], {}), ([4,4,4,2,2,89,1], {4:3, 2:2, 89:1 ,1:1})]):
        print("count_items works")
    else:
        print("whoops, count_items doesn't work :(")
    print("____________________________________________________________________\n")


    if all_passed:
        print("all the tests passed!")
    else:
        print("looks like not all the tests passed :(")

test_all()
