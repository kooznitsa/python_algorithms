"""DIVIDE AND CONQUER. KARATSUBA ALGORITHM
-----
{Input: binary integers x, y >= 0}
{Output: x * y}
1. Fall back to traditional multiplication.
2. Calculate the size of the numbers.
3. Split the digit sequences in the middle.
4. Perform 3 recursive calls made to numbers approximately half the size.
5. Sum results.
-----
Time complexity: O(n ** 1.59)
"""

from random import randint


def length(x: int) -> int:
    n = 0
    if x <= 1:
        return 1
    while x > 1:
        x >>= 1
        n += 1
    return n


def two_halfs(a: int, n: int) -> tuple[int, int]:
    half_n = n >> 1
    x_l = a >> (half_n)
    x_r = a & ((1 << half_n) - 1)
    return x_l, x_r


def karatsuba(x: int, y: int) -> int:
    n = max(length(x), length(y))

    if n == 1:
        return x * y
    
    half_n = n >> 1

    x_l, x_r = two_halfs(x, n)
    y_l, y_r = two_halfs(y, n)

    p1 = karatsuba(x_l, y_l)
    p2 = karatsuba(x_r, y_r)
    p3 = karatsuba(x_l + x_r, y_l + y_r)

    return (p1 << 2 * half_n) + ((p3 - p1 - p2) << half_n) + p2


if __name__ == '__main__':
    print(karatsuba(randint(3 ** 12, 9 ** 21), randint(3 ** 12, 9 ** 21)))