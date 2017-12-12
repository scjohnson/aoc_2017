"""Solutions for AOC Day 12"""


def read_data(file_name):
    links = {}
    for line in open(file_name):
        inp, outputs = line.split('<->')
        outs = outputs.split(',')
        inp = inp.strip()
        for out in outs:
            out = out.strip()
            if inp not in links:
                links[inp] = []
            links[inp].append(out)
    return links


def connected_to(base, data):
    connected_to_base = [base, ]
    new = [base, ]
    while new:
        old = new
        new = []
        for n in old:
            for conn in data[n]:
                if conn not in connected_to_base:
                    connected_to_base.append(conn)
                    new.append(conn)
    return connected_to_base


def solution_1():
    data = read_data("12.txt")

    return len(connected_to('0', data))


def solution_2():
    data = read_data("12.txt")
    groups = 0
    in_a_group = []
    while len(in_a_group) != len(data):
        for k in data:
            if k not in in_a_group:
                in_a_group.extend(connected_to(k, data))
                break
        groups += 1
    return groups


if __name__ == "__main__":
    # 380
    print "Solution 1: ", solution_1()
    print "Solution 2: ", solution_2()
