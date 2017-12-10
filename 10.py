"""Solutions for AOC Day 10"""
import numpy
import operator


def convert(a, lengths, pos=0, skip=0):
    num_elements = len(a)
    for length in lengths:
        a = numpy.append(numpy.flip(a[0:length], 0), (a[length:]))
        a = numpy.append(a[(length + skip) %
                           num_elements:], (a[0:(length + skip) % num_elements]))
        pos += length + skip
        skip += 1
    return a, pos, skip


def solution_1(num_elements, lengths):
    a = range(0, num_elements)
    a, pos, skip = convert(a, lengths)
    return a[-pos % num_elements] * a[(-pos + 1) % num_elements]


def sparse_hash(a):
    b = []
    for i in xrange(len(a) / 16):
        b.append(reduce(operator.xor, a[i * 16:(i + 1) * 16]))
    return b


def knot_hash(sparse):
    kh = ''
    for s in sparse:
        h = hex(s)
        if len(h) == 3:
            kh += ('0')
        kh += (hex(s)[2:-1])
    return kh


def solution_2(num_elements, lengths):
    a = range(0, num_elements)
    pos = 0
    skip = 0
    for _ in xrange(64):
        a, pos, skip = convert(a, lengths, pos, skip)
    sparse = sparse_hash(a)
    kh = knot_hash(sparse)
    return kh

if __name__ == "__main__":
    assert solution_1(5, [3, 4, 1, 5]) == 12
    print "Solution 1: ", solution_1(
        256, [130, 126, 1, 11, 140, 2, 255, 207, 18, 254, 246, 164, 29, 104, 0, 224])
    converted = [ord(c) for c in
                 "130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224"]
    converted = numpy.append(converted, [17, 31, 73, 47, 23])
    assert sparse_hash(
        [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22])[0] == 64
    print solution_2(256, converted)
