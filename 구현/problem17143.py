
# 1. 낚시왕이 오른쪽으로 한 칸 이동한다.
# 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
# 3. 상어가 이동한다.

# 상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동한다.
# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
# 상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있다. 이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.
# 즉 이동 중에는 상어가 겹쳐도 된다는 말인듯 싶다.

import copy
import sys
input = sys.stdin.readline


def fishing(grpah, col):
    for row in range(1, n+1):
        if graph[row][col] == 0:
            continue
        size = graph[row][col][0]
        graph[row][col] = 0
        return size
    return 0


def whole_move():
    global graph
    buf = [[[] for _ in range(m+1)]for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if graph[i][j] != 0:
                x, y, z, s, d = move(i, j, graph[i][j])
                buf[x][y].append((z, s, d))

    for i in range(1, n+1):
        for j in range(1, m+1):
            if len(buf[i][j]) >= 2:
                buf[i][j].sort(reverse=True)
                buf[i][j] = [buf[i][j][0]]

    graph = [[0 for _ in range(m+1)]for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if buf[i][j]:
                graph[i][j] = buf[i][j][0]


def move(x, y, shark):
    z, s, d = shark
    nx, ny = x, y
    idx = 0
    while idx < s:
        nx, ny = nx + dx[d], ny + dy[d]
        idx += 1
        if nx == 0 or nx == n+1 or ny == 0 or ny == m+1:
            nx, ny = nx - dx[d], ny - dy[d]
            if d in [1, 2]:
                d = 2 if d == 1 else 1
            elif d in [3, 4]:
                d = 4 if d == 3 else 3
            idx -= 1

    return (nx, ny, z, s, d)


n, m, k = map(int, input().split())
dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, 1, -1]
graph = [[0 for _ in range(m+1)]for _ in range(n+1)]

for _ in range(k):
    r, c, s, d, z = map(int, input().split())
    graph[r][c] = (z, s, d)  # 사이즈, 스피드, 방향

ans = 0
for i in range(1, m+1):
    ans += fishing(graph, i)

    whole_move()


print(ans)
