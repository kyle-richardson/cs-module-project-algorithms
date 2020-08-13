#!/usr/bin/python

import sys


def making_change(amount, denominations, cache={}):
  # base case
    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    elif amount in cache:
        return cache[amount]
    else:
        value = 0
        for x in denominations:
            value += making_change(amount - x, denominations)
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
