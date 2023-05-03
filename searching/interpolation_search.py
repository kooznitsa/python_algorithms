"""INTERPOLATION SEARCH
-----
The array should contain unique values.
Steps:
1. In a loop, calculate the value of “pos” using the probe position formula. 
2. If it is a match, return the index of the item, and exit. 
3. If the item is less than arr[pos], calculate the probe position of the left sub-array. 
Otherwise, calculate the same in the right sub-array. 
4. Repeat until a match is found or the sub-array reduces to zero.
-----
Time complexity: O(n) worst case, O(log(log n)) best case
"""


def interpolation_search(arr: list, x: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1

        # Probing the position with keeping
        # uniform distribution in mind
        pos = low + (((high - low) // (arr[high] - arr[low])) * (x - arr[low]))

        # Condition of target found
        if arr[pos] == x:
            return pos

        # If x is larger, x is in upper part
        if arr[pos] < x:
            low = pos + 1

        # If x is smaller, x is in lower part
        else:
            high = pos - 1

    return -1


if __name__ == '__main__':
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    item = 18

    assert interpolation_search(arr, item) == arr.index(item)
    assert interpolation_search(arr, 200) == -1