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