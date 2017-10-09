#searches linearly through a sorted list of numbers: nums for a number: target and returns whether or not the list contains the number
def linear_search(nums, target):
	for num in nums:
		if num is target:
			return True
	return False

#uses binary search to go through a sorted list of numbers: nums for a number: target and returns whether or not the list contains the number
def binary_search(nums, target):
	#TODO: implement this!
	return False



def test_binary_search(nums, target, desired_result):
	if binary_search(nums, target) is desired_result:
		print "TEST SUCCESSS on: " + str(nums)
	else:
		print "TEST FAILED on: " + str(nums)


test_binary_search([1,2,3,6,7,10,10,10], 7, True)
test_binary_search([1,6,10,10,10], 7, False)
test_binary_search([], 20, False)
test_binary_search([-80, -60, -10, 0, 12, 13], -80, True)
test_binary_search([-80, -60, -10, 0, 12, 13], -79, False)