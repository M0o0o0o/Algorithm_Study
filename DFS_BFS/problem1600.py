# https://www.acmicpc.net/problem/1600

from collections import deque
import sys
input = sys.stdin.readline


K = int(input())
m, n = map(int, input().split())
INF = int(1e9)
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[[INF for _ in range(m)] for _ in range(n)] for _ in range(K + 1)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
hx, hy = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, -2, -1, 1, 2]
visited[0][0][0] = 0
q = deque([(0, 0, 0)])

while q:
    x, y, k = q.popleft()
    if k < K:
        for i in range(8):
            nx, ny = x + hx[i], y + hy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                if visited[k+1][nx][ny] > visited[k][x][y] + 1:
                    visited[k+1][nx][ny] = visited[k][x][y] + 1
                    q.append((nx, ny, k + 1))

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[k][nx][ny] > visited[k][x][y] + 1:
                visited[k][nx][ny] = visited[k][x][y] + 1
                q.append((nx, ny, k))


ans = INF
for i in range(K+1):
    ans = min(visited[i][n-1][m-1], ans)

if ans == INF:
    print(-1)
else:
    print(ans)
