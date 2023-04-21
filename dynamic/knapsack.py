"""DYNAMIC PROGRAMMING. KNAPSACK
-----
Columns (j) are knapsack sizes from 1 to 4 kg,
one row (i) for each item:
        1   2  3  4
Guitar |__|__|__|__|
Laptop |__|__|__|__|
Book   |__|__|__|__|

Te grid starts out empty. Fill in each cell of the grid.
Once the grid is filled in, you’ll have your answer to the problem.

cell[i][j] = max(
    1. The previous max (value at cell[i - 1][j])
    vs
    2. Value of current item + value of the remaining space
    (cell[i - 1][j - item's weight])
)
-----
Time complexity: O(n * W) where W is max weight
"""

from collections import namedtuple
from functools import lru_cache


def knapsack(W: int, weights: list, costs: list) -> int:
    """Build matrix K[][] in bottom up manner."""
    n = len(weights)
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i - 1] <= w:
                K[i][w] = max(
                    costs[i - 1] + K[i - 1][w - weights[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


def knapsack_with_repetitions(W: int, weights: list, costs: list) -> int:
    """Knapsack with repetitions in bottom up manner."""
    K = [0] * (W + 1)
    for w in range(W + 1):
        for i in range(len(weights)):
            if weights[i] <= w:
                K[w] = max(K[w], K[w - weights[i]] + costs[i])
    return K[W]



Test = namedtuple('Test', 'max_weight weights result')
tests = [
    Test(10, [1, 4, 8], 9),
    Test(139, [2, 3, 4, 8, 10, 20, 100], 139),
    Test(7419, [2, 3, 4, 8, 10, 400, 7000], 7419),
    Test(1000, [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 
                7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 
                9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 
                10, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 
                13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15,
                15, 15, 15, 15, 15, 15], 946),
]


if __name__ == '__main__':
    for t in tests:
        output = knapsack(t.max_weight, t.weights, t.weights)
        assert output == t.result
    
    assert knapsack_with_repetitions(10, [6, 3, 4, 2], [30, 14, 16, 9]) == 48