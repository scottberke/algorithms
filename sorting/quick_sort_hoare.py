import random
# QuickSort - Hoare Partition
def quick_sort(arr, low, high):
	# Keep going while our low and high values don't cross
	if low < high:
		# Get a partition point
		par = partition(arr, low, high)
		# Sort subarray of low index to parition index
		quick_sort(arr, low, par)
		# Sort subarray of parition to high index
		quick_sort(arr, par + 1, high)

# Heavy lifting takes place here
def partition(arr, low, high):
	# Use low value as our sort value
    piv_value = arr[low]
	# Start low index at lowest point in subarray
    piv_low = low - 1
	# Start high index at highest point in subarray
    piv_high = high + 1

	# Loop until we've correctly placed our piv_value
    while True:
		# While value at piv_low < piv_value, Increment our piv_low index
        while True:
            piv_low += 1
            if arr[piv_low] >= piv_value:
                break
		# While value at piv_high > piv_value, decrement our piv_high index
        while True:
            piv_high -= 1
            if arr[piv_high] <= piv_value:
                break
		# If our index values touch, piv_value index is correct. Return index
        if piv_low >= piv_high:
            return piv_high
		# Otherwise, swap values at piv_low and piv_high index
        arr[piv_low], arr[piv_high] = arr[piv_high], arr[piv_low]


# Testing:
arr = [ random.randrange(0,100) for i in range(0,100) ]
print("Unsorted Array:")
print(arr)
print("Sorted Array:")

quick_sort(arr, 0, len(arr) - 1)
print(arr)
