# Sorted Merge

# This method takes a 'python' approach where the array doesnt nessecarily
# have a buffer but is dynamic in size.
def merge(a_arr, b_arr):
    # If either array is empty just concatenate them and return
    if not a_arr or not b_arr:
        return a_arr + b_arr
    # Keep track of a_array index
    a_index = 0
    # Go through all b_arr elements
    for b_index, b_val in enumerate(b_arr):
        # Increment a_index until its value > b_val
        while b_val > a_arr[a_index]:
            a_index += 1
            # If were at the end of a_arr, just concat b_arr and return
            # since we know all remaining b_vals go at the end
            if a_index == len(a_arr):
                return a_arr + b_arr[b_index:]

        # Insert b_val into a where it belongs
        a_arr.insert(a_index, b_val)

    return a_arr




# This approach assumes that the a array is actually fixed size with an
# adequate buffer to hold all of b array
def buffer_merge(a_arr, b_arr):
    # If either array is empty just concatenate them and return
    if not a_arr or not b_arr:
        return a_arr + b_arr

    # Keep track of our indices and a_arrays end index
    b_index = len(b_arr) - 1
    a_index = len(a_arr) - 1
    a_end = len(a_arr) - 1

    # Work backwards so we dont have to shift the entire array
    while a_index >= 0 and b_index >= 0:
        # Decrement a_index until were out of the buffer
        if not a_arr[a_index]:
            a_index -= 1
            continue
        # Put a's value at the end if its larger and decrement a's index
        if a_arr[a_index] > b_arr[b_index]:
               a_arr[a_end] = a_arr[a_index]
               a_index -= 1
        # Otherwise, b's value is larger so put it at the end and
        # decrement b's index
        else:
            a_arr[a_end] = b_arr[b_index]
            b_index -= 1

        # Update our end index
        a_end -= 1

    return a_arr
