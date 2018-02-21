# Sorting
- Used to place elements of a list in a certain order
- Beyond obvious benefits of having a sorted data structure, sorting allows efficient searching
	- Searching from random group -> difficult
	- Searching from sorted group -> easier
- Stable sort algorithms sort identical elements in the same order as they appear when inputed
- - - -

### Sorting Algorithms
- Selection Sort
- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Bucket Sort

## Selection Sort

### Description:
This sort works in-place and is a comparison sort. It works by iteratively selecting the next smallest element from an array and placing it at the end of the sorted subarray.

- Maintains two subarrays in given array:
	1. Already sorted array
	2. Remaining unsorted array
- Selection sort never makes more than O(n) swaps -> good when memory writing is costly

### Steps:
1. Find the minimum element in the array
2. Place element at the beginning of the array
3. Find the minimum element in the remaining unsorted array
4. Place that at the end of the sorted array
5. Repeat until nothing remains in the unsorted array

### Examples:
- [Python](./selection_sort.py)

- - - -

### Bubble Sort - O(n^2)
- Repeatedly swaps adjacent elements if they’re in the wrong order
	- Largest value ‘bubbles’ up to the end
- Sorts in place
```python
arr = [10, 15, 9, 25, 17, 2, 99, 109, 34, 72, 40]

swap_made = True 				# Keeps track of whether or not a swap occured
while swap_made:				# If no swaps are made then array is sorted
	swap_made = False			# Set to false since no swaps have been made yet
	for i in range(len(arr)-1):	# Iterate through array len - 1
		first = arr[i]			
		second = arr[i+1]
		if first > second:		# If we find a value pair out of order swap them
			arr[i], arr[i+1] = arr[i+1], arr[i]
			swap_made = True	# Set swap made so we keep going


# Recursive Bubble Sort
def bubble(arr, swapped = True):
	if not swapped:
		return arr
	else:
		swapped = False
		for i in range(len(arr)-1):
			first = arr[i]
			second = arr[i+1]
			if first > second:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				swapped = True
		return bubble(arr, swapped)		

```
- - - -

### Insertion Sort - O(n^2)
- Takes each item and deals with it one at a time building the final sorted array in place.  similar to sorting a hand of cards

```python
arr = [10, 15, 9, 25, 17, 2, 99, 109, 34, 72, 40]   

for i in range(1, len(arr)): 				# Assume first element is sorted 	
	el = arr[i] 							# Grab value we're inserting
	while i > 0 and el < arr[i-1]: 			# Go through sorted portion of array
		arr[i], arr[i-1] = arr[i-1], arr[i]# Swap values until el is in proper place
		i -= 1								# decrement to check backwards neighbor

# Recursive Insertion Sort
def insertion(arr, start=0):
	if start == len(arr):					# If were at the end, arrays sorted
		return arr							# Return sorted array
	else:
		el = arr[start]						# Grab our current element
		index = start						# Grab its index
		while index > 0 and el < arr[index-1]:		# Work backwards comparing el
			arr[index], arr[index-1] = arr[index-1], arr[index] # Swap out of order
			index -= 1						# Check the next neighbor
		return insertion(arr,start+1)		# Call again with next element
```
- - - -

### Merge Sort - O(n log n)
- Divide and conquer algorithm
- Divides input into two halves, sorts the two halves and then merges the sorted halves
- Faster but requires more memory
- Heavy lifting takes place in merging two halves
```python
def merge_sort(arr):
	if len(arr) == 1:		# Array len of 1 is already sorted so just return		
		return arr

	mid = len(arr) // 2		# Otherwise, find the midpoint of the array
	first = merge_sort(arr[:mid])	# Sort the first half
	second = merge_sort(arr[mid:]) # Sort the second half
	return merge(first,second)		# Merge the two halves back together

def merge(first,second):
	merged = []		# Array to hold sorted elements
	f_index = 0		# Counter for first array index
	s_index = 0		# Counter for second array index

	# Iterate while we have not finished placing one of the halves
	while f_index < len(first) and s_index < len(second):
		f_val = first[f_index]		# Grab first array val at current index
		s_val = second[s_index]		# Grab second array val at current index

		if f_val < s_val:
			merged.append(f_val)	# Add first value to sorted array if its lower
			f_index += 1			# Increment our index for first array
		else:
			merged.append(s_val)	# If first value isn't lower, add second to sorted
			s_index += 1			# Increment our index for second array

	# Return our sorted list with remaining elements either the first or second array
	# Remaining elements are implicitly sorted and are the highest elements left
	return merged + first[f_index:] + second[s_index:]
```
- - - -

### Quick Sort - O(n log n)
- Another divide and conquer sort algorithm
- We pick a partition spot, usually the last element, and move all elements lower than the partitions value before it and all elements higher than partition spot after it. Basically,  putting the value of the partition index in its correct spot on each call and then updating the call to take the elements below and the elements above it
```python
import random
# QuickSort - Lomuto Partition
# Consumes the array to be sorted, the low index, usually 0, and the high index
def quick_sort(arr, low, high):
	# we'll keep making recusive calls until the low index is less than high index
	if low < high:
		# We find out parition index, which is the index of the item just sorted into place. This index value will be correctly sorted
		par = partition(arr, low, high)

		# With par index in its correct place, we do the same thing for the values below par and above par index
		quick_sort(arr, low, par - 1)
		quick_sort(arr, par + 1, high)

# Heavy lifting takes place here. Consumes arrayto be sorted, low and high index
def partition(arr, low, high):
	# piv_index keeps track of where all elements lower than our piv value end. We start at the lowest value as our first place to check
	piv_index = low
	# piv_value is the last item in the array and the item we want to put in sorted order
	piv_value = arr[high]
	# Iterate from low index through high index checking
	for i in range(low, high):
		# If our value at i is less than the value were sorting into place 	
		if arr[i] <= piv_value:
			# We swap the piv_index value, with the i element, essentially taking elements lower than our piv_value and placing them all within the range from low to piv_index
			arr[piv_index], arr[i] = arr[i], arr[piv_index]
			# Update piv_index to keep track of where all lower than elements end
			piv_index += 1
	# We swap the value were sorting into the position just above all elements lower than itself
	arr[piv_index], arr[high] = arr[high], arr[piv_index]
	# Return the index of where we just sorted
	return piv_index

arr = [ random.randrange(0,100) for i in range(0,100) ]
quick_sort(arr, 0, len(arr) - 1)

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
	piv_low = low
	# Start high index at highest point in subarray
	piv_high = high

	# Loop until we've correctly placed our piv_value
	while True:
		# While value at piv_low < piv_value, Increment our piv_low index
		while arr[piv_low] < piv_value:
			piv_low += 1
		# While value at piv_high > piv_value, decrement our piv_high index
		while arr[piv_high] > piv_value:
			piv_high -= 1

		# If our index values touch, piv_value index is correct. Return index
		if piv_low >= piv_high:
			return piv_high
		# Otherwise, swap values at piv_low and piv_high index
		else:
			arr[piv_low], arr[piv_high] = arr[piv_high], arr[piv_low]

arr = [ random.randrange(0,100) for i in range(0,100) ]
quick_sort(arr, 0, len(arr) - 1)
```
***

### Heap Sort
TODO
***

### Radix Sort
TODO
