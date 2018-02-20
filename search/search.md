## Search
- The ‘search problem’ -> Retrieving information stored within a data structure, or calculated in the search space of a problem domain
- Choosing the correct search algorithm depends on the data structure being searched
***

### Linear Search - O(n)
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
