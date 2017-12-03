"""Solutions for AOC Day 3"""
import math


def sol_1(num):
    """Solution to #1"""
    # bottom right corner is an odd perfect square
    length = int(math.ceil(math.sqrt(num)))
    if length % 2 == 0:
        length += 1

    bottom_right = length * length

    a = (bottom_right - num) % (length - 1)
    b = a - (length - 1) / 2
    steps = (length - 1) / 2 + abs(b)

    return steps

def test_sol_1():
    assert sol_1(12) == 3
    assert sol_1(23) == 2
    assert sol_1(1024) == 31

if __name__ == "__main__":
    print sol_1(289326)
