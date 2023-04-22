"""DIVIDE AND CONQUER. JUMP SEARCH
-----
1. Sort the array if it is not sorted.
2. Determine the step size m by taking the sqrt of the length of the array n.
3. Start at the first element of the array and jump m steps until the value 
at that position is greater than the target value.
4. Once a value greater than the target is found, perform a linear search 
starting from the previous step until the target is found or it is clear 
that the target is not in the array.
5. If the target is found, return its index. 
If not, return -1 to indicate that the target was not found in the array.
-----
Time complexity: O(sqrt(n)) where sqrt(n) is jump size and n is the array's length
(In terms of performance, jump search is between linear and binary search.
This algorithm does not use the costly division operator (/).) 
"""


import math
from random import choice, randint


def jump_search(arr, val):
    length = len(arr)
    jump = int(math.sqrt(length))
    left, right = 0, 0

    while left < length and arr[left] <= val:
        right = min(length - 1, left + jump)
        if arr[left] <= val and arr[right] >= val:
            break
        left += jump

    if left >= length or arr[left] > val:
        return -1
    
    right = min(length - 1, right)
    i = left

    while i <= right and arr[i] <= val:
        if arr[i] == val:
            return i
        i += 1

    return -1


if __name__ == '__main__':
    arr = sorted(randint(0, 9) for _ in range(10))
    val = choice(arr)

    print(arr)
    print(f'Index of element {val}: {jump_search(arr, val)}')