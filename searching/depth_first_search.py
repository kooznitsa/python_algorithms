"""GRAPHS. DEPTH-FIRST SEARCH (DFS)
-----
The algorithm starts at the root node (selecting some arbitrary node as the root node 
in the case of a graph) and explores as far as possible along each branch before backtracking.
-----
Time complexity: O(V + E)
(V for number of vertices (= nodes), E for number of edges)
"""

from typing import Any


def depth_first(
        graph: dict[Any, set], 
        start: str, 
        visited: set = None
    ) -> set:
    if visited is None:
        visited = set()
    visited.add(start)

    for nxt in graph[start] - visited:
        depth_first(graph, nxt, visited)
    return visited


graph = {
    'Julia': {'Mark', 'Alex', 'Olga'},
    'Alex': {'Julia', 'Mariam'},
    'Mariam': {'Olga', 'Julia', 'Mark'},
    'Olga': {'Alex'},
    'Mark': {'Olga'},
}

if __name__ == '__main__':
    assert depth_first(graph, 'Julia') == {'Julia', 'Mark', 'Mariam', 'Olga', 'Alex'}