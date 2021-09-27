# https://www.acmicpc.net/problem/2573
from collections import deque
n, m = map(int,input().split())
answer = 0
graph = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]
visited = [[False] * m for _ in range(n)]
counting = [[0] * m for _ in range(n)]
q = deque([])

for _ in range(n) :
    graph.append(list(map(int,input().split())))

def bfs() :
    global visited
    global q
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] > 0 :
                q.append((nx,ny))
                visited[nx][ny] = True

def minus(x,y) :
    global counting
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 :
            counting[x][y] +=1 


while True : 
    counting = [[0] * m for _ in range(n)]
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] > 0 :
                minus(i, j)
    for i in range(n) :
        for j in range(m) :
            if counting[i][j] > 0 :
                graph[i][j] -= counting[i][j]
                if graph[i][j] < 0 : graph[i][j] = 0
    
    answer += 1
    
    visited = [[False] * m for _ in range(n)]
    count = 0
    q = deque([])
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] > 0 and not visited[i][j] :  
                count += 1
                if count > 1 :
                    break
                visited[i][j] = True
                q.append((i,j))
                bfs()
    if count > 1 :
        break
    if count == 0 :
        answer = 0
        break

for i in range(n) :
    print(graph[i])                   
    
print(answer)

