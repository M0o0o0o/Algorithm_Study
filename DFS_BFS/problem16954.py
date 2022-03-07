# https://www.acmicpc.net/problem/16954

from collections import deque


def rotate(lst):
    newGraph = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            newGraph[n-1-r][n-1-c] = lst[r][c]
    return newGraph


n = 8
graph = [list(input().strip('\n')) for _ in range(n)]
graph = rotate(graph)
result = 0

timeGraph = [[] for _ in range(n + 1)]
dx, dy = [0, 0, 1, 0, -1, -1, -1, 1, 1], [0, 1, 0, -1, 0, -1, 1, -1, 1]

for i in range(n + 1):
    tgIndex = 0
    for t in range(i, n):
        timeGraph[i].append(list(''.join(graph[t])))
        tgIndex += 1
    for b in range(tgIndex, n):
        timeGraph[i].append(list(''.join('........')))

q = deque([(0, n-1, 0)])

while q:
    x, y, t = q.popleft()
    if timeGraph[t][x][y] == '#':
        continue
    if (x, y) == (n-1, 0):
        result = 1
        break
    for i in range(9):
        nx, ny = x + dx[i], y + dy[i]
        tPlus = t + 1 if t + 1 < 8 else 8
        if 0 <= nx < n and 0 <= ny < n and timeGraph[t][nx][ny] == '.':
            timeGraph[t][nx][ny] = 'o'
            q.append((nx, ny, tPlus))

print(result)
