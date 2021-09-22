# https://www.acmicpc.net/problem/1261

from collections import deque

m, n = map(int,input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

graph = []
answer = [[int(1e9)] * m for _ in range(n)]

for i in range(n) :
    graph.append(list(map(int,input())))

queue = deque([(0,0)])
answer[0][0] = 0

while queue :
    x, y = queue.popleft()  
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            if answer[nx][ny] > answer[x][y] + graph[nx][ny] : 
                answer[nx][ny] = answer[x][y] + graph[nx][ny] 
                queue.append((nx,ny))

print(min(answer[n-2][m-1], answer[n-1][m-2]))
