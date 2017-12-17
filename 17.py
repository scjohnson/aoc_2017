"""Solutions for AOC Day 17"""
from tqdm import tqdm


def solution(step_size, iters):
    a = [0, ]
    pos = 0
    for i in xrange(1, iters):
        pos = (pos + step_size) % len(a)
        if (pos + 1) == len(a):
            a.append(i)
            pos = len(a) - 1
        else:
            a.insert(pos + 1, i)
            pos += 1
    return a


def after_zero(step_size, iters):
    ret = 0
    pos = 0
    for i in tqdm(xrange(1, iters)):
        pos = (pos + step_size) % i
        if pos == 0:
            ret = i
        pos += 1
    return ret


def value_after(value, a):
    return a[a.index(value) + 1]

if __name__ == "__main__":
    print "solution 1:", value_after(2017, solution(376, 2018))
    print "solution 2:", after_zero(376, 50000000)
