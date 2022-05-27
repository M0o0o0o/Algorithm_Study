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
