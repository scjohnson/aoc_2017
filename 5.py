"""Solutions for AOC Day 5"""
import math
import numpy
import itertools


def sol_1(a):
    """Solution to #1"""
    jumps = 0
    index = 0
    while True:
        steps = a[index]
        a[index] += 1
        jumps += 1
        index += steps
        if index < 0 or index >= len(a):
            return jumps

    return False


def sol_2(a):
    """Solution to #2"""
    jumps = 0
    index = 0
    while True:
        steps = a[index]
        if steps >= 3:
            a[index] -= 1
        else:
            a[index] += 1
        jumps += 1
        index += steps
        if index < 0 or index >= len(a):
            return jumps

    return False


if __name__ == "__main__":
    a = []
    for line in open("5.txt"):
        a.append(int(line))
    print sol_1(a)
    a = []
    for line in open("5.txt"):
        a.append(int(line))
    print sol_2(a)
