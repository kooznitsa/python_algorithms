"""GREEDY ALGORITHM. KNAPSACK PROBLEM"""


from collections import namedtuple
import heapq
import sys
from typing import Optional


def get_values(
        objects: list[tuple] = Optional[None],
        max_weight: int = Optional[None]
    ) -> tuple[int, list[tuple]]:
    """Transform given data or get data from stdin.
    Sample input:
    3 50
    60 20
    100 50
    120 30
    Return max weight, list of objects' cost/weight.
    """
    if not objects and not max_weight:
        first_line, *objects = [(i.strip().split()) for i in sys.stdin.readlines()]
        _, max_weight = map(int, first_line)

    Object = namedtuple('Object', 'cost weight')
    objects = [Object(int(i[0]), int(i[1])) for i in objects]
    objects = sorted(objects, key=lambda x: x.cost / x.weight, reverse=True)

    return max_weight, objects


def fill_knapsack(
        max_weight: int, 
        objects: list[tuple]
    ) -> str:
    """Return the maximum cost of parts of items 
    (any part can be taken from each item, 
    the cost and weight will decrease proportionally) 
    that fit into the given knapsack.
    """
    cost, weight = 0, 0

    for obj in objects:
        if weight + obj.weight <= max_weight:
            cost += obj.cost
            weight += obj.weight

        else:
            new_weight = max_weight - weight
            weight += new_weight
            cost += obj.cost / obj.weight * new_weight

    return f'{cost:.3f}'


def fractional_knapsack_sort(
        capacity: int, 
        values_and_weights: list[tuple]
    ) -> str:
    """Fractional knapsack with sorted list.
    Returns the maximum cost of parts of items.
    """
    order = [(v / w, w) for v, w in values_and_weights]
    order.sort(reverse=True)

    acc = 0
    for v_per_w, w in order:
        if w < capacity:
            acc += v_per_w * w
            capacity -= w
        else:
            acc += v_per_w * capacity
            break
    return f'{acc:.3f}'


def fractional_knapsack_heap(
        capacity: int, 
        values_and_weights: list[tuple]
    ) -> str:
    """Fractional knapsack with heap.
    Returns the maximum cost of parts of items.
    """
    order = [(-v / w, w) for v, w in values_and_weights]
    heapq.heapify(order)

    acc = 0
    while order and capacity:
        v_per_w, w = heapq.heappop(order)
        can_take = min(w, capacity)
        acc -= v_per_w * can_take
        capacity -= can_take
    return f'{acc:.3f}'


THINGS = {
    'lighter': 20, 'compas': 100, 'fruits': 500, 'shirt': 300,
    'thermos': 1000, 'medicine box': 200, 'jacket': 600, 'binocular': 400, 
    'fishing rod': 1200, 'napkins': 40, 'sandwiches': 820, 'tent': 5500, 
    'sleeping bag': 2250, 'bubblegum': 10,
}

def fill_knapsack_whole_things(weight: int, things: dict = THINGS) -> None:
    """Print names of the whole items (division of items not allowed) 
    that fit into the given knapsack.
    """
    weight *= 1000
    result = []

    for key, value in sorted(things.items(), key=lambda x: x[1], reverse=True):
        if value <= weight:
            result.append(key)
            weight -= value
    return result


if __name__ == '__main__':
    max_weight, objects = get_values([(60, 20), (100, 50), (120, 30)], 50)

    assert (fill_knapsack(max_weight, objects) 
            == fractional_knapsack_sort(max_weight, objects) 
            == fractional_knapsack_heap(max_weight, objects) 
            == '180.000')
    
    print(fill_knapsack_whole_things(weight=10))