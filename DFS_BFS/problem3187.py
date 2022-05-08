# https://www.acmicpc.net/problem/3187

from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    global board
    q = deque([(x, y)])
    s, w = 1 if board[x][y] == 'k' else 0, 1 if board[x][y] == 'v' else 0
    board[x][y] = '#'

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != '#':
                s = 1 + s if board[nx][ny] == 'k' else s
                w = 1 + w if board[nx][ny] == 'v' else w
                board[nx][ny] = '#'
                q.append((nx, ny))
    if s > w:
        return (s, 0)
    else:
        return (0, w)


dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
n, m = map(int, input().split())
sheep, wolf = 0, 0
board = [list(input().strip('\n')) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] != '#':
            (s, w) = bfs(i, j)
            sheep, wolf = sheep + s, wolf + w

print(sheep, wolf)
