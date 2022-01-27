# https://www.acmicpc.net/problem/1926
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
count, big = 0, 0


def bfs(i, j):
    global big
    picture = 1
    graph[i][j] = 2
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                picture += 1
                q.append((nx, ny))
    big = max(big, picture)


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            count += 1
            bfs(i, j)

print(count)
print(big)
