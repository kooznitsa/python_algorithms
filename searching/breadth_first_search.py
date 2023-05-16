"""GRAPHS. BREADTH-FIRST SEARCH (BFS)
-----
BFS is used to calculate the shortest path in an unweighted graph (a graph without weights). 
It answers questions:
1. Is there a path from node A to node B?
2. What is the shortest path from node A to node B?
-----
Steps:
1. Keep a queue containing the elements to check.
2. Pop an element off the queue.
3. Check this element. If it is, you're done. If not, add all its neighbors to the queue.
4. Loop.
5. If the queue is empty, there is no element you're searching for.
-----
Time complexity: O(V + E)
(V for number of vertices (= nodes), E for number of edges)
"""

from typing import Generator, Optional
from collections import deque


def breadth_first(graph: dict, name: str, condition: bool) -> bool:
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        element = search_queue.popleft()
        if not element in searched:
            if condition:
                return True
            search_queue += graph[element]
            searched.append(element)
    return False


def bfs(graph: dict, start: str) -> dict:
    parents = {start: None}              # Parents
    Q = deque([start])                   # FIFO queue
    while Q:
        node = Q.popleft()               # Constant-time for deque
        for nxt in graph[node]:
            if nxt in parents:
                continue                 # Already has parent
            parents[nxt] = node          # Reached from node: node is parent
            Q.append(nxt)
    return parents


def iddfs(graph: dict, start: str) -> Generator:
    """Iterative Deepening Depth-First Search (IDDFS).
    There is one situation where IDDFS would be preferable over BFS: 
    when searching a huge tree.
    """
    yielded = set()                                         # Visited for the first time
    def recurse(
            graph: dict, 
            start: str, 
            depth: int, 
            S: Optional[set] = None
        ) -> Optional[Generator]:                           # Depth-limited DFS
        if start not in yielded:
            yield start
            yielded.add(start)
        if depth == 0:
            return                                          # Max depth zero: Backtrack
        if S is None:
            S = set()
        S.add(start)
        for node in graph[start]:
            if node in S:
                continue
            for nxt in recurse(graph, node, depth - 1, S):  # Recurse with depth - 1
                yield nxt
    n = len(graph)
    for depth in range(n):                                  # Try all depths 0...nxt - 1
        if len(yielded) == n:
            break                                           # All nodes seen?
        for node in recurse(graph, start, depth):
            yield node


def main():
    """Find a friend with a name ending in -m"""
    graph = {
        'Julia': ('Mark', 'Alex', 'Olga'),
        'Alex': ('Julia', 'Mariam'),
        'Mariam': ('Olga', 'Julia', 'Mark'),
        'Olga': (),
        'Mark': (),
    }
    name = 'Alex'
    condition = lambda x: x.endswith('m')
    print(breadth_first(graph, name, condition))


if __name__ == '__main__':
    main()