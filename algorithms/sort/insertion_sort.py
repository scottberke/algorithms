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
    return arr
