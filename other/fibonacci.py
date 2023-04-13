"""FIBONACCI SEQUENCE"""

from random import randint


def fib(n: int) -> int:
    """Get N-th Fibonacci number."""
    f0, f1 = 0, 1
    for _ in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


def fib_digit(n: int) -> int:
    """Get last digit of the N-th Fibonacci number."""
    f = [0, 1]
    for i in range(2, n + 1):
        f.append((f[i - 1] + f[i - 2]) % 10)
    return f[-1]


def fib_mod(n: int, m: int) -> int:
    """Get N-th Fibonacci modulo. Examples:
    n = 6, m = 6 -> 2;
    n = 10, m = 2 -> 1;
    n = 1025, m = 55 -> 5;
    n = 1598753, m = 25897 -> 20305.
    """
    f = [0, 1]
    for i in range(2, n + 1):
        f.append((f[i - 2] + f[i - 1]) % m)
        if f[-2:] == [0, 1]:
            break
    if n > m:
        return f[n % len(f[:-2])]
    return f[-1]


if __name__ == '__main__':
    n = randint(1, 1000)
    m = randint(1, 55)

    print(fib(n))
    print(fib_digit(n))
    print(fib_mod(n, m))