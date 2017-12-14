"""Solutions for AOC Day 14"""
import numpy
import operator
import binascii
import scipy.ndimage
import matplotlib.pyplot as plt


def convert(a, lengths, pos=0, skip=0):
    """Twist of ring, return array, pos, skip"""
    num_elements = len(a)
    for length in lengths:
        a = numpy.append(numpy.flip(a[0:length], 0), (a[length:]))
        a = numpy.append(a[(length + skip) %
                           num_elements:], (a[0:(length + skip) % num_elements]))
        pos += length + skip
        skip += 1
    return a, pos, skip


def knot_hash(sparse):
    """Create hex hash"""
    kh = ''
    for s in sparse:
        h = hex(s)
        if len(h) == 4:
            kh += ('0')
        kh += (hex(s)[2:-1])
    return kh


def sparse_hash(arr):
    """Convert array into hash"""
    barr = []
    for i in xrange(len(arr) / 16):
        barr.append(reduce(operator.xor, arr[i * 16:(i + 1) * 16]))
    return barr


def hasher(num_elements, lengths):
    """Solution to problem 2"""
    arr = range(0, num_elements)
    pos = 0
    skip = 0
    for _ in xrange(64):
        arr, pos, skip = convert(arr, lengths, pos, skip)
    arr = numpy.append(arr[-pos % num_elements:], arr[0:-pos % num_elements:])
    sparse = sparse_hash(arr)
    return knot_hash(sparse)


def solution(puzzle_input):
    total = 0
    im = numpy.zeros([128, 128], dtype=int)
    for i in range(128):
        hash_input = puzzle_input + "-" + str(i)
        converted = [ord(h) for h in hash_input]
        converted = numpy.append(converted, [17, 31, 73, 47, 23])

        scale = 16  # equals to hexadecimal
        num_of_bits = 8

        hashed = hasher(256, converted)
        binary = ''
        for j, k in zip(hashed[0::2], hashed[1::2]):
            binary += bin(int(j + k, scale))[2:].zfill(num_of_bits)

        total += binary.count('1')

        for j, b in enumerate(binary):
            im[i, j] = int(b)

    blobs, number_of_blobs = scipy.ndimage.label(im)

    return total, number_of_blobs


if __name__ == "__main__":
    puzzle_input = "jzgqcdpd"
    print solution(puzzle_input)
