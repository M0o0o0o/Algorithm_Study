# https://www.acmicpc.net/problem/1726

from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)
ans = INF
dx, dy = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0]
dd = {1: [4, 3], 2: [3, 4], 3: [1, 2], 4: [1, 2]}
n, m = map(int, input().split())
graph = [0] + [[0] + list(map(int, input().split())) for _ in range(n)]

sx, sy, sd = map(int, input().split())
tx, ty, td = map(int, input().split())

visited = [[[INF for _ in range(5)] for _ in range(m+1)] for _ in range(n+1)]

q = deque([(sx, sy, sd)])
visited[sx][sy][sd] = 0

while q:
    x, y, d = q.popleft()
    if (x, y, d) == (tx, ty, td):
        print(visited[x][y][d])
        break

    moveLst = []
    nx, ny = x, y
    for f in [1, 2, 3]:
        nx, ny = nx + dx[d], ny + dy[d]
        if not (1 <= nx <= n and 1 <= ny <= m) or graph[nx][ny] == 1:
            break
        moveLst.append((nx, ny, d))
    for nd in dd[d]:
        moveLst.append((x, y, nd))
    for l in moveLst:
        nx, ny, nd = l
        if 1 <= nx <= n and 1 <= ny <= m and visited[nx][ny][nd] > visited[x][y][d] + 1 and graph[nx][ny] == 0:
            visited[nx][ny][nd] = visited[x][y][d] + 1
            q.append((nx, ny, nd))
