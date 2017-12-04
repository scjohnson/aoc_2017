"""Solutions for AOC Day 4"""
import math
import numpy
import itertools

def good_pass_1(passt):
    words = passt.split()
    set_words = set(words)
    if len(words) == len(set_words):
        return True
    return False

def good_pass_2(passt):
    words = passt.split()
    set_words = set(words)
    if len(words) != len(set_words):
        return False
    for pair in itertools.combinations(words, 2):
        if sorted(pair[0]) == sorted(pair[1]):
            return False
    return True

def sol_1():
    """Solution to #1"""
    good = 0
    for line in open("4.txt"):
        if good_pass_1(line):
            good += 1
    
    return good


def sol_2():
    """Solution to #1"""
    good = 0
    for line in open("4.txt"):
        if good_pass_2(line):
            good += 1
    
    return good


if __name__ == "__main__":
    print sol_1()
    print sol_2()
