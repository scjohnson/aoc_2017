"""Solutions for AOC Day 22"""
import numpy as np
from tqdm import tqdm


def turn_right(direction):
    return np.matmul(np.array([[0, 1], [-1, 0]]), direction)


def turn_left(direction):
    return np.matmul(np.array([[0, -1], [1, 0]]), direction)


def solution2(file_name, num_steps=10000000):
    matrix = np.zeros([1000, 1000], dtype=int)
    i = -1
    infected = 0
    for line in open(file_name):
        i += 1
        for j, c in enumerate(line):
            if c == "#":
                matrix[i + 500, j + 500] = 1
    loc = [500 + i / 2, 500 + j / 2]
    direction = [-1, 0]

    # 0 == clean
    # 1 == infected
    # 2 == weakened
    # 3 = flagged
    for _ in tqdm(xrange(num_steps)):
        if matrix[loc[0], loc[1]] == 1:
            direction = turn_right(direction)
        elif matrix[loc[0], loc[1]] == 2:
            direction = direction
        elif matrix[loc[0], loc[1]] == 3:
            direction = -direction
        else:
            direction = turn_left(direction)

        if matrix[loc[0], loc[1]] == 0:
            matrix[loc[0], loc[1]] = 2
        elif matrix[loc[0], loc[1]] == 2:
            matrix[loc[0], loc[1]] = 1
            infected += 1
        elif matrix[loc[0], loc[1]] == 1:
            matrix[loc[0], loc[1]] = 3
        else:
            matrix[loc[0], loc[1]] = 0

        loc += direction
    return infected


def solution(file_name):
    matrix = np.zeros([1000, 1000], dtype=int)
    i = -1
    infected = 0
    for line in open(file_name):
        i += 1
        for j, c in enumerate(line):
            if c == "#":
                matrix[i + 500, j + 500] = 1
    loc = [500 + i / 2, 500 + j / 2]
    direction = [-1, 0]

    for _ in xrange(10000):
        if matrix[loc[0], loc[1]] == 1:
            direction = turn_right(direction)
        else:
            direction = turn_left(direction)

        if matrix[loc[0], loc[1]] == 0:
            matrix[loc[0], loc[1]] = 1
            infected += 1
        else:
            matrix[loc[0], loc[1]] = 0

        loc += direction
    return infected


if __name__ == "__main__":
    print "Solution 1: ", solution("22.txt")  # 5411
    print "Solution 2: ", solution2("22.txt")
