"""Solutions for AOC Day 16"""
from string import maketrans
from tqdm import tqdm
import numpy
import numpy.linalg


def solution(file_name="16.txt", programs='abcdefghijklmnop', iters=1, partners=True):
    num_elements = 16
    for line in open(file_name):
        commands = line.split(',')
        for i in xrange(iters):
            for c in commands:
                if c[0] == 's':
                    n = int(c[1:])
                    programs = programs[-n:] + programs[0:num_elements - n]
                elif c[0] == 'p':
                    if partners:
                        mapping = maketrans(c[1] + c[3], c[3] + c[1])
                        programs = programs.translate(mapping)
                elif c[0] == 'x':
                    ab = c[1:].split("/")
                    a = programs[int(ab[0])]
                    b = programs[int(ab[1])]
                    mapping = maketrans(a + b, b + a)
                    programs = programs.translate(mapping)
            if programs is 'abcdefghijklmnop':
                print "repeat: ", i

    return programs


def mapping(inp, out):
    mapp = numpy.zeros([16, 16], dtype=int)
    for i, c in enumerate(inp):
        mapp[out.index(c), i] = 1
    return mapp


def apply_mapping(inp, ma):
    xs, ys = numpy.nonzero(ma)
    out = ''
    for x, y in zip(xs, ys):
        out += inp[y]
    return out


if __name__ == "__main__":
    print "solution 1:", solution()

    sol = solution(partners=False)
    inp = "abcdefghijklmnop"
    ma = mapping(inp, sol)
    print "Solution 2:", apply_mapping(inp, numpy.linalg.matrix_power(ma, 1000000000))
