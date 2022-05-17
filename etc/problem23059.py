# https://www.acmicpc.net/problem/23059

from collections import defaultdict, deque
import sys
import copy
input = sys.stdin.readline

n = int(input())
items = set()
graph, indgree = defaultdict(list), defaultdict(int)
ans = []

for _ in range(n):
    a, b = input().split()
    indgree[b] += 1
    if a not in indgree:
        indgree[a] = 0
    if b not in graph:
        graph[b] = []
    graph[a].append(b)

if len(graph) <= n:
    print(-1)
    exit(0)

q = deque([])

for key in indgree.keys():
    if indgree[key] == 0:
        q.append(key)

ans.extend(sorted(list(q)))

while True:
    subQ = deque([])
    while q:
        now = q.popleft()
        for node in graph[now]:
            indgree[node] -= 1
            if indgree[node] == 0:
                subQ.append(node)

    if not subQ:
        break
    ans.extend(sorted(list(subQ)))
    q = copy.deepcopy(subQ)

for a in ans:
    print(a)
