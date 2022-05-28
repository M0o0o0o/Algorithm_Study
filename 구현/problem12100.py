# https://www.acmicpc.net/problem/12100
from copy import deepcopy
import sys
input = sys.stdin.readline


def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret


def move(board, d):
    buf = deepcopy(board)
    for _ in range(d):
        buf = rotate_90(buf)
    check = set()
    i = 0
    while True:
        if i == n:
            break
        zero, find = False, False
        for j in range(1, n):
            if buf[i][j-1] == 0 and buf[i][j] != 0:
                buf[i][j-1], buf[i][j] = buf[i][j], buf[i][j-1]
                zero = True
        if zero:
            continue

        for j in range(1, n):
            if (i, j-1) in check or (i, j) in check:
                continue
            if buf[i][j] == buf[i][j-1] and buf[i][j] != 0:
                buf[i][j-1] *= 2
                buf[i][j] = 0
                find = True
                check.add((i, j-1))
                break
        if not zero and not find:
            i += 1
            continue

    for _ in range(4-d):
        buf = rotate_90(buf)

    return buf


def dfs(cnt, board):
    global ans
    ans = max(ans, max([max(board[i]) for i in range(n)]))

    if cnt == 5:
        return

    for i in range(4):
        buf = move(board, i)
        dfs(cnt + 1,  buf)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = max([max(board[i]) for i in range(n)])
dfs(0, board)
print(ans)

# n = 4
# test = [[2, 2, 4, 16], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# res = move(test, 0)
# for i in range(4):
#     print(res[i])
