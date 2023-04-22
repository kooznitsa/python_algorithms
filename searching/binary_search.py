"""DIVIDE AND CONQUER. BINARY SEARCH
-----
1. Sort the list if not sorted.
2. Find the middle number.
3. Eliminate half the remaining numbers.
4. Repeat 2–3 until the number is found.
-----
Time complexity: O(log n)
(100 elements => 7 guesses (log(100, 2) = 6.64))
"""

import sys
from bisect import bisect_left


def binary_search_0(array: list[int], key: int) -> int:
    """Given two arrays: sorted numbers and keys,
    return index of each number, starting from 0.
    If not found, return -1.
    """
    left = 0
    right = len(array) - 1
    mid = 0

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def binary_search_1(array: list[int], key: int) -> int:
    """Given two arrays: sorted numbers and keys,
    return index of each number, starting from 1.
    If not found, return -1.
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == key:
            return mid + 1
        elif array[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def binary_search_with_bisect_0(array: list[int], key: int) -> int:
    """Perform binary search using the bisect module, index starting from 0.
    i < low : array[i] < key
    i > low : array[i] >= key
    """
    low = bisect_left(array, key)
    if low < len(array) and array[low] == key:
        return low
    return -1


def binary_search_with_bisect_1(array: list[int], key: int) -> int:
    """Perform binary search using the bisect module, index starting from 1.
    i < low : array[i] < key
    i > low : array[i] >= key
    """
    low = bisect_left(array, key)
    if low < len(array) and array[low] == key:
        return low + 1
    return -1
    

if __name__ == '__main__':
    """Sample input:
    5 1 5 8 12 13
    5 8 1 23 1 11
    Output: 2 0 -1 0 -1 (index starting from 0)
    or 3 1 -1 1 -1 (index starting from 1)
    """
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *array = next(reader)
    k, *keys = next(reader)

    print(*[binary_search_0(array, key) for key in keys], sep=' ')
    print(*[binary_search_with_bisect_0(array, key) for key in keys], sep=' ')
    
    print(*[binary_search_1(array, key) for key in keys], sep=' ')
    print(*[binary_search_with_bisect_1(array, key) for key in keys], sep=' ')