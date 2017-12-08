"""Solutions for AOC Day 8"""
import operator

OPERATORS = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne
}


def sol_1(lines):
    max_value_ever = 0
    registers = {}
    for line in lines:
        elements = line.split()
        register = elements[0]
        command = elements[1]
        change = int(elements[2])
        cond_register = elements[4]
        conditional = elements[5]
        conditional_value = int(elements[6])

        if command == 'dec':
            change = -change

        if register not in registers:
            registers[register] = 0
        if cond_register not in registers:
            registers[cond_register] = 0

        if OPERATORS[conditional](registers[cond_register], conditional_value):
            registers[register] += change
            if registers[register] > max_value_ever:
                max_value_ever = registers[register]

    values = []
    for key, value in registers.iteritems():
        values.append(value)
    return max(values), max_value_ever

if __name__ == "__main__":
    max_value, max_value_ever = sol_1([l for l in open("8.txt")])
    print max_value, max_value_ever
