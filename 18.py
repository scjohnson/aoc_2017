"""Solutions for AOC Day 18"""


def value(registers, v):
    try:
        ret = int(v)
        return ret
    except:
        return registers[v]


class Program:

    def __init__(self, file_name, num):
        self.registers = {}
        self.registers['p'] = num
        self.receive_queue = []
        self.i = 0
        with open(file_name) as f:
            self.lines = f.readlines()
        self.number_sent = 0

    def set_pair(self, pair):
        self.pair = pair

    def next(self):
        if self.i == len(self.lines):
            return False

        elems = self.lines[self.i].split()
        if elems[1] not in self.registers and elems[0] != "snd":
            self.registers[elems[1]] = 0

        if elems[0] == "snd":
            self.pair.receive_queue.append(value(self.registers, elems[1]))
            self.number_sent += 1
        elif elems[0] == "set":
            self.registers[elems[1]] = value(self.registers, elems[2])
        elif elems[0] == "add":
            self.registers[elems[1]] += value(self.registers, elems[2])
        elif elems[0] == "mul":
            self.registers[elems[1]] *= value(self.registers, elems[2])
        elif elems[0] == "mod":
            self.registers[elems[1]] = self.registers[
                elems[1]] % value(self.registers, elems[2])
        elif elems[0] == "rcv":
            if len(self.receive_queue) > 0:
                self.registers[elems[1]] = value(
                    self.registers, self.receive_queue[0])
                if len(self.receive_queue) == 1:
                    self.receive_queue = []
                else:
                    self.receive_queue = self.receive_queue[1:]
            else:
                return False
        elif elems[0] == "jgz":
            if value(self.registers, elems[1]) > 0:
                self.i += value(self.registers, elems[2])
                self.i -= 1
                next
        self.i += 1
        return True


def solution_2(file_name):
    one = Program(file_name, 1)
    zero = Program(file_name, 0)
    one.set_pair(zero)
    zero.set_pair(one)
    while True:
        if not one.next() and not zero.next():
            return one.number_sent


def solution(file_name):
    registers = {}
    last_sound = 0
    with open(file_name) as f:
        lines = f.readlines()
    i = 0
    while True:
        elems = lines[i].split()
        if elems[1] not in registers:
            registers[elems[1]] = 0

        if elems[0] == "snd":
            last_sound = value(registers, elems[1])
        elif elems[0] == "set":
            registers[elems[1]] = value(registers, elems[2])
        elif elems[0] == "add":
            registers[elems[1]] += value(registers, elems[2])
        elif elems[0] == "mul":
            registers[elems[1]] *= value(registers, elems[2])
        elif elems[0] == "mod":
            registers[elems[1]] = registers[
                elems[1]] % value(registers, elems[2])
        elif elems[0] == "rcv":
            if registers[elems[1]] != 0:
                return last_sound
        elif elems[0] == "jgz":
            if value(registers, elems[1]) > 0:
                i += value(registers, elems[2])
                i -= 1
                next
        i += 1


if __name__ == "__main__":
    print "Solution 1: ", solution("18.txt")
    print "Solution 2: ", solution_2("18.txt")
