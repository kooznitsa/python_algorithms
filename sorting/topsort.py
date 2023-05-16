"""GRAPHS. TOPOLOGICAL SORTING (TOPSORT)
-----
Based on depth-first search (DFS). Using directed acyclic graph (DAG).
If we perform DFS on a DAG, we could simply sort the nodes based on their
descending finish times, and they’d be topologically sorted. Each node 
would then precede all its descendants in the DFS tree, which would be 
any nodes reachable from the node, that is, nodes that depend on the node.
"""


def dfs_topsort(graph: dict) -> list:
    """The nodes should be sorted in reverse, based on their finish times."""
    visited = set()                    # History
    res = []                           # Result
    
    def recurse(node):                 # Traversal subroutine
        if node in visited:
            return                     # Ignore visited nodes
        visited.add(node)              # Otherwise: Add to history
        for nxt in graph[node]:
            recurse(nxt)               # Recurse through neighbors
        res.append(node)               # Finished with u: Append it
    
    for node in graph:
        recurse(node)                  # Cover entire graph
    
    res.reverse()                      # It's all backward so far
    return res