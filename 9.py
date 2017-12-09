"""Solutions for AOC Day 9"""


def parse_garbage(text, loc):
    assert text[loc] == "<"
    loc += 1
    removed = 0
    while True:
        if text[loc] == ">":
            return loc, removed
        elif text[loc] == "!":
            loc += 1
        else:
            removed += 1
        loc += 1


def parse_group(text, loc, base_score=0):
    assert text[loc] == "{"
    loc += 1
    score = base_score + 1
    removed = 0
    while True:
        if text[loc] == "}":
            return score, loc, removed
        elif text[loc] == "{":
            sco, loc, rem = parse_group(text, loc, base_score + 1)
            score += sco
            removed += rem
        elif text[loc] == "<":
            loc, rem = parse_garbage(text, loc)
            removed += rem
        loc += 1


def score(text):
    return parse_group(text, 0)


def test_score():
    assert score("{}")[0] == 1
    assert score("{{{}}},")[0] == 6
    assert score("{{},{}}")[0] == 5
    assert score("{{{},{},{{}}}}")[0] == 16
    assert score("{<a>,<a>,<a>,<a>}")[0] == 1
    assert score("{{<ab>},{<ab>},{<ab>},{<ab>}}")[0] == 9
    assert score("{{<!!>},{<!!>},{<!!>},{<!!>}}")[0] == 9
    assert score("{{<a!>},{<a!>},{<a!>},{<ab>}}")[0] == 3

if __name__ == "__main__":
    for l in open("9.txt"):
        s, loc, rem = score(l)
        print "Score: ", s
        print "Removed: ", rem
