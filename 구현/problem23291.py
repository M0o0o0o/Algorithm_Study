# https://www.acmicpc.net/problem/23291

from copy import deepcopy
import sys
from collections import defaultdict
input = sys.stdin.readline


def devideAndLine(buf, r, nc):
    # 위에는 계산을 편하게 하기 위해서 2차원 배열로 합쳐줫다.
    check = defaultdict(int)
    dic = defaultdict(int)
    for x in range(r):
        for y in range(nc):
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < r and 0 <= ny < nc and check[(x, y), (nx, ny)] == 0 and check[(nx, ny), (x, y)] == 0:
                    check[(x, y), (nx, ny)] = 1
                    check[(nx, ny), (x, y)] = 1

                    if buf[x][y] != 0 and buf[nx][ny] != 0:
                        diff = abs(buf[x][y] - buf[nx][ny])
                        diff //= 5
                        if diff > 0:
                            if buf[x][y] > buf[nx][ny]:
                                dic[(x, y)] -= diff
                                dic[(nx, ny)] += diff
                            else:
                                dic[(x, y)] += diff
                                dic[(nx, ny)] -= diff
    for i in range(r):
        for j in range(nc):
            buf[i][j] += dic[(i, j)]
    new_lst = [0] * n
    idx = 0
    for j in range(nc):
        for i in range(r-1, -1, -1):
            if buf[i][j] == 0:
                continue
            new_lst[idx] = buf[i][j]
            idx += 1
    return new_lst


def rotate_90(board):
    x, y = len(board), len(board[0])
    N = max(x, y)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if x > r and y > c:
                ret[c][N-1-r] = board[r][c]
    return ret


def rotate_180(board, r):
    return [board[r-i-1][::-1] for i in range(r)]


def rotate2():
    r, c = 1, n
    board = [deepcopy(lst)]
    for _ in range(2):
        nr, nc = r * 2, c // 2
        # 회전할 배열 만들기
        left = rotate_180([[board[i][j] for j in range(c//2)]
                          for i in range(r)], r)
        right = [[board[i][j] for j in range(c//2, c)] for i in range(r)]
        buf = []
        for i in range(r):
            buf.append(deepcopy(left[i]))

        for i in range(r):
            buf.append(deepcopy(right[i]))
        r, c = nr, nc
        board = deepcopy(buf)

    res = devideAndLine(board, r, c)
    return res


def rotate():
    global lst
    r, c, idx = 2, 1, 0
    board = [[0 for _ in range(max(r, c))]for _ in range(max(r, c))]
    for i in range(r):
        for j in range(c):
            board[i][j] = lst[idx]
            idx += 1
    while True:
        nr, nc = r, c
        if r > c:
            nc += 1
        else:
            nr += 1
        if nr > n - idx:
            break
        buf = rotate_90(board)
        board = [[0 for _ in range(nc)] for _ in range(nr)]

        for i in range(max(r, c)):
            for j in range(max(r, c)):
                board[i][j] = buf[i][j]

        for i in range(nr):
            for j in range(nc):
                if board[i][j] != 0:
                    continue
                board[i][j] = lst[idx]
                idx += 1

        r, c = nr, nc

    nc = c + (n-idx)
    buf = [[0 for _ in range(nc)]for _ in range(nr)]
    for i in range(r):
        for j in range(c):
            buf[i][j] = board[i][j]
    for j in range(c, nc):
        board[r-1]
    for j in range(c, nc):
        buf[r-1][j] = lst[idx]
        idx += 1

    res = devideAndLine(buf, r, nc)
    return res


def addFish():
    global lst
    minV = min(lst)
    lst = [l+1 if l == minV else l for l in lst]


n, k = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

while True:
    if max(lst) - min(lst) <= k:
        break
    addFish()
    lst = deepcopy(rotate())

    lst = deepcopy(rotate2())
    ans += 1

print(ans)
