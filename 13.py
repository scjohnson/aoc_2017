"""Solutions for AOC Day 13"""
import numpy


def read_data(file_name="13.txt"):
    arr = numpy.zeros([97], dtype=int)
    for line in open(file_name):
        elems = line.split(':')
        arr[int(elems[0])] = int(elems[1])
    return arr


def solution_1():
    scanner = read_data()
    score = 0
    for i in range(97):
        if scanner[i] != 0 and (i) % (2 * (scanner[i] - 1)) == 0:
            score += i * scanner[i]
    return score


def solution_2():
    scanner = read_data()
    delay = 0
    while True:
        for i in range(97):
            if scanner[i] != 0 and (i + delay) % (2 * (scanner[i] - 1)) == 0:
                break
            if i == 96:
                return delay
        delay += 1

if __name__ == "__main__":
    print "Solution 1: ", solution_1()
    print "Solution 2: ", solution_2()
