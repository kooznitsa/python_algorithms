from heapq import heappush, heappop
import sys


def create_queue() -> None:
    """Sample input:
    6
    Insert 200
    Insert 10
    ExtractMax
    Insert 5
    Insert 500
    ExtractMax
    Output:
    200
    500
    """
    _, *ops = (i.strip().split() for i in sys.stdin.readlines())
    heap = []
    for i in ops:
        heappush(heap, -int(i[1])) if 'Insert' in i else print(abs(heappop(heap)))
