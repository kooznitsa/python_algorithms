"""DIVIDE AND CONQUER. GALLOPING SEARCH (DOUBLING SEARCH, STRUZIK SEARCH)
(Экспоненциальный поиск)
-----
This algorithm is used for unlimited or infinite arrays.
Steps:
1. Sort the array if it is not sorted.
2. Determine the range in which the searched element will most likely be located.
3. Within this range, use a binary search to find the index of the element.
    - Start with subarray size 1.
    - Compare its last element with x.
    - Then try size 2, then 4 and so on until last element of a subarray is not greater. 
    - Once we find an index i (after repeated doubling of i), we know that the element 
    must be present between i/2 and i. 
-----
Time complexity: O(log i) where i is the element's index
Worst case it's O(log n) if the searched element is the last element in the array 
(where n is the array's length)
"""

from random import choice, randint
from binary_search import binary_search_0


def galloping_search(arr: list, val: int) -> int:
    n = len(arr)
    if arr[0] == val:
        return 0
    index = 1
    while index < n and arr[index] < val:
        index *= 2
    return binary_search_0(arr[:min(index, n - 1)], val)


if __name__ == '__main__':
    arr = sorted(randint(0, 9) for _ in range(10))
    val = choice(arr)

    print(arr)
    print(f'Index of element {val}: {galloping_search(arr, val)}')