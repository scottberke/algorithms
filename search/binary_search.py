# Binary Search - Recursive
def recursive_search(arr, target):
    low = 0
    high = len(arr)

    def rec_search(arr, low, high, target):
    	# If low > high then target isn't in array
    	if low > high:
    		return False
    	# Find mid point
    	mid = low + ((high - low) // 2)
     	# See if mid point matches target
    	if arr[mid] == target:
    		# Return index if it does
    		return mid
    	# Search left half if mid point > target
    	elif arr[mid] > target:
    		return rec_search(arr, low, mid - 1, target)
    	# Search right half if mid point < target
    	else:
    		return rec_search(arr, mid + 1, high, target)

    return rec_search(arr, low, high, target)

# Binary Search - Iterative
def search(arr, target):
	# Set low and high index
	low = 0
	high = len(arr) - 1
	# Repeat until low index > high index
	while low <= high:
		# Grab our mid point index
		mid = (high + low) // 2
		# If value at midpoint is target, return index
		if arr[mid] == target:
			return mid
		# If midpoint value > target, increment high index
		elif arr[mid] > target:
			high = mid - 1
		# If midpoint value < target, increment low index
		else:
			low = mid + 1
	# If we've made it here, target isnt found
	return False
