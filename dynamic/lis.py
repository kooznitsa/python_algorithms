"""DYNAMIC PROGRAMMING. LARGEST INCREASING SEQUENCE (LIS)
-----
Finds the length of the longest subsequence of a given sequence 
such that all elements of the subsequence are sorted in increasing order.
E. g., the length of LIS for [10, 22, 9, 33, 21, 50, 41, 60, 80] 
is 6 and LIS is [10, 22, 33, 50, 60, 80].
-----
1. Declare the list for LIS and initialize LIS values for all indexes.
2. Compute optimized LIS values in bottom up manner.
3. Pick maximum of all LIS values.
-----
Time complexity: O(n ** 2)
"""


def lis_bottom_up(arr):
    """Returns length of the LIS."""
    n = len(arr)
    d = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    return max(d)


def lis_bottom_up_2(arr):
    """Returns length of the LIS where each element 
    can be divided by the previous one.
    """
    n = len(arr)
    d = [1] * n
    for i in range(1, n):
        for j in range(i):
            if (arr[i] % arr[j] == 0) and (d[j] + 1 > d[i]):
                d[i] = d[j] + 1
    return max(d)


if __name__ == '__main__':
    arr = [1, 2, 2, 4, 6, 12, 36, 8, 7, 9, 16, 48, 48, 3, 9, 48, 96]
    print(lis_bottom_up(arr))
    print(lis_bottom_up_2(arr))