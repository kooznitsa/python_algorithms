"""GREEDY ALGORITHM. TRAVELING SALESMAN PROBLEM (TSP)
-----
Given a list of cities and the distances between each pair of cities, what is the 
shortest possible route that visits each city exactly once and returns to the origin city?
-----
Time complexity: O(n ** 2 * log n) 
"""

import random


def tsp(cities, start=None):
    first = lambda x: next(iter(x))
    C = start or first(cities)
    distance_points = lambda x, y: abs(x - y)
    nearest_neighbor = lambda x, cities: min(cities, key=lambda C: distance_points(C, x))

    tour = [C]
    unvisited = set(cities - {C})

    while unvisited:
        C = nearest_neighbor(C, unvisited)
        tour.append(C)
        unvisited.remove(C)

    return tour


def generate_cities(number_of_cities):
    """Generate cities located in a rectangle 500 x 300."""
    seed = 111
    width = 500
    height = 300

    random.seed(number_of_cities, seed)

    return frozenset(
        complex(random.randint(1, width), random.randint(1, height)) 
        for _ in range(number_of_cities)
    )


if __name__ == '__main__':
    print(tsp(generate_cities(10)))