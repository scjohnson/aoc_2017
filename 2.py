"""Solutions for AOC Day 2"""
import itertools
running_sum = 0
for line in open("2.txt"):
    a = [int(s) for s in line.split()]
    running_sum += max(a) - min(a)

print running_sum

running_sum = 0
for line in open("2.txt"):
    numbers = [int(s) for s in line.split()]
    for pair in itertools.permutations(numbers, 2):
        if max(pair) % min(pair) == 0:
            running_sum += max(pair) / min(pair)
            break

print running_sum
