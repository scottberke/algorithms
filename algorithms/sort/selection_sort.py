def selection_sort(arr):
    # Iterate through the array
    for i in range(len(arr)): #
        # Assume the current position is the min value
        min_index = i
        # Iterate through the remaining unsorted array values
        for j in range(i+1, len(arr)):
            # If we find a lower value
            if arr[j] < arr[min_index]: # If we find a lower value
                # Then update our min value index
                min_index = j
        # Swap the value in the next lowest index with the actual lowest value
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
