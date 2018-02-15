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
```python
arr = [10, 15, 9, 25, 17, 2, 99, 109, 34, 72, 40]

for i in range(len(arr)):
	min_index = i

	for j in range(i+1, len(arr)):
		if arr[j] < arr[min_index]:
			min_index = j
	arr[i], arr[min_index] = arr[min_index], arr[i]
```
