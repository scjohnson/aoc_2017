"""Solutions for AOC Day 7"""
import re


def read_data(file_name):
    tree = {}
    weights = {}
    for line in open(file_name):
        items = re.search("(\w*) \((\d*)\)( -> (.*))?", line)
        element = items.group(1)
        weight = int(items.group(2))
        weights[element] = weight
        if items.group(3):
            subelements = [s.strip() for s in items.group(4).split(",")]
        else:
            subelements = []
        if element:
            tree[element] = subelements
    return tree, weights


def create_tree(file_name):
    tree, weights = read_data(file_name)
    pointed_to = {}
    for key, value in tree.iteritems():
        if value:
            if key not in pointed_to:
                pointed_to[key] = False
            for v in value:
                pointed_to[v] = True
    for key in pointed_to:
        if not pointed_to[key]:
            return key, tree, weights


def calc_weight(base, tree, weights):
    leaves = tree[base]
    if leaves == []:
        return weights[base]
    leaf_weights = []
    leaf_dict = {}
    for leaf in leaves:
        leaf_weight = calc_weight(leaf, tree, weights)
        if not leaf_weight:
            return False
        leaf_weights.append(leaf_weight)
        leaf_dict[leaf] = leaf_weight
    if len(set(leaf_weights)) != 1:
        print leaf_dict
        for leaf in leaves:
            print leaf, weights[leaf]
        return False
    return sum(leaf_weights) + weights[base]


if __name__ == "__main__":
    base, tree, weights = create_tree("7.txt")
    print "base = ", base
    calc_weight(base, tree, weights)
    # print sol_2(base) #1072
