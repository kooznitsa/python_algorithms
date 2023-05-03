"""DIVIDE AND CONQUER. QUICKSORT
-----
1. Pick a pivot.
2. Partition the array into 2 sub-arrays: 
    - elements less than the pivot and 
    - elements greater than the pivot.
If the array contains a lot of the same elements, partition 
the array into 3 sub-arrays (+ elements equal to the pivot).
Partition explained: https://www.youtube.com/watch?v=MZaf_9IZCrc
3. Call quicksort recursively on the 2 (or 3) sub-arrays.
-----
Time complexity: O(n * log n) on average,
O(n ** 2) worst case;
O(log n) with tail recursion eliminated.
"""

from random import randint, choice


def quicksort(arr: list) -> list:
    """Base case: arrays with 0 or 1 element are already “sorted.”
    Recursive case: arr[0].
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    

def random_quicksort(arr: list) -> list:
    """Base case: arrays with 0 or 1 element are already “sorted.”
    Recursive case: random element as a pivot.
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = choice(arr)
        arr.remove(pivot)
        less = [i for i in arr if i <= pivot]
        greater = [i for i in arr if i > pivot]
        return random_quicksort(less) + [pivot] + random_quicksort(greater)
    

if __name__ == '__main__':
    arr = [randint(1, 999) for _ in range(10)]
    print(quicksort(arr))
    print(random_quicksort(arr))