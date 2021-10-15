# https://www.acmicpc.net/problem/2638

from collections import deque

def bfs() :
    while q : 
        x, y = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n+2 and 0 <= ny < m+2 and graph[nx][ny] == 0 :
                graph[nx][ny] = 3
                q.append((nx,ny))

def check(x,y) :
    count = 0
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n+2 and 0 <= ny < m+2 and graph[nx][ny] == 3 :
            count += 1
    if count >= 2 : return True
    return False

n, m = map(int,input().split())
graph = []
dx, dy = [0,1,0,-1], [1,0,-1,0]
answer = 0 

graph.append([0] * (m+2))
for _ in range(n) :
    graph.append([0] + list(map(int,input().split())) + [0])
graph.append([0] * (m+2))

q = deque([(0,0)])
graph[0][0] = 3

bfs()

while True :
    lst = []

    for i in range(0, n+2) :
        for j in range(0, m+2) :
            if graph[i][j] == 1 and check(i,j) :
                lst.append((i,j))
    
    if not lst : break

    for x,y in lst :
        q.append((x,y))
        graph[x][y] = 3

    bfs()
    answer += 1

print(answer)

