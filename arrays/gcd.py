def gcd(a: int, b: int) -> int:
    """Greatest common denominator. Euclid’s algorithm.
    Using cycle.
    """
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)


def gcd(a: int, b: int) -> int:
    """Greatest common denominator. Euclid’s algorithm.
    Using recursion.
    """
    if a == 0 or b == 0:
        return max(a, b)
    return gcd(b % a, a)


def main() -> None:
    a, b = map(int, input().split())
    print(gcd(a, b))

if __name__ == '__main__':
    main()