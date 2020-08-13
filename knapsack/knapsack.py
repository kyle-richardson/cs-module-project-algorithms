#!/usr/bin/python

import itertools
import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


# def knapsack_solver(items, capacity):
#     items.sort(key=lambda x: x.value, reverse=True)
#     sack = []
#     cur_size = 0
#     for i in range(len(items)):
#         if cur_size + items[i].size <= capacity:
#             sack.append(items[i])

#     return sack


# def knapsack_solver(items, capacity):
#     all_combos = []
#     for i in range(1, len(items)+1):
#         list_of_combos = list(itertools.combinations(items, i))
#         for combo in list_of_combos:
#             all_combos.append(combo)
#     max_value = -1
#     best_combo = None
#     for combo in all_combos:
#         value = 0
#         size = 0
#         for item in combo:
#             value += item.value
#             size += item.size
#         if size <= capacity:
#             if value > max_value:
#                 max_value = value
#                 best_combo = combo
#     return best_combo

def knapsack_solver(items, capacity):
    items.sort(key=lambda x: (x.value / x.size), reverse=True)

    sack = []
    size = 0
    for i in items:
        added = size + i.size
        if added <= capacity:
            sack.append(i)
            size = added
        if added == capacity:
            return sack
    return sack


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
