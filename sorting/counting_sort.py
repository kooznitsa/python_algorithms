"""COUNTING SORT
-----
This stable algorithm is good for sorting arrays consisting of small integers with multiple counts.
1. Find the maximum element in the array.
2. Initialize an array of length max+1 with all elements 0. 
This array is used for storing the count of the elements in the array.
3. Store the count of each element at their respective index in count array.
4. Store cumulative sum of the elements of the count array.
5. Find the index of each element of the original array in the count array.
6. After placing each element at its correct position, decrease its count by one.
-----
Time complexity: O(n + M), where M is the maximum number
"""

from collections import defaultdict


def countint_sort_0(arr: list, key: int = lambda x: x) -> list:
    res = []
    counts = defaultdict(list)
    for x in arr:
        counts[key(x)].append(x)
    for k in range(min(counts), max(counts) + 1):
        res.extend(counts[k])
    return res


def counting_sort_1(arr: list) -> None:
    size = len(arr)
    maximum = max(arr) + 1
    output = [0] * size

    # Initialize count array
    count = [0] * maximum

    # Store the count of each elements in count array
    for i in range(0, size):
        count[arr[i]] += 1

    # Store the cummulative count
    for i in range(1, maximum):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # Place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        arr[i] = output[i]


if __name__ == '__main__':
    arr = [3, 3, 2, 1, 2, 3, 3, 2, 2, 1, 1, 2]
    assert countint_sort_0(arr) == sorted(arr)
    counting_sort_1(arr)
    print(arr)