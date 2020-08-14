#!/usr/bin/python

import sys
from collections import defaultdict


def making_change(amount, denominations, cache={}, previous=None):
    # denominations = denominations.sort(reverse=True)
    if previous is None:
        previous = denominations[-1]
    # print(f'start of method: amount: {amount}, previous: {previous}')
    # base case
    if amount == 0:
        # print(f'VALID')
        return 1
    elif amount < 0:
        # print(f'not valid')
        return 0

    # check cache
    # elif amount in cache and amount <= previous:
    #     print(f'found in cache: {cache[amount]}')
    #     return cache[amount]

    # compute value and add to cache
    else:
        value = 0
        removing_highs = [y for y in denominations if y <= previous]
        # print(f"removing highs: {removing_highs}")
        for x in removing_highs:
            value += making_change(amount - x, denominations, previous=x)
        # print(f'{amount}: {value}')
        cache[amount] = value
        return value


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
