import random

def bubble_sort(arr):
    # Keeps track of whether or not a swap occured
    swap_made = True
    # Swaps will be made until the list is sorted
    while swap_made:
        # No swap has been made on this iteration yet
        swap_made = False
        # Iterate through the array
        for i in range(len(arr)-1):
            # Grab two sequential items
            first = arr[i]
            second = arr[i+1]
            # If we find a value pair out of order swap them
            if first > second:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # If were here, we've made a swap on this iteration
                swap_made = True


# Testing:
arr = [ random.randrange(0,100) for i in range(0,100) ]
print("Unsorted Array:")
print(arr)
bubble_sort(arr)
print("Sorted Array:")
print(arr)
