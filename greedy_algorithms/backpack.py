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


def fill_backpack(max_weight: int, objects: list[tuple]) -> str:
    """Return the maximum cost of parts of items 
    (any part can be taken from each item, 
    the cost and weight will decrease proportionally) 
    that fit into the given backpack.
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


if __name__ == '__main__':
    max_weight, objects = get_objects()
    print(fill_backpack(max_weight, objects))
