# https://www.acmicpc.net/problem/14716


from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    global graph
    graph[x][y] = 2
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 2
                q.append((nx, ny))


dx, dy = [0, 1, 0, -1, -1, -1, 1, 1], [1, 0, -1, 0, -1, 1, 1, -1]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans += 1
            bfs(i, j)

print(ans)
