"""DIVIDE AND CONQUER. MERGE SORT
-----
1. Divide the unsorted list into n sublists, each containing one element 
(a list of one element is considered sorted).
2. Repeatedly merge sublists to produce new sorted sublists 
until there is only one sublist remaining. 
This will be the sorted list.
-----
Time complexity: O(n * log n)
"""

from random import randint
from collections import deque


def merge(left: list, right: list) -> list:
    """Merge two sorted lists into one."""
    result = []
    i, j = 0, 0

    while i <= len(left) - 1 and j <= len(right) - 1:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i > len(left) - 1:
        while j <= len(right) - 1:
            result.append(right[j])
            j += 1
    else:
        while i <= len(left) - 1:
            result.append(left[i])
            i += 1

    return result


def recursive_merge_sort_0(nums: list) -> list:
    """Perform recursive merge sort algorithm."""
    if len(nums) == 1:
        return nums
    
    mid = (len(nums) - 1) // 2
    left = recursive_merge_sort_0(nums[:mid + 1])
    right = recursive_merge_sort_0(nums[mid + 1:])

    return merge(left, right)


def recursive_merge_sort_1(nums: list) -> deque:
    """Perform recursive merge sort algorithm
    without merge function.
    """
    mid = len(nums) // 2
    left, right = nums[:mid], nums[mid:]

    if len(left) > 1:
        left = recursive_merge_sort_1(left)
    if len(right) > 1:
        right = recursive_merge_sort_1(right)

    res = deque()

    while left and right:
        if left[-1] >= right[-1]:
            res.appendleft(left.pop())
        else:
            res.appendleft(right.pop())

    return deque(left or right) + res


def iterative_merge_sort(nums: list) -> list:
    """Perform iterative merge sort algorithm."""
    d = deque()
    for i in nums:
        d.append([i])
    while len(d) > 1:
        d.append(merge(d.pop(), d.pop()))
    return d.pop()


if __name__ == '__main__':
    nums = [randint(1, 999) for _ in range(10)]

    assert (
        recursive_merge_sort_0(nums) 
        == list(recursive_merge_sort_1(nums)) 
        == iterative_merge_sort(nums) 
        == sorted(nums)
    )