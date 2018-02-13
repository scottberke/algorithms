### Big-O
- Describes performance or complexity of an algorithm by measuring the upper bound on asymptotic growth
- Always assumes upper limit or max number of iterations and describes the worst case scenario
- Expressed as rate of growth relative to input size
- [Big-O Algorithm Complexity Cheat Sheet (Know Thy Complexities!) @ericdrowell](http://bigocheatsheet.com/)
- - - -

#### Law of Addition and Multiplication for O()
-  Focus on the dominant terms
- `O(n) + O(n + n) = O(n + n^2) = O(n^2)` <- because of dominant terms
	- Applicable for sequential operations
- `O(n) * O(n) = O(n * n) = O(n^2)`
	- Applicable with nested loops
- - - -

#### Constant Time: O(1)
- Always executes in constant size, regardless of the input size
	-  ex: `x == true`
- Can by applied with loops when the number of iterations is independent from the input

#### Linear Time: O(n)
- Performance grows linearly in direct proportion to the size of the input data set
- Searching a list to see if an element is present
- Iterative and recursive factorial implementations should fall in this category  

#### Quadratic Time: O(n^2)
- Performance directly proportional to the square size of input
- Examples: Bubble Sort, Insertion Sor

#### Exponential Time: O(2^n)
- Growth doubles with each additional input
	-  Exponential grows -> starts shallow and grows very quickly
- Recursive functions where theres more than one recursive call for each side of problem

#### Logarithmic Time: O(log n)
- Logarithmic growth or iterative halving of data set with each iteration
	- Doubling the size of an input does little to cause growth after the first iteration
- Size of input is reduced by a constant factor at each step
- Examples: Binary Search, Bisection search

#### Log-Linear Time: O(n * log n)
- The result of performing an O(log n) operation n times
- Examples: Merge Sort, Quick Sort, and many more


![assets/big_o-2a6e5.png](./assets/big_o-2a6e5.png)
