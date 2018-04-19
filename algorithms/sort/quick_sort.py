# QuickSort - Lomuto Partition
# Consumes the array to be sorted, the low index, usually 0, and the high index
def quick_sort(arr, low, high):
	# Keep making recusive calls until the low index is less than high index
	if low < high:
		# Find parition index. This is the index of the item just sorted into
        # place. This index value will be correctly sorted
		par = partition(arr, low, high)

		# With par index in its correct place, we do the same thing for the
        # values below par and above par index
		quick_sort(arr, low, par - 1)
		quick_sort(arr, par + 1, high)

# Heavy lifting takes place here. Consumes array to be sorted, low and high index
def partition(arr, low, high):
	# piv_index keeps track of where all elements lower than our piv value end.
    # We start at the lowest value as our first place to check
	piv_index = low
	# piv_value is the last item in the array and the item we want to put in
    # sorted order
	piv_value = arr[high]
	# Iterate from low index through high index checking
	for i in range(low, high):
		# If our value at i is less than the value were sorting into place
		if arr[i] <= piv_value:
			# We swap the piv_index value, with the i element, essentially
            # taking elements lower than our piv_value and placing them all
            # within the range from low to piv_index
			arr[piv_index], arr[i] = arr[i], arr[piv_index]
			# Update piv_index to keep track of where all lower than elements end
			piv_index += 1
	# We swap the value were sorting into the position just above all elements lower than itself
	arr[piv_index], arr[high] = arr[high], arr[piv_index]
	# Return the index of where we just sorted
	return piv_index
