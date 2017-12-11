"""Solutions for AOC Day 11"""


def distance(steps):
    n = 0
    ne = 0
    nw = 0
    for step in steps:
        if step == 'n':
            n += 1
        elif step == 's':
            n -= 1
        elif step == 'ne':
            ne += 1
        elif step == 'sw':
            ne -= 1
        elif step == 'nw':
            nw += 1
        elif step == 'se':
            nw -= 1
        x = n
        y = -n
        x += nw
        z = -nw
        z += ne
        y -= ne
    return max([x, y, z])


if __name__ == "__main__":
    f = open("11.txt")
    for line in f:
        print "Final distance: ", distance(line.split(','))
        steps = line.split(',')
        partial_path = []
        max_dist = 0
        for step in steps:
            partial_path.append(step)
            max_dist = max(max_dist, distance(partial_path))
        print "Max distance: ", max_dist
