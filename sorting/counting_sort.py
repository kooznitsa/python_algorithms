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


def counting_sort(arr: list) -> None:
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
    counting_sort(arr)
    print(arr)