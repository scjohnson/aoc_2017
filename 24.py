"""Solutions for AOC Day 24"""
import numpy as np


def read_data(file_name):
    ports = []
    for line in open(file_name):
        ports.append([int(x) for x in line.split('/')])
    return ports


def add_port(attached, available):
    value = attached[-1][1]
    scores = []
    found = False
    for avail in available:
        if avail[0] == value:
            found = True
            att = list(attached)
            att.append(avail)
            ava = list(available)
            ava.remove(avail)
            scores.extend(add_port(att, ava))
        elif avail[1] == value:
            found = True
            avail = avail[::-1]
            att = list(attached)
            att.append(avail)
            ava = list(available)
            ava.remove(avail[::-1])
            scores.extend(add_port(att, ava))
    if found == False:
        return [int(np.sum(np.array(attached).flatten())), len(attached)]
    return scores


def solution(file_name):
    ports = read_data(file_name)
    scores = add_port([[0, 0]], ports)
    scores = np.array(scores)
    scores = scores.reshape(scores.shape[0] / 2, 2)
    max_l = 0
    max_v = 0
    for i in xrange(scores.shape[0]):
        if scores[i][1] >= max_l:
            if scores[i][0] >= max_v:
                max_l = scores[i][1]
                max_v = scores[i][0]

    return max(scores[:, 0]), max_v


if __name__ == "__main__":
    print "Solution 1: ", solution("24.txt")
