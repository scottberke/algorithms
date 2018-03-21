import random

def bucket_sort(arr):
	# Return arr if its empty
	if not arr:
		return arr
	# Get max value from our array
	max_val = max(arr)
	# Get our array length
	arr_len = len(arr)
	# Create empty buckets to hold elements
	buckets = [ [] for i in range(arr_len) ]
	# Iterate through array placeing elements into appropriate buckets
	for i in range(arr_len):
		# Bucket determined by value * array length // max value + 1
		bucket_no = arr[i] * arr_len // (max_val + 1)
		buckets[bucket_no].append(arr[i])
	# Sort each bucket. Variety of sort algorithms can be used for buckets
	for bucket in buckets:
		bucket.sort()

	# Return our flattened buckets
	return [ val for sub_arr in buckets for val in sub_arr ]

# TODO add proper test
# Testing:
arr = [ random.randrange(0,100) for i in range(0,100) ]
print("Unsorted Array:")
print(arr)
print("Sorted Array:")
print(bucket_sort(arr))
