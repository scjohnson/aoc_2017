"""Solutions for AOC Day 10"""
import operator
import numpy


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


def solution_1(num_elements, lengths):
    """Solution to problem 1"""
    a = range(0, num_elements)
    a, pos, skip = convert(a, lengths)
    return a[-pos % num_elements] * a[(-pos + 1) % num_elements]


def sparse_hash(arr):
    """Convert array into hash"""
    barr = []
    for i in xrange(len(arr) / 16):
        barr.append(reduce(operator.xor, arr[i * 16:(i + 1) * 16]))
    return barr


def knot_hash(sparse):
    """Create hex hash"""
    kh = ''
    for s in sparse:
        h = hex(s)
        if len(h) == 4:
            kh += ('0')
        kh += (hex(s)[2:-1])
    return kh


def solution_2(num_elements, lengths):
    """Solution to problem 2"""
    arr = range(0, num_elements)
    pos = 0
    skip = 0
    for _ in xrange(64):
        arr, pos, skip = convert(arr, lengths, pos, skip)
    arr = numpy.append(arr[-pos % num_elements:], arr[0:-pos % num_elements:])
    sparse = sparse_hash(arr)
    return knot_hash(sparse)


def test_all():
    """test some"""
    assert solution_1(5, [3, 4, 1, 5]) == 12
    assert sparse_hash(
        [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22])[0] == 64
    converted = numpy.empty([0], dtype=int)
    converted = numpy.append(converted, [17, 31, 73, 47, 23])
    assert solution_2(256, converted) == 'a2582a3a0e66e6e86e3812dcb672a272'

if __name__ == "__main__":
    print "Solution 1: ", solution_1(
        256, [130, 126, 1, 11, 140, 2, 255, 207, 18, 254, 246, 164, 29, 104, 0, 224])
    converted = [ord(c) for c in
                 "130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224"]
    converted = numpy.append(converted, [17, 31, 73, 47, 23])
    print "Solution 2 : ", solution_2(256, converted)
