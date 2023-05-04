"""LINEAR SEARCH
-----
Iterates through a list. If the element is found, returns True.
-----
Time complexity: O(n)
"""

from random import randint, choice


def linear_search(arr: list[int], item: int) -> int:
    if item in arr:
        return arr.index(item)
    return -1


if __name__ == '__main__':
    arr = [randint(1, 99) for _ in range(10)]
    item = choice(arr)
    assert linear_search(arr, item) == arr.index(item)
    assert linear_search(arr, 200) == -1