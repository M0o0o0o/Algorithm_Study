# https://www.acmicpc.net/problem/13565

from collections import deque
import sys
input = sys.stdin.readline


def bfs(y):
    global graph
    q = deque([(0, y)])
    graph[0][y] == 2
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                if nx == n-1:
                    print('YES')
                    exit(0)
                q.append((nx, ny))
                graph[nx][ny] = 2


dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
m, n = map(int, input().split())
m, n = n, m
graph = [list(map(int, input().strip('\n'))) for _ in range(n)]

for i in range(m):
    if graph[0][i] == 0:
        bfs(i)

print('NO')
