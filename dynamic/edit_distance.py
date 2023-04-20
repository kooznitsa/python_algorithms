"""DYNAMIC PROGRAMMING. EDIT DISTANCE
-----
Input: A[0, ..., n], B[0, ..., m]
Output: matrix[i][j]
The minimum number of removals, insertions or substitutions of a character in the string
is called Levenshtein distance, or edit distance.
- Insertion: matrix[i][j - 1] + 1
- Removal: matrix[i - 1][j] + 1
- Substitution: matrix[i - 1][j - 1]
-----
Time complexity: O(n * m)
(n for length of array A, m for length of array B)
"""


def edit_dist_0(a, b):
    n = len(a)
    m = len(b)
    mx = [[0 for i in range(m + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                mx[i][j] = j

            elif j == 0:
                mx[i][j] = i

            elif a[i - 1] == b[j - 1]:
                mx[i][j] = mx[i - 1][j - 1]

            else:
                mx[i][j] = 1 + min(
                    mx[i][j - 1], mx[i - 1][j], mx[i - 1][j - 1])
    return mx[n][m]


def edit_dist_1(a, b):
    n = len(a)
    m = len(b)
    mx = [[i + j if i * j == 0 else 0 for j in range(m + 1)]
        for i in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                mx[i][j] = mx[i - 1][j - 1]
            else:
                mx[i][j] = 1 + min(mx[i - 1][j], mx[i][j - 1], mx[i - 1][j - 1])
    return mx[n][m]


tests = {
    ('ab', 'ab'): 0,
    ('short', 'ports'): 3,
    ('sunday', 'saturday'): 3,
    ('food', 'money'): 4,
    ('voldemort', 'dumbledore'): 7,
    ('geek', 'gesek'): 1,
}

if __name__ == '__main__':
    for k, v in tests.items():
        assert edit_dist_0(*k) == v
        assert edit_dist_1(*k) == v