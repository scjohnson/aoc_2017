"""Solutions for AOC Day 15"""
from itertools import chain
from tqdm import tqdm


def gen(start, factor, multiple=False, value=1):
    divisor = 2147483647
    current = start
    while True:
        current = current * factor % divisor
        if not multiple:
            yield current
        else:
            if current % value == 0:
                yield current


def solution_2(a_start=512, b_start=191):
    # Generator A starts with 512
    # Generator B starts with 191
    score = 0
    a = gen(a_start, 16807, multiple=True, value=4)
    b = gen(b_start, 48271, multiple=True, value=8)
    for i in tqdm(range(5000000)):
        if bin(a.next())[-16:] == bin(b.next())[-16:]:
            score += 1
    return score


def solution_1(a_start=512, b_start=191):
    # Generator A starts with 512
    # Generator B starts with 191
    score = 0
    a = gen(a_start, 16807)
    b = gen(b_start, 48271)
    for i in tqdm(range(40000000)):
        if bin(a.next())[-16:] == bin(b.next())[-16:]:
            score += 1
    return score

if __name__ == "__main__":
    print "Solution 1 :", solution_1()
    print "Solution 2 :", solution_2()
