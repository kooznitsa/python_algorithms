"""BUBBLE SORT
-----
1. Run a nested for loop to traverse the input array using two variables i and j, 
such that 0 ≤ i < n - 1 and 0 ≤ j < n - i - 1.
2. If arr[j] is greater than arr[j + 1], then swap these adjacent elements, else move on.
-----
Time complexity: O(n ** 2)
"""

from random import randint


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    arr = [randint(0, 9) for _ in range(10)]
    bubble_sort(arr)
    print(arr)