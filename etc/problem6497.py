# https://www.acmicpc.net/problem/6497

import sys
input = sys.stdin.readline


def find_parent(parent, node):
    if node != parent[node]:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
        return
    parent[a] = b


while True:
    v, e = map(int, input().split())
    if v == 0 and e == 0:
        break
    parent = [i for i in range(v)]
    edges = []

    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))
    edges.sort()

    ans = 0
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            ans += cost

    print(sum([edge[0] for edge in edges]) - ans)
