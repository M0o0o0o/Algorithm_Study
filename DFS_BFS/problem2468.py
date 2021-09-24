# https://www.acmicpc.net/problem/2468

from collections import deque

n = int(input())
graph = []
answer = 0 
dx = [0,1,0,-1]
dy = [1,0,-1,0]
queue = deque([])

for _ in range(n) :
    graph.append(list(map(int,input().split())))

def bfs(rain, visited) :
    global queue
    while queue : 
        x, y = queue.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > rain :
                if visited[nx][ny] == False :
                    queue.append((nx,ny))
                    visited[nx][ny] = True

for rain in range(0, 100) :
    queue = deque([])
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n) :
        for j in range(n) :
            if graph[i][j] > rain and visited[i][j] == False :
                count += 1
                queue.append((i,j))
                visited[i][j] = True
                bfs(rain, visited)
    if count == 0 : 
        break
    answer = max(answer, count)

print(answer)


