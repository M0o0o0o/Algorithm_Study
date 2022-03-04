# https://www.acmicpc.net/problem/6593

import sys
from collections import deque
input = sys.stdin.readline

dx, dy, dz = [0, 1, 0, -1, 0, 0], [1, 0, -1, 0, 0, 0], [0, 0, 0, 0, 1, -1]
INF = int(1e9)
while True:
    l, r, c = map(int, input().split())
    start, end = (0, 0, 0), (0, 0, 0)
    if l + r + c == 0:
        break
    visited = [[[INF for _ in range(c)]for _ in range(r)] for _ in range(l)]
    board = []
    for f in range(l):
        floor = [list(input().strip('\n')) for _ in range(r)]
        input()
        for i in range(r):
            for j in range(c):
                if floor[i][j] == 'S':
                    start = (f, i, j)
                    floor[i][j] = '.'
                if floor[i][j] == 'E':
                    end = (f, i, j)
                    floor[i][j] = '.'

        board.append(floor)

    visited[start[0]][start[1]][start[2]] = 0
    q = deque([start])
    while q:
        z, x, y = q.popleft()
        current = visited[z][x][y]
        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c and visited[nz][nx][ny] > current + 1 and board[nz][nx][ny] == '.':
                q.append((nz, nx, ny))
                visited[nz][nx][ny] = current + 1
    endValue = visited[end[0]][end[1]][end[2]]
    if endValue != INF:
        print('Escaped in ' + str(endValue) + ' minute(s).')
        continue
    print('Trapped! ')
