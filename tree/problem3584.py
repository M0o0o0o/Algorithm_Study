# https://www.acmicpc.net/problem/3584

import copy
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

findA, findB, lst = [], [], []


def dfs(tree, root, a, b):
    global findA, findB
    if findA and findB:
        return
    if root == a:
        findA = copy.deepcopy(lst)
    if root == b:
        findB = copy.deepcopy(lst)
    if not tree[root]:
        return
    for node in tree[root]:
        lst.append(node)
        dfs(tree, node, a, b)
        lst.pop()


for _ in range(int(input())):
    n = int(input())
    tree = dict()
    parent, child = dict(), dict()
    findA, findB = [], []
    for _ in range(n-1):
        a, b = map(int, input().split())
        if a in tree:
            tree[a].append(b)
        else:
            tree[a] = [b]
        if b not in tree:
            tree[b] = []
        child[a] = True
        parent[b] = True

    a, b = map(int, input().split())
    root = -1
    for key in tree.keys():
        if key not in parent and key in child:
            root = key
            break
    lst = [root]
    dfs(tree, root, a, b)
    ans = -1
    for node in findA:
        if node in findB:
            ans = node
    print(ans)
