# https://www.acmicpc.net/problem/2589

from collections import deque

def bfs() :
    global q
    num = -1
    while q : 
        x, y = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i] 
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'L' and visited[nx][ny] == 0 :
                visited[nx][ny] = visited[x][y] + 1
                num = max(num ,visited[nx][ny])
                q.append((nx,ny))
    return num


n, m = map(int,input().split())
graph = []
q = deque([])
visited = [[0] * m for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for _ in range(n) :
    graph.append(list(input()))

answer = -1

for i in range(n) :
    for j in range(m) :
        visited = [[0] * m for _ in range(n)]
        if visited[i][j] == 0 and graph[i][j] == 'L' :
            q.append((i,j))
            visited[i][j] = 1
            answer = max(answer, bfs())

print(answer -1)





