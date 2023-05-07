# Algorithms

## Big O Notation

- **O (Big O)**: strict maximum complexity; the algorithm under no circumstances will run longer (f(n) <= O(g(n))).
- **Θ (Big Theta)**: approximate complexity (f(n) = Θ(g(n))).
- **Ω (Big Omega)**: strict notation of the lower bound; the algorithm will not run faster than this value (f(n) >= Ω(g(n))).

![big_o.png](https://raw.githubusercontent.com/kooznitsa/python_algorithms/main/images/big_o.png)

**Big O run times, from fastest to slowest:**

| Big O         | Name               | Examples                                      |
| ------------- | ------------------ | --------------------------------------------- |
| O(1)          | Constant           | Determining if a binary number is even or odd |
| O(log log n)  | Double logarithmic | Interpolation search                          |
| O(log n)      | Log(arithmic)      | Binary search                                 |
| O(n)          | Linear             | Linear search, iterating over a list          |
| O(n \* log n) | Loglinear          | Quicksort, heapsort, mergesort                |
| O(n \*\* 2)   | Quadratic          | Selection sort, bubble sort, insertion sort   |
| O(n \*\* 3)   | Cubic              | Floyd and Warshall’s algorithms               |
| O(n \*\* k)   | Polynomial         | k nested for loops over n, k > 0              |
| O(k \*\* n)   | Exponential        | Producing every subset of n items             |
| O(n!)         | Factorial          | Traveling salesperson via brute-force search  |

**Examples of operations:**

- O(1): accessing a dictionary by key; push/pop from a stack.
- O(log n): volume of data decreases with each iteration.
- O(n): searching for an element in an array; finding a minimum element in an array.
- O(n \*\* 2): 2 nested foor loops.
- O(n \*\* 3): 3 nested foor loops.
- O(n!): producing every ordering of n values.

![array_sorting.png](https://raw.githubusercontent.com/kooznitsa/python_algorithms/main/images/array_sorting.png)

**Examples of specific times:**

| n          | 1   | 10        | 100                   | 1,000                |
| ---------- | --- | --------- | --------------------- | -------------------- |
| log n      | 0   | 3.32      | 6.64                  | 9.97                 |
| n \* log n | 0   | 33.22     | 664.39                | 9,965.78             |
| n \*\* 2   | 1   | 100       | 10,000                | 1,000,000            |
| n \*\* k   | 1   | 10 \*\* k | 100 \*\* k            | 1,000 \*\* k         |
| 2 \*\* n   | 2   | 1,024     | 1.3 \* (10 \*\* 30)   | 10 \*\* 301          |
| n!         | 1   | 3,628,800 | 9.33 \* (10 \*\* 157) | 4 \* (10 \*\* 2,567) |

You take only the fastest-growing term and ignore constants and terms that grow more slowly:

f + g = O(max(f, g))
(n ** 2) + n = O(n ** 2)
(2 ** n) + (n ** 9) = O(2 \*\* n)

## Recurrences

The recurrence describes the running time of an algorithm that divides a problem of size n into subproblems which are solved recursively.

A recurrence relation is an equation that relates a function to itself, in a recursive way (such as T(n) = T(n/2) + 1). These equations are often used to describe the running times of recursive algorithms.

Some important recurrences (one or two recursive calls on problems of size n – 1 or n / 2, with either constant or linear additional work in each call).

| Recurrence         | Solution     | Example                                         |
| ------------------ | ------------ | ----------------------------------------------- |
| T(n) = T(n–1) + 1  | Θ(n)         | Processing a sequence, for example, with reduce |
| T(n) = T(n–1) + n  | Θ(n \*\* 2)  | Handshake problem                               |
| T(n) = 2T(n–1) + 1 | Θ(2 \*\* n)  | Towers of Hanoi                                 |
| T(n) = 2T(n–1) + n | Θ(2 \*\* n)  |                                                 |
| T(n) = T(n/2) + 1  | Θ(lg n)      | Binary search                                   |
| T(n) = T(n/2) + n  | Θ(n)         | Randomized Select, average case                 |
| T(n) = 2T(n/2) + 1 | Θ(n)         | Tree traversal                                  |
| T(n) = 2T(n/2) + n | Θ(n \* lg n) | Sorting by divide and conquer                   |

Three main ways of solving recurrences:

1. Repeatedly apply the original equation to unravel the recursive occurrences of T until you find a pattern.
2. Guess a solution, and try to prove that it’s correct using induction.
3. For divide and conquer recurrences that fit one of the cases of the master theorem, simply use the corresponding solution.

- **Reduction** means transforming one problem to another. We normally reduce an unknown problem to one we know how to solve. The reduction may involve transforming both the input (so it works with the new problem) and the output (so it’s valid for the original problem).
- **Induction** is used to show that a statement is true for a large class of objects (often the natural numbers). We do this by first showing it to be true for a base case (such as the number 1) and then showing that it “carries over” from one object to the next (if it’s true for n –1, then it’s true for n).
- **Recursion** is what happens when a function calls itself. Here we need to make sure the function works correctly for a (nonrecursive) base case and that it combines results from the recursive calls into a valid solution.

Example of perfectly balanced binary tree:
![binary_tree.png](https://raw.githubusercontent.com/kooznitsa/python_algorithms/main/images/binary_tree.png)

## Divide and Conquer (D&C) Algorithms

1. Figure out a simple case as the base case. If you're using D&C on a list, the best case is probably an empty array or an array with one element.
2. Figure out how to reduce your problem and get to the best case.
3. Merge solutions to subproblems into the solution of the original problem.

**Examples:**

- [Array inversions](https://github.com/kooznitsa/python_algorithms/blob/main/other/array_inversions.py)
- [Binary search](https://github.com/kooznitsa/python_algorithms/blob/main/searching/binary_search.py)
- [Galloping search](https://github.com/kooznitsa/python_algorithms/blob/main/searching/galloping_search.py)
- [Jump search](https://github.com/kooznitsa/python_algorithms/blob/main/searching/jump_search.py)
- [Karatsuba algorithm](https://github.com/kooznitsa/python_algorithms/blob/main/other/karatsuba.py)
- [Merge sort](https://github.com/kooznitsa/python_algorithms/blob/main/sorting/merge_sort.py)
- [Quicksort](https://github.com/kooznitsa/python_algorithms/blob/main/sorting/quicksort.py)

## Greedy Algorithms

At each step, you pick the locally optimal solution, and in the end you’re left with the globally optimal solution.

**Examples:**

- [Dijkstra's algorithm](https://github.com/kooznitsa/python_algorithms/blob/main/searching/dijkstra.py)
- [Huffman code](https://github.com/kooznitsa/python_algorithms/blob/main/greedy/huffman.py)
- [Knapsack problem](https://github.com/kooznitsa/python_algorithms/blob/main/greedy/knapsack.py)
- [Traveling Salesman Problem](https://github.com/kooznitsa/python_algorithms/blob/main/greedy/tsp.py)

## Dynamic Programming

- Dynamic programming is useful when you’re trying to optimize something given a constraint.
- Dynamic programming starts by solving subproblems and builds up to solving the big problem.
- Dynamic programming only works when each subproblem is discrete — when it doesn’t depend on other subproblems.
- Every dynamic-programming solution involves a grid (matrix).
- Each cell is a subproblem. Think about how you can divide your problem into subproblems. That will help you figure out what the axes are.
- The values in the cells are usually what you’re trying to optimize.

**Examples:**

- [Edit distance](https://github.com/kooznitsa/python_algorithms/blob/main/dynamic/edit_distance.py)
- [Knapsack problem](https://github.com/kooznitsa/python_algorithms/blob/main/dynamic/knapsack.py)
- [Largest Increasing Sequence (LIS)](https://github.com/kooznitsa/python_algorithms/blob/main/dynamic/lis.py)