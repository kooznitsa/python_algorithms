"""LINEAR SEARCH
-----
Iterates through a list. If the element is found, returns True.
-----
Time complexity: O(n)
"""

from random import randint, choice


def linear_search(arr: list, item: int) -> bool:
    index = 0
    found = False

    while index < len(arr) and not found:
        if arr[index] == item:
            found = True
        else:
            index += 1
    return found


if __name__ == '__main__':
    arr = [randint(1, 99) for _ in range(10)]
    item = choice(arr)
    assert linear_search(arr, item) == True
    assert linear_search(arr, 200) == False