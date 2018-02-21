import random

def insertion_sort(arr, start=0):
    # If were at the end, arrays sorted
    if start == len(arr):
        return arr
    else:
        # Grab our current element
        el = arr[start]
        # Grab its index
        index = start
        # Work backwards comparing el to sorted values
        while index > 0 and el < arr[index-1]:
            # Swap out of order elements
            arr[index], arr[index-1] = arr[index-1], arr[index]
            # Check the next neighbor
            index -= 1
        # Call sort again with next element
        return insertion_sort(arr,start+1)


# Testing:
arr = [ random.randrange(0,100) for i in range(0,100) ]
print("Unsorted Array:")
print(arr)
insertion_sort(arr)
print("Sorted Array:")
print(arr)
