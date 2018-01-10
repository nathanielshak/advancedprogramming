import random
import time


# Sorts the nums array using selection sort.
def selection_sort(nums):
    result = nums[:]
    # TODO: write the code to sort the result array!
    return result


BUCKET_NUM = 10

# Sorts the nums array using bucket sort with selection sort.
# The number of buckets is declared in BUCKET_NUM above.
def bucket_sort(nums):
    # Initializes a list of lists - each of these lists is a bucket!
    buckets = [[] for i in range(BUCKET_NUM)]

    # TODO: put the numbers each into their respective buckets
    for num in nums:
        pass

    # TODO: sort each bucket using the selection_sort function you wrote earlier
    for bucket in buckets:
        pass

    # TODO: put all the sorted buckets together into the results list
    result = []
    for bucket in buckets:
        pass

    return result


print "testing selection_sort:"
start = time.time()
print selection_sort([random.randint(0, 999) for _ in xrange(1000)])
diff = time.time() - start
print 'selection_sort took %s seconds' % diff

print "testing bucket_sort:"
start = time.time()
print bucket_sort([random.randint(0, 99) for _ in xrange(1000)])
diff = time.time() - start
print 'bucket_sort took %s seconds' % diff
