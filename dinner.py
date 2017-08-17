#!/usr/bin/env python

import random


def select(places):
    max_probability = 0
    for place in places:
        max_probability += place[0]

    num = random.uniform(0.0, max_probability)

    accumulator = 0.0
    for place in places:
        current_chance = place[0]

        if (num - accumulator) > current_chance:
            accumulator += current_chance
        else:
            return f"{place[1]}, because {num}"

    return "Unknown"

all_places = [
    (40, "Arbat"),
    (40, "Myata"),
    (15, "Lido"),
    (5, "Shaverma"),
]

print(select(all_places))


