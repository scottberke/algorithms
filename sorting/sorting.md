# Sorting
- Used to place elements of a list in a certain order
- Beyond obvious benefits of having a sorted data structure, sorting allows efficient searching
	- Searching from random group -> difficult
	- Searching from sorted group -> easier
- Stable sort algorithms sort identical elements in the same order as they appear when inputed
- - - -

### Sorting Algorithms
- [Selection Sort - O(n^2)](#selection-sort)  
- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Bucket Sort

## Selection Sort
### Runtime
**O(n^2)** Average and worst case.
Memory: O(1)

### Description:
This sort works in-place and is a comparison sort. It works by iteratively selecting the next smallest element from an array and placing it at the end of the sorted subarray.

- Maintains two subarrays within given array:
	1. Already sorted array
	2. Remaining unsorted array
- Selection sort never makes more than O(n) swaps -> good when memory writing is costly
### Use Cases:
- Has performance advantages over more complicated sorts when memory is limited
- Can be used for smaller data sets

### Steps:
1. Find the minimum element in the array
2. Place element at the beginning of the array
3. Find the minimum element in the remaining unsorted array
4. Place that at the end of the sorted array
5. Repeat until nothing remains in the unsorted array

### Examples:
- [Python](./selection_sort.py)

- - - -

## Bubble Sort
### Runtime:
**O(n^2)** Average and worst case
Memory: O(1)

### Description:
This sort works in-place and is a comparison sort. It works by iteratively evaluating pairs in an array and swapping larger elements forward. Largest element iteratively 'bubbles' to the end of the array

- Repeatedly swaps adjacent elements if they’re in the wrong order
	- Largest value ‘bubbles’ up to the end
- Considered a simple sorting algorithm
### Use Cases:
- Good for small number of items - Where asymptotic inefficiency is not high
- Good for a list thats nearly sorted
- Not good for large, high unordered sets

### Steps:
1. Create a loop that continues until no elements have been swapped
2. Within the loop, iterate through elements in the array
3. Grab two sequential elements
4. If those elements are out of numerical order, swap the elements
5. Record that a swap has been made
6. Repeat until no swaps have been made

### Examples:
- [Python](./bubble_sort.py)

- - - -

## Insertion Sort
### Runtime:
**O(n^2)** Average and worst case
Memory: O(1)

### Description:
This sort works in-place and is stable. It works by building a final sorted array, one item at a time. Insertion sort maintains two subarrays, a sorted and non-sorted array, and iteratively selects items to place into their correct place in the sorted array.

- Maintains two subarrays within given array:
	1. Already sorted array
	2. Remaining unsorted array
- Takes each item and deals with it one at a time building the final sorted array in place. Similar to sorting a hand of cards

### Use Cases:
- Good for use with smaller data sets. Preferable, performance-wise over bubble and selection sort

### Steps:
1. Consider the first element in the array to be sorted
2. Iterate from index 1 through end of the array
3. Insert next value from unsorted array into sorted side of array
	1. Backtrack through sorted array from i-1 to zero
	2. If the value being inserted is < element in sorted side, swap them

### Examples:
- [Python](./insertion_sort.py)
- [Python - Recursive](./insertion_sort_recur.py)

- - - -

## Merge Sort
### Runtime:
**O(n log n)** Average and worst case
Memory: varies

### Description:
This sort considered to be an efficient, comparison based, general purpose sorting algorithm. Merge sort is a divide and conquer algorithm. This sort works by repeatedly dividing the array to be sorted into smaller subarrays until the subarrays are of length 1. Arrays of length 1 are implicitly sorted, so this algorithm will merge all subarrays until the array is fully sorted.

- Divide and conquer algorithm
- Divides input into two halves, sorts the two halves and then merges the sorted halves
- Faster but requires more memory
- Heavy lifting takes place in merging two halves

### Use Cases:
- Considered more efficient for large sets of data when compared to other sorts such as selection, insertion and bubble
- Often choosen when sorting linked lists

### Steps:
1. Find the middle point of the array to be sorted
2. Call merge sort on the first half of the array
3. Call merge sort on the second half of the array
4. Merge both sides together
	1. Create an empty array to hold sorted/merged elements
	2. Initialize counters to track indices of both sides being merged
	3. Iterate while both sides still have values to merge
	4. Add lowest value among both sides to the merged array and increment index of that side
	5. Return merged array with any remaining values from remaining side which are implicitly sorted/higher than merged arrays highest value


### Examples:
- [Python](./merge_sort.py)

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
