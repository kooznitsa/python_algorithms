# Big O notation

- **O (Big O)**: strict maximum complexity; the algorithm under no circumstances will run longer (f(n) <= O(g(n))).
- **Θ (Big Theta)**: approximate complexity (f(n) = Θ(g(n))).
- **Ω (Big Omega)**: strict notation of the lower bound; the algorithm will not run faster than this value (f(n) >= Ω(g(n))).

![big_o.png](https://raw.githubusercontent.com/kooznitsa/python_algorithms/main/__images/big_o.png)

**Big O run times, from fastest to slowest:**

| Big O            | Name               | Example                                             |
| :---------------:| :----------------: | :-------------------------------------------------: |
| O(1)             | Constant           | Determining if a binary number is even or odd       |
| O(log log n)     | Double logarithmic | Interpolation search                                |
| O(log n)         | Log                | Binary search                                       |
| O(n)             | Linear             | Simple search                                       |
| O(n * log n)     | Loglinear          | Quicksort, heapsort, mergesort                      |
| O(n ** 2)        | Quadratic          | Selection sort, bubble sort, insertion sort         |
| O(2 ** n)        | Exponential        | Brute-force equivalence of 2 statements             |
| O(n!)            | Factorial          | Traveling salesperson via brute-force search        |

![array_sorting.png](https://raw.githubusercontent.com/kooznitsa/python_algorithms/main/__images/array_sorting.png)

**Examples of specific times:**

| n         | 1     | 10               | 100                | 1,000             |
| :--------:| :---: | :--------------: | :----------------: | :---------------: |
| log n     | 0     | 3.32             | 6.64               | 9.97              |
| n * log n | 0     | 33.22            | 664.39             | 9,965.78          |
| n ** 2    | 1     | 100              | 10,000             | 1,000,000         |
| n ** k    | 1     | 10 ** k          | 100 ** k           | 1,000 ** k        |
| 2 ** n    | 2     | 1,024            | 1.3 * (10 ** 30)   | 10 ** 301         |
| n!        | 1     | 3,628,800        | 9.33 * (10 ** 157) | 4 * (10 ** 2,567) |

You take only the fastest-growing term and ignore constants and terms that grow more slowly:

f + g = O(max(f, g))
(n ** 2) + n = O(n ** 2), (2 ** n) + (n ** 9) = O(2 ** n)