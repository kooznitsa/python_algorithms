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
sys.path.append('./')

from decorators.test_time_exec import test_time_exec


@test_time_exec(iters=1)
def binary_search(array: list[int], key: int) -> int:
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


if __name__ == '__main__':
    array = map(int, input().split())
    keys = map(int, input().split())

    print(*[binary_search(array, k) for k in keys], sep=' ')
