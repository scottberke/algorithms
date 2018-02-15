## Sorting
- Beyond obvious benefits of having a sorted data structure, sorting allows efficient searching
	- Searching from random group -> difficult
	- Searching from sorted group -> easier
- - - -

### Selection Sort - O(n^2)
- Iteratively select the next smallest element
- Maintains two subarrays in given array:
	- Already sorted array
	- Remaining unsorted array
- Selection sort never makes more than O(n) swaps -> good when memory writing is costly
```python
arr = [10, 15, 9, 25, 17, 2, 99, 109, 34, 72, 40]

for i in range(len(arr)): # Start at the begining of the array
	min_index = i			 # Assume the current position is the min value

	for j in range(i+1, len(arr)):  # Go through the remaining values  

		if arr[j] < arr[min_index]: # If we find a lower value
			min_index = j 			 # Update min position to lower value

	arr[i], arr[min_index] = arr[min_index], arr[i] # Swap start position with min
```
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
