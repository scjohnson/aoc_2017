"""Solutions for AOC Day 10"""
import numpy


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

if __name__ == "__main__":
    assert solution_1(5, [3, 4, 1, 5]) == 12
    print "Solution 1: ", solution_1(
        256, [130, 126, 1, 11, 140, 2, 255, 207, 18, 254, 246, 164, 29, 104, 0, 224])
    # 38628
    converted = [ord(c) for c in
                 "130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224"]
    converted = numpy.append(converted, [17, 31, 73, 47, 23])
