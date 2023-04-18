"""HEAPSORT
-----
1. Call the buildMaxHeap() (heapify()) function on the list. 
This builds a heap from a list in O(n) operations.
2. Swap the first element of the list with the final element. 
Decrease the considered range of the list by one.
3. Call the siftDown() function on the list to sift the new 
first element to its appropriate index in the heap.
4. Go to step 2 unless the considered range of the list is one element.
-----
Time complexity: O(n * log n)
"""


import heapq
from random import randint


def heapsort(arr):
    heapq.heapify(arr)
    result = []
    while arr:
        result.append(heapq.heappop(arr))
    return result


if __name__ == '__main__':
    arr_0 = [randint(1, 100) for _ in range(10)]
    print(heapsort(arr_0))