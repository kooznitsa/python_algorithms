def get_components(num: int) -> None:
    """find the maximum number k for which n can be represented 
    as the sum of k different components. 
    Print number k in the first line, k terms in the second line.
    """
    result = []
    rest = num

    i = 1
    while i <= num + 1:
        num -= i
        if num > i:
            result += [i]
            rest -= i
        i += 1
    result += [rest]

    print(len(result))
    print(*result, sep=' ')


if __name__ == '__main__':
    num = int(input())
    get_components(num)
