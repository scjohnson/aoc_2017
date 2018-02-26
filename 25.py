"""Solutions for AOC Day 25"""
import numpy as np
from tqdm import tqdm


def solution(file_name):
    arr = np.zeros([100000000, 1])
    index = 50000000
    state = 'A'
    for _ in tqdm(xrange(12964419)):
        if state == 'A':
            if arr[index] == 0:
                arr[index] = 1
                index += 1
                state = 'B'
            else:
                arr[index] = 0
                index += 1
                state = 'F'
        elif state == 'B':
            if arr[index] == 0:
                arr[index] = 0
                index -= 1
                state = 'B'
            else:
                arr[index] = 1
                index -= 1
                state = 'C'
        elif state == 'C':
            if arr[index] == 0:
                arr[index] = 1
                index -= 1
                state = 'D'
            else:
                arr[index] = 0
                index += 1
                state = 'C'
        elif state == 'D':
            if arr[index] == 0:
                arr[index] = 1
                index -= 1
                state = 'E'
            else:
                arr[index] = 1
                index += 1
                state = 'A'
        elif state == 'E':
            if arr[index] == 0:
                arr[index] = 1
                index -= 1
                state = 'F'
            else:
                arr[index] = 0
                index -= 1
                state = 'D'
        elif state == 'F':
            if arr[index] == 0:
                arr[index] = 1
                index += 1
                state = 'A'
            else:
                arr[index] = 0
                index -= 1
                state = 'E'
        if index > len(arr) or index < 0:
            print "Index out of bounds: ", index
    return np.sum(arr)


if __name__ == "__main__":
    print "Solution 1: ", solution("test.txt")
    # print "Solution 1: ", solution("25.txt") # not 6482209 or 4407
