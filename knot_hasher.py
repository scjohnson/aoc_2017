"""Our knot hashing algorithm"""
import numpy
import operator


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


def hash_string(string_to_hash):
    """Return the hash for this string"""
    converted = [ord(h) for h in string_to_hash]
    converted = numpy.append(converted, [17, 31, 73, 47, 23])
    return hasher(256, converted)
