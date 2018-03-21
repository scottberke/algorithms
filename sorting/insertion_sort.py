import random

def insertion_sort(arr):
    # Assume first element is sorted so iterate from index 1 on
    for i in range(1, len(arr)):
        # Grab value we're inserting
        value = arr[i]
        # Go through sorted portion of array
        while i > 0 and value < arr[i-1]:
            # Swap values until value is in proper place
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1

# TODO add proper test
# Testing:
arr = [ random.randrange(0,100) for i in range(0,100) ]
print("Unsorted Array:")
print(arr)
insertion_sort(arr)
print("Sorted Array:")
print(arr)
