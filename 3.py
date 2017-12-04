"""Solutions for AOC Day 3"""
import math
import numpy


def sol_1(num):
    """Solution to #1"""
    # bottom right corner is an odd perfect square
    length = int(math.ceil(math.sqrt(num)))
    if length % 2 == 0:
        length += 1

    bottom_right = length * length

    a = (bottom_right - num) % (length - 1)
    b = a - (length - 1) / 2
    steps = (length - 1) / 2 + abs(b)

    return steps


def half_length(length):
    return (length - 1) / 2


def indices_iterator(length):
    x_index = half_length(length)
    y_index = half_length(length)
    yield (x_index, y_index)
    current_length = 1
    while current_length < length:
        current_length += 2
        x_index += 1
        yield (x_index, y_index)
        for _ in range(current_length-2):
            y_index += 1
            yield (x_index, y_index)
        for _ in range(current_length-1):
            x_index -= 1
            yield (x_index, y_index)
        for _ in range(current_length-1):
            y_index -= 1
            yield (x_index, y_index)
        for _ in range(current_length-1):
            x_index += 1
            yield (x_index, y_index)



def sol_2(num):
    length = 11
    array = numpy.zeros([length, length])
    array[half_length(length), half_length(length)] = 1
    i = 0
    for indices in indices_iterator(length):
        i += 1
        value = int(numpy.sum(array[indices[0]-1:indices[0]+2, indices[1]-1:indices[1]+2]))
        if value > num:
            return value
        array[indices[0], indices[1]] = value
        # print array


def test_sol_1():
    assert sol_1(12) == 3
    assert sol_1(23) == 2
    assert sol_1(1024) == 31

def test_sol_2():
    assert sol_2(9) == 10
    assert sol_2(50) == 54
    assert sol_2(300) == 304

if __name__ == "__main__":
    print sol_1(289326)
    print sol_2(289326) # not 60
