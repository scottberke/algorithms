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
	# Grab index and value
	for index, val in enumerate(arr):
		# If we find our target
		if val == target:						
			# Return index
			return index						
	# Otherwise, return False		
	return False 								
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
	# If low > high then target isn't in array
	if low > high:						
		return False
	# Find mid point
	mid = low + ((high - low) // 2)		
 	# See if mid point matches target
	if arr[mid] == target:				
		# Return index if it does
		return mid						
	# Search left half if mid point > target
	elif arr[mid] > target:				
		return search(arr, low, mid - 1, target)
	# Search right half if mid point < target
	else:								
		return search(arr, mid + 1, high, target)

# Binary Search - Iterative
def search(arr, target):
	# Set low and high index
	low = 0						
	high = len(arr)			
	# Repeat until low index > high index
	while low <= high:			
		# Grab our mid point index
		mid = low + ((high - low) // 2) 	
		# If value at midpoint is target, return index
		if arr[mid] == target:
			return mid
		# If midpoint value > target, increment high index
		elif arr[mid] > target:
			high = mid - 1
		# If midpoint value < target, increment low index
		else:					
			low = mid + 1
	# If we've made it here, target isnt found		
	return False				
```
