# https://www.acmicpc.net/problem/16946

from collections import deque
import sys
input = sys.stdin.readline


def bfs(i, j):
    global graph, visited
    q = deque([(i, j)])
    cnt = 1
    visited[i][j] = True
    adjwalls = set()
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) in walls:
                    adjwalls.add((nx, ny))
                elif graph[nx][ny] == 0 and not visited[nx][ny]:
                    q.append((nx, ny))
                    cnt += 1
                    visited[nx][ny] = True
    for wall in list(adjwalls):
        graph[wall[0]][wall[1]] += cnt


n, m = map(int, input().split())
graph = [list(map(int, input().strip('\n'))) for _ in range(n)]
walls, visited = dict(), [[False for _ in range(m)]for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            walls[(i, j)] = True

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if (i, j) in walls:
            print(graph[i][j] % 10, end='')
            continue
        print(graph[i][j], end='')

    print()
