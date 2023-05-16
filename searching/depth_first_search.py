"""GRAPHS. DEPTH-FIRST SEARCH (DFS)
-----
The algorithm starts at the root node (selecting some arbitrary node as the root node 
in the case of a graph) and explores as far as possible along each branch before backtracking.
-----
Time complexity: O(V + E)
(V for number of vertices (= nodes), E for number of edges)
"""

from typing import Any, Generator


def depth_first(
        graph: dict[Any, set], 
        start: str, 
        visited: set = None
    ) -> set:
    """Recursive depth-first search."""
    if visited is None:
        visited = set()
    visited.add(start)

    for nxt in graph[start] - visited:
        depth_first(graph, nxt, visited)
    return visited


def iter_dfs(graph: dict[Any, set], start: str) -> Generator:
    """Iterative depth-first search."""
    visited = set()               # Visited-set
    Q = []                        # Queue
    Q.append(start)               # We plan on visiting start
    while Q:                      # Planned nodes left?
        nxt = Q.pop()             # Get one
        if nxt in visited:
            continue              # Already visited? Skip it
        visited.add(nxt)          # We've visited it now
        Q.extend(graph[nxt])      # Schedule all neighbors
        yield nxt                 # Report nxt as visited


if __name__ == '__main__':
    graph = {
        'Julia': {'Mark', 'Alex', 'Olga'},
        'Alex': {'Julia', 'Mariam'},
        'Mariam': {'Olga', 'Julia', 'Mark'},
        'Olga': {'Alex'},
        'Mark': {'Olga'},
    }
    start = 'Julia'
    result = {'Julia', 'Mark', 'Mariam', 'Olga', 'Alex'}
    
    assert depth_first(graph, start) == set(iter_dfs(graph, start)) == result