# Bottom Up Algorithms Vs Recursion
A bottom up approach can be used to avoid recursion while at the same time optimize memory usage that occurs with recursive solutions.

In a recursive solution, the call stack grows as the number of recursive calls grow.
For example a recursive factorial solution:

```python
  def factorial(n):
    if n in (1, 0):
      return 1
    return n * factorial(n-1)  
```

In the above factorial solution, the call stack grows O(n) relative to the starting input.

A bottom up approach may look something like this:

```python
  def factorial(n):
    res = 1
    for i in range(res,n + 1):
      res *= i
    return res   
```

This approach starts with our recusive base case and builds up from there. It may not be as elegant a solution, however, it uses O(1) space regardless of the input value.

Some languages support tail recursion as a way to optimize the memory usage and avoid building up the call stack. Python does not support tail recursion optimization and only some Ruby interpreters do.

Here is a tail recursive example. Notice how the result is included in the method signature so that when we reach the last recursive call, the result is returned rather than bubbling back up through the previous calls. 

```python
  def factorial(res, n):
    if n == 1:
      return res
    return factorial(res * n, n - 1)

```
