# https://www.acmicpc.net/problem/17086

from collections import deque


def bfs(X, Y):
    q = deque([(X, Y, 0)])
    while q:
        x, y, count = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in sharks and graph[nx][ny] > count + 1:
                graph[nx][ny] = count + 1
                q.append((nx, ny, count + 1))


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 1, 0, -1, -1, -1, 1, 1], [1, 0, -1, 0, -1, 1, 1, -1]
INF = int(1e9)
ans = -1
sharks = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            sharks.append((i, j))
        else:
            graph[i][j] = INF

for x, y in sharks:
    bfs(x, y)

for i in range(n):
    for j in range(m):
        if (i, j) not in sharks and ans < graph[i][j]:
            ans = graph[i][j]

print(ans)
