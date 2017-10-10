def max_diff(nums):
    cur_max_diff = 0
    for index1 in range(len(nums)):
        for index2 in range(index1 + 1, len(nums)):
            diff = abs(nums[index1] - nums[index2])
            if diff > cur_max_diff:
                cur_max_diff = diff
    return cur_max_diff

print max_diff([1,7,8,8,8,8,8,8,8,8,5,5,5,3,474,74,8,4])