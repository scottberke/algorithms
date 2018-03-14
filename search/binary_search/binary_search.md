# Binary Search  
**O(log n)**
- Requires that the array is sorted prior to search
- Works by repeatedly dividing the search interval in half
	1. Check the target against the middle element
	2. If the target is doesn’t match, determine if target is < or > than middle
	3. Perform the same operation on the corresponding side until you the element or nothing is left to search

## Implementation
- [Binary Search - Python](./binary_search.py)
- [Binary Search Test Cases - Python](./binary_search_test.py)
