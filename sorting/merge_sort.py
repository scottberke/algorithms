import random

def merge_sort(arr):
    # Array len of 1 is already sorted so just return
    if len(arr) == 1:
        return arr
    # Find the midpoint of the array
    mid = len(arr) // 2
    # Sort the first half
    first = merge_sort(arr[:mid])
    # Sort the second half
    second = merge_sort(arr[mid:])
    # Merge the two halves back together
    return merge(first, second)

def merge(first, second):
    # Array to hold sorted elements
    merged = []
    # Counters to track index of merging arrays
    f_index = 0
    s_index = 0
	# Iterate while we have not finished placing one of the halves
    while f_index < len(first) and s_index < len(second):
        # Grab values at current index positions
        f_val = first[f_index]
        s_val = second[s_index]

        if f_val < s_val:
            # Add first value to sorted array if its lower
            merged.append(f_val)
            # Increment our index for first array
            f_index += 1
        else:
            # If first value isn't lower, add second to sorted
            merged.append(s_val)
            # Increment our index for second array
            s_index += 1

	# Return our sorted list with remaining elements either the first or second array
	# Remaining elements are implicitly sorted and are the highest elements left
    # First or Second array is empty
    return merged + first[f_index:] + second[s_index:]

# TODO add proper test
# Testing:
arr = [ random.randrange(0,100) for i in range(0,100) ]
print("Unsorted Array:")
print(arr)
print("Sorted Array:")
print(merge_sort(arr))
