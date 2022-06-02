# https://www.acmicpc.net/problem/1197

import sys
input = sys.stdin.readline


def find_parent(parents, x):
    if x != parents[x]:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]


def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


n, m = map(int, input().split())
edges = []
parents = [i for i in range(n+1)]
ans = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        ans += cost
print(ans)
