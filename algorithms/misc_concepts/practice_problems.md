# Practice Problems - Misc Concepts

## Triple Step
Q) A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.


- Test Cases: [Triple Step](./triple_step_test.py)
- Solution: [Triple Step](./triple_step.py)

***

## Robot In A Grid
Q) Imagine a robot sitting in the upper left corner of a grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are off limits such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.
* CTCI lists this under Chapter 8 (Recursion and Dynamic Programing) but, given the wording of the problem, it would be odd not to approach this as a graph traversal problem. Solution below includes a breadth first search approach and a recursive search approach

- Test Cases: [Robot In A Grid](./robot_in_grid_test.py)
- Solution: [Robot In A Grid](./robot_in_grid.py)

***

## Magic Index
Q) A magic index in an array A[0..n-1] is defined to be an index such that A[i] == i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists in array A.

- Test Cases: [Magic Index](./magic_index_test.py)
- Solution: [Magic Index](./magic_index.py)

***

## Permutations Of A String
Q) Write a program to return all permutations of a given string.

- Test Cases: [String Permutations](./string_perm_test.py)
- Solution: [String Permutations](./string_perm.py)

***

## English Int
Q) Given any integer, print an english phrase that describes the integer. (ie: "One Thousand, Two Hundred Thirty Four")

- Test Cases: [English Int](./english_int_test.py)
- Solution: [English Int](./english_int.py)

***

## Recursive Multiply
Q) Write a recursive function to multiply two positive integers without using the * operator. You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.

- Test Cases: [Recursive Multiply](./recursive_multiply_test.py)
- Solution: [Recursive Multiply](./recursive_multiply.py)
