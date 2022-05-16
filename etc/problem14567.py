# https://www.acmicpc.net/problem/14567

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indgree = [0] * (n+1)
ans = [1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    indgree[b] += 1
    graph[a].append(b)

q = deque([])
for i in range(1, n+1):
    if indgree[i] == 0:
        q.append(i)
while q:
    now = q.popleft()
    for node in graph[now]:
        indgree[node] -= 1
        ans[node] = max(ans[node], ans[now] + 1)
        if indgree[node] == 0:
            q.append(node)

print(*ans[1:])
