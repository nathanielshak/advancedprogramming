import numpy as np

BUCKET_NUM = 10

def selection_sort(nums):
	#TODO: write the code to sort the nums array!
	return nums

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
print selection_sort(np.random.choice(100,1000).tolist())
print "testing bucket_sort:"
print bucket_sort(np.random.choice(100,1000).tolist())
