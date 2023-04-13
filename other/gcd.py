"""GREATEST COMMON DENOMINATOR (GCD). EUCLID'S ALGORITHM
-----
1. If we subtract a smaller number from a larger one 
(we reduce a larger number), GCD doesn’t change. 
If we keep subtracting repeatedly the larger of two, we end up with GCD.
2. Instead of subtraction, if we divide the smaller number, 
the algorithm stops when we find the remainder 0.
-----
Time complexity: O(log n)
"""

from random import randint


def gcd_loop(a: int, b: int) -> int:
    """Using loop."""
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)


def gcd_recursive(a: int, b: int) -> int:
    """Using recursion."""
    if a == 0 or b == 0:
        return max(a, b)
    return gcd_recursive(b % a, a)


if __name__ == '__main__':
    a = randint(12, 63967072)
    b = randint(12, 63967072)

    print(gcd_loop(a, b))
    print(gcd_recursive(a, b))