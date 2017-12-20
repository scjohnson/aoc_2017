"""Solutions for AOC Day 19"""


def solution(file_name):
    with open(file_name) as f:
        lines = f.readlines()

    j = lines[0].index('|')
    i = 0
    directions = []
    steps = 1
    while True:
        if (i != 0) and (not lines[i - 1][j].isspace()):
            while lines[i - 1][j] != '+':
                if lines[i-1][j].isspace():
                    return "".join(directions), steps
                i -= 1
                steps +=1
                if lines[i][j].isalpha():
                    directions.append(lines[i][j])
                if i == 0:
                    return "".join(directions), steps
            i -= 1
            steps +=1
        else:
            while lines[i + 1][j] != '+':
                if lines[i+1][j].isspace():
                    return "".join(directions), steps
                i += 1
                steps +=1
                if lines[i][j].isalpha():
                    directions.append(lines[i][j])
                if i == len(lines):
                    return "".join(directions), steps
            i += 1
            steps +=1

        if (j != 0) and (not lines[i][j - 1].isspace()):
            # going left
            while lines[i][j - 1] != '+':
                if lines[i][j-1].isspace():
                    return "".join(directions), steps
                j -= 1
                steps +=1
                if lines[i][j].isalpha():
                    directions.append(lines[i][j])
                if j == 0:
                    return "".join(directions), steps
            j -= 1
            steps +=1
        else:
            # going right
            while lines[i][j + 1] != '+':
                if lines[i][j+1].isspace():
                    return "".join(directions), steps
                j += 1
                steps +=1
                if lines[i][j].isalpha():
                    directions.append(lines[i][j])
                if j == len(lines[i]):
                    return "".join(directions), steps
            j += 1
            steps +=1


if __name__ == "__main__":
    print "Solution 1: ", solution("test.txt")
    # BPDKCZWHGT, 17728
    print "Solution 1: ", solution("19.txt")
