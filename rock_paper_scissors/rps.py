#!/usr/bin/python

import sys

rps_list = ['rock', 'paper', 'scissors']


def rock_paper_scissors(n, item=rps_list[0]):
    count = n
    if count == 0:
        return
    else:
        return rock_paper_scissors(n-1, )


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
