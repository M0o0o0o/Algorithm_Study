# https://www.acmicpc.net/problem/2234
from collections import deque


def bfs(room_count, X, Y):
    global visited
    q = deque([(X, Y)])
    visited[X][Y] = room_count
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if int(bin(dic[str(dx[i]) + str(dy[i])] & graph[x][y]), 2) == 0:
                    visited[nx][ny] = room_count
                    count += 1
                    q.append((nx, ny))
    return count


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
dic = {"01": 4, "10": 8, "0-1": 1, "-10": 2}
visited = [[-1 for _ in range(m)] for _ in range(n)]


room_count = 0
room = {}
for i in range(n):
    for j in range(m):
        if visited[i][j] == -1:
            room[room_count] = bfs(room_count, i, j)
            room_count += 1

roomCombineMax = 0
for x in range(n):
    for y in range(m):
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[x][y] != visited[nx][ny]:
                roomCombineMax = max(
                    roomCombineMax, room[visited[x][y]] + room[visited[nx][ny]])


print(room_count)
print(max(list(room.values())))
print(roomCombineMax)
