"""Solutions for AOC Day 23"""
from sympy import sieve


def value(registers, v):
    try:
        ret = int(v)
        return ret
    except:
        return registers[v]


def fast_solution2():
    h = 0
    for b in xrange(108100, 125100 + 1, 17):
        if b not in sieve:
            h += 1
    return h


def solution2():
    # Initialize
    # set b 81            | b = 81
    # set c b             | c = 81
    # jnz a 2             | jump2
    # jnz 1 5
    # mul b 100           | b = 8100
    # sub b -100000       | b = 108100
    # set c b             | c = 108100
    # sub c -17000        | c = 125100
    b = 108100
    c = 125100

    # set f 1 | f = 1 - - begin loop
    # set d 2 | d = 2
    while True:  # b iterates up by 17s
        f = 1
        d = 2
        # set e 2 | e = 2 - - begin loop
        while True:
            e = 2
            # set g d | g = d - - begin loop
            while True:
                g = d
                print g, e, d
                # mul g e | g *= e
                # sub g b | g -= b
                g *= e
                g -= b
                # jnz g 2
                if g == 0:  # if d*e == b
                    # set f 0 | f = 0
                    f = 0
                # sub e - 1 | e += 1
                e += 1
                # set g e | g = e
                g = e
                # sub g b | g -= b
                g -= b
                # jnz g - 8 | -- end loop while g != 0
                if g == 0:
                    break
            # sub d - 1 | d += 1
            d += 1
            # set g d | g = d
            g = d
            # sub g b | g -= b
            g -= b
            # jnz g - 13 | -- end loop while g != 0
            if g == 0:
                break
        # jnz f 2 | if f == 0
        # d and e keep iterating by one, then we check if multiplied together,
        # they equal b. Checking if b is composable -- prime.
        if f == 0:  # f = 0 is set in the inner loop -- checks if d*e == b
            # sub h - 1 | h += 1
            h += 1
        # set g b | g = b
        g = b
        # sub g c | g -= c
        g -= c
        # jnz g 2 | if g == 0
        if g == 0:  # if b == c
            # jnz 1 3 | end
            return h
        # sub b - 17 | b += 17
        b += 17
        # jnz 1 - 23 | -- end loop def solution_2(file_name):


def solution(file_name, a=0):
    registers = {'a': a, 'h': 0, 'g': 0}
    with open(file_name) as f:
        lines = f.readlines()
    i = 0
    mul_invoked = 0
    max_i = 0

    while True:

        elems = lines[i].split()
        if elems[1] not in registers:
            registers[elems[1]] = 0

        if elems[0] == "set":
            registers[elems[1]] = value(registers, elems[2])
        elif elems[0] == "sub":
            registers[elems[1]] -= value(registers, elems[2])
        elif elems[0] == "mul":
            registers[elems[1]] *= value(registers, elems[2])
            mul_invoked += 1
        elif elems[0] == "jnz":
            if value(registers, elems[1]) != 0:
                i += value(registers, elems[2])
                i -= 1
                next
        i += 1
        if i == len(lines):
            return mul_invoked, registers['h']


if __name__ == "__main__":
    print "Solution 1: ", solution("23.txt")[0]
    # print "Solution 2: ", solution2()
    print "Solution 2: ", fast_solution2()
