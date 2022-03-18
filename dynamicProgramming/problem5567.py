# https://www.acmicpc.net/problem/5567
from collections import deque

n, m = int(input()), int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n+1)]
visited[1] = True
q = deque([(1, 0)])
ans = 0
while q:
    me, d = q.popleft()
    for fri in graph[me]:
        nd = d + 1
        if not visited[fri] and nd <= 2:
            q.append((fri, nd))
            ans += 1

            visited[fri] = True

print(ans)
