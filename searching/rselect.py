"""RSELECT (RANDOMIZED SELECTION ALGORITHM, QUICKSELECT)
-----
Find the x-th smallest element in an array without sorting, based on QuickSort.
Input: array A consisting of n numbers and integer x which is in the array A.
Output: index of element x in the array A.
-----
Steps:
1. Select a random pivot (a base element).
2. Split the array around the pivot.
3. Make recursion calls.
4. Return element x in the partitioned array.
-----
Time complexity: Θ(n ** 2) worst case, O(n) best case
"""

from random import randrange, randint


def partition(arr: list, pivot_index: int = 0) -> tuple[list, int]:
    """Makes partitions in the array."""
    i = 0
    if pivot_index != 0:
        arr[0], arr[pivot_index] = arr[pivot_index], arr[0]
    for j in range(len(arr) - 1):
        if arr[j + 1] < arr[0]:
            arr[j + 1], arr[i + 1] = arr[i + 1], arr[j + 1]
            i += 1
    arr[0], arr[i] = arr[i], arr[0]
    return arr, i


def rselect(arr: list, x: int) -> int:
    """RSelect algorithm."""
    n = len(arr)
    if n == 1:
        return arr[0]
    
    partitioned, pivot_idx = partition(arr, randrange(n))
    
    if pivot_idx == x:
        return partitioned[pivot_idx]
    elif pivot_idx > x:
        return rselect(partitioned[:pivot_idx], x)
    else:
        return rselect(arr[pivot_idx + 1:], x - pivot_idx - 1)


if __name__ == '__main__':
    arr = [randint(1, 99) for _ in range(10)]
    x = randint(1, 10)
    assert rselect(arr, x) == sorted(arr)[x]