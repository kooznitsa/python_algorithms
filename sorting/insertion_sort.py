"""INSERTION SORT
-----
1. Iterate from arr[1] to arr[N] over the array. 
2. Compare the current element (key) to its predecessor. 
3. If the key element is smaller than its predecessor, compare it to the elements before. 
Move the greater elements one position up to make space for the swapped element.
-----
Time complexity: Θ(n ** 2)
"""

import sys
sys.path.append('./')

from random import randint
from decorators.test_time_exec import test_time_exec


@test_time_exec(iters=1)
def insertion_sort(arr: list) -> list:
    for i in range(len(arr)):
        j = i
        while j >= 1 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1
    return arr


if __name__ == '__main__':
    arr = [randint(1, 100) for _ in range(100)]
    assert insertion_sort(arr) == sorted(arr)