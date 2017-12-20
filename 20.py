"""Solutions for AOC Day 20"""
import numpy
from collections import Counter


class Particle:

    def __init__(self, line):
        [p, v, a, _] = line.split('>')
        p = p.split('<')[1]
        v = v.split('<')[1]
        a = a.split('<')[1]
        self.position = [int(x) for x in p.split(',')]
        self.velocity = [int(x) for x in v.split(',')]
        self.acceleration = [int(x) for x in a.split(',')]

    def step(self):
        self.velocity = numpy.array(
            numpy.add(self.velocity, self.acceleration), dtype=int)
        self.position = numpy.array(
            numpy.add(self.position, self.velocity), dtype=int)

    def manhattan(self):
        return sum(map(abs, self.position))


def solution(file_name, repeats = 400):
    particles = []
    for line in open(file_name):
        particles.append(Particle(line))

    last = -1
    count = 0
    while True:
        # for _ in tqdm(xrange(400)):
        manhattans = []
        for p in particles:
            p.step()
            manhattans.append(p.manhattan())
        m = manhattans.index(min(manhattans))
        if m == last:
            count += 1
            if count > repeats:
                return m
        else:
            count = 0
            last = m

    return m


def solution2(file_name, repeats = 400):
    particles = []
    for line in open(file_name):
        particles.append(Particle(line))

    last = -1
    count = 0
    while True:
        positions = []
        for p in particles:
            p.step()
            positions.append(p.position)

        counter = Counter(map(tuple, positions))
        removes = []
        for i, p in enumerate(positions):
            if counter[tuple(p)] > 1:
                removes.append(i)
        for index in sorted(removes, reverse=True):
            del particles[index]

        if last == len(particles):
            count += 1
            if count > repeats:
                return len(particles)
        else:
            count = 0
            last = len(particles)

    return

if __name__ == "__main__":
    print "Solution 1: ", solution("20.txt")  # 243
    print "Solution 2: ", solution2("20.txt")  # not 243
