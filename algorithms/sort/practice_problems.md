# Practice Problems - Sorting

## Sorted Merge
Q) You're given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order.


- Test Cases: [Sorted Merge]((./sorted_merge_test.py))
- Solution: [Sorted Merge](./sorted_merge.py)

Source: CTCI p.149
***

## Group Anagrams
Q) Write a method to sort an array of strings so that all the anagrams are next to each other.

- Test Cases: [Group Anagram](./group_anagram_test.py)
- Solution: [Group Anagram](./group_anagram.py)

***

## Wiggle Sort
Q) Given an unsorted array `nums`, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]....`.

- Test Cases: [Wiggle Sort](./wiggle_sort_test.py)
- Solution: [Wiggle Sort](./wiggle_sort.py)

***

## Peaks And Valleys
Q) In an array of integers, a "peak" is an element which is greater than or equal to the adjacent integer and a "valley" is an element which is less than or equal to the adjacent integer. For example, in the array [5 ,8, 6, 2, 3, 4, 6], [8, 6] are peaks and [5, 2] are valleys. Given an array of integers, sort the array into an alternating sequence of peaks and valleys.
Example:
Input: [5, 3, 1, 2, 3]
Output: [5, 1, 3, 2, 3]
