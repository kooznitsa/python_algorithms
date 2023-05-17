"""GREEDY ALGORITHM. HUFFMAN CODE
-----
1. Create a leaf node for each symbol and add it to the priority queue.
2. While there is more than one node in the queue:
    1) Remove the two nodes of highest priority (lowest probability) from the queue.
    2) Create a new internal node with these two nodes as children and with 
    probability equal to the sum of the two nodes' probabilities.
    3) Add the new node to the queue.
3. The remaining node is the root node and the tree is complete.
-----
Time complexity: O(n ** 2) with an array,
O(n * log n) with a heap
"""

from heapq import heapify, heappush, heappop
from itertools import count


def huffman(seq: str | list, frq: list[int]) -> list:
    """Huffman's algorithm."""
    num = count()
    trees = list(zip(frq, num, seq))         # num ensures valid ordering
    heapify(trees)                           # A min-heap based on freq
    while len(trees) > 1:                    # Until all are combined
        fa, _, a = heappop(trees)            # Get the two smallest trees
        fb, _, b = heappop(trees)
        n = next(num)
        heappush(trees, (fa + fb, n, [a, b])) # Combine and re-add them
    return trees[0][-1]


if __name__ == '__main__':
    seq = 'abcdefghi'
    frq = [4, 5, 6, 9, 11, 12, 15, 16, 20]
    assert huffman(seq, frq) == [['i', [['a', 'b'], 'e']], [['f', 'g'], [['c', 'd'], 'h']]]


import heapq
import random
from string import ascii_letters
import sys


def create_heap(text: str) -> list:
    """Given a string (e. g. 'abacabad'):
    1. Count letters in the string (counter list).
    2. Take 2 smallest values and assign 0 and 1, respectively.
    3. Add tuples to a heap [('c', '0'), ('d', '1')].
    4. Concatenate letters ('cd'), add to the counter. 
    5. Repeat 2–4.
    Return a list of tuples: 
    [('c', '0'), ('d', '1'), ('b', '0'), ('cd', '1'), ('a', '0'), ('bcd', '1')].
    """
    counter = sorted({(text.count(i), i) for i in text})
    heap = []

    if len(set(text)) < 2:
        return [(0, text)]
    
    while len(counter) > 1:
        min_0, min_1 = heapq.nsmallest(2, counter)
        heap.extend([(0, min_0[1]), (1, min_1[1])])

        heapq.heappop(counter)
        heapq.heappop(counter)

        new_value = tuple(map(lambda x: x[0] + x[1], zip(min_0, min_1)))
        heapq.heappush(counter, new_value)

    return heap

def huffman_encode(text: str) -> tuple[str, dict]:
    """Count letters and concatenate values from right to left:
    с: 0 -> 1 -> 1 = 011
    a: 0 
    Return encoded string and a dictionary of values.
    """
    heap = create_heap(text)
    d = {}
    for char in set(text):
        for binary, value in reversed(heap):
            if char in value:
                d[char] = d.setdefault(char, '') + str(binary)
    return (
        ''.join(d[i] for i in text),
        dict(sorted(d.items()))
    )

def print_encode() -> None:
    """Print number of unique letters and the length of string.
    Then print letter: code.
    Finally, print the encoded string.
    """
    text = input()
    chars = set(text)
    new_text, d = huffman_encode(text)

    print(len(chars), len(new_text))
    print(*(f'{k}: {v}' for k, v in d.items()), sep='\n')
    print(new_text)


def huffman_decode(text: str, codes: dict) -> str:
    """Given the encoded string and a list of codes (letter: code),
    return the original string.
    """
    result = []
    for _ in text:
        for k, v in codes.items():
            if text.startswith(v):
                result.append(k)
                text = text[text.index(v) + len(v):]
    return ''.join(result)

def print_decode() -> None:
    """Print the original string."""
    _, *codes, text = [(i.strip().split()) for i in sys.stdin.readlines()]
    codes = {i[0][:-1]: i[1] for i in codes}
    print(huffman_decode(text[0], codes))


def huffman_test(n_iter: int = 100) -> None:
    """Test encode[decode]_huffman on random data."""
    for _ in range(n_iter):
        length = random.randint(0, 32)
        old_text = ''.join(random.choice(ascii_letters) for _ in range(length))
        new_text, codes = huffman_encode(old_text)
        assert huffman_decode(new_text, codes) == old_text


if __name__ == '__main__':
    huffman_test()