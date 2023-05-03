# Algorithms

## Big O Notation

- **O (Big O)**: strict maximum complexity; the algorithm under no circumstances will run longer (f(n) <= O(g(n))).
- **Θ (Big Theta)**: approximate complexity (f(n) = Θ(g(n))).
- **Ω (Big Omega)**: strict notation of the lower bound; the algorithm will not run faster than this value (f(n) >= Ω(g(n))).

![big_o.png](https://raw.githubusercontent.com/kooznitsa/python_algorithms/main/images/big_o.png)

**Big O run times, from fastest to slowest:**

| Big O         | Name               | Example                                       |
| ------------- | ------------------ | --------------------------------------------- |
| O(1)          | Constant           | Determining if a binary number is even or odd |
| O(log log n)  | Double logarithmic | Interpolation search                          |
| O(log n)      | Log                | Binary search                                 |
| O(n)          | Linear             | Simple search                                 |
| O(n \* log n) | Loglinear          | Quicksort, heapsort, mergesort                |
| O(n \*\* 2)   | Quadratic          | Selection sort, bubble sort, insertion sort   |
| O(2 \*\* n)   | Exponential        | Brute-force equivalence of 2 statements       |
| O(n!)         | Factorial          | Traveling salesperson via brute-force search  |

**Examples of operations:**
- O(1): accessing a dictionary by key; push/pop from a stack.
- O(log n): volume of data decreases with each iteration.
- O(n): searching for an element in an array; finding a minimum element in an array.
- O(n ** 2): 2 nested foor loops.
- O(n ** 3): 3 nested foor loops.

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

At each step, you pick the locally optimal solution, and in the end you’re lef with the globally optimal solution.

**Examples:**

- [Dijkstra's algorithm](https://github.com/kooznitsa/python_algorithms/blob/main/searching/dijkstra.py)
- [Huffman code](https://github.com/kooznitsa/python_algorithms/blob/main/greedy/huffman.py)
- [Knapsack problem](https://github.com/kooznitsa/python_algorithms/blob/main/greedy/knapsack.py)

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