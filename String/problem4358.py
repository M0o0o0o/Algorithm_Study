# https://www.acmicpc.net/problem/4358

import sys

trees = {}
treeNum = 0

for t in sys.stdin:
    if t == '\n':
        break
    tree = t.rstrip()
    treeNum += 1
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

sorted_trees = sorted(trees.items(), key=lambda x: x[0])

for t, c in sorted_trees:
    print(t, '%.4f' % (round((c/treeNum) * 100, 4)))
