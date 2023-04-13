"""GREEDY ALGORITHM. KNAPSACK PROBLEM"""


from collections import namedtuple
import sys


def get_objects() -> tuple[int, list[tuple]]:
    """Get data from stdin.
    Sample input:
    3 50
    60 20
    100 50
    120 30
    Return max weight, list of objects' cost/weight.
    """
    first_line, *objects = [(i.strip().split()) for i in sys.stdin.readlines()]
    _, max_weight = map(int, first_line)

    Object = namedtuple('Object', 'cost weight')
    objects = [Object(int(i[0]), int(i[1])) for i in objects]
    objects = sorted(objects, key=lambda x: x.cost / x.weight, reverse=True)

    return max_weight, objects


def fill_knapsack(max_weight: int, objects: list[tuple]) -> str:
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


THINGS = {
    'lighter': 20, 'compas': 100, 'fruits': 500, 'shirt': 300,
    'thermos': 1000, 'medicine box': 200, 'jacket': 600, 'binocular': 400, 
    'fishing rod': 1200, 'napkins': 40, 'sandwiches': 820, 'tent': 5500, 
    'sleeping bag': 2250, 'bubblegum': 10,
}

def fill_knapsack_whole_things(weight: str, things: dict = THINGS) -> None:
    """Print names of the whole items (division of items not allowed) 
    that fit into the given knapsack.
    """
    weight = int(input()) * 1000

    for key, value in sorted(things.items(), key=lambda x: x[1], reverse=True):
        if value <= weight:
            print(key)
            weight -= value


if __name__ == '__main__':
    max_weight, objects = get_objects()
    print(fill_knapsack(max_weight, objects))