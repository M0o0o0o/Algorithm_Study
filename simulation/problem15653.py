# https://www.acmicpc.net/problem/15653

from collections import deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
n, m = map(int, input().split())
rx, ry, bx, by = -1, -1, -1, -1
graph = []
visited = set()
for i in range(n):
    lst = list(input().strip('\n'))
    graph.append(lst)
    for j in range(m):
        if lst[j] == 'R':
            rx, ry = i, j
        if lst[j] == 'B':
            bx, by = i, j

graph[rx][ry], graph[bx][by] = '.', '.'
visited.add((rx, ry, bx, by))
q = deque([(rx, ry, bx, by, 0)])

while q:
    RX, RY, BX, BY, cnt = q.popleft()
    for i in range(4):
        rx, ry, bx, by = RX, RY, BX, BY
        isRed, isBlue, inRedHole, inBlueHole = True, True, False, False
        while isRed or isBlue:
            if inBlueHole:
                break

            while isRed:
                nrx, nry = rx + dx[i], ry + dy[i]
                if graph[nrx][nry] == '#':
                    isRed = False
                elif (nrx, nry) == (bx, by):
                    if not isBlue:
                        isRed = False
                    else:
                        break

                elif graph[nrx][nry] == '.':
                    rx, ry = nrx, nry
                elif graph[nrx][nry] == 'O':
                    rx, ry = -1, -1
                    isRed, inRedHole = False, True
            while isBlue:
                nbx, nby = bx + dx[i], by + dy[i]
                if graph[nbx][nby] == '#':
                    isBlue = False
                elif (nbx, nby) == (rx, ry):
                    if not isRed:
                        isBlue = False
                    else:
                        break
                elif graph[nbx][nby] == '.':
                    bx, by = nbx, nby
                elif graph[nbx][nby] == 'O':
                    inBlueHole = True
                    break
        if inBlueHole:
            continue
        if inRedHole:
            print(cnt + 1)
            exit(0)
        if (rx, ry, bx, by) not in visited:
            visited.add((rx, ry, bx, by))
            q.append((rx, ry, bx, by, cnt + 1))
print(-1)
