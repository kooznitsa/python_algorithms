"""RUSSIAN PEASANT MULTIPLICATION (RPM)
-----
To multiply A and B:
1. Put a smaller number A into division column and bigger number B into mutiplication column.
2. Division column: A // 2 until the number is 1.
3. Multiplication column: multiply B until the number of lines is equal to the division column.
4. From both columns remove lines where division column number % 2 == 0.
5. Sum all numbers in the multiplication column. That would be the result.
-----
Time complexity: Θ(log n)
"""

from random import randint


def rpm(a: int, b: int) -> int:
    if a > b:
        a, b = b, a

    halving = [a]
    while min(halving) > 1:
        halving.append(min(halving) // 2)
    
    doubling = [b]
    while(len(doubling) < len(halving)):
        doubling.append(max(doubling) * 2)

    filtered = filter(lambda x: x[0] % 2 == 1, zip(halving, doubling))
    return sum(i[1] for i in filtered)


if __name__ == '__main__':
    a, b = randint(2, 100), randint(2, 100)
    assert rpm(a, b) == a * b