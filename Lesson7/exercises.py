import numpy as np

#sorts the nums array using selection sort
def selection_sort(nums):
	result = nums[:]
	#TODO: write the code to sort the result array!
	return result


BUCKET_NUM = 10

#sorts the nums array using bucket sort with selection sort. The number of buckets is declared in BUCKET_NUM.
def bucket_sort(nums):
	#initializes a list of lists - each of these lists are a bucket!
	buckets = [[] for i in range(BUCKET_NUM)]

	#TODO: put the numbers each into their respective buckets
	for num in nums:
		pass

	#TODO: sort each bucket using the selection_sort function you wrote earlier
	for bucket in buckets:
		pass

	#TODO: put all the sorted buckets together into the results list
	result = []
	for bucket in buckets:
		pass

	return result

print "testing selection_sort:"
print selection_sort(np.random.choice(1000,1000).tolist())
print "testing bucket_sort:"
print bucket_sort(np.random.choice(100,1000).tolist())
