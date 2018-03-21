# Sorting
- Used to place elements of a list in a certain order
- Beyond obvious benefits of having a sorted data structure, sorting allows efficient searching
	- Searching from random group -> difficult
	- Searching from sorted group -> easier
- Stable sort algorithms sort identical elements in the same order as they appear when inputed
- - - -

- [Practice Problems](#interview-questions)


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

## Quick Sort
### Runtime:
**O(n log n)** Average, Worst: O(n^2)
Memory: O(log n)

### Description:
Quick sort is another divide and conquer sorting algorithm that works in-place and is a comparison sort. This sort works by finding a partition value and moving all elements smaller than the partition value to the left of it and all items greater than the partition value to the right of it.

- We pick a partition spot, usually the last element, and move all elements lower than the partitions value before it and all elements higher than partition spot after it. Basically,  putting the value of the partition index in its correct spot on each call and then updating the call to take the elements below and the elements above it
- Heavy lifting takes place in the partition step
- Performance varies depending on how or where you choose your partition pivot
- Not stable ie same value elements dont remain in the same order
- Two popular partition schemes: Lomuto and Hoare
	- Hoare is considered more performant

### Use Cases:
- Not good when same value items need to remain in order
- Operates in place so uses less memory than merge sort
- Merge sort generally preferred over this with very large data sets

### Steps:
1. Pick a pivot point from the array
2. Reorder the array so that elements < pivot come before the pivot and elements > pivot come after the pivot
	1. Grab low index as start of compare point
	2. Grab high index value as our pivot value
	3. Iterate from low to high index
	4. If we find a value at index thats <= our pivot value
	5. Swap our compare point with our index values
	6. Increment our pivot point compare index
	7. Swap pivot value with pivot index value
3. Call QuickSort on the remaining sides > and < the pivot point

### Examples:
- [Python - Lomuto Partition](./quick_sort.py)
- [Python - Hoare Partition](./quick_sort_hoare.py)


***

## Bucket Sort
### Runtime:
**O(n^2)** Can be O(n) with evenly distributed data set
Memory: O(n*k)

### Description:
Bucket sort is another divide and conquer sort. It works by putting the array into a series of buckets distributed in the range of the data and then sorts the buckets before recombinding them. This sort works best when you have a uniformly distributed data set

### Use Cases:
- Good for data like sorting people based on age when the values are uniformly distributed

### Steps:
1. Get max value and length from array being sorted
2. Create an array of buckets thats the lenght of the array being sorted
3. Iterate through the array being sorted
4. Place values into buckets corresponding to the value * array length / max value + 1
5. Sort each of the buckets with any sorting algorithm
6. Return flattened array of buckets

### Examples:
- [Python](./bucket_sort.py)

### Heap Sort
TODO
***

### Radix Sort
TODO


## Interview Questions
- [Sorted Merge](./interview_questions.md#sorted-merge)
