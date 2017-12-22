"""Solutions for AOC Day 21"""
import numpy as np


def read_rules(file_name):
    rules = {}
    for line in open(file_name):
        [begin, end] = line.split("=>")
        rules[begin.strip().replace("/", "")] = end.strip()
    return rules


def get_rule(subimage, rules):
    pots = []
    pots.append("".join(subimage.flatten()))
    pots.append("".join(np.rot90(subimage).flatten()))
    pots.append("".join(np.rot90(np.rot90(subimage)).flatten()))
    pots.append("".join(np.rot90(np.rot90(np.rot90(subimage))).flatten()))
    pots.append("".join(np.flipud(subimage).flatten()))
    pots.append("".join(np.fliplr(subimage).flatten()))
    pots.append("".join(np.rot90(np.flipud(subimage)).flatten()))
    pots.append("".join(np.rot90(np.fliplr(subimage)).flatten()))
    for pot in pots:
        if pot in rules:
            return rules[pot]


def solution(file_name, steps):
    rules = read_rules(file_name)
    image = np.array([[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]])

    for step in xrange(steps):
        if image.shape[0] % 2 == 0:
            size = 3 * image.shape[0] / 2
            new_image = np.empty([size, size], dtype='|S1')
            for i in xrange(0, image.shape[0] / 2):
                for j in xrange(0, image.shape[0] / 2):
                    subimage = image[2 * i:2 * i + 2, 2 * j:2 * j + 2]
                    rows = get_rule(subimage, rules).split("/")
                    for sm_j, row in enumerate(rows):
                        for sm_i, c in enumerate(row):
                            new_image[3 * i + sm_i, 3 * j + sm_j] = c
            image = new_image
        else:
            size = 4 * image.shape[0] / 3
            new_image = np.empty([size, size], dtype='|S1')
            for i in xrange(0, image.shape[0] / 3):
                for j in xrange(0, image.shape[0] / 3):
                    subimage = image[3 * i:3 * i + 3, 3 * j:3 * j + 3]
                    rows = get_rule(subimage, rules).split("/")
                    for sm_j, row in enumerate(rows):
                        for sm_i, c in enumerate(row):
                            new_image[4 * i + sm_i, 4 * j + sm_j] = c
            image = new_image
        print "(step, count)", (step, np.count_nonzero(new_image == '#'))

    return np.count_nonzero(new_image == '#')

if __name__ == "__main__":
    print "Solution 1: ", solution("test.txt", 2)
    print "Solution 1: ", solution("21.txt", 18)  # 216 too high
