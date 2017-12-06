"""Solutions for AOC Day 5"""

def redistribute(arr):
    highest = arr.index(max(arr))
    num = arr[highest]
    arr[highest] = 0
    for i in range(highest + 1, highest + num + 1):
        arr[i % len(arr)] += 1
    return arr


def sol_1(arr):
    previous = {}
    redistributions = 0
    while True:
        if str(arr) in previous:
            return redistributions, redistributions - previous[str(arr)]
        previous[str(arr)] = redistributions
        arr = redistribute(arr)
        redistributions += 1

if __name__ == "__main__":
    print sol_1([4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5])
