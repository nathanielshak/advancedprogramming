# This file contains the max_diff examples from the lesson text.


def max_diff1(nums):
    cur_max_diff = 0
    for num1 in nums:
        for num2 in nums:
            diff = abs(num1 - num2)
            if diff > cur_max_diff:
                cur_max_diff = diff

    return cur_max_diff

def max_diff2(nums):
    cur_min = float("inf")
    cur_max = -float("inf")
    for num in nums:
        if num > cur_max:
            cur_max = num
        if num < cur_min:
            cur_min = num
    return cur_max - cur_min


print max_diff1([1,7,-2,8,8,8,8,8,8,8,5,5,5,3,474,74,8,4])
print max_diff2([1,7,-2,8,8,8,8,8,8,8,5,5,5,3,474,74,8,4])