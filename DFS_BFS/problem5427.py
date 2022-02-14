# https://www.acmicpc.net/problem/5427

from collections import deque
for _ in range(int(input())):
    m, n = map(int, input().split())
    graph = [list(input()) for _ in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    INF = int(1e9)
    visited = [[INF for _ in range(m)] for _ in range(n)]
    f_visited = [[INF for _ in range(m)] for _ in range(n)]
    fq, sq = deque([]), deque([])
    ans = INF

    for i in range(n):
        for j in range(m):
            if graph[i][j] == '@':
                sq.append((i, j))
                visited[i][j] = 0
            if graph[i][j] == '*':
                fq.append((i, j))
                f_visited[i][j] = 0

    while fq:
        x, y = fq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.' and f_visited[nx][ny] == INF:
                fq.append((nx, ny))
                f_visited[nx][ny] = f_visited[x][y] + 1
    while sq:
        x, y = sq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.' and visited[nx][ny] == INF:
                sq.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    for x in range(n):
        for y in range(m):
            if x != 0 and x != n-1 and y != 0 and y != m-1:
                continue
            if visited[x][y] < f_visited[x][y]:
                ans = min(ans, visited[x][y])

    if ans == INF:
        print('IMPOSSIBLE')
    else:
        print(ans + 1)
