"""SHELL SORT
(For partly sorted arrays < 6000 elements)
-----
The method begins by sorting pairs of elements far apart from each other, 
then gradually narrows the gap between elements to be compared. 
Some out-of-place elements can be moved into position faster than 
what a simple nearest-neighbor exchange would, by starting with far apart elements.
-----
Time complexity: O(n * log n)
"""

from random import randint


def shell_sort(arr: list) -> list:
    distance = len(arr) // 2
    while distance > 0:
        for i in range(distance, len(arr)):
            temp = arr[i]
            j = i
            while j >= distance and arr[j - distance] > temp:
                arr[j] = arr[j - distance]
                j = j - distance
                arr[j] = temp
        distance //= 2
    return arr


if __name__ == '__main__':
    arr = [randint(1, 100) for _ in range(100)]
    assert shell_sort(arr) == sorted(arr)