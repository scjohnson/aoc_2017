"""Solutions for AOC Day 14"""
import binascii
import numpy
import scipy.ndimage

import knot_hasher


def solution(puzzle_input):
    total = 0
    im = numpy.zeros([128, 128], dtype=int)
    for i in range(128):
        hash_input = puzzle_input + "-" + str(i)

        hashed = knot_hasher.hash_string(hash_input)
        binary = ''
        for j, k in zip(hashed[0::2], hashed[1::2]):
            binary += bin(int(j + k, 16))[2:].zfill(8)

        total += binary.count('1')

        for j, b in enumerate(binary):
            im[i, j] = int(b)

    # cheat:
    blobs, number_of_blobs = scipy.ndimage.label(im)

    return total, number_of_blobs


if __name__ == "__main__":
    puzzle_input = "jzgqcdpd"
    print solution(puzzle_input)
