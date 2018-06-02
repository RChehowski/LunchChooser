#!/usr/bin/env python

import random
import yaml

from functools import reduce


def gen(places: dict):
    acc = 0
    for k, v in places.items():
        acc += v
        yield (k, (acc - v, acc))


def select(places: dict):
    random_num = int(random.uniform(0.0, reduce(lambda x, y: x + y, places.values())))

    for i in gen(places):
        place, rng = i[0], i[1]
        if random_num in range(*rng):
            return f'{place}, because {random_num}'

    return 'I dunno, lol'


def main():
    with open('places.yml') as stream:
        places = yaml.load(stream)
        print(select(places))


if __name__ == '__main__':
    main()
