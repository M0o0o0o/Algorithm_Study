# https://www.acmicpc.net/problem/1303

from collections import deque


def bfs(X, Y):
    global visited
    q = deque([(X, Y)])
    visited[X][Y] = True
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[x][y] == graph[nx][ny]:
                visited[nx][ny] = True
                count += 1
                q.append((nx, ny))
    return count


m, n = map(int, input().split())
graph = [list(input().strip('\n')) for _ in range(n)]
visited = [[False for _ in range(m)] for i in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
answer = {'W': 0, 'B': 0}

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            answer[graph[i][j]] += bfs(i, j) ** 2

print(*list(answer.values()))
