# https://www.acmicpc.net/problem/1531

import sys
input = sys.stdin.readline


n, m = map(int, input().split())
board = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    lx, ly, rx, ry = map(int, input().split())
    for x in range(min(lx, rx), max(lx, rx) + 1):
        for y in range(min(ly, ry), max(ly, ry) + 1):
            board[x][y] += 1

ans = 0
for i in range(101):
    for j in range(101):
        if board[i][j] > m:
            ans += 1

print(ans)
