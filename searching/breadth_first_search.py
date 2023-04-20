"""GRAPHS. BREADTH-FIRST SEARCH
-----
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