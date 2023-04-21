"""GRAPHS. DIJKSTRA'S ALGORITHM
-----
- WEIGHT: a number associated with each edge in the graph.
- WEIGHTED GRAPH: a graph with weights.
- UNWEIGHTED GRAPH: a graph without weights. 
- UNDIRECTED GRAPHS: when both nodes point to each other and create a cycle.
Dijkstra's algorithm only works with DIRECTED ACYCLIC GRAPHS (DAGs).
-----
Dijkstra's algorithm is used to calculate the shortest path in a weighted graph.
You can’t use Dijkstra’s algorithm if you have negative-weight edges (use the Bellman-Ford algorithm). 
Steps:
1. Find the “cheapest” node. This is the node you can get to in the least amount of time.
2. Check whether there’s a cheaper path to the neighbors of this node.
If so, update their costs.
3. Repeat until you’ve done this for every node in the graph.
4. Calculate the fnal path.
-----
Time complexity: O(V ** 2) where V is the number of vertices in the graph
"""


def dijkstra(graph, costs, parents):
    processed = []

    def find_lowest_cost_node(costs):
        lowest_cost = ﬂoat('inf')
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    # Find the lowest-code node that you haven't processed yet
    node = find_lowest_cost_node(costs)
    # If you've processed all the nodes, this loop is done
    while node:
        cost = costs[node]
        neighbors = graph[node]
        # Go through all the neighbors of this node
        for n in neighbors.keys():
            # If it’s cheaper to get to this neighbor by going through this node...
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                # ...update the cost for this node
                costs[n] = new_cost
                # This node becomes the new parent for this neighbor
                parents[n] = node
        # Mark the node as processed
        processed.append(node)
        # Find the next node to process, and loop
        node = find_lowest_cost_node(costs)
    return costs


def create_hash_tables():
    """
        6----->A -----1
        |      ^      |
    START      |    FINISH
        |      3      |
        |      |      |
        2----->B -----5
    """
    graph = {}
    graph['start'] = {}
    graph['start']['a'] = 6
    graph['start']['b'] = 2
    graph['a'] = {}
    graph['a']['fin'] = 1
    graph['b'] = {}
    graph['b']['a'] = 3
    graph['b']['fin'] = 5
    graph['fin'] = {}

    costs = {}
    costs['a'] = 6
    costs['b'] = 2
    costs['fin'] = ﬂoat('inf')

    parents = {}
    parents['a'] = 'start'
    parents['b'] = 'start'
    parents['fin'] = None

    return graph, costs, parents


if __name__ == '__main__':
    graph, costs, parents = create_hash_tables()
    result = dijkstra(graph, costs, parents)
    print('Cheapest cost to get to the finish node:', result['fin'])
    assert result['fin'] == 6