"""DIVIDE AND CONQUER. ARRAY INVERSIONS
-----
Array inversion: if an element that comes earlier is bigger than that that comes later.
This algorithm is used to compare two ordered arrays, for "collaborative filtering" — 
making automatic predictions about the interests of a user by collecting 
preferences or taste information from many users.
-----
Input: array A of n integers
Output: number of inversions, pairs of array indexes (i, j) 
where i < j and A[i] > A[j]
-----
Maximum number of inversions = (n * (n - 1)) / 2
In the array [1, 3, 5, 2, 4, 6] there are 3 inversions:
(5, 2), (3, 2), (5, 4)
-----
Left inversion: i, j <= n / 2
Right inversion: i, j > n / 2
Split inversion: i <= n / 2 < j
-----
Time complexity: O(n * log n)
"""


def count_inv(
        arr: list, 
        temp_arr: list, 
        left: list, 
        right: list
    ) -> int:
    """Recursively divides list in halves to be sorted."""
    inv_count = 0

    if left < right:
        mid = (left + right) // 2
        inv_count += count_inv(arr, temp_arr, left, mid)
        inv_count += count_inv(arr, temp_arr, mid + 1, right)
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count


def merge(
        arr: list, 
        temp_arr: list, 
        left: list, 
        mid: int, 
        right: list
    ) -> int:
    """Merges two subarrays in a single sorted subarray.
    i: starting index of left subarray
    j: starting index of right subarray
    k: starting index of to be sorted subarray
    """
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += mid - i + 1
            k += 1
            j += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count


if __name__ == '__main__':
    tests = [
        ([1, 2, 3, 4], 0),
        ([1, 3, 5, 2, 4, 6], 3),
        ([1, 20, 6, 4, 5], 5),
        ([8, 7, 6, 5, 4, 3, 2, 1], 28),
        ([54044, 14108, 79294, 29649, 25260, 60660, 2995, 53777, 49689, 9083], 28),
    ]
    for arr, res in tests:
        n = len(arr)
        temp_arr = [0] * n
        assert count_inv(arr, temp_arr, 0, n - 1) == res