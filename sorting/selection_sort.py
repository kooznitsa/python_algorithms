""""SELECTION SORT
-----
1. Find index of the smallest value.
2. Find the smallest element in the list, pop it and save to a new array.
-----
Time complexity: O(n ** 2)
"""

import sys
sys.path.append('./')

from random import randint
from decorators.test_time_exec import test_time_exec


def find_smallest(arr: list) -> int:
    """ Find the index of the smallest value in a list."""
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


@test_time_exec(iters=1)
def selection_sort(arr: list) -> list:
    """Sort list by selection.
    Works faster than selection_sort_1.
    """
    new_arr = []
    for _ in range(1, len(arr) + 1):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


@test_time_exec(iters=1)
def selection_sort_1(arr):
    for i in range(len(arr)):
        k = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[k]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]


if __name__ == '__main__':
    arr_0 = [randint(1, 100) for _ in range(1000)]
    print(selection_sort(arr_0))

    arr_1 = [randint(1, 100) for _ in range(1000)]
    selection_sort_1(arr_1)
    print(arr_1)