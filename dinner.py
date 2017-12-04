#!/usr/bin/env python

import random
from functools import reduce


def gen(places: dict):
    accumulator = 0
    for k, v in places.items():
        accumulator += v
        yield (k, (accumulator - v, accumulator))


def select(places: dict):
    random_num = int(random.uniform(0.0, reduce(lambda x, y: x + y, places.values())))

    for i in gen(places):
        place, rng = i[0], i[1]
        if random_num in range(*rng):
            return f'{place}, because {random_num}'

    return 'I dunno, lol'


def main():
    all_places = {
        'Litwiny': 40,
        'Terra pizza': 40,
        'Arena city': 20
    }

    print(select(all_places))


if __name__ == '__main__':
    main()
