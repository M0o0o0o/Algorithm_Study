# https://www.acmicpc.net/problem/11559

from collections import deque


def bfs(x, y):
    q = deque([(x, y)])
    visited = [[False for _ in range(c)] for _ in range(r)]
    visited[x][y] = True
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
                count += 1
                q.append((nx, ny))
                visited[nx][ny] = True

    if count >= 4:
        for i in range(r):
            for j in range(c):
                if visited[i][j]:
                    graph[i][j] = '.'
        return True
    return False


def move(tr, tc):
    start = tr
    for i in range(start + 1, r):
        if graph[i][tc] != '.':
            graph[start][tc] = graph[i][tc]
            graph[i][tc] = '.'
            start += 1


r, c = 12, 6
buf = [list(input()) for _ in range(r)]
graph = [[0] * c for _ in range(r)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
result = 0

# rotate
for i in range(r):
    for j in range(c):
        graph[r-1-i][c-1-j] = buf[i][j]

while True:
    count = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j] != '.':
                check = bfs(i, j)
                if check:
                    count += 1
    if count == 0:
        break
    result += 1

    for i in range(r):
        for j in range(c):
            if graph[i][j] == '.':
                move(i, j)


print(result)
