## Search
- The ‘search problem’ -> Retrieving information stored within a data structure, or calculated in the search space of a problem domain
- Choosing the correct search algorithm depends on the data structure being searched
***

### Practice Problems
- [Search in Rotated Array](./practice_problems/practice_problems.md#search-in-rotated-arrar)

### Linear Search  
**O(n)**
- Simplest search approach:
	1. Start from left most element in array
	2. Compare elements, one by one, with target
	3. If you have a match, return the index
	4. If you don’t have a match, return -1 or False
- Rarely used due to inefficiency
- In the worst case, the element is at the end of the list so we have to search the entire list of n items
- In the best case, the element is first in the array and we search 1 item
```python
def search(arr, target):
	for index, val in enumerate(arr):			# Grab index and value
		if val == target:						# If we find our target
			return index						# Return index
	return False 								# Otherwise, return False
```
- - - -

### Binary Search  
**O(log n)**
- Requires that the array is sorted prior to search
- Works by repeatedly dividing the search interval in half
	1. Check the target against the middle element
	2. If the target is doesn’t match, determine if target is < or > than middle
	3. Perform the same operation on the corresponding side until you the element or nothing is left to search
```python
# Binary Search - Recursive
def search(arr, low, high, target):
	if low > high:						# If low > high then target isnt in array
		return False

	mid = low + ((high - low) // 2)		# Find mid point
	if arr[mid] == target:				# See if mid point matches target
		return mid						# Return index if it does
	elif arr[mid] > target:				# Search left half if mid point > target
		return search(arr, low, mid - 1, target)
	else:								# Search right half if mid point < target
		return search(arr, mid + 1, high, target)

# Binary Search - Iterative
def search(arr, target):
	low = 0						# Set low index
	high = len(arr)				# Set high index

	while low <= high:			# Repeat until low index > high index
		mid = low + ((high - low) // 2) 	# Grab our mid point index

		if arr[mid] == target:	# If value at midpoint is target, return index
			return mid
		elif arr[mid] > target:	# If midpoint value > target, increment high index
			high = mid - 1
		else:					# If midpoint value < target, increment low index
			low = mid + 1

	return False				# If we've made it here, target isnt found
```
