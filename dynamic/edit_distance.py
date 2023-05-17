"""DYNAMIC PROGRAMMING. EDIT DISTANCE / LONGEST COMMON SEQUENCE (LCS)
-----
Input: A[0, ..., n], B[0, ..., m]
Output: matrix[i][j]
The minimum number of removals, insertions or substitutions of a character in the string
is called Levenshtein distance, or edit distance.

- Insertion: matrix[i][j - 1] + 1
- Removal: matrix[i - 1][j] + 1
- Substitution: matrix[i - 1][j - 1]

matrix[i][j] = 
    0                                          if i = 0 or j = 0
    1 + matrix[i - 1][j - 1]                   if ai = bj
    max(matrix[i - 1][j], matrix[i][j - 1])    otherwise
-----
Time complexity: O(n * m)
(n for length of array A, m for length of array B)
"""

from functools import wraps


def memo(func):
    """Memoization (caching) decorator"""
    cache = {}                        # Stored subproblem solutions
    @wraps(func)                      # Make wrap look like func
    def wrap(*args):                  # The memoized wrapper
        if args not in cache:         # Not already computed?
            cache[args] = func(*args) # Compute & cache the solution
        return cache[args]            # Return the cached solution
    return wrap                       # Return the wrapper

def rec_lcs(a, b): 
    """A Memoized Recursive Solution to the LCS Problem"""
    @memo                                # L is memoized
    def L(i, j):                         # Prefixes a[:i] and b[:j]
        if min(i, j) < 0: 
            return 0                     # One prefix is empty
        if a[i] == b[j]: 
            return 1 + L(i-1, j-1)       # Match! Move diagonally
        return max(L(i-1, j), L(i, j-1)) # Chop off either a[i] or b[j]
    return L(len(a)-1, len(b)-1)         # Run L on entire sequences

def lcs(a,b):
    """An Iterative Solution to the LCS Problem"""
    n, m = len(a), len(b)
    pre, cur = [0] * (n+1), [0] * (n+1)    # Previous/current row
    for j in range(1, m+1):                # Iterate over b
        pre, cur = cur, pre                # Keep prev., overwrite cur.
    for i in range(1, n+1):                # Iterate over a
        if a[i-1] == b[j-1]:               # Last elts. of pref. equal?
            cur[i] = pre[i-1] + 1          # L(i,j) = L(i-1,j-1) + 1
        else:                              # Otherwise...
            cur[i] = max(pre[i], cur[i-1]) # max(L(i,j-1),L(i-1,j))
    return cur[n]                          # L(n,m)


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